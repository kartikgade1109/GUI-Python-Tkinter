from tkinter import *
win = Tk()
win.geometry("500x400")

def sub():
    lb3.config(text=em.get())

lb1=Label(win,text="Email Address:",font=(30))
lb1.place(x=50,y=100)
em=StringVar()
ent1 = Entry(win,font=(30),bd=8,textvariable=em)
ent1.place(x=50,y=130,width=300)

lb2=Label(win,text="Password:",font=(30))
lb2.place(x=50,y=170)
pas=StringVar()
ent2 = Entry(win,font=(30),show="*",bd=8,textvariable=pas)
ent2.place(x=50,y=200,width=300)

bt=Button(win,text="Submit",font=(30),command=sub)
bt.place(x=50,y=240,width=150)

lb3=Label(win,text="",font=(30))
lb3.place(x=50,y=280)

win.mainloop()