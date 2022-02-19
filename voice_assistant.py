import tkinter #for UI
import datetime #for time
import  sys,os,time
import webbrowser
import pynput #control and monitor input devices
window= tkinter.Toplevel()
#window= tkinter.Toplevel()
window.title("Voice assistant")#gives name to the interface
window.geometry("336x450") # defines the geometry of the interface
window.attributes('-topmost',1)#to be the first window visible
bg_img=tkinter.PhotoImage(file="voice_background.png") #creates an object for storing image
#bg_label=tkinter.Label(window,image=bg_img)
#bg_label.place(x=0,y=0)
bg_canvas=tkinter.Canvas(window,width=336,height=450,bd=0,highlightthickness=0)
bg_canvas.pack(fill="both",expand=True)
bg_canvas.create_image(0,0,image=bg_img,anchor="nw")
text_canvas=tkinter.Canvas(window,width=336,height=350,bd=0,highlightthickness=0)
text_canvas.pack(fill="both",expand=True)
""" 
def round_rectangle(x1, y1, x2, y2, r=25, **kwargs):
    points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
    return bg_canvas.create_polygon(points, **kwargs, smooth=True)
round_rectangle(40,80,270,130, r=20, fill="#fd3a46",outline="#fd3a46",width="3")
"""
#for input
"""
input=tkinter.Entry(window,width=30,borderwidth=0)
input.place(x=50,y=390,height=25)
input.insert(0,"Search..")
def  three():
    print(input.get())
"""
x=45
y=80
"""

"""
def output_text(texts):
    global x,y
    print(len(texts))
    if len(texts) <32:
        bg_canvas.create_text(x,y,text=texts,font=('calibri',16),fill='white',anchor=tkinter.NW)
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
        """
        while z<len(text_list)-1 and length<27 :
            length=length+len(text_list[z])+1
            str=str+" "+text_list[z]
            z=z+1
        else:
            for b in text_list[z:]:
                str2=str2+" "+b
        bg_canvas.create_text(x, y, text=str, font=('calibri', 16), fill='white', anchor=tkinter.NW)
        #typing_effect(str)
        y=y+30
        print(str)
        print(str2)
        bg_canvas.create_text(x, y, text=str2, font=('calibri', 16), fill='white', anchor=tkinter.NW)
        y=y+30
        """
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
    bg_canvas.create_text(x, y, text=str, font=('calibri', 16), fill='white', anchor=tkinter.NW)
    y=y+20

    if len(str2)<32:
        bg_canvas.create_text(x, y, text=str2, font=('calibri', 16), fill='white', anchor=tkinter.NW)
    else:
        change(str2)
    y=y+20
print("len:",len("Hi this is Voice Assistance .."))
output_text("Hi this is your  Voice Assistance ")
#output_text("This is Rohit How can i help you?")

def clock():
    t=datetime.datetime.now()
    hour=str(t.hour)
    minute=str(t.minute)
    second=str(t.second)
    if len(hour)==1:
        hour="0"+hour
    if len(minute)==1:
        minute= "0" + minute
    if len(second)==1:
        second="0"+second

    current_time=str(hour)+":"+str(minute)+":"+str(second)
    bg_canvas.itemconfig(time_text,text=current_time)
    window.after(1000,clock)
time_text=bg_canvas.create_text(250,55,text="",font = ('calibri', 20),fill= 'white')

#MIC
from speech_recognition import *
import pyttsx3
a=Recognizer()#this creates an object
extract_text=""

def text_to_speech(text1) :
    voice_obj=pyttsx3.init()
    voices=voice_obj.getProperty("voices")
    voice_obj.setProperty('voice',voices[1].id)
    voice_obj.setProperty("rate",160)
    voice_obj.say(text1)
    voice_obj.runAndWait()

