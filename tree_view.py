#Hierarchical
#Treview()
from tkinter import *
from tkinter import ttk
win=Tk()

label=Label(win,text="Gurukul",font=(30))
label.place(x=10,y=20,height=50,width=100)

tree=ttk.Treeview(win)
tree.insert("",END,text="Class",iid=0)
tree.insert("",END,text="Subject",iid=1)
tree.insert("",END,text="Board",iid=2)

tree.insert("",END,text="1st TO 5th",iid=3)
tree.insert("",END,text="6th TO 10th",iid=4)

tree.insert("",END,text="English",iid=5)
tree.insert("",END,text="Maths",iid=6)
tree.insert("",END,text="Science",iid=7)
tree.insert("",END,text="Marathi",iid=8)

tree.insert("",END,text="CBSC",iid=9)
tree.insert("",END,text="SSC",iid=10)

tree.move(3,0,0)
tree.move(4,0,1)

tree.move(5,1,0)
tree.move(6,1,1)
tree.move(7,1,2)
tree.move(8,1,3)

tree.move(9,2,0)
tree.move(10,2,1)

tree.place(x=10,y=90,height=500,width=300)
win.mainloop()