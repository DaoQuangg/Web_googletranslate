from tkinter import *
from PIL import Image, ImageTk
from googletrans import Translator

root = Tk()
root.title('Google Galaxy')
root.geometry('500x630')
root.iconbitmap('./logo.ico')

load = Image.open('R.jpg')
render = ImageTk.PhotoImage(load)
img = Label(root,image=render)
img.place(x=0,y=0)

name = Label(root,text='Translator',fg="#FFFFFF", bd=0, bg='#031520')
name.config(font=('Transformers Movie', 30))
name.pack(pady=10)

box= Text(root,width=28, height=8, font=('ROBOTO',16))
box.pack(pady=20)

Button_frame = Frame(root).pack(side=BOTTOM)

def clear():
    box.delete(1.0,END)
    box1.delete(1.0,END)

def translate():
    input = box.get(1.0,END)
    print(input)
    t = Translator()
    a = t.translate(input, src="en", dest="vi")
    b=a.text
    box1.insert(END,b)

def translate_1():
    input = box.get(1.0,END)
    print(input)
    z = Translator()
    x = z.translate(input, src="vi", dest="en")
    y=x.text
    box1.insert(END,y)
 
clear_button = Button(Button_frame, text='Clear text', font=(('Arial'),10,'bold'), bg="#303030", fg='#FFFFFF', command=clear)
clear_button.place(x=70,y=310)
trans_button = Button(Button_frame, text='Translate', font=(('Arial'),10,'bold'), bg="#303030", fg='#FFFFFF', command=translate)
trans_button.place(x=220,y=310)
trans_button_1 = Button(Button_frame, text='Dịch', font=(('Arial'),10,'bold'), bg="#303030", fg='#FFFFFF', command=translate_1)
trans_button_1.place(x=370,y=310)

box1= Text(root,width=28, height=8, font=('ROBOTO',16))
box1.pack(pady=50)

root.mainloop()
