# MEGA PROJECT IN PYTHON :> DESKTOP VOICE ASSISTANCE [ IRON MAN : JARVIS]
import pyttsx3 # type: ignore
import speech_recognition as sr  # type: ignore
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12 :
        speak("Good Morning Boss!")
    elif hour >= 12 and hour < 18 :
        speak("Good Afternoon Boss!")
    else:
        speak("Good Evening Boss!")

    speak("I am Jarvis. Please tell me how can i help you !")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            print(e)
            print("Say that again please...")
            return "None"
        return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()