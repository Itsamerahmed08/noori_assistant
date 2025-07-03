# 🌟 Noori Assistant - AI Desktop Voice Assistant

![Noori Logo](assets/logo/logo.png)

**Noori** is a fully-featured desktop voice assistant built using Python. It responds to both voice and text commands, performs smart tasks like opening apps/websites, telling jokes, answering queries via ChatGPT, and even supports toggling features like voice output — all within a modern GUI using `customtkinter`.

---

## ✨ Features

* 🎧 Voice recognition with SpeechRecognition
* 🧠 ChatGPT integration using `openai`
* 🌐 Open websites like Google, YouTube, Instagram, etc.
* 📱 Launch applications from your PC
* 📖 Wikipedia summary on any topic
* 😂 Jokes with `pyjokes`
* 📆 Date & time responses
* 🔊 Voice output ON/OFF toggle
* 🪄 Beautiful modern UI with dark/light themes
* 🖼️ Background image & logo support
* ⚙️ Smart commands like:

  * "Open WhatsApp"
  * "Open Calculator"
  * "Search for pizza near me"
  * "Take a screenshot"
  * "Turn voice off"

---

## 📸 Screenshots

| Main UI                 | Voice Command     |Output Example       |
| ----------------------- | ----------------- |-------------------- |
| ![UI](assets/bg/bg.png) | "open youtube" |
                          |"open camera"   |
                          |"what is the time"|

output: 

![Screenshot 2025-07-03 112745](https://github.com/user-attachments/assets/b4fbd017-ebe6-4abd-a295-ccadfcc0fb4b)



![Screenshot 2025-07-03 113502](https://github.com/user-attachments/assets/9b2ff8fe-fc42-4ba3-b139-6c4d0b644d49)


![image](https://github.com/user-attachments/assets/cccc421c-a343-4186-9ec3-095cdad80fc1)




---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your_username/noori_assistant.git
cd noori_assistant
```

### 2. Create virtual environment

```bash
python -m venv .venv
```

### 3. Activate virtual environment

* **Windows PowerShell:**

```bash
.\.venv\Scripts\Activate.ps1
```

* **CMD:**

```bash
.\.venv\Scripts\activate.bat
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Add your OpenAI API key

In `main.py`, replace `your_openai_api_key_here` with your actual key:

```python
client = openai.OpenAI(api_key="your_openai_api_key_here")
```

---

## 🚀 Run the Assistant

```bash
python main.py
```

---

## 🗂️ Folder Structure

```
noori_assistant/
├── assets/
│   ├── logo/
│   │   └── logo.ico
│   └── bg/
│       └── bg.png
├── main.py
├── requirements.txt
└── README.md
```

---

## 🧐 Voice Commands Examples

* "What time is it?"
* "Tell me a joke"
* "Who is Elon Musk"
* "Open Google"
* "Open YouTube"
* "Turn off voice output"
* "Open WhatsApp"
* "Search nearby cafes"
* "Take screenshot"

---

## 🛠️ Built With

* Python 3.10+
* customtkinter
* speechrecognition
* openai
* pyttsx3
* pywhatkit
* wikipedia
* pyjokes
* pyautogui (for screenshots)
* webbrowser

---

## 📌 To-Do / Enhancements

* Add GUI settings for API key
* Add more smart phone-like commands (e.g., "Call someone")
* Add image generation via DALL·E
* Add notification & weather updates
* Add support for mobile notifications

---

## 🤝 Contributing

Pull requests are welcome! For major changes, open an issue first to discuss what you would like to change.

---

## 📄 License

MIT

---

Made with ❤️ by (https://github.com/itsamerahmed08)
