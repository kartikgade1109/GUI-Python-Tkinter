from tkinter import *
win = Tk()
win.title("K Window")
win.iconbitmap(r"C:\Users\gade\Downloads\kartik.ico")
win.attributes('-alpha',1) # this is use to operate opacity of window value must be 0 to 1
win.config(bg="lightgreen") # is use to change backrgound color
win.geometry("500x300+100+200") # we use geometry for size of window we want minimum
win.mainloop()
'''
import tkinter as tk
win = tk.Tk()
win.geometry("500x300")
win.resizable(False,False)
win.mainloop()
'''