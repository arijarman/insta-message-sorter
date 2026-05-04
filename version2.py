import os
from bs4 import BeautifulSoup
from datetime import datetime
import pytz

# -------- CONFIG --------
INPUT_FOLDER = os.getcwd()
OUTPUT_FOLDER = os.getcwd()

ALASKA_TZ = pytz.timezone("US/Alaska")
LOCAL_TZ = datetime.now().astimezone().tzinfo


# -------- PARSE --------
def parse_html(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    messages = []
    blocks = soup.find_all("div", class_="pam")

    for block in blocks:
        try:
            sender = block.find("h2").text.strip()
            message = block.find("div", class_="_a6-p").get_text("\n", strip=True)
            raw_time = block.find("div", class_="_a6-o").text.strip()

            dt = datetime.strptime(raw_time, "%b %d, %Y %I:%M %p")
            dt = ALASKA_TZ.localize(dt).astimezone(LOCAL_TZ)

            messages.append({
                "sender": sender,
                "message": message,
                "time": dt
            })
        except:
            continue

    messages.sort(key=lambda x: x["time"])
    return messages


# -------- HELPERS --------
def format_time(dt):
    return dt.strftime("%I:%M %p").lstrip("0").lower()

def format_date(dt):
    return dt.strftime("%d %b %Y")

def format_month(dt):
    return dt.strftime("%b %Y")

def get_participants(messages):
    return list(set(msg["sender"] for msg in messages))


# -------- HTML --------
def generate_html(messages, index, total_files, right_user):
    html = """
    <html>
    <head>
    <meta charset="UTF-8">
    <style>

        body {
            margin: 0;
            padding: 0;
            font-family: Arial;
            background: #0f0f0f;
            overflow-x: hidden;
        }

        .chat {
            max-width: 700px;
            margin: auto;
            padding: 20px;
            box-sizing: border-box;
        }

        .msg {
            padding: 12px 16px;
            border-radius: 14px;
            margin: 8px 0;
            max-width: 75%;
            word-wrap: break-word;
            overflow-wrap: break-word;
        }

        .left {
            background: #262626;
            color: #ffffff;
        }

        .right {
            background: #0084ff;
            color: #ffffff;
            margin-left: auto;
        }

        .name {
            font-weight: bold;
            font-size: 14px;
            margin-bottom: 4px;
        }

        .text {
            font-size: 14px;
            line-height: 1.4;
        }

        .meta {
            font-size: 11px;
            opacity: 0.7;
            margin-top: 5px;
        }

        .right .meta {
            text-align: right;
        }

        .separator {
            text-align: center;
            margin: 20px 0;
            font-size: 12px;
            color: #aaa;
        }

        .nav {
            text-align: center;
            margin: 20px 0;
        }

        .nav a {
            color: white;
            text-decoration: none;
            margin: 0 10px;
            padding: 6px 12px;
            background: #333;
            border-radius: 6px;
        }

        @media (max-width: 768px) {
            .chat {
                padding: 10px;
            }
            .msg {
                max-width: 90%;
            }
        }

    </style>
    </head>
    <body>

    <div class="nav">
    """

    # Navigation
    if index > 1:
        html += f'<a href="chat_{index-1}.html">⬅ Previous</a>'
    if index < total_files:
        html += f'<a href="chat_{index+1}.html">Next ➡</a>'

    html += "</div><div class='chat'>"

    last_month = None

    for msg in messages:
        current_month = format_month(msg["time"])

        if current_month != last_month:
            html += f'<div class="separator">— {current_month} —</div>'
            last_month = current_month

        is_right = msg["sender"] == right_user
        side = "right" if is_right else "left"

        html += f"""
        <div class="msg {side}">
            <div class="name">{msg['sender']}</div>
            <div class="text">{msg['message']}</div>
            <div class="meta">{format_time(msg['time'])} • {format_date(msg['time'])}</div>
        </div>
        """

    html += "</div></body></html>"
    return html


# -------- MAIN --------
def main():
    files = sorted([f for f in os.listdir(INPUT_FOLDER) if f.endswith(".html")])
    total = len(files)

    if total == 0:
        print("❌ No HTML files found.")
        return

    # Collect all messages
    all_messages = []
    for file in files:
        all_messages.extend(parse_html(os.path.join(INPUT_FOLDER, file)))

    participants = get_participants(all_messages)

    print("\nDetected participants:")
    for i, p in enumerate(participants, 1):
        print(f"{i}) {p}")

    choice = int(input("\nEnter who should be on RIGHT side: "))
    right_user = participants[choice - 1]

    print(f"\n✅ '{right_user}' will be on RIGHT side.\n")

    # Generate output files
    for i, file in enumerate(files, 1):
        messages = parse_html(os.path.join(INPUT_FOLDER, file))
        html = generate_html(messages, i, total, right_user)

        with open(f"chat_{i}.html", "w", encoding="utf-8") as f:
            f.write(html)

    print(f"🚀 Generated {total} chat files successfully.")


if __name__ == "__main__":
    main()
