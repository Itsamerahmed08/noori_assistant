import customtkinter as ctk
import threading
import pyttsx3
import speech_recognition as sr
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import os
import openai
from PIL import Image, ImageTk

# Initialize TTS
engine = pyttsx3.init()
engine.setProperty('rate', 175)

def speak(text):
    output_box.insert(ctk.END, f"NOORI: {text}\n")
    output_box.see(ctk.END)
    if voice_enabled.get():
        engine.say(text)
        engine.runAndWait()

# Initialize OpenAI Client
client = openai.OpenAI(api_key="your_openai_key")

# Command Handler
recognizer = sr.Recognizer()

def take_command():
    with sr.Microphone() as source:
        output_box.insert(ctk.END, "NOORI: \U0001F3A4 Listening...\n")
        output_box.see(ctk.END)
        try:
            audio = recognizer.listen(source, timeout=15)
            query = recognizer.recognize_google(audio)
            output_box.insert(ctk.END, f"You: {query}\n")
            return query.lower()
        except sr.WaitTimeoutError:
            speak("Timeout. Please try again.")
        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand.")
        return ""

def run_command():
    query = take_command()
    if not query:
        return

    if 'play' in query:
        song = query.replace('play', '')
        speak(f'Playing {song}')
        pywhatkit.playonyt(song)

    elif 'time' in query:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak(f'Current time is {time}')

    elif 'who is' in query:
        person = query.replace('who is', '')
        try:
            info = wikipedia.summary(person, 1)
            speak(info)
        except:
            try:
                chat_response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": f"Who is {person}?"}]
                )
                speak(chat_response.choices[0].message.content)
            except:
                speak("Couldn't find info on that person.")

    elif 'say a joke' in query:
        speak(pyjokes.get_joke())

    elif 'open youtube' in query:
        webbrowser.open('https://youtube.com')
        speak("Opening YouTube")

    elif 'open google' in query:
        webbrowser.open('https://google.com')
        speak("Opening Google")

    elif 'open whatsapp' in query:
        webbrowser.open('https://web.whatsapp.com')
        speak("Opening WhatsApp")

    elif 'open instagram' in query:
        webbrowser.open('https://instagram.com')
        speak("Opening Instagram")

    elif 'open camera' in query:
        os.system("start microsoft.windows.camera:")
        speak("Opening Camera")

    elif 'shutdown' in query:
        speak("Shutting down. Goodbye!")
        app.destroy()

    else:
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": query}]
            )
            speak(response.choices[0].message.content)
        except:
            speak("Sorry, ChatGPT is currently unavailable.")

# GUI
app = ctk.CTk()
app.title("NOORI Assistant")
app.geometry("720x500")

# Logo and background
bg_image = ctk.CTkImage(Image.open("assets/bg.png"), size=(720, 500))
bg_label = ctk.CTkLabel(app, image=bg_image, text="")
bg_label.place(x=0, y=0)

logo = ctk.CTkImage(Image.open("assets/logo.ico"), size=(100, 100))
logo_label = ctk.CTkLabel(app, image=logo, text="")
logo_label.place(x=20, y=10)

# Output box
output_box = ctk.CTkTextbox(app, width=600, height=280, corner_radius=10)
output_box.place(x=60, y=120)
output_box.insert(ctk.END, "NOORI: Hey there! I'm Noori – your smart assistant. Ready when you are.\n")

# Voice toggle
voice_enabled = ctk.BooleanVar(value=True)
toggle = ctk.CTkSwitch(app, text="Voice", variable=voice_enabled)
toggle.place(x=600, y=30)

# Listen Button
listen_button = ctk.CTkButton(app, text="\U0001F399️ Start Listening", command=lambda: threading.Thread(target=run_command).start(), font=("Arial", 16))
listen_button.place(x=270, y=420)

app.mainloop()
