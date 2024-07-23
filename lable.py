from tkinter import *
ent=input("Enter your data:") #Run time change we can do using this method

win=Tk()
win.title("Lable Widget Demo")
win.config(bg="tomato")
win.geometry("800x500")
win.resizable(False,False)

var=StringVar()

lb=Label(win,font=("Arial Rounded MT Bold",30,"normal"),bg="yellow",fg="brown",cursor="Plus",relief="sunken",justify=LEFT,textvariable=var)
lb.place(x=10,y=100)
var.set(ent)

win.mainloop()
