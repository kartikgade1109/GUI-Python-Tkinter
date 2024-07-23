from tkinter import *
win = Tk()

frame1=Frame(win,bd=4,bg="blue",relief="sunken")
frame1.place(x=0,y=0,height=500,width=500)
lab1=Label(frame1,text="hellow")
lab1.place(x=100,y=100)

win.mainloop()