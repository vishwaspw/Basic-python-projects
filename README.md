# 🐍 Basic Python Projects

Welcome to the **Basic Python Projects** repository! This collection contains beginner to intermediate-level Python scripts — including automation tools, mini-games, image processing, GUIs, and more.

---

## 📁 Project List

Each project below is described with its input, output, required dependencies, and special file requirements.

---

### 1. `alarm_clock.py`
- ⏰ **Description**: Plays an alarm sound at a specific time.
- 📥 **Input**: User-defined alarm time in `HH:MM` format
- 📎 **Files Used**: `sound.wav`
- ⚙️ **Dependencies**: `datetime`, `time`, `playsound`
- 💡 **Output**: Rings alarm with `.wav` sound at the given time

---

### 2. `chatgpt.py`
- 🤖 **Description**: OpenAI ChatGPT prompt interface
- 📥 **Input**: Text prompt
- ⚙️ **Dependencies**: `openai`
- 🗝️ Requires API key
- 💡 **Output**: Text response generated by ChatGPT

---

### 3. `convert_image-sketch.py`
- 🖼️ **Description**: Converts an image into a pencil sketch
- 📥 **Input**: An image file (`img_61.png`)
- ⚙️ **Dependencies**: `cv2`, `numpy`
- 💡 **Output**: A sketch version of the input image (`sketch.png` or shown via OpenCV)

---

### 4. `creating_watermark.py`
- 💧 **Description**: Adds watermark text to an image
- 📥 **Input**: Image file and watermark text
- ⚙️ **Dependencies**: `PIL`
- 💡 **Output**: Image saved with watermark

---

### 5. `digital_clock.py`
- ⌚ **Description**: Digital clock GUI that displays real-time
- 📥 **Input**: None
- ⚙️ **Dependencies**: `tkinter`
- 💡 **Output**: Real-time clock in a GUI window

---

### 6. `Drawing_turtle.py`
- 🐢 **Description**: Uses Turtle graphics to draw patterns
- 📥 **Input**: None
- ⚙️ **Dependencies**: `turtle`
- 💡 **Output**: Opens a Turtle window with generated art

---

### 7. `gui_stopwatch.py`
- ⏱️ **Description**: GUI-based stopwatch
- 📥 **Input**: Start, stop, reset button clicks
- ⚙️ **Dependencies**: `tkinter`
- 💡 **Output**: Functional stopwatch GUI

---

### 8. `image-pdf.py`
- 📄 **Description**: Converts images to a single PDF
- 📥 **Input**: Image files (e.g., `.jpg`)
- ⚙️ **Dependencies**: `PIL`
- 💡 **Output**: PDF file containing the images

---

### 9. `insta_account_details.py`
- 📸 **Description**: Extracts public Instagram profile data
- 📥 **Input**: Instagram username
- ⚙️ **Dependencies**: `instaloader`
- 💡 **Output**: Username, followers, posts, bio etc., printed in terminal

---

### 10. `lang_detect.py`
- 🌐 **Description**: Detects the language of a given sentence
- 📥 **Input**: A text sentence
- ⚙️ **Dependencies**: `langdetect`
- 💡 **Output**: Predicted language (e.g., English, French)

---

### 11. `otp_verification.py`
- 🔐 **Description**: Sends OTP to email and verifies input
- 📥 **Input**: Email address and OTP from user
- ⚙️ **Dependencies**: `smtplib`, `random`, `email.message`
- 💡 **Output**: Prints verification success/failure

---

### 12. `phone_no-info.py`
- 📞 **Description**: Displays location and carrier of phone numbers
- 📥 **Input**: Phone number with country code
- ⚙️ **Dependencies**: `phonenumbers`
- 💡 **Output**: Country, carrier, and region of phone number

---

### 13. `plagarism_detect.py`
- 📑 **Description**: Checks similarity between text documents
- 📥 **Input**: Text files (`text.txt`)
- ⚙️ **Dependencies**: `difflib`
- 💡 **Output**: Plagiarism percentage or similarity score

---

### 14. `quiz_app.py`
- ❓ **Description**: Multiple-choice quiz in a GUI
- 📥 **Input**: Answer selections (buttons)
- ⚙️ **Dependencies**: `tkinter`
- 💡 **Output**: Final score and correct answers shown at end

---

### 15. `rock_paper_scissor.py`
- ✊✋✌️ **Description**: Rock-paper-scissors game with user vs. computer
- 📥 **Input**: User's choice (rock/paper/scissors)
- ⚙️ **Dependencies**: `random`
- 💡 **Output**: Game result printed on terminal

---

### 16. `scientific_calculator.py`
- ➗ **Description**: GUI-based calculator with scientific functions
- 📥 **Input**: Button clicks (numbers/operators)
- ⚙️ **Dependencies**: `tkinter`, `math`
- 💡 **Output**: Display of computed result on GUI

---

### 17. `send_whatsapp_msg.py`
- 💬 **Description**: Sends scheduled WhatsApp messages
- 📥 **Input**: Phone number, message, time
- ⚙️ **Dependencies**: `pywhatkit`
- 💡 **Output**: WhatsApp web opens & sends the message

---

### 18. `text-speech.py`
- 🗣️ **Description**: Converts input text into audible speech
- 📥 **Input**: String of text
- ⚙️ **Dependencies**: `pyttsx3`
- 💡 **Output**: Spoken audio using system voice

---

### 19. `wifi_password.py`
- 🔐 **Description**: Retrieves saved WiFi passwords (Windows only)
- 📥 **Input**: None
- ⚙️ **Dependencies**: `subprocess`, `re`
- 💡 **Output**: Network names & passwords printed on terminal

---

### 20. `word_cloud.py`
- ☁️ **Description**: Generates a word cloud from a given text
- 📥 **Input**: Text string or file
- ⚙️ **Dependencies**: `wordcloud`, `matplotlib`, `PIL`
- 💡 **Output**: Displays and/or saves word cloud image

---

## ⚙️ Setup Instructions

```bash
# Clone the repository
git clone https://github.com/vishwaspw/Basic-python-projects.git
cd Basic-python-projects

# (Optional) Set up virtual environment
python -m venv venv
venv\Scripts\activate  # Windows

# Manually install packages as per project
pip install -r requirements.txt  # (If you create one)
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Author**: Vishwas R

## Contributions

Contributions are welcome! If you want to contribute, follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a new Pull Request.

## YAML Configuration

Here is an example of the YAML configuration for the project:

```yaml
name: Basic Python Projects
version: 1.0
license: MIT
author:
  name: Vishwas R
  email: vishwasramesh939@gmail.com
contributions:
  - Fork the repository.
  - Create a new branch.
  - Commit your changes.
  - Push your branch.
  - Create a pull request.```
