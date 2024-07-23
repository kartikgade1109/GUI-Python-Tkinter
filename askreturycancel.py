from tkinter import *
from tkinter.messagebox import askretrycancel
def ask():
    ans=askretrycancel(title="Python",message="Do you want to install ide of python?")
    print(ans)

    if ans:
        ask()
    else:
        lab.config(text="Thank you")
win=Tk()

but=Button(win,text="Ok",command=ask)
but.place(x=10,y=10)

lab=Label(win,text="")
lab.place(x=10,y=50)
win.mainloop()