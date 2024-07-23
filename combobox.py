from tkinter import *
from tkinter import ttk
win = Tk()

def comb():
    p=tex.get()
    la1.config(text=p)

list1 = ["C","C++","Python","Java"]

tex=StringVar()

com = ttk.Combobox(win,values=list1,font=(30),textvariable=tex)
com.set("Select Language")
com.place(x=100,y=100)

la1=Label(win,text="",font=(30))
la1.place(x=100,y=200)

but=Button(win,text="OK",command=comb)
but.place(x=100,y=300)

win.mainloop()