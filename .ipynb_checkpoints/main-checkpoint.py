import tkinter
main= tkinter.Tk()
main.title("UI")#gives name to the interface
main.geometry("800x500") # defines the geometry of the interface
img=tkinter.PhotoImage(file="background2.png") #creates an object for storing image
main_canvas=tkinter.Canvas(main,width=800,height=500,bd=0,highlightthickness=0)
main_canvas.pack(fill="both",expand=True)
main_canvas.create_image(0,0,image=img,anchor="nw")

#label=tkinter.Label(main,image=img)
#label.place(x=0,y=0)
def one():
    import voice_assistant
def two():
    import  keyboard
#voice_back=tkinter.PhotoImage(main, file="voice_logo.png") #creates an object for storing image
#label2=tkinter.PhotoImage(main,image=voice_back)
#label2.place(x=190,y=152)

button=tkinter.Button(main,text="Creating your own tune",command=two)
button.place(x=130,y=150)
button=tkinter.Button(main,text="Find the song with tune")
button.place(x=563,y=149)
button=tkinter.Button(main,text="Speak out your opening",command=one)
button.place(x=115,y=346)
button=tkinter.Button(main,text="")
button.place(x=555,y=347)
# Code to add widgets will go here...
main.mainloop()
