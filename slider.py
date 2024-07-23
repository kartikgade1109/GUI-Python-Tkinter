from tkinter import *
from tkinter import ttk
win = Tk()

def call(p):
    p=str(var.get())
    lb1.config(text=p)

var=DoubleVar()
sc=Scale(win,from_=0,to=100,orient="vertical",variable=var,command=call,fg="orange")
sc.place(x=100,y=100,height=300,width=50)

lb1=Label(win,text="",font=(50))
lb1.place(x=200,y=100)

win.mainloop()