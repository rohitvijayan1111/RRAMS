import tkinter #for UI
import time #for time
window= tkinter.Toplevel()
window.title("keyboard")#gives name to the interface
window.geometry("1587x374") # defines the geometry of the interface
bg_img=tkinter.PhotoImage(file="keyboard.png") #creates an object for storing image
bg_canvas=tkinter.Canvas(window,width=374,height=1587,bd=0,highlightthickness=0)
bg_canvas.pack(fill="both",expand=True)
bg_canvas.create_image(0,0,image=bg_img,anchor="nw")

window.mainloop()
