from tkinter import *

def test():
    lb.config(text=var.get())

win = Tk()
win.title("CheckBok")

var=StringVar()

cb=Checkbutton(win,text="Python",onvalue="Python",offvalue="Java",variable=var,command=test)
cb.deselect()
cb.place(x=100,y=100)

lb=Label(win,text="")
lb.place(x=150,y=150)

#bt=Button(win,text="Check",command=test)
#bt.place(x=200,y=200)
win.mainloop()