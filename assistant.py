import speech_recognition as sr
import pyttsx3
import os

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 0.8
        audio = r.listen(source)
        try:
            print("Recognizing")
            Query = r.recognize_google(audio, language='en-in')
            print("the query is printed='", Query, "'")
        except Exception as e:
            print(e)
            print("Try again")
            return "None"
    return Query
command()

def Speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait()


def shutdown(self):
    self.Speak("do u want to switch off ?")
    take = command()
    choice = take
    if choice.lower() == 'yes':
        print("Shutting down the computer")
        self.Speak("Shutting the computer")
        os.system("shutdown /s /t 30")
    if choice == 'no':
        print("Okay")
        self.Speak("Okay")


