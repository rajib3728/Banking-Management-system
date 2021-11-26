from tkinter import *
from tkinter import ttk
from tkinter import ttk,messagebox
from PIL import ImageTk 
import mysql.connector as mysql
def well():
    if e1.get()=="" or e2.get()=="":
        messagebox.showinfo("STATUS","both required if any thing is zreo then type 0")
    else:
        credit=e1.get()
        debit=e2.get()
        db3=mysql.connect(host="localhost",user="root",password="",database="bankacc")   
        mycursor3=db3.cursor() 
        sq3="insert into work(credit,debit)values(%s,%s)"
        val3=(credit,debit)

        mycursor3.execute(sq3,val3)
        db3.commit()
        e1.delete(0,'end')
        e2.delete(0,'end')
        messagebox.showinfo("INSERT STATUS","Inserted sucessfully");
        db3.close() 
def exit():
    rt.destroy()  
def good():    
    if e1.get()=="" or e2.get()=="":
        messagebox.showinfo("Status","both required if any thing is zreo then type 0")
    else:
        credit=e1.get()
        debit=e2.get()
        db=mysql.connect(host="localhost",user="root",password="",database="bankacc")   
        mycursor=db.cursor() 
        sq="insert into work(credit,debit)values(%s,%s)"
        val=(credit,debit)

        mycursor.execute(sq,val)
        db.commit()
        e1.delete(0,'end')
        e2.delete(0,'end')
        messagebox.showinfo("INSERT STATUS","Inserted sucessfully");
        db.close()    
def det():
    db2 = mysql.connect(host="localhost", user="root", password="", database="bankacc")
    mycursor2 = db2.cursor()
    mycursor2.execute("delete from work")
    messagebox.showinfo("status","success")
    db2.commit()
    db2.close()   
def vt():
    db1 = mysql.connect(host="localhost", user="root", password="", database="bankacc")
    mycursor1 = db1.cursor()
    mycursor1.execute("select * from work")
    rows=mycursor1.fetchall()
    if len(rows)!=0:
        medtab.delete(*medtab.get_children())
    for row in rows:
       medtab.insert('',END,values=row)
    db1.commit()
    db1.close()
def ref():
    rt.destroy()
    import workpage    
rt=Tk()
rt.geometry("1600x900")
bg=ImageTk.PhotoImage(file="C:\\Users\\Rajib Kr paul\\OneDrive\Documents\\visiual stdio code\\project\\locker.jpg")
bglb=Label(rt,image=bg)
bglb.place(x=0,y=0,relwidth=1,relheight=1)
l_title=Message(rt,text="work page",relief="raised",width=2000,padx=600,pady=0,fg="black",bg="yellow",justify="center",anchor="center")
l_title.config(font=("Courier","50","bold"))
l_title.pack(side="top")
rt.title("Workplace")
l1=Label(rt,text="Enter credit:",relief="raised",bg="yellow",font=30)
l1.place(x=600,y=200)
e1=Entry(rt,bg="cyan")
e1.place(x=700,y=200)
l2=Label(rt,text="Enter debit:",relief="raised",bg="yellow",font=30)
l2.place(x=600,y=250)
e2=Entry(rt,bg="cyan")
e2.place(x=700,y=250)
b=Button(rt,text="debit",command=well,font=30,bg="green")
b.place(x=900,y=240)
b1=Button(rt,text="credit",command=good,font=30,bg="green")
b1.place(x=900,y=200)
b2=Button(rt,text="EXIT",command=exit,font=30,bg="red")
b2.place(x=750,y=350)
b3=Button(rt,text="delete transaction",font=30,bg="yellow",command=det)
b3.place(x=600,y=300)
b4=Button(rt,text="view transaction",font=30,bg="yellow",command=vt)
b4.place(x=780,y=300)
b5=Button(rt,text="Refresh",font=30,bg="yellow",command=ref)
b5.place(x=950,y=300)
detfrm=Frame(rt,bd=4,relief=RIDGE,bg="light blue")
detfrm.place(x=400,y=400,width=780,height=300)
detfrm=Frame(rt,bd=4,relief=RIDGE,bg="light blue")
detfrm.place(x=460,y=430,width=650,height=250)
tabfrm=Frame(detfrm,bd=4,relief=RIDGE,bg="lightblue")
tabfrm.place(x=10,y=10,width=600,height=230)
scrollx=Scrollbar(tabfrm,orient=HORIZONTAL)
scrolly=Scrollbar(tabfrm,orient=VERTICAL)
medtab=ttk.Treeview(tabfrm,columns=("credit","debit"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
scrollx.pack(side=BOTTOM,fill=X)
scrolly.pack(side=RIGHT,fill=Y)
scrollx.config(command=medtab.xview)
scrolly.config(command=medtab.yview)
medtab.heading("credit",text="credit")
medtab.heading("debit",text="debit")
medtab['show']="headings"
medtab.column("credit",width=200)
medtab.column("debit",width=300)
medtab.pack(fill=BOTH,expand=1)
medtab.bind("<ButtonRelease-1>",vt)
rt.mainloop()