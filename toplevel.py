from tkinter import *

def top():
    tp=Toplevel(win)
    tp.title("Python_1")
    tp.config(bg="lightgreen")
    label=Label(tp,text="Thankyou")
    label.place(x=10,y=10)
    tp.mainloop()
    
win = Tk()
win.title("Python")
win.config(bg="skyblue")
but=Button(win,text="OK",command=top)
but.place(x=20,y=20)
win.mainloop()