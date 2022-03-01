import math
import wave
import numpy as np
import wavio
import sounddevice as device
import matplotlib.pyplot as plt
import audioop
import speech_recognition as sr
import pyttsx3
import tkinter
a=sr.Recognizer()#this creates an object
extract_text=""
def text_to_speech(text1) :
    voice_obj=pyttsx3.init()
    voices=voice_obj.getProperty("voices")
    voice_obj.setProperty('voice',voices[0].id)
    voice_obj.setProperty("rate",160)
    voice_obj.say(text1)
    voice_obj.runAndWait()

def output_text(texts):
    global x,y
    print(len(texts))
    if len(texts) <32:
        bg_canvas.create_text(x,y,text=texts,font=('Georgia',14),fill='white',anchor=tkinter.NW)
        #typing_effect(texts)
        y = y + 20
    else:
        x=40
        text_list=texts.split()
        length=0
        str=""
        str2=""
        z=0
        change(texts)

    #x=x+30
def change(texts):
    global x,y,z
    text_list = texts.split()
    str = ""
    str2 = ""
    z=0
    length = 0
    while z < len(text_list)-1 and length < 32:
        length = length + len(text_list[z]) + 1
        str = str + " " + text_list[z]
        z = z + 1
    else:
        for b in text_list[z:]:
            str2 = str2 + " " + b
    bg_canvas.create_text(x, y, text=str, font=('Georgia',14), fill='white', anchor=tkinter.NW)
    y=y+20

    if len(str2)<32:
        bg_canvas.create_text(x, y, text=str2, font=('Georgia',14), fill='white', anchor=tkinter.NW)
    else:
        change(str2)
    y=y+20


def record():
    fs = 44100  # sampling frequency sometimes it is 44800
    record_time = 10
    recording = device.rec(int(record_time * fs), samplerate=fs, channels=1)

    print("Recording..")
    device.wait()
    print("Recordind over")
    a = input("Enter the name of the file to be stored") + ".wav"
    wavio.write(a, recording, fs, sampwidth=2)
    return a

def findeb(a):
    wav = wave.open(a, "rb")
    raw = wav.readframes(-1)  # -1 means all the frames to be extracted,returns in byte values
    r = np.frombuffer(raw, "int16")
    sr = wav.getframerate()
    width = wav.getsampwidth()
    if wav.getnchannels()==1:
        print("Mono file detected")
        rs = audioop.rms(raw, width)  # audioop.rms(wav.readframes(wav.getnframes()), wav.getsampwidth())
        print("The rms value of wave is", rs)
        db = 20 * math.log10(rs)
        print("The decibel value of wave is ", db)
    elif wav.getnchannels()==2:
        print("""Stereo file detected 
        Do you want to continue,then input a mono audio file YES/NO""")
        ch=input("Enter a mono audiofile ").upper()
        if ch == "YES":
            c=input("Enter a mono audio file")
            findeb(c)
        elif ch == "NO":
            wav.close()
            return
    wav.close()
"""
def timer(t):
    while t:
        mins, secs = divmod(t, 60)
        tr = '{:02d}:{:02d}'.format(mins,secs)
        time.sleep(1)
        t -= 1
"""
def showgraph(a):
    wav = wave.open(a, "r")
    raw = wav.readframes(-1)  # -1 means all the frames to be extracted,returns in byte values
    r = np.frombuffer(raw, "int16")
    sr = wav.getframerate()
    t=np.linspace(0,len(r)/sr,num=len(r))#this formula gives the duration of the wave  x coordinates
    plt.title("wave file")
    plt.plot(t,r,color="blue")#t-x r-y
    plt.ylabel("Amplitude")
    plt.xlabel("Time")#in seconds
    t = int(input("Enter the duration of the graph to be shown"))
    plt.show()  # x axis shows no of frames without labe
    wav.close()
b=record()
findeb(b)
showgraph(b)
#20 * Math. Log10(rms)



