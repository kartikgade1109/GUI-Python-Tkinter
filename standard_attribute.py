from tkinter import *
win=Tk()
win.config(bg="purple")
win.geometry("520x120")

lab=Label(win,text="Hellow Python",font=("Matura MT Script Capitals",30),relief="ridge")
lab.place(x=10,y=10,height=100,width=500)

win.mainloop()