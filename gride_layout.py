from tkinter import *
win = Tk()
win.title("Kartik")
win.config(bg="lightgreen")

lab = Label(win,text="Ram",font=("Time New Roman",30,"bold"),bg="red")
lab.grid(row="0",column="0",padx="20",pady="20",columnspan="3")

lab1 = Label(win,text="Ram",font=("Time New Roman",30,"bold"),bg="red")
lab1.grid(row="1",column="0",rowspan="2")
win.mainloop()