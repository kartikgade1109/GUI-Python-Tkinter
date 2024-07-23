#Generating marksheet using message box

from tkinter import *
from tkinter.messagebox import askokcancel

#functions

def data():
    name=st_name1.get()
    marathi=marathis.get()
    english=englishs.get()
    maths=mathss.get()
    science=sciences.get()

    total=marathi+english+maths+science
    per=(total/400)*100

    div=""

    if per>=60:
        div="A"
    elif per<60 and per>=50:
        div="B"
    elif per<50 and per>=40:
        div="C"
    elif per<40 and per>=30:
        div="D"
    else:
        div="Fail"
    
    messagebox(name,total,per,div)

def messagebox(*data):
    print_1=f"""
    Name : {data[0]}
    Total Marks : {data[1]}
    Percentage : {data[2]}
    Grade : {data[3]}
    """
    askokcancel(title="Result",message=print_1)

#Windows all Designing
win=Tk()
win.config(bg="skyblue")
win.geometry("600x600")
win.title("Shivamati Surekha Abasaheb Gade English Medium School")
win.iconbitmap(r"E:\Coding\GUI\Project\s.ico")
win.resizable(False,False)

#Heading of Window
school_name=Label(win,text="Shivamati Surekha Abasaheb Gade\n English Medium School",font=("Times new Roman",25,"bold"),bg="skyblue",anchor=N)
school_name.place(x=50,y=20,height=100,width=500)

#Student Name and Entrybox
s_name=Label(win,text="Student Name:",font=("Times New Roman",20,"bold"),bg="skyblue")
s_name.place(x=10,y=120,height=40,width=200)
st_name1=StringVar()
s_name_text=Entry(win,font=("Times New Roman",20,"bold"),textvariable=st_name1)
s_name_text.place(x=230,y=120,height=40,width=300)

#Subject Heading
school_name=Label(win,text="Subject",font=("Times new Roman",20,"bold"),bg="skyblue")
school_name.place(x=50,y=160,height=100,width=500)

#Subject Name and Mark

sub_name_marathi=Label(win,text="Marathi:",font=("Times New Roman",20,"bold"),bg="skyblue")
sub_name_marathi.place(x=10,y=240,height=40,width=200)
marathis=IntVar()
sub_name_entry_marathi=Entry(win,font=("Times New Roman",20,"bold"),textvariable=marathis)
sub_name_entry_marathi.place(x=230,y=240,height=40,width=300)

sub_name_english=Label(win,text="English:",font=("Times New Roman",20,"bold"),bg="skyblue")
sub_name_english.place(x=10,y=300,height=40,width=200)
englishs=IntVar()
sub_name_entry_english=Entry(win,font=("Times New Roman",20,"bold"),textvariable=englishs)
sub_name_entry_english.place(x=230,y=300,height=40,width=300)

sub_name_maths=Label(win,text="Maths:",font=("Times New Roman",20,"bold"),bg="skyblue")
sub_name_maths.place(x=10,y=360,height=40,width=200)
mathss=IntVar()
sub_name_entry_maths=Entry(win,font=("Times New Roman",20,"bold"),textvariable=mathss)
sub_name_entry_maths.place(x=230,y=360,height=40,width=300)

sub_name_science=Label(win,text="Science:",font=("Times New Roman",20,"bold"),bg="skyblue")
sub_name_science.place(x=10,y=420,height=40,width=200)
sciences=IntVar()
sub_name_entry_science=Entry(win,font=("Times New Roman",20,"bold"),textvariable=sciences)
sub_name_entry_science.place(x=230,y=420,height=40,width=300)

#Button for Print Marksheet
button=Button(win,text="Submit",font=("Times New Roman",20,"bold"),command=data)
button.place(x=200,y=480,height=60,width=200)

win.mainloop()