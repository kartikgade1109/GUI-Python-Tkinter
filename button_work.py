from tkinter import *
def python():
    lb.config(text="Python",bg="red")

win=Tk()
win.title("Click Button")
win.config(bg="orange")
bt=Button(win,text="Click",font=(30),bg="black",fg="white",relief="groove",command=python)
bt.place(x=100,y=100)
lb=Label(win,text="Hello",font=(30))
lb.place(x=200,y=200)

win.mainloop()