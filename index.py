
# pip install pyaudio

import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
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

    speak("I am Monojit. Hello Sir or Mam Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

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
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        

     

        elif'open my website' in query:
            webbrowser.open("https://bbianstudymaterial.github.io/bbchome/")
        elif'open notes' in query:
            webbrowser.open('https://bbianstudymaterial.github.io/bscitnotes/')
        elif'open note' in query:
            webbrowser.open('https://bbianstudymaterial.github.io/bscitnotes/')
        elif'open nots' in query:
            webbrowser.open('https://bbianstudymaterial.github.io/bscitnotes/')
        elif'open not' in query:
            webbrowser.open('https://bbianstudymaterial.github.io/bscitnotes/')
        elif'open no' in query:
            webbrowser.open('https://bbianstudymaterial.github.io/bscitnotes/')
         
        elif'notes' in query:
            webbrowser.open('https://bbianstudymaterial.github.io/bscitnotes/')
        elif'no' in query:
            webbrowser.open('https://bbianstudymaterial.github.io/bscitnotes/')
        elif'notess' in query:
            webbrowser.open('https://bbianstudymaterial.github.io/bscitnotes/')
         
        elif'open Previous ' in query:
            webbrowser.open('https://bbianstudymaterials.github.io/codingwithm/')
        elif'open Pre' in query:
            webbrowser.open('https://bbianstudymaterials.github.io/codingwithm/')
        elif'open Year' in query:
            webbrowser.open('https://bbianstudymaterials.github.io/codingwithm/')
        
       )
        elif'open Question' in query:
            webbrowser.open('https://bbianstudymaterials.github.io/codingwithm/')
        elif'Previous' in query:
            webbrowser.open('https://bbianstudymaterials.github.io/codingwithm/')
        elif'Year' in query:
            webbrowser.open('https://bbianstudymaterials.github.io/codingwithm/')
        elif'pyq' in query:
            webbrowser.open('https://bbianstudymaterials.github.io/codingwithm/')
        elif'Previous Year Question' in query:
            webbrowser.open('https://bbianstudymaterials.github.io/codingwithm/')
        elif'previousyearquestion' in query:
            webbrowser.open('https://bbianstudymaterials.github.io/codingwithm/')
        elif'previousyear' in query:
            webbrowser.open('https://bbianstudymaterials.github.io/codingwithm/')
        elif'previous' in query:
            webbrowser.open('https://bbianstudymaterials.github.io/codingwithm/')
        




        elif 'open google' in query:
            webbrowser.open("google.com")

      


       

        elif 'Thanks' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "monojityengkhom7@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")    
        else:
            print("No query matched")