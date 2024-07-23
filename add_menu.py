from tkinter import *
win = Tk()
win.title("Menu")

def new():
    print("hello")

w_menu=Menu(win)
win.config(menu=w_menu)

#file Menu
f_menu=Menu(w_menu,tearoff=0)

f_menu.add_command(label="New File",command=new)
f_menu.add_command(label="Open File")
f_menu.add_separator()
f_menu.add_command(label="Save ")
f_menu.add_command(label="Save as")

#sub menu of file export
s_menu=Menu(f_menu,tearoff=0)
s_menu.add_command(label="PDF",command=new)
s_menu.add_command(label="Other")
f_menu.add_cascade(label="Export",menu=s_menu)


w_menu.add_cascade(label="File",menu=f_menu)

#edit Menu
e_menu=Menu(w_menu,tearoff=0)

e_menu.add_command(label="Undo")
e_menu.add_command(label="Redo")
e_menu.add_separator()
e_menu.add_command(label="Cut")
e_menu.add_command(label="Copy")
e_menu.add_command(label="Paste")
w_menu.add_cascade(label="Edit",menu=e_menu)

win.mainloop()