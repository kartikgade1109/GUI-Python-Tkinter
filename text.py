from tkinter import *
win = Tk()
win.geometry("500x400")

def rep():
    tex1=tb1.get("1.0","end")
    lb1.config(text=tex1)

tb1=Text(win,font=("Arial",30))
tb1.place(x=20,y=10,width=500,height=300)

bt=Button(win,text="Ok",font=(30),command=rep)
bt.place(x=20,y=530)

lb1=Label(win,text="")
lb1.place(x=20,y=570)

win.mainloop()