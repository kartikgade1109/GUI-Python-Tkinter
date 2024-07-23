from tkinter import*
#Variables in tkinter
win = Tk()
win.title("Var")
var = StringVar(win,value="Hello",name="v1") #Master we set variable type,vale,we can use name with getvar or setvar, etc
print(var.get())
var.set("Python") #we can use this for store any value in variable
print(var.get())

a=IntVar(win,value=222) #Int variable type
print(a.get())

boo=BooleanVar(win,value=True) #Boolean variable type
print(boo.get())

do=DoubleVar(win, value=23.15) #Double variable type
print(do.get())

win.mainloop()