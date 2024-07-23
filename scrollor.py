from tkinter import *
from tkinter import ttk
win = Tk()

text=Text(win,font=(30))
text.place(x=10,y=10,height=400,width=400)

scroll=Scrollbar(win,orient="vertical",command=text.yview)
scroll.place(x=420,y=10,height=400,width=20)

text["yscrollcommand"]=scroll.set # this is use to cordonate with scrollobar and text

win.mainloop()