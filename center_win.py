from tkinter import *
win = Tk()
win.config(bg="yellow")
width = 300
height = 500
sys_width = win.winfo_screenwidth()
sys_height = win.winfo_screenheight()
cx = int(sys_width / 2 - width / 2)
cy = int(sys_height / 2 - height / 2)
win.geometry(f"{width}x{height}+{cx}+{cy}")
win.mainloop()