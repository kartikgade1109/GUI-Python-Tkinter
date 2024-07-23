from tkinter import *
win=Tk()
win.config(bg="red")
photo=PhotoImage(file="img.png")

lb=Label(win,image=photo,text="drone",compound="bottom",font=("TkDefaultFont",30))
lb.place(x=100,y=100) # we can crop the image using height and width
win.mainloop()