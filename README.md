
# Insta Message Sorter 📨

A tool to reverse and beautify your Instagram chat history HTML files! This project transforms the plain, server-time-stamped Instagram `messages.html` file into a user-friendly, chat-themed format that sorts messages from top to bottom and converts the timezone from Alaska to your local time.

---

## 📜 Features

- **Reverse Message Order**: Automatically sorts messages from "oldest to newest," making it easier to read.
- **Chat Bubble Styling**: Converts plain HTML into a chat-bubble style format for enhanced readability.
- **Timezone Conversion**: Changes the timezone from Alaska Time to your local timezone.
- **Merge Multiple Files**: Merges all `messages.html` files into a single, sorted, and edited chat-themed HTML.

## 🚀 Installation Guide

Follow these steps to set up the project on your local machine.

### 1. Install Git

You need Git to clone the repository. Follow the instructions below based on your operating system.

<details>
  <summary><strong>Ubuntu/Debian/Linux Mint</strong></summary>

  bash
  sudo apt update
  sudo apt install git
  
</details>

<details>
  <summary><strong>Arch/Manjaro</strong></summary>

  bash
  sudo pacman -S git
  
</details>

<details>
  <summary><strong>Red Hat/Fedora</strong></summary>

  bash
  sudo dnf install git
  
</details>

<details>
  <summary><strong>openSUSE</strong></summary>

  bash
  sudo zypper install git
  
</details>

<details>
  <summary><strong>macOS</strong></summary>

  bash
  brew install git
  
</details>

<details>
  <summary><strong>Windows</strong></summary>

  Download and install Git from the [official website](https://git-scm.com/download/win).

</details>

### 2. Clone the Repository and Run the Script


git clone https://github.com/arijarman/insta-message-sorter
cd insta-message-sorter


### 3. Install Required Python Packages

Ensure you have `BeautifulSoup` installed:


pip install beautifulsoup4


### 4. Run the Script

Make sure to keep the `messages.html` file in the same directory as `main.py`:


python main.py


### 📥 Alternative Method: Manual Download

If you prefer not to use Git, you can manually download the `main.py` file:

1. Go to the [main.py file](https://github.com/arijarman/insta-message-sorter/blob/main/main.py).
2. Copy and paste the code into your local system.

## 📊 Before and After Comparison

Below is a visual comparison of the original Instagram `messages.html` versus the chat-themed format generated by this tool:

| Original Instagram HTML                      | Chat-Themed HTML Generated by the Tool         |
| --------------------------------------------- | ---------------------------------------------- |
| ![Original HTML](https://raw.githubusercontent.com/arijarman/insta-message-sorter/main/web/old.png)       | ![Chat Bubble HTML](https://raw.githubusercontent.com/arijarman/insta-message-sorter/main/web/new.png)     |

## 🎨 How It Works

This script uses **BeautifulSoup** to parse and manipulate the HTML content:

1. **Reverses Message Order**: The script reverses the order from "newest to oldest" to "oldest to newest."
2. **Chat Bubble Format**: Applies custom CSS styles to format messages in a chat-bubble style.
3. **Timezone Conversion**: Uses Python libraries to convert timestamps from Alaska Time to your local timezone.

Simply run the Python script, and it will process all `messages.html` files in the directory!

## 💡 Why Use This Tool?

Reading Instagram chat history manually is cumbersome due to its default formatting. This tool simplifies the entire process, providing a more intuitive and visually appealing format. It’s especially helpful for:

- **Journalists** or **Researchers** analyzing conversations.
- **Data Enthusiasts** exploring chat patterns.
- Anyone who wants to relive their chat moments without scrolling endlessly!

## 🤝 Contributing

We welcome contributions! Feel free to fork the repository, make changes, and submit a pull request. If you find any bugs or have suggestions, please open an issue on GitHub.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## ✨ Acknowledgments

This project was brought to life with the help of ChatGPT, which assisted in generating the code and solving key formatting challenges.

---

Happy Sorting! ✨

