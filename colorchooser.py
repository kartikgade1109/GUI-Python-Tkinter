from tkinter import *
from tkinter.colorchooser import askcolor
def colo():
    col=askcolor(title="Color")
    win.config(bg=col[1])

win=Tk()
win.geometry("500x200")
but=Button(win,text="Choose Your color",command=colo)
but.pack(pady=10)
win.mainloop()