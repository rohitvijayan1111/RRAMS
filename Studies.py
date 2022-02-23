import math
import wave
import numpy as np
import sys
import matplotlib.pyplot as plt
#import scipy
#i.mport math
import audioop
import time
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
#
def timer(t):
    while t:
        mins, secs = divmod(t, 60)
        tr = '{:02d}:{:02d}'.format(mins,secs)
        time.sleep(1)
        t -= 1
#
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
k="amma.wav"
findeb(k)
showgraph(k)
#20 * Math. Log10(rms)

