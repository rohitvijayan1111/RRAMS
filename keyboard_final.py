import tkinter
import wavio
from threading import *

window = tkinter.Toplevel()
window.title("keyboard")
window.geometry("633x374")
window_img = tkinter.PhotoImage(file="keyboard1.png")
window_canvas = tkinter.Canvas(window, width=374, height=633, bd=0, highlightthickness=0)
window_canvas.pack(fill="both", expand=True)
window_canvas.create_image(0, 0, image=window_img, anchor="nw")
key = tkinter.PhotoImage(file="key.png")
string = ""
ak = ""


def C():
    global string
    string = string + "C"
    string = string + "-"


def c():
    global string
    string = string + "c"
    string = string + "-"


def D():
    global string
    string = string + "D"
    string = string + "-"


def d():
    global string
    string = string + "d"
    string = string + "-"


def E():
    global string
    string = string + "E"
    string = string + "-"


def e():
    global string
    string = string + "e"
    string = string + "-"


def F():
    global string
    string = string + "F"
    string = string + "-"


def f():
    global string
    string = string + "f"
    string = string + "-"


def G():
    global string
    string = string + "G"
    string = string + "-"


def g():
    global string
    string = string + "g"
    string = string + "-"


def A():
    global string
    string = string + "A"
    string = string + "-"


def a():
    global string
    string = string + "a"
    string = string + "-"


def B():
    global string
    string = string + "B"
    string = string + "-"


def b():
    global string
    string = string + "b"
    string = string + "-"


def save():
    global string
    import numpy
    import tkinter
    import time
    from scipy.io.wavfile import write
    sample = 44000
    global string
    string = string[:-1]

    def popup():
        global ak

        popupwindow = tkinter.Toplevel(window)
        popupwindow.title("Song Output")
        popupwindow.geometry("600x453")
        bg2_img = tkinter.PhotoImage(file="music_bg.png")
        bg2_canvas = tkinter.Canvas(popupwindow, width=600, height=453, bd=0, highlightthickness=0)
        bg2_canvas.pack(fill="both", expand=True)
        bg2_canvas.create_image(0, 0, image=bg2_img, anchor="nw")

        stri = tkinter.StringVar()
        stri.set("")
        def text_get():
            global ak
            ak = stri.get()
            print(ak)
            def waves(freq, duration=0.5):
                amplitude = 4100
                t = numpy.linspace(0, duration, int(sample * duration))
                w = amplitude * numpy.sin(2 * numpy.pi * freq * t)
                return w

            def songs(music):
                notefreq = {'C':261.63,'D':293.66, 'E': 329.63, 'F':349.23,'G':392,'A':440,'B':493.88,'c':523.25,
                            'd':587.33, 'e':659.26, 'f':698.46, 'g':783.99,'a':880, 'b':987.77}
                song = []
                for note in music.split('-'):
                    x = waves(notefreq[note])
                    song.append(x)
                song = numpy.concatenate(song)
                k = song.astype(numpy.int16)
                return k
            def main(name):
                music = string  # To be inputted using mayank's code
                data1 = songs(music)
                name = name + ".wav"
                write(name, sample, data1.astype(numpy.int16))
            main(ak)

        def play_sounds():
            import playsound
            global ak
            try:
                playsound.playsound(ak + ".wav")
                window.destroy()

            except:
                print("Music is over")
        textbox1 = tkinter.Entry(popupwindow, textvariable=stri, width=40)
        button1 = tkinter.Button(popupwindow, text="Ok",font=('Georgia', 12), command=text_get)
        bg2_canvas.create_text(50,200, text="Give the Song Name:", font=('Georgia', 18), fill='Black', anchor=tkinter.NW)
        button1.place(x=550,y=200)
        textbox1.place(x=300,y=205)

        button2 = tkinter.Button(popupwindow, text="  Play music  ",font=('Georgia', 16), command=play_sounds)
        button2.place(x=240,y=250)

        popupwindow.mainloop()
    popup()


def delete():
    window.withdraw()


button_1=tkinter.Button(window,image=key,borderwidth=0,width=44,height=98,fg="black",activebackground="blue2",command=C)
button_1.place(x=0,y=242)
button_2=tkinter.Button(window,image=key,borderwidth=0,width=44,height=98,fg="black",activebackground="blue2",command=D)
button_2.place(x=46,y=242)
button_3=tkinter.Button(window,image=key,borderwidth=0,width=44,height=98,fg="black",activebackground="blue2",command=E)
button_3.place(x=92,y=242)
button_4=tkinter.Button(window,image=key,borderwidth=0,width=44,height=98,fg="black",activebackground="blue2",command=F)
button_4.place(x=138,y=242)
button_5=tkinter.Button(window,image=key,borderwidth=0,width=44,height=98,fg="black",activebackground="blue2",command=G)
button_5.place(x=184,y=242)
button_6=tkinter.Button(window,image=key,borderwidth=0,width=44,height=98,fg="black",activebackground="blue2",command=A)
button_6.place(x=230,y=242)
button_7=tkinter.Button(window,image=key,borderwidth=0,width=44,height=98,fg="black",activebackground="blue2",command=B)
button_7.place(x=276,y=242)
button_8=tkinter.Button(window,image=key,borderwidth=0,width=44,height=98,fg="black",activebackground="blue2",command=c)
button_8.place(x=322,y=242)
button_9=tkinter.Button(window,image=key,borderwidth=0,width=44,height=98,fg="black",activebackground="blue2",command=d)
button_9.place(x=368,y=242)
button_10=tkinter.Button(window,image=key,borderwidth=0,width=44,height=98,fg="black",activebackground="blue2",command=e)
button_10.place(x=414,y=242)
button_11=tkinter.Button(window,image=key,borderwidth=0,width=44,height=98,fg="black",activebackground="blue2",command=f)
button_11.place(x=460,y=242)
button_12=tkinter.Button(window,image=key,borderwidth=0,width=44,height=98,fg="black",activebackground="blue2",command=g)
button_12.place(x=506,y=242)
button_13=tkinter.Button(window,image=key,borderwidth=0,width=44,height=98,fg="black",activebackground="blue2",command=a)
button_13.place(x=552,y=242)
button_14=tkinter.Button(window,image=key,borderwidth=0,width=44,height=98,fg="black",activebackground="blue2",command=b)
button_14.place(x=598,y=242)
button_14=tkinter.Button(window,text=" Save ",borderwidth=0,fg="black",activebackground="blue2",command=save)
button_14.place(x=595,y=0)
"""def thread():
    Thread(target=popup()).start()
    Thread(target=delete()).start()
"""
window.mainloop()
