from tkinter import *
win = Tk()

def pyt():
    lb.config(text=str(tex.get()))

win.title("Spinbox")

tex=IntVar()
sp=Spinbox(win,font=(30),from_=0,to=10,textvariable=tex,command=pyt,wrap=True)
sp.place(x=10,y=10,height=30,width=100)

lb=Label(win,text="",font=(30))
lb.place(x=10,y=50)

win.mainloop()