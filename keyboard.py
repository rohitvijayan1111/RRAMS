import tkinter #for UI
import time #for time
window= tkinter.Toplevel()
window.title("keyboard")#gives name to the interface
window.geometry("1587x374") # defines the geometry of the interface
bg_img=tkinter.PhotoImage(file="keyboard.png") #creates an object for storing image
bg_canvas=tkinter.Canvas(window,width=374,height=1587,bd=0,highlightthickness=0)
bg_canvas.pack(fill="both",expand=True)
bg_canvas.create_image(0,0,image=bg_img,anchor="nw")
key=tkinter.PhotoImage(file="key.png") #creates an object for storing image
string=""
def C():
    global string
    string=string+"C"
    print(string)
def c():
    global string
    string=string+"c"
    print(string)
def D():
    global string
    string=string+"D"
    print(string)
def d():
    global string
    string=string+"d"
    print(string)
def E():
    global string
    string=string+"E"
    print(string)
def e():
    global string
    string=string+"e"
    print(string)
def F():
    global string
    string=string+"F"
    print(string)
def f():
    global string
    string=string+"f"
    print(string)
def G():
    global string
    string=string+"G"
    print(string)
def g():
    global string
    string=string+"g"
    print(string)
def A():
    global string
    string=string+"A"
    print(string)
def a():
    global string
    string=string+"a"
    print(string)
def B():
    global string
    string=string+"B"
    print(string)
def b():
    global string
    string=string+"b"
    print(string)
keyboard_button_1=tkinter.Button(window,image=key,borderwidth=0,width=44,height=98,fg="black",activebackground="blue2",command="C")
keyboard_button_1.place(x=0,y=242)
keyboard_button_2=tkinter.Button(window,image=key,borderwidth=0,width=44,height=98,fg="black",activebackground="blue2")
keyboard_button_2.place(x=46,y=242)
keyboard_button_3=tkinter.Button(window,image=key,borderwidth=0,width=44,height=98,fg="black",activebackground="blue2")
keyboard_button_3.place(x=92,y=242)
keyboard_button_4=tkinter.Button(window,image=key,borderwidth=0,width=44,height=98,fg="black",activebackground="blue2")
keyboard_button_4.place(x=138,y=242)

keyboard_button_5=tkinter.Button(window,image=key,borderwidth=0,width=44,height=98,fg="black",activebackground="blue2")
keyboard_button_5.place(x=184,y=242)
keyboard_button_6=tkinter.Button(window,image=key,borderwidth=0,width=44,height=98,fg="black",activebackground="blue2")
keyboard_button_6.place(x=230,y=242)
keyboard_button_7=tkinter.Button(window,image=key,borderwidth=0,width=44,height=98,fg="black",activebackground="blue2")
keyboard_button_7.place(x=276,y=242)
keyboard_button_8=tkinter.Button(window,image=key,borderwidth=0,width=44,height=98,fg="black",activebackground="blue2")
keyboard_button_8.place(x=322,y=242)

keyboard_button_9=tkinter.Button(window,image=key,borderwidth=0,width=44,height=98,fg="black",activebackground="blue2")
keyboard_button_9.place(x=368,y=242)
keyboard_button_10=tkinter.Button(window,image=key,borderwidth=0,width=44,height=98,fg="black",activebackground="blue2")
keyboard_button_10.place(x=414,y=242)
keyboard_button_11=tkinter.Button(window,image=key,borderwidth=0,width=44,height=98,fg="black",activebackground="blue2")
keyboard_button_11.place(x=460,y=242)
keyboard_button_12=tkinter.Button(window,image=key,borderwidth=0,width=44,height=98,fg="black",activebackground="blue2")
keyboard_button_12.place(x=506,y=242)

keyboard_button_13=tkinter.Button(window,image=key,borderwidth=0,width=44,height=98,fg="black",activebackground="blue2")
keyboard_button_13.place(x=552,y=242)
keyboard_button_14=tkinter.Button(window,image=key,borderwidth=0,width=44,height=98,fg="black",activebackground="blue2")
keyboard_button_14.place(x=598,y=242)

print(string)
window.mainloop()
