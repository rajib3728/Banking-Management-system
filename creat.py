from tkinter import *
from tkinter import ttk
from tkinter import ttk,messagebox
import mysql.connector as mysql
from PIL import ImageTk 
def log():
    if e1.get()=="" or e2.get()=="" or e3.get()=="":
        messagebox.showinfo("All field are required")
    else:
        en=e1.get()
        eoc=e2.get()
        edp=e3.get()
        db=mysql.connect(host="localhost",user="root",password="",database="bankacc")   
        mycursor=db.cursor() 
        sql="insert into creat(en,eoc,edp)values(%s,%s,%s)"
        val=(en,eoc,edp)

        mycursor.execute(sql,val)
        db.commit()
        e1.delete(0,'end')
        e2.delete(0,'end')
        e3.delete(0,'end')
        messagebox.showinfo("INSERT STATUS","Inserted sucessfully");
        db.close()
        
def back():
    crwn.destroy()
    import main 
def logo():
    crwn.destroy()
    import login           
crwn=Tk()
crwn.geometry("1600x900")
crwn.title("Create Account")
bg=ImageTk.PhotoImage(file="C:\\Users\\Rajib Kr paul\\OneDrive\Documents\\visiual stdio code\\project\\candle.jpg")
bglb=Label(crwn,image=bg)
bglb.place(x=-50,y=-50,width=1600,height=900)
fr1=Frame(crwn,bg="blue")
l_title=Message(crwn,text="OPEN ACCOUNT",relief="raised",width=2000,padx=1600,pady=0,fg="white",bg="black",justify="center",anchor="center")
l_title.config(font=("Courier","50","bold"))
l_title.pack(side="top")
l1=Label(crwn,text="Enter Name:",relief="raised",bg="cyan",font=30)
l1.place(x=600,y=200)
e1=Entry(crwn)
e1.place(x=800,y=200)
l2=Label(crwn,text="Enter email id:",relief="raised",bg="cyan",font=30)
l2.place(x=600,y=250)
e2=Entry(crwn)
e2.place(x=800,y=250)
l3=Label(crwn,text="Enter desired PIN:",relief="raised",bg="cyan",font=30)
l3.place(x=600,y=300)
e3=Entry(crwn,show="*")
e3.place(x=800,y=300)
b=Button(crwn,text="Submit",command=log,bg="green",font=30)
b.place(x=700,y=350)
b=Button(crwn,text="Login now",command=logo,bg="blue",font=30)
b.place(x=800,y=350)
c=Button(crwn,text="Back to home",command=back,bg="red",font=14)
c.pack(side="top")
crwn.mainloop()