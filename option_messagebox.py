from tkinter import *
from tkinter.messagebox import askokcancel
win = Tk()
def ask():
    ans=askokcancel(title="Delete",message="Are Your Suer to Delete file")
    print(ans)

btn1=Button(win,text="OK",command=ask)
btn1.place(x=10,y=10)

win.mainloop()