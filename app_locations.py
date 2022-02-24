import tkinter #for UI
window= tkinter.Toplevel()
#window= tkinter.Toplevel()
window.title("Voice assistant")#gives name to the interface
window.geometry("336x450") # defines the geometry of the interface
window.attributes('-topmost',1)#to be the first window visible
bg_img=tkinter.PhotoImage(file="voice_background.png") #creates an object for storing image
#bg_label=tkinter.Label(window,image=bg_img)
#bg_label.place(x=0,y=0)
bg_canvas=tkinter.Canvas(window,width=336,height=450,bd=0,highlightthickness=0)
bg_canvas.pack(fill="both",expand=True)
bg_canvas.create_image(0,0,image=bg_img,anchor="nw")
text_x=45#45
text_y=80
count=0
y1=80
y2=110
line=0
no_time=0
def round_rectangle(text,r=25, **kwargs):
    global y1, y2,line,no_time
    line=1
    x1 =40#75
    x2 =280#295
    def no_lines(text):
        global line
        for b in range(len(text)):
            if b in [28, 56, 84, 112, 140]:
                line = line + 1
    no_lines(text)
    print("DF",line)
    for b in range(line):
        y2=y2+20
    points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
    y1 = y1 + 80
    y2 = y2 + 80
    if no_time==0:y2=y2-20
    if no_time == 1: y2 = y2 - 40
    if no_time == 2: y2 = y2 - 60
    if no_time == 3: y2 = y2 - 80
    no_time=no_time+1
    return bg_canvas.create_polygon(points, **kwargs, smooth=True)


def change(texts):
    global text_x,text_y,z,count
    text_list = texts.split()
    str = ""
    str2 = ""
    z=0 # to traverse the list text_list
    length = 0
    while z < len(text_list)-1 and length < 28:  #to print for a line and rest all to the next line
        length = length + len(text_list[z]) + 1
        str = str + " " + text_list[z]
        z = z + 1
    else:
        count=count+1
        for b in text_list[z:]: # storing remaining text in str2
            str2 = str2 + " " + b
    bg_canvas.create_text(text_x, text_y, text=str, font=('calibri', 14), fill='white', anchor=tkinter.NW)
    text_y=text_y+20

    if len(str2)<28:  #printing the text in the next line
        bg_canvas.create_text(text_x,text_y, text=str2, font=('calibri', 14), fill='white', anchor=tkinter.NW)
        text_y=text_y+80
        count=count+1
    else: # if more than a line then calling change function again
        change(str2)
    text_y=text_y+20

def output_text_admin(texts,type):
    global text_x,text_y,count
    print(len(texts))
    count=0
    bg_canvas.create_text(text_x, text_y, text=type, font=('calibri', 14), fill='white', anchor=tkinter.NW)
    text_y = text_y + 20
    if len(texts) <28:
        bg_canvas.create_text(text_x,text_y,text=texts,font=('calibri',14),fill='white',anchor=tkinter.NW)
        text_y = text_y + 20
        count=count+1
        text_y=text_y+80
    else:
        count=count+1
        text_x=45#40
        text_list=texts.split()
        length=0
        str=""
        str2=""
        z=0
        change(texts)

round_rectangle(" Hi this is your,RRAMS voice assistant difsdhfl dshfhl  ",r=20, fill="#fd3a46",outline="#fd3a46",width="3")
output_text_admin(" Hi this is your,RRAMS voice assistant,difsdhf ldshfhl ","user")
round_rectangle(" Hi this is your,RRAMS voice assistant",r=20, fill="#fd3a46",outline="#fd3a46",width="3")
output_text_admin(" Hi this is your,RRAMS voice assistant","admin")
round_rectangle(" Hi this is your,RRAMS voice assistant",r=20, fill="#fd3a46",outline="#fd3a46",width="3")
output_text_admin(" Hi this is your,RRAMS voice assistant","admin")

window.mainloop()

