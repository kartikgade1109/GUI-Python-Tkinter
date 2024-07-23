from tkinter import *
win = Tk()

var= StringVar()

rb1=Radiobutton(win,text="Python",value="Py",variable=var)
rb1.deselect()
rb1.place(x=100,y=100)

rb2=Radiobutton(win,text="Java",value="Ja",variable=var)
rb1.deselect()
rb2.place(x=200,y=100)

win.mainloop()