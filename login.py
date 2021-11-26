from tkinter import *
from tkinter import ttk
from tkinter import ttk,messagebox
from PIL import ImageTk
import mysql.connector as mysql 
def work():
    if e1.get()=="" or e3.get()=="":
        messagebox.showerror("Error","All fields are required")
    else:
        eoc=e1.get()
        edp=e3.get()
        try:
            db=mysql.connect(host="localhost",user="root",password="",database="bankacc")
            mycursor=db.cursor()
            mycursor.execute("select * from creat where eoc=%s and edp=%s",(eoc,edp))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid UserName and Password")
            else:
                messagebox.showinfo("Success", "Welcome")
                db.commit()
                e1.delete(0,'end')
                e3.delete(0,'end')
                loginwn.destroy()
                import workpage
        except:
            messagebox.showerror("try again")
            e1.delete(0,'end')
            e3.delete(0,'end')
        db.rollback()
        db.close()    
def back():
    loginwn.destroy() 
    import main
loginwn=Tk()
loginwn.geometry("1600x900")
loginwn.title("Log in")
bg=ImageTk.PhotoImage(file="C:\\Users\\Rajib Kr paul\\OneDrive\Documents\\visiual stdio code\\project\\tree.jpg")
bglb=Label(loginwn,image=bg)
bglb.place(x=-50,y=-50,width=1600,height=900)
fr1=Frame(loginwn,bg="blue")
l_title=Message(loginwn,text="login page",relief="raised",width=2000,padx=600,pady=0,fg="white",bg="black",justify="center",anchor="center")
l_title.config(font=("Courier","50","bold"))
l_title.pack(side="top")
l1=Label(loginwn,text="Enter Gmail id:",relief="raised",bg="yellow",font=30)
l1.place(x=600,y=250)
e1=Entry(loginwn)
e1.place(x=800,y=250)
#l2=Label(loginwn,text="Enter account number:",relief="raised",bg="yellow",font=30)
#l2.place(x=600,y=250)
#e2=Entry(loginwn)
#e2.place(x=800,y=250)
l3=Label(loginwn,text="Enter your PIN:",relief="raised",bg="yellow",font=30)
l3.place(x=600,y=300)
e3=Entry(loginwn,show="*")
e3.place(x=800,y=300)
b=Button(loginwn,text="Submit",command=work,font=30,bg="green")
b.place(x=700,y=350)
b1=Button(text="Back to Home",relief="raised",bg="black",fg="white",command=back)
b1.pack(side="top")
loginwn.mainloop()