def open():
    global extract_text
    output_text(extract_text)
    extract_text = extract_text.lower()
    print(extract_text)
    if "calculator" in extract_text:
        text_to_speech("opening calculator")
        output_text("opening calculator")
        os.system("Calc.exe")
    elif extract_text in ("open teams","open team","open microsoft teams","open microsoft team")  :
        print("Working")
        text_to_speech("opening microsoft teams")
        output_text("opening microsoft teams")
        time.sleep(3)
        os.system(r'C:\Users\rohit\AppData\Local\Microsoft\Teams\Update.exe --processStart "Teams.exe"')
    elif "google chrome" in extract_text:
        text_to_speech("opening google chrome")
        output_text("opening google chrome")
        os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
    elif "python" in extract_text:
        text_to_speech("opening python ")
        output_text("opening python ")
        #os.startfile(r"C:\Users\rohit\AppData\Local\Programs\Python\Python37\pythonw.exe")
        os.startfile(r"C:\Users\rohit\AppData\Local\Programs\Python\Python39\Lib\idlelib\idle.py")

    #   elif "edge" in extract_text:
    #        os.startfile("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
    elif "note" in extract_text:
        text_to_speech("opening Onenote")
        output_text("opening Onenote")
        os.startfile("C:\Program Files\Microsoft Office\root\Office16\ONENOTE.EXE")
        #os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\OneNote.exe")

    elif "powerpoint" in extract_text:
        text_to_speech("opening powerpoint")
        output_text("opening powerpoint ")
        os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE")
    elif extract_text in ("open microsoft word" ,"open word"):
        text_to_speech("opening word")
        output_text("opening word") 
        os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE")
    elif "start" in extract_text:
        text_to_speech("opening start")
        output_text("opening start")
        keyboard = pynput.keyboard.Controller()
        keyboard.press(pynput.keyboard.Key.cmd)
        keyboard.release(pynput.keyboard.Key.cmd)
        """
        keyboard = Controller()
        keyboard.press(Key.cmd)
        keyboard.release(Key.cmd)
        """
    elif "system volume" in extract_text:
        no= [int(i) for i in extract_text.split() if i.isdigit()]
        print("no:",no)
        x=no[0]
        y=x[0]
        print(x)
        if x % 2 == 0:
            x = x // 2
        else:
            x = x // 2 + 1
        print(x)
        keyboard = pynput.keyboard.Controller()
        for b in range(50):
            keyboard.press(pynput.keyboard.Key.media_volume_down)
            keyboard.release(pynput.keyboard.Key.media_volume_down)

        for b in range(x):
            keyboard.press(pynput.keyboard.Key.media_volume_up)
            keyboard.release(pynput.keyboard.Key.media_volume_up)
        text_to_speech("adjusted volume to"+str(y))
        output_text("adjusted volume to"+str(y))

    elif "settings" in extract_text:
        keyboard.press(Key.cmd)
        keyboard.press('i')
        keyboard.release(Key.cmd)
        keyboard.release('i')
        text_to_speech("opening settings")
        output_text("opening settings")

    elif "brightness" in extract_text:
        keyboard.press(Key.cmd)
        keyboard.press("a")
        keyboard.release(Key.cmd)
        keyboard.release("a")
        text_to_speech("brightness slider at bottom right.")
        output_text("brightness slider at bottom right.")

    elif "wi-fi" in extract_text:
        from pynput.mouse import Button, Controller
        keyboard.press(Key.cmd)
        keyboard.press('i')
        keyboard.release(Key.cmd)
        keyboard.release('i')
        mouse = Controller()
        mouse.position = (612, 227)
        mouse.click(Button.right, 1)
        keyboard.type("wifi settings")
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
    elif "Microsoft edge" in extract_text:
        import webbrowser
        edge_path = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
        webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))
        webbrowser.get('edge').open('http://www.microsoft.com')
    else:
        import webbrowser
        user_query = extract_text
        user = ""
        for b in user_query.split():
            user = user + "+" + b
        user = user[1::]
        print(user)
        URL = "https://www.google.com/search?q=" + user_query
        webbrowser.open(URL)

import pyaudio
count=0
def Microphone_click():
    global count
    count=count+1
    if count>3:
        window.destroy()
        os.system("voice_assistant.py")
        microphone_click()
    global extract_text
    with Microphone() as b:
        text_to_speech("speak please")
        a.adjust_for_ambient_noise(b)  # handles Noise
        Audio=a.listen(b)  # captures audio
        print("converting speech to text..")
        try:
            extract_text=a.recognize_google((Audio))
        except:
            print("try again")
            microphone_click()
    open()

mic_img=tkinter.PhotoImage(file="mic_check.png") #creates an object for storing image
#bg_canvas.create_image(90,300,image=mic_img,anchor="nw")
time.sleep(1)
mic_button=tkinter.Button(window,image=mic_img,borderwidth=0,width=41,height=74,fg="black",command=Microphone_click)
mic_button.place(x=143,y=340)

"""
temp=str(datetime.date.today())
date=temp[-2:]+"-"+temp[5:7]+"-"+temp[0:4]
time_date=bg_canvas.create_text(245,55,text=date,font = ('calibri', 18),fill= 'white')
"""
clock()
window.mainloop()
