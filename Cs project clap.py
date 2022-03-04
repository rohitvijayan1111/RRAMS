import tkinter
#import pyaudio
import wavio
import sounddevice as device
import audioop
import numpy as np
import wave
import math
import pyttsx3
import speech_recognition
from threading import *
window= tkinter.Toplevel()
window.title("CLAP_CLAP")#gives name to the interface
window.geometry("803x499")
window.attributes('-topmost',1)# defines the geometry of the interface
bg_canvas4 = tkinter.Canvas(window, bg="black", width=336, height=450, bd=0, highlightthickness=0)
a=""
db=0
sa=""
def text_to_speech(text1) :
    voice_obj=pyttsx3.init()
    voices=voice_obj.getProperty("voices")
    voice_obj.setProperty('voice',voices[0].id)
    voice_obj.setProperty("rate",160)
    voice_obj.say(text1)
    voice_obj.runAndWait()
def clap():
    global a
    global db
    def record():
        fs = 44100  # sampling frequency sometimes it is 44800
        record_time = 4
        recording = device.rec(int(record_time * fs), samplerate=fs, channels=1)
        print("Recording..")
        device.wait()
        print("Recordind over")
        a = "clcl.wav"
        wavio.write(a, recording, fs, sampwidth=2)
    record()

    def findeb(l):
        try:
            wav = wave.open(l, "rb")
            raw = wav.readframes(-1)  # -1 means all the frames to be extracted,returns in byte values
            r = np.frombuffer(raw, "int16")
            sr = wav.getframerate()
            width = wav.getsampwidth()
            rs = audioop.rms(raw, width)  # audioop.rms(wav.readframes(wav.getnframes()), wav.getsampwidth())
            db = 20 * math.log10(rs)
            wav.close()
        except:
            window.withdraw()
            import main
    findeb(a)

    if db >= 65 and db<=80:
        window.withdraw()
        newwin = tkinter.Toplevel(window)
        newwin.title("RRAMS Registration")
        newwin.geometry("803x499")
        newwin.attributes('-topmost', 1)
        def yes():
            text_to_speech("Thanks for using RRams")
            newwin.destroy()

        def no():
            import main
        bg_canvas3 = tkinter.Canvas(newwin, bg="black", width=336, height=450, bd=0, highlightthickness=0)
        bg_canvas3.pack(fill="both", expand=True)
        bg_img4 = tkinter.PhotoImage(file="C:\\Users\\91984\\Downloads\\db.png")
        bg_canvas3.create_text(50, 240, text="Are you sure you want to turn off:", font=('Georgia', 18, "italic"), fill='Red',anchor=tkinter.NW)
        button4 = tkinter.Button(newwin, text="Yes", font=('Georgia', 10, "italic",), bg="black", fg="white",command=yes)
        button5 = tkinter.Button(newwin, text="No", font=('Georgia', 10, "italic",), bg="black", fg="white", command=no)
        bg_canvas3.create_image(150, 10, image=bg_img4, anchor="nw")
        button4.place(x=320, y=320)
        button5.place(x=340, y=340)
    else:
        bg_canvas4.create_text(50, 240, text="Decibel level low", font=('Georgia', 18, "italic"), fill='Red', anchor=tkinter.NW)
        window.withdraw()
        import main




bg_img2 = tkinter.PhotoImage(file="C:\\Users\\91984\\Downloads\\db.png")
bg_img3 = tkinter.PhotoImage(file="C:\\Users\\91984\\Downloads\\clap clap pic.png")

bg_canvas3 = tkinter.Canvas(window, bg="black", width=336, height=450, bd=0, highlightthickness=0)
bg_canvas3.pack(fill="both", expand=True)
bg_canvas3.create_image(150,10,image=bg_img2, anchor="nw")
clap_button=tkinter.Button(window,image=bg_img3,borderwidth=0,width=100,height=100,fg="black",bg="black",command=clap)
clap_button.place(x=350,y=350)

#button2 = tkinter.Button(window, text="RRAMS SOUNDMETER", font=('Georgia', 14, "italic",), bg="black", fg="red",command=thread2)
#button2.place(x=300, y=350)
window.mainloop()
#db from 65-80







