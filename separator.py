from tkinter import *
from tkinter import ttk
win = Tk()
win.geometry("500x300")
win.resizable(False,False)

lb1 = Label(win,text="Python",font=(60))
lb1.pack()

sep =ttk.Separator(win,orient="horizontal")
sep.pack(fill=X)

lb2 = Label(win,text="Java",font=(60))
lb2.pack()

win.mainloop()