from tkinter import *
from tkinter import messagebox

class CustomTitleBar(Frame):
    def __init__(self, parent):
        super().__init__(parent, bg='#333333', bd=2)
        self.parent = parent
        self.parent.overrideredirect(True)  # Remove the default title bar
        
        self.close_button = Button(self, text='X', command=self.parent.destroy, bg='#333333', fg='white', font=(30),bd=0)
        self.close_button.pack(side=RIGHT, padx=5)
    
        self.pack(fill=X)

        self.bind('<Button-1>', self.start_move)
        self.bind('<B1-Motion>', self.do_move)

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def do_move(self, event):
        x = self.parent.winfo_pointerx() - self.x
        y = self.parent.winfo_pointery() - self.y
        self.parent.geometry(f'+{x}+{y}')

def login():
    user = "kartikgade@123gmail.com"
    passw = "KAG@123"
    if userentry.get() == user and passwordentry.get() == passw:
        messagebox.showinfo(title="Successful", message="Login Successful!")
    else:
        messagebox.showwarning(title="Wrong Password", message="Invalid Username and Password")

win = Tk()
win.geometry("400x400")
win.resizable(False, False)
win.configure(bg="#333333")

title_bar = CustomTitleBar(win)

frame = Frame(win, bg="#333333")
frame.pack(expand=True)

label = Label(frame, text="Login", bg="#333333", fg="#ff3399", font=("Arial", 30))
label.grid(row=0, column=0, columnspan=2, sticky="news", pady=10)

username = Label(frame, text="Username:", bg="#333333", fg="#ffffff", font=("Arial", 16))
username.grid(row=1, column=0)

userentry = Entry(frame, font=("Arial", 16))
userentry.grid(row=1, column=1, pady=20)

password = Label(frame, text="Password:", bg="#333333", fg="#ffffff", font=("Arial", 16))
password.grid(row=2, column=0, pady=20)

passwordentry = Entry(frame, show="*", font=("Arial", 16))
passwordentry.grid(row=2, column=1)

button = Button(frame, text="Login", bg="#ff3399", fg="#ffffff", font=("Arial", 16), command=login)
button.grid(row=3, column=0, columnspan=2, pady=30)

win.mainloop()
