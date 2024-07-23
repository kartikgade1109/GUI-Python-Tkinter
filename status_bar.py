from tkinter import *
win = Tk()
win.geometry("900x700")

def leb():
    status_bar.config(text="Go")

status_bar=Label(win,text="Ready",font=(30),relief=SUNKEN,anchor=W,bg="blue",fg="white")
status_bar.pack(side=BOTTOM,fill=X,ipady=5)

button=Button(win,text="OK",command=leb)
button.place(x=20,y=20)

win.mainloop()