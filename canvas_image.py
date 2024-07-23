from tkinter import *
win=Tk()

can1=Canvas(win,bg="purple")
can1.place(x=10,y=10,height=700,width=700)

can1.create_text(300,500,text="Hello",font=(200),fill="white")

file_1=PhotoImage(file="img.png")
can1.create_image(10,10,image=file_1)

win.mainloop()