# Insta Message Sorter

Insta Message Sorter is a Python tool that processes and formats Instagram chat history. It enhances the readability and usability of your chat data by organizing messages, adjusting time zones, and creating a visually appealing HTML file.

## Features

- **Reorder Messages**: Automatically reorders messages from newest to oldest for a more intuitive reading experience.
- **Chat Bubbles**: Adds chat bubbles around messages for a familiar chat-like appearance.
- **Timezone Adjustment**: Converts message timestamps from Alaska's server time to your local timezone for accurate chronological order.
- **HTML Merging**: Combines multiple `messages.html` files into a single, sorted HTML file, streamlining the chat history into one cohesive document.
- **Top-to-Bottom Reading**: Formats the final HTML so that messages are read from top to bottom, contrary to the original bottom-to-top format.
- **Customizable Output**: Easily modify the script to adjust the appearance or sorting rules according to your needs.
- **User-Friendly**: Simple command-line interface and minimal setup requirements make it easy to use.

## Installation

### Method 1: Using Git and Python

1. **Install Git**:
   - **Ubuntu/Debian/Linux Mint**:
     ```bash
     sudo apt update
     sudo apt install git
     ```
   - **Arch/Manjaro**:
     ```bash
     sudo pacman -S git
     ```
   - **RedHat/Fedora/OpenSUSE**:
     ```bash
     sudo dnf install git
     ```
   - **macOS**:
     ```bash
     brew install git
     ```
   - **Windows**:
     Download and install Git from [git-scm.com](https://git-scm.com/download/win).

2. **Clone the Repository**:
   ```bash
   git clone https://github.com/arijarman/insta-message-sorter
