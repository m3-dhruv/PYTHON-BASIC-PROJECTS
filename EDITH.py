# EDITH = advance desktop assistance and ai
import pyttsx3
import speech_recognition as sr  
import datetime
import wikipedia
import webbrowser
import os
import openai


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

    speak("I am EDITH AI")
  

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
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


if __name__ == '__main__':
   wishMe()
   while True:
        query = takeCommand().lower()
        sites = [["youtube", "youtube.com"],
                ["google","google.com"],
                ["facebook","facebook.com"],
                ["instagram","instagram.com"],
                ["twitter","twitter.com"],
                ["whatsapp","web.whatsapp.com"],
                ["github","github.com"],
                ["linkedin","linkedin.com"]]
        for site in sites:
            if f"open {site[0]}" in query:
                speak(f"opening {site[0]} boss...")
                webbrowser.open(site[1])

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'play music' in query:
            music_dir = 'C:\\Users\\HP\\Music\\Songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        
        elif 'the time' in query:
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            speak(f"Boss, The time is {hour} hour and {min} minutes")

        elif 'open vs code' in query:
            codePath = "C:\\Users\\panch\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak(  "opening vs code boss...")
            os.startfile(codePath)

        