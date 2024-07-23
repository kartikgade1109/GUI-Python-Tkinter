from tkinter import *
win=Tk()

can1=Canvas(win,bg="lightgreen")
can1.place(x=0,y=0,height=700,width=700)

arc1=can1.create_arc(50,50,200,200,start=0,extent=180,fill="blue",width=5)

win.mainloop()