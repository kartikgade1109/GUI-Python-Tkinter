from tkinter import *
win=Tk()
win.title("Button")
win.config(bg="orange")

#photo=PhotoImage(file="img.png")

bt=Button(win,text="Click",font=(30),bg="black",fg="white",relief="groove",compound="left") #we can use image using fun image=photo
bt.place(x=100,y=100)

win.mainloop()