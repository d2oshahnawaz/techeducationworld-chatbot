import speech_recognition as sr
import pyttsx3
import random
from train_model import predict_intent
from chatbot_model import responses

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Voice settings (better output)
engine.setProperty('rate', 150)
engine.setProperty('volume', 1)

voices = engine.getProperty('voices')
if len(voices) > 1:
    engine.setProperty('voice', voices[1].id)  # female voice (if available)

def speak(text):
    print("Bot:", text)
    engine.say(text)
    engine.runAndWait()

# Initialize recognizer
recognizer = sr.Recognizer()

def listen():
    try:
        with sr.Microphone() as source:
            print("🎤 Listening...")
            
            # reduce noise
            recognizer.adjust_for_ambient_noise(source, duration=1)
            
            audio = recognizer.listen(source, timeout=5)

        text = recognizer.recognize_google(audio)
        print("You:", text)
        return text.lower()

    except sr.WaitTimeoutError:
        print("⏳ Listening timeout...")
        return ""

    except sr.UnknownValueError:
        print("❌ Could not understand audio")
        return ""

    except sr.RequestError:
        print("⚠️ Network error")
        return ""

# Main chatbot loop
print("🤖 Tech Education World Voice Chatbot Started (Say 'bye' to exit)\n")

while True:
    user_input = listen()

    if user_input == "":
        continue

    if user_input in ["bye", "exit", "quit"]:
        speak("Goodbye! Have a nice day.")
        break

    intent = predict_intent(user_input)

    if intent in responses:
        reply = random.choice(responses[intent])
    else:
        reply = "Sorry, I don't understand your question."

    speak(reply)