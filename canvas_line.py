from tkinter import *
win=Tk()

can1=Canvas(win,bg="lightgreen")
can1.place(x=0,y=0,height=700,width=700)

line1=can1.create_line(0,0,700,700,fill="blue",width=5)
line2=can1.create_line(700,0,0,700,fill="blue",width=5)

win.mainloop()