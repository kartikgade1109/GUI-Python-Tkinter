from tkinter import *
win = Tk()

def value_change(var):
    var=val.get()
    lb.config(text=var)

opl=["C","C++","Python","Java","Go"]
val=StringVar()
val.set("Option")

opm=OptionMenu(win,val,command=value_change,*opl)
opm.place(x=100,y=100,height=30,width=100)

lb=Label(win,text="")
lb.place(x=300,y=100)

win.mainloop()