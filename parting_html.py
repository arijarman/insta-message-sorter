from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import os

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

            # Find base URL to resolve relative paths
            base_url = soup.find('base')['href'] if soup.find('base') else ''

            for div in message_divs:
                sender = div.find('div', class_='_3-95 _2pim _a6-h _a6-i').text.strip()
                message = div.find('div', class_='_3-95 _a6-p').text.strip()
                timestamp = div.find('div', class_='_3-94 _a6-o').text.strip()

                # Convert the time to IST
                timestamp_ist = convert_to_ist(timestamp)

                # Check for images and videos
                images = [base_url + img['src'] for img in div.find_all('img')]
                videos = [base_url + video['src'] for video in div.find_all('video')]

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

# Generate HTML content with navigation between files
def generate_html(messages, left_sender, right_sender, part_num, total_parts):
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Enhanced Love-Themed Instagram Chat - Part {part_num}</title>
        <style>
            body {{ 
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
                background: linear-gradient(to right, #74ebd5, #ACB6E5); /* macOS Big Sur-like gradient */
                padding: 20px; 
                margin: 0; 
                display: flex;
                overflow-x: hidden; /* Prevent horizontal scrolling */
                justify-content: center;
            }}
            .chat-container {{ 
                max-width: 600px; 
                width: 100%;
                background-color: rgba(255, 255, 255, 0.8); 
                border-radius: 20px;
                box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
                padding: 20px;
                backdrop-filter: blur(10px); /* Slight blur for a modern feel */
                position: relative;
            }}
            .message {{ 
                margin: 15px 0; 
                padding: 12px; 
                border-radius: 15px; 
                max-width: 80%; /* Ensure messages don't exceed this width */
                box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1); /* Depth with shadow */
                transition: background-color 0.3s ease;
            }}
            .message:hover {{
                background-color: rgba(255, 255, 255, 0.9); /* Hover effect */
            }}
            .left-sender {{ 
                background-color: #d3e5ff; 
                color: #0056b3; 
                text-align: left; 
                float: left; /* Align to the left */
                clear: both;
            }}
            .right-sender {{ 
                background-color: #fff5e1; 
                color: #b35a00; 
                text-align: right; 
                float: right; /* Align to the right */
                clear: both;
            }}
            .time {{ 
                font-size: 10px; 
                color: gray;
                margin-top: 5px; /* Better spacing for the timestamp */
                display: block;
            }}
            .emoji {{
                font-size: 18px; /* Make emojis more prominent */
                margin-right: 5px;
            }}
            .reaction {{ 
                margin-top: 5px; 
                font-size: 12px; 
                color: #888; 
            }}
            .image, .video {{ 
                max-width: 100%; /* Ensure images and videos fit within the message bubble */
                height: auto;
                margin-top: 10px;
                border-radius: 10px;
            }}
            .nav-links {{
                text-align: center;
                margin-top: 20px;
            }}
            .nav-links a {{
                margin: 0 10px;
                text-decoration: none;
                font-weight: bold;
                color: #0056b3;
            }}
        </style>
    </head>
    <body>
        <div class="chat-container">
    """

    for message in messages:
        sender_class = "left-sender" if message['sender'] == left_sender else "right-sender"
        
        html_content += f"""
        <div class="message {sender_class}">
            <span class="emoji">😊</span><strong>{message['sender']}</strong><br>
            {message['message']}<br>
            <span class="time">{message['timestamp']}</span>
        """

        for image in message['images']:
            html_content += f'<img src="{image}" class="image" alt="Image" />'

        for video in message['videos']:
            html_content += f'<video controls class="video"><source src="{video}" type="video/mp4"></video>'

        html_content += "</div>"

    # Add navigation links
    html_content += '<div class="nav-links">'
    if part_num > 1:
        html_content += f'<a href="part_{part_num - 1}.html">&laquo; Previous</a>'
    if part_num < total_parts:
        html_content += f'<a href="part_{part_num + 1}.html">Next &raquo;</a>'
    html_content += '</div>'

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

    # Get unique senders from messages
    unique_senders = list(set([msg['sender'] for msg in all_messages]))

    # Display senders to the user for input
    print("Detected senders:")
    for i, sender in enumerate(unique_senders):
        print(f"{i + 1}. {sender}")

    # Ask the user who should be on the left
    left_choice = int(input(f"Choose the number for the sender to display on the left side: ")) - 1

    left_sender = unique_senders[left_choice]
    right_sender = [sender for sender in unique_senders if sender != left_sender][0]

    # Split messages into chunks (e.g., 3 parts)
    total_parts = 3
    chunk_size = len(all_messages) // total_parts

    for part_num in range(1, total_parts + 1):
        start_index = (part_num - 1) * chunk_size
        end_index = start_index + chunk_size if part_num < total_parts else len(all_messages)
        chunk_messages = all_messages[start_index:end_index]

        # Generate the HTML for this part
        part_html_content = generate_html(chunk_messages, left_sender, right_sender, part_num, total_parts)

        # Save the HTML content to a new file
        with open(f'part_{part_num}.html', 'w', encoding='utf-8') as output_file:
            output_file.write(part_html_content)

    print(f"Enhanced love-themed chat split into {total_parts} parts successfully.")
