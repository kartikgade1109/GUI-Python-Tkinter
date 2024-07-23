from tkinter import *
from tkinter.messagebox import showerror,showinfo,showwarning

win=Tk()
def info():
    showinfo(title="Python",message="Hi, This is Information box")
def err():
    showerror(title="Python",message="Hi, This is Error box")
def war():
    showwarning(title="Python",message="Hi, This is Warning box")


button=Button(win,text="Information",command=info)
button.place(x=10,y=10)

button1=Button(win,text="Error",command=err)
button1.place(x=10,y=60)

button2=Button(win,text="Warning",command=war)
button2.place(x=10,y=110)

win.mainloop()