import tkinter #for UI
import datetime #for time
import webbrowser
 #control and monitor input devices
window= tkinter.Tk()
#window= tkinter.Toplevel()
window.title("Voice assistant")#gives name to the interface
window.geometry("803x450") # defines the geometry of the interface
 #creates an object for storing image
#bg_label=tkinter.Label(window,image=bg_img)
#bg_label.place(x=0,y=0)
bg_img=tkinter.PhotoImage(file="C:\\Users\\VMSCL6\\AppData\\Local\\Programs\\Python\\Python36\\logo.png")
bg_canvas=tkinter.Canvas(window,bg="#060c40",width=336,height=450,bd=0,highlightthickness=0)
bg_canvas.pack(fill="both",expand=True)
bg_canvas.create_image(250,80,image=bg_img,anchor="nw")
text_canvas=tkinter.Canvas(window,width=336,height=450,bd=0,highlightthickness=0)
text_canvas.pack(fill="both",expand=True)
window.mainloop()