from tkinter import *
win = Tk()
win.title("Raja")
win.config(bg="purple")
win.geometry("500x300")

lab=Label(win, text="kartik", font=("Arial",50),bg="white",foreground="gray5")
lab.place(x=20,y=200,height="100",width="200")

win.mainloop()