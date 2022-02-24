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

yy1=80
yy2=130

def round_rectangle_admin(text,r=25,**kwargs):
    global yy1,yy2
    x1=40#75
    x2=275#295
    points = (x1+r, yy1, x1+r, yy1, x2-r, yy1, x2-r, yy1, x2, yy1, x2, yy1+r, x2, yy1+r, x2, yy2-r, x2, yy2-r, x2, yy2, x2-r, yy2, x2-r, yy2, x1+r, yy2, x1+r, yy2, x1, yy2, x1, yy2-r, x1, yy2-r, x1, yy1+r, x1, yy1+r, x1,yy1)
    a=len(text)
    while a>=0:
        if a<=22:pass
        else:yy1=yy1+20;yy2=yy2+20
    yy1=yy1+120
    yy2=yy2+120
    return bg_canvas.create_polygon(points, **kwargs, smooth=True)
round_rectangle_admin(" Hi this is your, voice assistant and i am here to check for a logic that makes the UI looks good",r=20,fill="#fd3a46",outline="black",width="1")

def round_rectangle_admin(text,r=25,**kwargs):
    global yy1,yy2
    x1=40#75
    x2=275#295
    points = (x1+r, yy1, x1+r, yy1, x2-r, yy1, x2-r, yy1, x2, yy1, x2, yy1+r, x2, yy1+r, x2, yy2-r, x2, yy2-r, x2, yy2, x2-r, yy2, x2-r, yy2, x1+r, yy2, x1+r, yy2, x1, yy2, x1, yy2-r, x1, yy2-r, x1, yy1+r, x1, yy1+r, x1,yy1)
    a=len(text)
    while a>=0:
        if a<=22:pass
        else:yy1=yy1+20;yy2=yy2+20
    yy1=yy1+120
    yy2=yy2+120
    return bg_canvas.create_polygon(points, **kwargs, smooth=True)
round_rectangle_admin(" Hi this is your, voice assistant and i am here to check for a logic that makes the UI looks good",r=20,fill="#fd3a46",outline="black",width="1")

count=0

y1=140
y2=190
def round_rectangle(r=25, **kwargs):
    global y1, y2
    x1 =75# 40
    x2 =295# 270
    points = (x1+r, y1, x1+r, y1, x2-r, y1, x2-r, y1, x2, y1, x2, y1+r, x2, y1+r, x2, y2-r, x2, y2-r, x2, y2, x2-r, y2, x2-r, y2, x1+r, y2, x1+r, y2, x1, y2, x1, y2-r, x1, y2-r, x1, y1+r, x1, y1+r, x1, y1)
    y1 = y1 + 120
    y2 = y2 + 120
    return bg_canvas.create_polygon(points, **kwargs, smooth=True)

round_rectangle(r=20, fill="#fd3a46",outline="#fd3a46",width="3")

def change(texts):
    global text_x,text_y,z
    text_list = texts.split()
    str = ""
    str2 = ""
    z=0
    length = 0
    while z < len(text_list)-1 and length < 28:  #to print for a line and rest all to the next line
        length = length + len(text_list[z]) + 1
        str = str + " " + text_list[z]
        z = z + 1
    else:
        for b in text_list[z:]: # storing remaining text in str2
            str2 = str2 + " " + b
    bg_canvas.create_text(text_x, text_y, text=str, font=('calibri', 14), fill='white', anchor=tkinter.NW)
    text_y=text_y+20

    if len(str2)<28:  #printing the text in the next line
        bg_canvas.create_text(text_x,text_y, text=str2, font=('calibri', 14), fill='white', anchor=tkinter.NW)
        text_y=text_y+80
    else: # if more than a line then calling change function again
        change(str2)
    text_y=text_y+20


text_x=45#45
text_y=80
def output_text_admin(texts):
    global text_x,text_y,count
    print(len(texts))
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

output_text_admin(" Hi this is your, voice assistant and i am here to check for a logic that makes the UI looks good")

text_x1=80
text_y1=140
count2=0
def change_user(texts):
    global text_x1,text_y1,z
    text_list = texts.split()
    str = ""
    str2 = ""
    z=0
    length = 0
    while z < len(text_list)-1 and length < 30:
        length = length + len(text_list[z]) + 1
        str = str + " " + text_list[z]
        z = z + 1
    else:
        for b in text_list[z:]:
            str2 = str2 + " " + b
    bg_canvas.create_text(text_x1, text_y1, text=str, font=('calibri', 14), fill='white', anchor=tkinter.NW)
    text_y1=text_y1+20

    if len(str2)<30:
        bg_canvas.create_text(text_x1,text_y1, text=str2, font=('calibri', 14), fill='white', anchor=tkinter.NW)
        text_y1=text_y1+80
    else:
        change(str2)
    text_y1=text_y1+20

def output_text(text):
    global text_x1,text_y1,count2
    if len(text)<30:
        bg_canvas.create_text(text_x1, text_y1, text=text, font=('calibri', 14), fill='white', anchor=tkinter.NW)
        #text_y1 = text_y1 + 20
        count2 = count2 + 1
        text_y1 = text_y1 + 80
    else:
        count2 = count2 + 1
        text_x1 =80 # 40
        text_list = text.split()
        length = 0
        str = ""
        str2 = ""
        z = 0
        change_user(text)

window.mainloop()

