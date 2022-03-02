import tkinter #for UI
import datetime #for time
import speech_recognition
import playsound
import pyttsx3
from threading import *
 #control and monitor input devices
#window= tkinter.Tk()
window= tkinter.Toplevel()
window.title("RRAMS")#gives name to the interface
window.geometry("803x499")
window.attributes('-topmost',1)# defines the geometry of the interface
x=42
y=80
#creates an object for storing image
#bg_label=tkinter.Label(window,image=bg_img)
#bg_label.place(x=0,y=0)

def output_text(texts):
    global x,y
    if len(texts) <32:
        bg_canvas.create_text(x,y,text=texts,font=('Georgia',14,"italic"),fill='white',anchor=tkinter.NW)
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
    while z < len(text_list)-1 and length < 70:
        length = length + len(text_list[z]) + 1
        str = str + " " + text_list[z]
        z = z + 1
    else:
        for b in text_list[z:]:
            str2 = str2 + " " + b
    bg_canvas.create_text(x, y, text=str, font=('Georgia',14,"italic"), fill='white', anchor=tkinter.NW)
    y=y+20

    if len(str2)<32:
        bg_canvas.create_text(x, y, text=str2, font=('Georgia',14,"italic"), fill='white', anchor=tkinter.NW)
    else:
        change(str2)
    y=y+20

def text_to_speech(text1) :
    voice_obj=pyttsx3.init()
    voices=voice_obj.getProperty("voices")
    voice_obj.setProperty('voice',voices[0].id)
    voice_obj.setProperty("rate",160)
    voice_obj.say(text1)
    voice_obj.runAndWait()

def one():
    window.destroy()
def sptx():
    output_text("hello")
    text_to_speech("hello")
def thread():
    Thread(target=output_text("hello this is rrams")).start()
    Thread(target=playsound.playsound("C:\\Users\\91984\\Downloads\\sound.mp3"))
    Thread(target=text_to_speech("hello this is rrams")).start()
    button_2.destroy()
bg_img=tkinter.PhotoImage(file="C:\\Users\\91984\\Downloads\\bg (1).png")
bg_canvas=tkinter.Canvas(window,bg="#000d3c",width=336,height=450,bd=0,highlightthickness=0)
bg_canvas.pack(fill="both",expand=True)
bg_canvas.create_image(0,0,image=bg_img,anchor="nw")
button_1=tkinter.Button(window,text="Next",borderwidth=0,font=('Georgia',10,"italic","bold"),width=5,bg="#060c40",height=2,fg="white",command=one)
button_1.place(x=670,y=400)
button_2=tkinter.Button(window,text="ARE YOU READY TO BEGIN YOUR MUSIC JOURNEY",borderwidth=0,font=('Georgia',10,"italic","bold"),bg="#060c40",fg="white",command =thread)
button_2.place(x=200,y=240)
window.mainloop()
