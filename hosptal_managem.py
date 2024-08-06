from tkinter import*
from tkinter import messagebox
import csv
import os

UserNmae=[];password=[];mo_number=[];gmail=[];age=[]   # not neaded
# data=[]
def login():
    username = entry1.get()
    password = entry2.get()

    if  username == ''and password =='':
        messagebox.showerror('login','blank are not allowed ')
    
    elif os.path.exists("file1.csv"):
        f=open("file1.csv","r")
        creat=csv.reader(f)
        name=[]
        passw=[]
        for i in creat:                                                
            name.append(i[0]) 
            passw.append(i[1])
            if username in name and password in passw:
                messagebox.showinfo('login','login successfill')
                root.destroy()
                top=Tk()
                top.configure(bg='white')
    
    else:
        messagebox.showwarning('login','incorrect username and password')

def register():
    root.destroy()
    top=Tk()
    top.configure(bg='black')

    Label1=Label(top,text='enter your details',bg="blue",fg='black',font=("areal",25))
    Label1.place(x=600,y=10)

    Label2=Label(top,text="UserNmae :",font=("areal",20),bg="blue4",fg='white',)
    Label2.place(x=110,y=120)
    Label3=Label(top,text="password :",font=("areal",20),bg="blue4",fg='white',)
    Label3.place(x=110,y=200)
    Label4=Label(top,text="mo.number :",font=("areal",20),bg="blue4",fg='white',)
    Label4.place(x=110,y=280)
    Label5=Label(top,text="gmail:",font=("areal",20),bg="blue4",fg='white',)
    Label5.place(x=110,y=360)
    Label6=Label(top,text="age:",font=("areal",20),bg="blue4",fg='white',)
    Label6.place(x=110,y=440)

    entry3=Entry(top,font=("areal",20))
    entry3.place(x=280,y=120)
    entry4=Entry(top,font=("areal",20))
    entry4.place(x=280,y=200)
    entry5=Entry(top,font=("areal",20))
    entry5.place(x=280,y=280)
    entry6=Entry(top,font=("areal",20))
    entry6.place(x=280,y=360)
    entry7=Entry(top,font=("areal",20))
    entry7.place(x=280,y=440)
    
    def register_complet():

        UserNmae=entry3.get()
        password=entry4.get()
        mo_number=entry5.get()
        gmail=entry6.get()
        age=entry7.get()

        # data.append([UserNmae,password,mo_number,gmail,age])

        if UserNmae == '' and password =='' and mo_number =='' and gmail =='' and age =='':
            messagebox.showerror('REGISTER','blank are not allowed ')
        else:
            messagebox.showinfo('REGISTER','register is complet successfully ')
            if os.path.exists("file1.csv")==FALSE:
                with open("file1.csv","w",newline='') as f:
                    creat=csv.writer(f) 
                    creat.writerow([UserNmae,password,mo_number,gmail,age])     
                    top.destroy()
                import hosptal_managem

            else:
                with open("file1.csv","a",newline='') as f:
                    creat=csv.writer(f) 
                    creat.writerow([UserNmae,password,mo_number,gmail,age])
                    top.destroy()
                import hosptal_managem

    button3=Button(top,text="register complet",bg='maroon',fg='white',font=("areal",17),bd=6,command=register_complet)
    button3.place(x=550,y=550)


root=Tk()
root.configure(bg='black')

global entry1
global entry2


Label1=Label(root,text='login page',bg="blue",fg='black',font=("areal",25))
Label1.place(x=600,y=10)

Label2=Label(root,text="UserNmae :",font=("areal",20),bg="blue4",fg='white',)
Label2.place(x=110,y=120)
Label3=Label(root,text="password :",font=("areal",20),bg="blue4",fg='white',)
Label3.place(x=110,y=200)


entry1=Entry(root,font=("areal",20))
entry1.place(x=280,y=120)
entry2=Entry(root,font=("areal",20))
entry2.place(x=280,y=200)

button1=Button(root,text='login',bg='blue4',fg='white',font=("areal",17),bd=5,command=login)
button1.place(x=400,y=400)
button2=Button(root,text="register:",font=("areal",20),bg="blue4",fg='white',bd=5,command=register)
button2.place(x=110,y=400)

root.mainloop()
