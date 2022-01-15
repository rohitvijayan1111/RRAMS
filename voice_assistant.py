import tkinter #for UI
import time #for time
window= tkinter.Toplevel()
window.title("Voice assistant")#gives name to the interface
window.geometry("336x450") # defines the geometry of the interface
bg_img=tkinter.PhotoImage(file="voice_background.png") #creates an object for storing image
#bg_label=tkinter.Label(window,image=bg_img)
#bg_label.place(x=0,y=0)
bg_canvas=tkinter.Canvas(window,width=336,height=450,bd=0,highlightthickness=0)
bg_canvas.pack(fill="both",expand=True)
bg_canvas.create_image(0,0,image=bg_img,anchor="nw")
mic_img=tkinter.PhotoImage(file="mic_check.png") #creates an object for storing image
#bg_canvas.create_image(90,300,image=mic_img,anchor="nw")
mic_button=tkinter.Button(window,image=mic_img,borderwidth=0,width=41,height=74,fg="black")
mic_button.place(x=143,y=295)
def clock():
    t=time.localtime()
    current_time=time.strftime("%H:%M:%S",t)
    bg_canvas.itemconfig(time_text,text=current_time)
    window.after(1000,clock)
time_text=bg_canvas.create_text(250,57,text="",font = ('calibri', 18),fill= 'white')
clock()
window.mainloop()
