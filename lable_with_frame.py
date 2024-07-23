from tkinter import *
win = Tk()
win.title("Frame")
win.config(bg="lime")

lf=LabelFrame(win,text="Python",font=(30),labelanchor=NW,border=5)
lf.place(x=100,y=100,height=100,width=500)

la=Label(win,text="Java",font=(30))
la.place(x=150,y=150)
win.mainloop()