import tkinter #for UI
import datetime #for time
#import webbrowser

 #control and monitor input devices
window= tkinter.Tk()
#window= tkinter.Toplevel()
window.title("Voice assistant")#gives name to the interface
window.geometry("803x450") # defines the geometry of the interface
 #creates an object for storing image
#bg_label=tkinter.Label(window,image=bg_img)
#bg_label.place(x=0,y=0)
def one():
    window.withdraw()
    import exp
def two():
    #window.withdraw()
    window.destroy()
bg_img=tkinter.PhotoImage(file="C:\\Users\\91984\\Downloads\\logo.png")
bg_canvas=tkinter.Canvas(window,bg="#060c40",width=336,height=450,bd=0,highlightthickness=0)
bg_canvas.pack(fill="both",expand=True)
bg_canvas.create_image(250,80,image=bg_img,anchor="nw")
button_1=tkinter.Button(window,text="Next",borderwidth=0,font=('lovelo', 14),width=5,bg="#060c40",height=1,fg="white",command=one)
button_1.place(x=630,y=330)
button_2=tkinter.Button(window,text="Skip",borderwidth=0,font=('lovelo', 14),width=5,bg="#060c40",height=1,fg="white",command=two)
button_2.place(x=700,y=330)
window.mainloop()