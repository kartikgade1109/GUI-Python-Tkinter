from tkinter import *

def clk():
    lb.config(text=var.get())

win = Tk()

list = (("Python","I Love Python"),("Java","I Love Java"),("C++","I Love C++"))
var = StringVar()
for i in list:
    rb=Radiobutton(win,text=i[0],font=(30),value=i[1],variable=var,command=clk)
    rb.pack(padx=10,pady=10)

lb = Label(win,text="",font=(30))
lb.pack(padx=20,pady=20)

#bt=Button(win,text="OK",command=clk)
#bt.pack()
win.mainloop()