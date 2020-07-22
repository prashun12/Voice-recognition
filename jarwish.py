import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import requests



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")
    speak("I am jarwish sir. please tell me how I help you")

def takeCommand():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,key=None,language="en-US",show_all= False)
        print (f"User said: {query}\n")

    
    except Exception as e:
        # print(e)


        print("say that again please...")
        return "None"
    return query             

if __name__== "__main__":
    wishMe() 
    while True:
        # if = 1:
        query = takeCommand().lower()
        # Logic for executing takes based on query
        if "how are you" in query:
            speak("I am fine sir,how can i help you?")
        elif "who  are you?" in query:
            speak("I am desktop assistence jarvis , made by Mr Vivek.")
            

        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query , sentences = 2)
            speak("According to Wikipedia")
            speak(results)
            print(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open microsoft' in query:
            webbrowser.open("microsoft.com")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime} ")
        elif 'open code' in query:
            codePath= "a\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

            
    