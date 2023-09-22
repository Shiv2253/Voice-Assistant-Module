import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")

    else:
        speak("Good Evening Sir!")

    speak("I am Jarvis Please tell me how may I help you")

def takeCommand():
    # It take microphone input from the user and returns string 
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        # sr.energy_threshold = 100
        sr.pause_threshold = 1     # Energy threshold will be used to control voice volume and noise
        audio = r.listen(source)

    try:
        print("Recongnizing....")
        query = r.recognize_google(audio, Language ='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please....")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences = 2)
            speak("Acccording to wkipedia")
            print(results)
            speak(results)
        
        # elif 'open youtube' in query:
        #     webbrowser.open("youtube.com")

        # elif 'open google' in query:
        #     webbrowser.open("google.com")

        # elif 'open stackoverflow' in query:
        #     webbrowser.open("stackoverflow.com")
            
        # elif 'play music' in query:
        #     music_dir = 'E:\ \Music'
        #     songs = os.listdir(music_dir)
        #     print(songs)
        #     os.startfile(os.path.join(music_dir, songs[0]))      #use random number by import random

        # elif 'the time' in query:
        #     strTime = datetime.datetime.now().strfTime("%H:%M")
        #     speak(f"The time is {strTime} ")
        
        # elif 'open vs code' in query:
        #     codePath = "C:\\sers\\Lenovo\\AppData\\Local\\Programs\\Microsoft VS Code"
        #     os.startfile(codePath)








