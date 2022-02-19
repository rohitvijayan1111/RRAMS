import tkinter #for UI
window= tkinter.Toplevel()
window.title("Voice assistant")#gives name to the interface
window.geometry("336x450") # defines the geometry of the interface
#bg_img=tkinter.PhotoImage(file="voice_background.png") #creates an object for storing image
bg_canvas=tkinter.Canvas(window,width=336,height=450,bd=0,highlightthickness=0)

texts=""" Welcome to our interface. Here you will find three unique features each created for your different needs.Have fun!

1. Creating Your Own Tune:
            Ready To Be The Next A.R Rahman ? Clickety Clackety Clacks!! You're right on time.
            
            We are excited to tell you that about our VIRTUAL PIANO to kickstart your musical side.
            
            Compact, easy to use, state of the art software to create and store the tunes which run freely on your mind!
            All you have to do is just start playing the Piano by using the mouse pointer and let the software do the rest.
            If you want the tune in your system, click the download button.

2.             

about_text=bg_canvas.create_text(0,0,text=,font = ('calibri', 18),fill= 'white')
