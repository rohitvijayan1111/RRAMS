import tkinter,time
main= tkinter.Tk()
main.title("UI")#gives name to the interface
main.geometry("800x500") # defines the geometry of the interface
#main.attributes('-topmost',1)#to be the first window visible
img=tkinter.PhotoImage(file="background3.png") #creates an object for storing image
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
assistant_img=tkinter.PhotoImage(file="assistant-pic.png") #creates an object for storing image
assistant_button=tkinter.Button(main,image=assistant_img,borderwidth=0,width=174,height=187,fg="black",command=one)
assistant_button.place(x=103,y=55)

piano_img=tkinter.PhotoImage(file="piano-pic.png") #creates an object for storing image
piano_button=tkinter.Button(main,image=piano_img,borderwidth=0,width=183,height=187,fg="black",command=two)
piano_button.place(x=535,y=55)

decibel_img=tkinter.PhotoImage(file="decibel-pic.png") #creates an object for storing image
decibel_button=tkinter.Button(main,image=decibel_img,borderwidth=0,width=186,height=187,fg="black")
decibel_button.place(x=92,y=249)

clap_img=tkinter.PhotoImage(file="clap clap pic.png") #creates an object for storing image
clap_button=tkinter.Button(main,image=clap_img,borderwidth=0,width=183,height=184,fg="black")
clap_button.place(x=533,y=251)

# Code to add widgets will go here...
#import app_locations

main.mainloop()
