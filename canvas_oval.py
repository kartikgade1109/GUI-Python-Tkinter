from tkinter import *
win=Tk()

can1=Canvas(win,bg="skyblue")
can1.place(x=20,y=20,height=700,width=700)

ovel=can1.create_oval(30,30,300,200,fill="yellow",width=3)
ovel1=can1.create_oval(30,300,300,550,fill="yellow",width=3)

win.mainloop()