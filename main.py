from tkinter import *
from tkinter import ttk
from tkinter import ttk,messagebox
from PIL import ImageTk 
def log_in():
    rt.destroy()
    import login
def reg_win():
    rt.destroy()
    import creat
rt=Tk()
rt.title("HOME PAGE")
rt.geometry("1600x900")
bg=ImageTk.PhotoImage(file="C:\\Users\\Rajib Kr paul\\OneDrive\Documents\\visiual stdio code\\project\\candle.jpg")
bglb=Label(rt,image=bg)
bglb.place(x=-50,y=-50,width=1600,height=900)
bg1=ImageTk.PhotoImage(file="C:\\Users\\Rajib Kr paul\\OneDrive\Documents\\visiual stdio code\\project\\bank.jpg")
logolb=Label(rt,image=bg1)
logolb.place(x=50,y=100,width=470,height=630)
frame=Frame(rt,bg='lightblue')
frame.place(x=520,y=100,width=800,height=630)
reg=Label(frame,text="Welcome to our bank",font=("Monotype Corsiva",35,"bold"),fg="darkgreen",bg="yellow")
reg.place(x=50,y=30,width=700)
b2=Button(frame,text="Login",command=log_in,font=("Times New Roman",15,"bold"),bg="lightblue")
b2.place(x=370,y=130)
b3=Button(frame,text="Creat Account",command=reg_win,font=("Times New Roman",15,"bold"),bg="lightblue")
b3.place(x=480,y=130)
bg4=ImageTk.PhotoImage(file="C:\\Users\\Rajib Kr paul\\OneDrive\Documents\\visiual stdio code\\project\\bank2.jpg")
logolb1=Label(frame,image=bg4,bg='cyan')
logolb1.place(x=370,y=180,width=350,height=350)
lb=Label(frame,text="Here you can \nkeep your bankinging detail\n and  can check anytime ",font=("Monotype Corsiva",15,"bold"),bg="cyan",fg="red")
lb.place(x=0,y=180,width=370,height=350)
rt.mainloop()