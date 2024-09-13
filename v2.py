from bs4 import BeautifulSoup
from datetime import datetime, timedelta

# Function to adjust the timezone from Alaska to IST
def convert_to_ist(alaska_time_str):
    alaska_time = datetime.strptime(alaska_time_str, "%b %d, %Y, %I:%M %p")
    # Corrected time difference from Alaska to IST
    ist_time = alaska_time + timedelta(hours=13, minutes=30)
    return ist_time.strftime("%b %d, %Y, %I:%M %p")

# Parse HTML files and extract messages
def parse_html_files(file_paths):
    messages = []
    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')
            message_divs = soup.find_all('div', class_='pam _3-95 _2ph- _a6-g uiBoxWhite noborder')

            for div in message_divs:
                sender = div.find('div', class_='_3-95 _2pim _a6-h _a6-i').text.strip()
                message = div.find('div', class_='_3-95 _a6-p').text.strip()
                timestamp = div.find('div', class_='_3-94 _a6-o').text.strip()
                
                # Convert the time to IST
                timestamp_ist = convert_to_ist(timestamp)

                # Check for images and videos
                images = [img['src'] for img in div.find_all('img')]
                videos = [video['src'] for video in div.find_all('video')]

                messages.append({
                    'sender': sender,
                    'message': message,
                    'timestamp': timestamp_ist,
                    'images': images,
                    'videos': videos
                })

    # Reversing the order of messages to get oldest to newest
    messages.reverse()
    return messages

# Generate love-themed HTML content
def generate_html(messages):
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Love Themed Instagram Chat</title>
        <style>
            body { font-family: Arial, sans-serif; background-color: #f2f2f2; padding: 20px; }
            .chat-container { max-width: 600px; margin: auto; }
            .message { margin: 10px 0; padding: 10px; border-radius: 15px; width: fit-content; }
            .sender-jasmin { background-color: #d3e5ff; color: #0056b3; text-align: left; }
            .sender-white-flower { background-color: #fff5e1; color: #b35a00; text-align: right; }
            .time { font-size: 10px; color: gray; }
            .reaction { margin-top: 5px; font-size: 12px; color: #888; }
            .chat-right { float: right; clear: both; }
            .chat-left { float: left; clear: both; }
            .image, .video { max-width: 100%; margin-top: 5px; }
        </style>
    </head>
    <body>
        <div class="chat-container">
    """

    for message in messages:
        sender_class = "sender-jasmin" if message['sender'] == "Jasmin Sarkar" else "sender-white-flower"
        alignment = "chat-left" if sender_class == "sender-jasmin" else "chat-right"
        
        html_content += f"""
        <div class="message {sender_class} {alignment}">
            <strong>{message['sender']}</strong><br>
            {message['message']}<br>
            <span class="time">{message['timestamp']}</span>
        """

        # Add images if any
        for image in message['images']:
            html_content += f'<img src="{image}" class="image" alt="Image" />'

        # Add videos if any
        for video in message['videos']:
            html_content += f'<video controls class="video"><source src="{video}" type="video/mp4"></video>'

        html_content += "</div>"

    html_content += """
        </div>
    </body>
    </html>
    """
    return html_content

# Main execution
if __name__ == "__main__":
    # Ask user for the number of HTML files to process
    num_files = int(input("Enter the number of HTML message files to process: "))
    files = [f"message_{i}.html" for i in range(1, num_files + 1)]

    # Extract and parse the messages
    all_messages = parse_html_files(files)

    # Generate the new HTML with love theme
    final_html_content = generate_html(all_messages)

    # Save the HTML content to a new file
    with open('love_theme_chat.html', 'w', encoding='utf-8') as output_file:
        output_file.write(final_html_content)

    print("Love-themed Instagram chat generated successfully as 'love_theme_chat.html'.")
