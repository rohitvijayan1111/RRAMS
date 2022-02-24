import tkinter
import time
window= tkinter.Tk()
window.title("keyboard")
window.geometry("633x374")
bg_img=tkinter.PhotoImage(file="keyboard.png")
bg_canvas=tkinter.Canvas(window,width=374,height=633,bd=0,highlightthickness=0)
bg_canvas.pack(fill="both",expand=True)
bg_canvas.create_image(0,0,image=bg_img,anchor="nw")
key=tkinter.PhotoImage(file="key.png")
string=" "
def C():
    global string
    string=string+"C"
def c():
    global string
    string=string+"c"
def D():
    global string
    string=string+"D"
def d():
    global string
    string=string+"d"
def E():
    global string
    string=string+"E"
def e():
    global string
    string=string+"e"
def F():
    global string
    string=string+"F"
def f():
    global string
    string=string+"f"
def G():
    global string
    string=string+"G"
def g():
    global string
    string=string+"g"
def A():
    global string
    string=string+"A"
def a():
    global string
    string=string+"a"
def B():
    global string
    string=string+"B"
def b():
    global string
    string=string+"b"
def save():
          global string
          import "Keyboard piano.py"
button_1=tkinter.Button(window,image=key,borderwidth=0,width=44,height=98,fg="black",activebackground="blue2",command=C)
button_1.place(x=0,y=242)
button_2=tkinter.Button(window,image=key,borderwidth=0,width=44,height=98,fg="black",activebackground="blue2",command=c)
button_2.place(x=46,y=242)
button_3=tkinter.Button(window,image=key,borderwidth=0,width=44,height=98,fg="black",activebackground="blue2",command=D)
button_3.place(x=92,y=242)
button_4=tkinter.Button(window,image=key,borderwidth=0,width=44,height=98,fg="black",activebackground="blue2",command=d)
button_4.place(x=138,y=242)
button_5=tkinter.Button(window,image=key,borderwidth=0,width=44,height=98,fg="black",activebackground="blue2",command=E)
button_5.place(x=184,y=242)
button_6=tkinter.Button(window,image=key,borderwidth=0,width=44,height=98,fg="black",activebackground="blue2",command=e)
button_6.place(x=230,y=242)
button_7=tkinter.Button(window,image=key,borderwidth=0,width=44,height=98,fg="black",activebackground="blue2",command=F)
button_7.place(x=276,y=242)
button_8=tkinter.Button(window,image=key,borderwidth=0,width=44,height=98,fg="black",activebackground="blue2",command=f)
button_8.place(x=322,y=242)
button_9=tkinter.Button(window,image=key,borderwidth=0,width=44,height=98,fg="black",activebackground="blue2",command=G)
button_9.place(x=368,y=242)
button_10=tkinter.Button(window,image=key,borderwidth=0,width=44,height=98,fg="black",activebackground="blue2",command=g)
button_10.place(x=414,y=242)
button_11=tkinter.Button(window,image=key,borderwidth=0,width=44,height=98,fg="black",activebackground="blue2",command=A)
button_11.place(x=460,y=242)
button_12=tkinter.Button(window,image=key,borderwidth=0,width=44,height=98,fg="black",activebackground="blue2",command=a)
button_12.place(x=506,y=242)
button_13=tkinter.Button(window,image=key,borderwidth=0,width=44,height=98,fg="black",activebackground="blue2",command=B)
button_13.place(x=552,y=242)
button_14=tkinter.Button(window,image=key,borderwidth=0,width=44,height=98,fg="black",activebackground="blue2",command=b)
button_14.place(x=598,y=242)
button_14=tkinter.Button(window,text="Save",borderwidth=0,width=44,height=98,fg="black",activebackground="blue2",command=save)
button_14.place(x=598,y=242)
window.mainloop()






    





import tkinter
import time
window= tkinter.Tk()
window.title("keyboard")
window.geometry("633x374")
bg_img=tkinter.PhotoImage(file="keyboard.png")
bg_canvas=tkinter.Canvas(window,width=374,height=633,bd=0,highlightthickness=0)
bg_canvas.pack(fill="both",expand=True)
bg_canvas.create_image(0,0,image=bg_img,anchor="nw")
key=tkinter.PhotoImage(file="key.png")
string=" "
def C():
    global string
    string=string+"C"
def c():
    global string
    string=string+"c"
def D():
    global string
    string=string+"D"
def d():
    global string
    string=string+"d"
def E():
    global string
    string=string+"E"
def e():
    global string
    string=string+"e"
def F():
    global string
    string=string+"F"
def f():
    global string
    string=string+"f"
def G():
    global string
    string=string+"G"
def g():
    global string
    string=string+"g"
def A():
    global string
    string=string+"A"
def a():
    global string
    string=string+"a"
def B():
    global string
    string=string+"B"
def b():
    global string
    string=string+"b"
button_1=tkinter.Button(window,image=key,borderwidth=0,width=44,height=98,fg="black",activebackground="blue2",command=C)
button_1.place(x=0,y=242)
button_2=tkinter.Button(window,image=key,borderwidth=0,width=44,height=98,fg="black",activebackground="blue2",command=c)
button_2.place(x=46,y=242)
button_3=tkinter.Button(window,image=key,borderwidth=0,width=44,height=98,fg="black",activebackground="blue2",command=D)
button_3.place(x=92,y=242)
button_4=tkinter.Button(window,image=key,borderwidth=0,width=44,height=98,fg="black",activebackground="blue2",command=d)
button_4.place(x=138,y=242)
button_5=tkinter.Button(window,image=key,borderwidth=0,width=44,height=98,fg="black",activebackground="blue2",command=E)
button_5.place(x=184,y=242)
button_6=tkinter.Button(window,image=key,borderwidth=0,width=44,height=98,fg="black",activebackground="blue2",command=e)
button_6.place(x=230,y=242)
button_7=tkinter.Button(window,image=key,borderwidth=0,width=44,height=98,fg="black",activebackground="blue2",command=F)
button_7.place(x=276,y=242)
button_8=tkinter.Button(window,image=key,borderwidth=0,width=44,height=98,fg="black",activebackground="blue2",command=f)
button_8.place(x=322,y=242)
button_9=tkinter.Button(window,image=key,borderwidth=0,width=44,height=98,fg="black",activebackground="blue2",command=G)
button_9.place(x=368,y=242)
button_10=tkinter.Button(window,image=key,borderwidth=0,width=44,height=98,fg="black",activebackground="blue2",command=g)
button_10.place(x=414,y=242)
button_11=tkinter.Button(window,image=key,borderwidth=0,width=44,height=98,fg="black",activebackground="blue2",command=A)
button_11.place(x=460,y=242)
button_12=tkinter.Button(window,image=key,borderwidth=0,width=44,height=98,fg="black",activebackground="blue2",command=a)
button_12.place(x=506,y=242)
button_13=tkinter.Button(window,image=key,borderwidth=0,width=44,height=98,fg="black",activebackground="blue2",command=B)
button_13.place(x=552,y=242)
button_14=tkinter.Button(window,image=key,borderwidth=0,width=44,height=98,fg="black",activebackground="blue2",command=b)
button_14.place(x=598,y=242)

print(string)
C()
c()
D()
d()
E()
e()
F()
f()
G()
g()
A()
a()
B()
b()
window.mainloop()




    


