from tkinter import *
from tkinter import ttk

win = Tk()
win.geometry("500x500")

notebook = ttk.Notebook(win)
notebook.pack(pady=10, expand=True)

# Style configuration for frames
style = ttk.Style()
style.configure("TFrame", background="white")

# Frame 1
f1 = ttk.Frame(notebook, height=500, width=500)
f1.pack(fill="both", expand=True)
lbf1 = Label(f1, text="Python", bg="white")
lbf1.place(x=10, y=10)

# Frame 2
f2 = ttk.Frame(notebook, height=500, width=500)
f2.pack(fill="both", expand=True)
lbf2 = Label(f2, text="Java", bg="white")
lbf2.place(x=10, y=10)

# Frame 3
f3 = ttk.Frame(notebook, height=500, width=500)
f3.pack(fill="both", expand=True)
lbf3 = Label(f3, text="C/C++", bg="white")
lbf3.place(x=10, y=10)

# Add frames to notebook
notebook.add(f1, text="New")
notebook.add(f2, text="Open")
notebook.add(f3, text="Save")

win.mainloop()
