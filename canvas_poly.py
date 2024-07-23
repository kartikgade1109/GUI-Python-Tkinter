from tkinter import *
win=Tk()

can1=Canvas(win,bg="skyblue")
can1.place(x=20,y=20,height=700,width=700)

cor=[20,20,100,100,40,100]
can1.create_polygon(cor,fill="yellow")

win.mainloop()