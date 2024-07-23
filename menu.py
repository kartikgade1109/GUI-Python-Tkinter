from tkinter import *
win = Tk()

def file():
    lb.config(text="File manu")

mb=Menubutton(win,text="File")
mb.menu = Menu(mb,tearoff=0)
mb["menu"]=mb.menu

mb.menu.add_checkbutton(label="New File",command=file)
mb.menu.add_checkbutton(label="Open File")
mb.menu.add_checkbutton(label="Save File")

lb=Label(win,text="",font=(30))
lb.place(x=200,y=100)

mb.pack()
win.mainloop()