import mysql.connector
from tkinter import *
import tkinter.messagebox as MessageBox
from tkinter import *
import webbrowser
from tkinter import *
from tkinter import ttk
import random
import tkinter.messagebox
from datetime import datetime
import time
from tkinter import *
from functools import partial
import math


def FrameRaiser(frame):
	frame.grid(row=0,column=0,ipadx="850",ipady="430",sticky="NEWS")
	frame.tkraise()

#MainWindow 
root=Tk()
root.geometry("850x430")
root.title("DataManagement")
#root.resizable(0,0)




#Frames
menu=Frame(root)
customer=Frame(root)
staff=Frame(root)
item=Frame(root)
adorn=Frame(root)
cake=Frame(root)
beverage=Frame(root)
about=Frame(root)
mainlogin=Frame(root)
billl=Frame(root)


FrameRaiser(mainlogin)

 #______________________login_______________________________

loginpage=PhotoImage(file="login.png")

Label(mainlogin,image= loginpage , bg="Black").place(x=-10,y=0)

user = Label(mainlogin, text = "Enter username:", fg = "#c78851", bg = "#10181e", font =("Goudy Old Style", 30)).place(x=450,y=500)
user = Entry(mainlogin,fg = "black", bg = "#c78851", font = ("Goudy Old Style", 25))
user.place(x=750,y=500)

password = Label(mainlogin, text = "Enter password:", fg = "#c78851", bg = "#10181e",font=("Goudy Old Style", 30)).place(x=450,y=570)
password = Entry(mainlogin,fg = "black", bg = "#c78851", font = ("Goudy Old Style", 25), show = "*")
password.place(x=750,y=570)
def click():
    if user.get()=="whippedbakery" and password.get()=='1234':
        FrameRaiser(menu)
    else:
        MessageBox.showerror()
Button(mainlogin,text="LOGIN",fg="white",bg="#10181e",bd=5,relief= RAISED,font = ("Goudy Old Style", 20),command = click).place(x=750,y=650)
         
      
      #______________________main menu_______________________________

mainmenu=PhotoImage(file="mu.png")

Label(menu,image= mainmenu , bg="Black").place(x=-10,y=0)

Button(menu, text="Customer",fg="white",bg="black",bd=5, relief= RAISED,font = ("Goudy Old Style",20), command=lambda: FrameRaiser(customer)).place(x=280,y=650)
Button(menu,text="Staff",fg="white",bg="black",bd=5,relief= RAISED,font = ("Goudy Old Style", 20), command=lambda: FrameRaiser(staff)).place(x=580,y=650)
Button(menu,text="Items",fg="white",bg="black",bd=5,relief= RAISED,font = ("Goudy Old Style", 20), command=lambda: FrameRaiser(item)).place(x=890,y=650)
Button(menu,text="Order here",fg="white",bg="black",bd=5,relief= RAISED,font = ("Goudy Old Style", 20), command=lambda: FrameRaiser(billl)).place(x=1150,y=650)
Button(menu,text="About Us",fg="white",bg="black",bd=5,relief= RAISED,font = ("Goudy Old Style", 20), command=lambda: FrameRaiser(about)).place(x=1440,y=650)

#______________________________customer________________________________________



def Cinsert():
    customer_id = e_id.get()
    name = e_name.get()
    phone_number = e_phone.get()
    bill_amount = e_amount.get()

    if(customer_id==" " or name==" " or phone_number==" " or bill_amount==" " ):
        MessageBox.showinfo("insert status", "all fields are required")
    else:
        connection = mysql.connector.connect(host = "localhost",user="cs",passwd="hamdard", database = "whipped_bakery",auth_plugin='mysql_native_password')
        cursor = connection.cursor()
        cursor.execute("insert into customer_info values('"+ customer_id +"', '"+ name +"', '"+ phone_number +"', '"+ bill_amount +"')")
        cursor.execute("commit")

        e_id.delete(0,'end') 
        e_name.delete(0,'end') 
        e_phone.delete(0,'end') 
        e_amount.delete(0,'end')
        Cshow() 
        MessageBox.showinfo("insert status","inserted successfully")
        connection.close()
def Cupdate():
    id = e_id.get()
    name = e_name.get()
    phone_number = e_phone.get()
    bill_amount = e_amount.get()

    if(customer_id==" " or name==" " or phone_number==" " or bill_amount==" " ):
        MessageBox.showinfo("update status", "all fields are required")
    else:
        connection = mysql.connector.connect(host = "localhost",user="cs",passwd="hamdard", database = "whipped_bakery",auth_plugin='mysql_native_password')
        cursor = connection.cursor()
        cursor.execute("update customer_info set name = '" + name + "', phone_number= '" + phone_number + "',bill_amount = '" + bill_amount + "' where customer_id = '"+ id +"'")
        cursor.execute("commit")

        e_id.delete(0,'end') 
        e_name.delete(0,'end') 
        e_phone.delete(0,'end') 
        e_amount.delete(0,'end')
        Cshow() 
        MessageBox.showinfo("update status","updated successfully")
        connection.close()

def Cdelete():
    if(e_id.get() == ""):
        MessageBox.showinfo("delete status", "all fields are required")
    else:
        connection = mysql.connector.connect(host = "localhost",user="cs",passwd="hamdard", database = "whipped_bakery",auth_plugin='mysql_native_password')
        cursor = connection.cursor()
        cursor.execute("delete from customer_info where customer_id='"+e_id.get()+"'")
        cursor.execute("commit")

        e_id.delete(0,'end') 
        e_name.delete(0,'end') 
        e_phone.delete(0,'end') 
        e_amount.delete(0,'end') 
        Cshow()
        MessageBox.showinfo("delete status","deleted successfully")
        connection.close()


def Cshow():
    connection = mysql.connector.connect(host = "localhost",user="cs",passwd="hamdard", database = "whipped_bakery",auth_plugin='mysql_native_password')
    cursor = connection.cursor()
    cursor.execute("select * from customer_info")
    rows = cursor.fetchall()
    Clist.delete(0,Clist.size())

    for row in rows:
        insertdata = str(row[0] + ' ' + row[1])
        Clist.insert(Clist.size() + 1, insertdata)

    connection.close() 

def Cget():
    if(e_id.get() == ""):
        MessageBox.showinfo("fetch status", "ID is compulsory to delete")
    else:
        connection = mysql.connector.connect(host = "localhost" ,user="cs",passwd="hamdard",  database = "whipped_bakery",auth_plugin='mysql_native_password')
        cursor = connection.cursor()
        cursor.execute("select * from customer_info where customer_id = '"+ e_id.get() + "'")
    rows = cursor.fetchall()
    Cshow()

    for row in rows:
        e_name. insert(0,row[1])
        e_phone. insert(0,row[2])
        e_amount. insert(0,row[3])

    connection.close()


Customerpic=PhotoImage(file="CUST.png")
Label(customer,image=Customerpic, bg="Black").place(x=-40,y=1)

customer_id = Label(customer, text="enter id ", font=("Goudy Old Style", 20), fg = "black")
customer_id.place(x=700,y=550)

name = Label(customer, text="enter name ", font=("Goudy Old Style", 20),  fg = "black")
name.place(x=700,y=600)

phone_number= Label(customer, text="enter number ", font=("Goudy Old Style", 20),  fg = "black")
phone_number.place(x=700,y=650)

bill_amount= Label(customer, text="enter amount ", font=("Goudy Old Style", 20), fg = "black")
bill_amount.place(x=700,y=700)

e_id = Entry(customer,font = ("Goudy Old Style",15))
e_id.place(x=900,y=550)

e_name = Entry(customer,font = ("Goudy Old Style",15))
e_name.place(x=900,y=600)

e_phone = Entry(customer,font = ("Goudy Old Style",15))
e_phone.place(x=900,y=650)

e_amount = Entry(customer,font = ("Goudy Old Style",15))
e_amount.place(x=900,y=700)
#button
insert = Button(customer, text = "insert", fg = "black" , font = ("Goudy Old Style",15),relief= RAISED,   command = Cinsert)
insert.place(x=600,y=770)

Button(customer, text = "delete",fg = "black", font = ("Goudy Old Style",15),command = Cdelete).place(x=670,y=770) 


Button(customer, text = "update", fg = "black", font = ("Goudy Old Style",15),command =  Cupdate).place(x=750,y=770)

Button(customer, text = "get", fg = "black", font = ("Goudy Old Style",15), command = Cget).place(x=840,y=770)

Button(customer, text = "home", fg = "black", font = ("Goudy Old Style",15),  command=lambda: FrameRaiser(menu)).place(x=900,y=770)

Clist = Listbox(customer, font = ("Goudy Old Style", 20) ,fg = "black")
Clist.place(x=1200,y=500)
Cshow()

#______________________________staff________________________________________
def Sinsert():
    staff_id = s_id.get()
    name = s_name.get()
    phone_number = s_phone.get()
    staff_add = s_address.get()
    present_or_left = s_pl.get()
    male_or_female = s_mf.get()
    age = s_age.get()
    email_id = s_email.get()

    if(staff_id==" " or name==" " or phone_number==" " or staff_add==" " or present_or_left=="" or male_or_female=="" or age=="" or email_id==""):
       MessageBox.showinfo("insert status", "all fields are required")
    else:
        connection = mysql.connector.connect(host = "localhost",user="cs",passwd="hamdard", database = "whipped_bakery",auth_plugin='mysql_native_password')
        cursor = connection.cursor()
        cursor.execute("insert into staff_info values('"+staff_id +"', '"+ name +"', '"+ phone_number +"', '"+ staff_add + "','"+ present_or_left +"','"+ male_or_female +"', '"+ age +"', '" + email_id +"'  )")
        cursor.execute("commit")

        s_id.delete(0,'end') 
        s_name.delete(0,'end') 
        s_phone.delete(0,'end')
        s_address.delete(0,'end')
        s_pl.delete(0,'end')
        s_mf.delete(0,'end')
        s_age.delete(0,'end')
        s_email.delete(0,'end') 
        Sshow() 
        MessageBox.showinfo("insert status","inserted successfully")
        connection.close()
def Supdate():          
    id = s_id.get()
    name = s_name.get()
    phone_number = s_phone.get()
    staff_add = s_address.get()
    present_or_left = s_pl.get()
    male_or_female = s_mf.get()
    age = s_age.get()
    email_id = s_email.get()

    if(staff_id==" " or name==" " or phone_number==" " or staff_add==" " or present_or_left=="" or male_or_female=="" or age=="" or
    email_id==""):
       MessageBox.showinfo("update status", "all fields are required")
    else:
        connection = mysql.connector.connect(host = "localhost",user="cs",passwd="hamdard", database = "whipped_bakery",auth_plugin='mysql_native_password')
        cursor = connection.cursor()
        cursor.execute("update staff_info set name = '" + name + "', phone_number= '" + phone_number + "', staff_add = '" + staff_add + "' where staff_id = '"+ id +"'")
        cursor.execute("commit")

        s_id.delete(0,'end') 
        s_name.delete(0,'end') 
        s_phone.delete(0,'end')
        s_address.delete(0, 'end')
        s_pl.delete(0,'end')
        s_mf.delete(0,'end')
        s_age.delete(0,'end')
        s_email.delete(0,'end') 
        Sshow() 
        MessageBox.showinfo("update status","updated successfully")
        connection.close()

def Sdelete():
    if(s_id.get() == ""):
       MessageBox.showinfo("delete status", "all fields are required")
    else:
        connection = mysql.connector.connect(host = "localhost",user="cs",passwd="hamdard", database = "whipped_bakery",auth_plugin='mysql_native_password')
        cursor = connection.cursor()
        cursor.execute("delete from staff_info where staff_id='"+s_id.get()+"'")
        cursor.execute("commit")

        s_id.delete(0,'end') 
        s_name.delete(0,'end') 
        s_phone.delete(0,'end') 
        s_address.delete(0,'end')
        s_pl.delete(0,'end')
        s_mf.delete(0,'end')
        s_age.delete(0,'end')
        s_email.delete(0,'end')
        Sshow()
        MessageBox.showinfo("delete status","deleted successfully")
        connection.close()

def Sshow():
    connection = mysql.connector.connect(host = "localhost",user="cs",passwd="hamdard", database = "whipped_bakery",auth_plugin='mysql_native_password')
    cursor = connection.cursor()
    cursor.execute("select * from staff_info")
    rows = cursor.fetchall()
    Slist.delete(0,Slist.size())

    for row in rows:
        insertdata = str(row[0] + ' ' + row[1])
        Slist.insert(Slist.size() + 1, insertdata)

    connection.close() 

def Sget():
    if(s_id.get() == ""):
        MessageBox.showinfo("fetch status", "ID is compulsory to delete")
    else:
        connection = mysql.connector.connect(host = "localhost" ,user="cs",passwd="hamdard",  database = "whipped_bakery",auth_plugin='mysql_native_password')
        cursor = connection.cursor()
        cursor.execute("select * from staff_info where staff_id = '"+ s_id.get() + "'")
    rows = cursor.fetchall()
    Sshow()

    for row in rows:
        s_name. insert(0,row[1])
        s_phone. insert(0,row[2])
        s_address. insert(0,row[3])
        s_pl.delete(0,row[4])
        s_mf.delete(0,row[5])
        s_age.delete(0,row[6])
        s_email.delete(0,row[7])

    connection.close()



staffpic=PhotoImage(file="S.png")
Label(staff,image=staffpic, bg="Black").place(x=-40,y=1)

staff_id = Label(staff, text="Enter id ", font=("Goudy Old Style", 20),  fg = "black")
staff_id.place(x=100,y=400)

name = Label(staff, text="Enter name ", font=("Goudy Old Style", 20), fg = "black")
name.place(x=100,y=450)

phone_number= Label(staff, text="Enter number ", font=("Goudy Old Style", 20),fg = "black")
phone_number.place(x=100,y=500)

address = Label(staff, text = "Enter address ", font = ("Goudy Old Style", 20), fg = "black")
address.place(x=100,y=550)

present_or_left = Label(staff, text = "Present or Left", font=("Goudy Old Style", 20), fg = "black")
present_or_left.place(x=100,y=600)

male_or_female = Label(staff, text = "Male or Female", font=("Goudy Old Style", 20), fg = "black")
male_or_female.place(x=100,y=650)

age = Label(staff, text = "Age", font=("Goudy Old Style", 20), fg = "black")
age.place(x=100,y=700)

email_id = Label(staff, text = "Email id", font=("Goudy Old Style", 20), fg = "black")
email_id.place(x=100,y=750)

s_id = Entry(staff, fg = "black" , font = ("Goudy Old Style",20))
s_id.place(x=400,y=400)

s_name = Entry(staff, fg = "black" , font = ("Goudy Old Style",20))
s_name.place(x=400,y=450)

s_phone = Entry(staff, fg = "black" , font = ("Goudy Old Style",20))
s_phone.place(x=400,y=500)

s_address = Entry(staff, fg= "black" , font = ("Goudy Old Style",20))
s_address.place(x=400,y=550)

s_pl = Entry(staff, fg= "black" , font = ("Goudy Old Style",20))
s_pl.place(x=400,y=600)

s_mf = Entry(staff, fg= "black" , font = ("Goudy Old Style",20))
s_mf.place(x=400,y=650)

s_age = Entry(staff, fg= "black" , font = ("Goudy Old Style",20))
s_age.place(x=400,y=700)

s_email = Entry(staff, fg= "black" , font = ("Goudy Old Style",20))
s_email.place(x=400,y=750)

Entry(staff, fg = "black" , font = ("Goudy Old Style",20)).place
    
#button
insert = Button(staff, text = "insert", font = ("Goudy Old Style",15), fg = "black",relief= RAISED,   command = Sinsert)
insert.place(x=700,y=750)

Button(staff, text = "delete", font = ("Goudy Old Style",15), fg = "black", command = Sdelete).place(x=790,y=750) 

Button(staff, text = "update", font = ("Goudy Old Style",15), fg = "black", command =  Supdate).place(x=890,y=750)

Button(staff, text = "get",font = ("Goudy Old Style",15), fg = "black", command = Sget).place(x=1000,y=750)

Button(staff, text = "home", font = ("Goudy Old Style",15), fg = "black", command=lambda: FrameRaiser(menu)).place(x=1050,y=750)

Slist = Listbox(staff, font = ("Goudy Old Style", 20) , fg = "black")
Slist.place(x=800,y=400)
Sshow()

#_____________________________item__________________________________


itempic=PhotoImage(file="it.png")
Label(item,image=itempic, bg="Black").place(x=-40,y=1)

#button

Button(item, text = "ADORN", font = ("Goudy Old Style",20), fg = "black", command = lambda: FrameRaiser(adorn)).place(x=120,y=700)

cakes = Button(item, text = "CAKE", font = ("Goudy Old Style",20), fg = "black", command = lambda: FrameRaiser(cake))
cakes.place(x=450,y=700)

beverages = Button(item, text = "BEVERAGES", font = ("Goudy Old Style",20), fg = "black", command = lambda: FrameRaiser(beverage))
beverages.place(x=850,y=700)

Button(item, text = "HOME", font = ("Goudy Old Style",20), fg = "black", command=lambda: FrameRaiser(menu)).place(x=1270,y=700)

#_________________________________adorn___________________________________________

def Kinsert():
    s_no = k_no.get()
    name = k_name.get()
    cost = k_cost.get()
    qty  = k_qty.get()

    if(s_no==" " or name==" " or cost==" " or qty==" "  ):
       MessageBox.showinfo("insert status", "all fields are required")
    else:
        connection = mysql.connector.connect(host = "localhost",user="cs",passwd="hamdard", database = "whipped_bakery",auth_plugin='mysql_native_password')
        cursor = connection.cursor()
        cursor.execute("insert into adorn values('"+ s_no +"', '"+ name +"', '"+ cost +"', '"+ qty +"')")
        cursor.execute("commit")

        k_no.delete(0,'end') 
        k_name.delete(0,'end') 
        k_cost.delete(0,'end') 
        k_qty.delete(0,'end')
        Kshow() 
        MessageBox.showinfo("insert status","inserted successfully")
        connection.close()

def Kupdate():          #not working
    s_no = k_no.get()
    name = k_name.get()
    cost = k_cost.get()
    qty  = k_qty.get()
   

    if(s_no==" " or name==" " or cost==" " or qty==" "  ):
       MessageBox.showinfo("update status", "all fields are required")
    else:
        connection = mysql.connector.connect(host = "localhost",user="cs",passwd="hamdard", database = "whipped_bakery",auth_plugin='mysql_native_password')
        cursor = connection.cursor()
        cursor.execute("update adorn set name = '" + name + "', cost = '" + cost + "',qty = '" + qty + "' where s_no = '"+ s_no +"'")
        cursor.execute("commit")

        
        k_no.delete(0,'end') 
        k_name.delete(0,'end') 
        k_cost.delete(0,'end') 
        k_qty.delete(0,'end')
        Kshow() 
        MessageBox.showinfo("update status","updated successfully")
        connection.close()

def Kdelete():       
    if(k_no.get() == ""):
       MessageBox.showinfo("delete status", "all fields are required")
    else:
        connection = mysql.connector.connect(host = "localhost",user="cs",passwd="hamdard", database = "whipped_bakery",auth_plugin='mysql_native_password')
        cursor = connection.cursor()
        cursor.execute("delete from adorn where s_no ='"+ k_no .get()+"'")
        cursor.execute("commit")

        
        k_no.delete(0,'end') 
        k_name.delete(0,'end') 
        k_cost.delete(0,'end') 
        k_qty.delete(0,'end')
        Kshow() 
        MessageBox.showinfo("delete status","deleted successfully")
        connection.close()

def Kshow():
    connection = mysql.connector.connect(host = "localhost",user="cs",passwd="hamdard", database = "whipped_bakery",auth_plugin='mysql_native_password')
    cursor = connection.cursor()
    cursor.execute("select * from adorn")
    rows = cursor.fetchall()
    Ilist.delete(0,Ilist.size())

    for row in rows:
        insertdata = str(row[0] + ' ' + row[1])
        Ilist.insert(Ilist.size() + 1, insertdata)

    connection.close() 

def Kget():
    if(k_no.get() == ""):
        MessageBox.showinfo("fetch status", "ID is compulsory to delete")
    else:
        connection = mysql.connector.connect(host = "localhost" ,user="cs",passwd="hamdard",  database = "whipped_bakery",auth_plugin='mysql_native_password')
        cursor = connection.cursor()
        cursor.execute("select * from adorn where s_no = '"+ k_no.get() + "'")
    rows = cursor.fetchall()
    Kshow()

    for row in rows:
        k_name. insert(0,row[1])
        k_cost. insert(0,row[2])
        k_qty. insert(0,row[3])


    connection.close()

adornpic=PhotoImage(file="ADORN.png")
Label(adorn,image=adornpic, bg="Black").place(x=1,y=2)

s_no = Label(adorn, text="enter s_no ", font=("Goudy Old Style", 20), fg = "black")
s_no.place(x=200,y=420)

name = Label(adorn, text="enter name ", font=("Goudy Old Style", 20), fg = "black")
name.place(x=200,y=470)

cost= Label(adorn, text="enter cost ", font=("Goudy Old Style", 20), fg = "black")
cost.place(x=200,y=520)

qty= Label(adorn, text="enter qty ", font=("Goudy Old Style",20), fg = "black")
qty.place(x=200, y=570)


k_no = Entry(adorn,bg = "white" , font = ("Goudy Old Style",15))
k_no.place(x=350,y=425)

k_name = Entry(adorn,bg = "white" , font = ("Goudy Old Style",15))
k_name.place(x=350,y=475)

k_cost = Entry(adorn,bg = "white" , font = ("Goudy Old Style",15))
k_cost.place(x=350,y=525)

k_qty = Entry(adorn,bg = "white" , font = ("Goudy Old Style",15))
k_qty.place(x=350,y=575)

    
#button
insert = Button(adorn, text = "INSERT", fg = "black" , font = ("Goudy Old Style",15),relief= RAISED,   command = Kinsert)
insert.place(x=200,y=700)

delete = Button(adorn, text = "DELETE", font = ("Goudy Old Style",15), fg = "black", relief= RAISED, command=  Kdelete)
delete.place(x=300,y=700)

update = Button(adorn, text = "UPDATE", font = ("Goudy Old Style",15), fg = "black", command = Kupdate)
update.place(x=400,y=700)

get = Button(adorn, text = "GET", font = ("Goudy Old Style",15), fg = "black", command= Kget)
get.place(x=510,y=700)
Button(adorn, text = "home", fg = "black", font = ("Goudy Old Style",15),  command=lambda: FrameRaiser(menu)).place(x=900,y=800)

Ilist = Listbox(adorn, font = ("Goudy Old Style", 15) , fg = "black")
Ilist.place(x=700,y=400)        #not working
Kshow()

#_______________________________________cake___________________________________________
def Binsert():         #not showing
    s_no = b_no.get()
    cakes = b_name.get()
    qty  = b_qty.get()
    price = b_price.get()

    if(s_no==" " or cakes==" " or  qty==" " or price==" "  ):
       MessageBox.showinfo("insert status", "all fields are required")
    else:
        connection = mysql.connector.connect(host = "localhost",user="cs",passwd="hamdard", database = "whipped_bakery",auth_plugin='mysql_native_password')
        cursor = connection.cursor()
        cursor.execute("insert into cake values('"+ s_no +"', '"+ cakes +"', '"+ qty +"', '"+ price +"')")
        cursor.execute("commit")

        b_no.delete(0,'end') 
        b_name.delete(0,'end') 
        b_qty.delete(0,'end') 
        b_price.delete(0,'end')
        Bshow() 
        MessageBox.showinfo("insert status","inserted successfully")
        connection.close()

def Bupdate():         #not showing
    s_no = b_no.get()
    cakes = b_name.get()
    qty  = b_qty.get()
    price = b_price.get()

    if(s_no==" " or cakes==" " or  qty==" " or price==" "  ):
       MessageBox.showinfo("update status", "all fields are required")
    else:
        connection = mysql.connector.connect(host = "localhost",user="cs",passwd="hamdard", database = "whipped_bakery",auth_plugin='mysql_native_password')
        cursor = connection.cursor()
        cursor.execute("update cake set cakes = '" + cakes + "', qty= '" + qty + "',price = '" + price + "' where s_no = '"+ s_no +"'")
        cursor.execute("commit")

        b_no.delete(0,'end') 
        b_name.delete(0,'end') 
        b_qty.delete(0,'end') 
        b_price.delete(0,'end')
        Bshow() 
        MessageBox.showinfo("update status","updated successfully")
        connection.close()

def Bdelete():         #not showing
    if(b_no.get() == ""):
       MessageBox.showinfo("delete status", "all fields are required")
    else:
        connection = mysql.connector.connect(host = "localhost",user="cs",passwd="hamdard", database = "whipped_bakery",auth_plugin='mysql_native_password')
        cursor = connection.cursor()
        cursor.execute("delete from cake where s_no ='"+ b_no .get()+"'")
        cursor.execute("commit")

        
        b_no.delete(0,'end') 
        b_name.delete(0,'end') 
        b_price.delete(0,'end') 
        b_qty.delete(0,'end')
        Bshow() 
        MessageBox.showinfo("delete status","deleted successfully")
        connection.close()

def Bshow():
    connection = mysql.connector.connect(host = "localhost",user="cs",passwd="hamdard", database = "whipped_bakery",auth_plugin='mysql_native_password')
    cursor = connection.cursor()
    cursor.execute("select * from cake")
    rows = cursor.fetchall()
    Ilist.delete(0,Ilist.size())

    for row in rows:
        insertdata = str(row[0] + ' ' + row[1])
        Ilist.insert(Ilist.size() + 1, insertdata)

    connection.close() 

def Bget():
    if(b_no.get() == ""):
        MessageBox.showinfo("fetch status", "ID is compulsory to delete")
    else:
        connection = mysql.connector.connect(host = "localhost" ,user="cs",passwd="hamdard",  database = "whipped_bakery",auth_plugin='mysql_native_password')
        cursor = connection.cursor()
        cursor.execute("select * from cake where s_no = '"+ b_no.get() + "'")
        rows = cursor.fetchall()
        Bshow()

    for row in rows:
        b_name. insert(0,row[1])
        b_price. insert(0,row[2])
        b_qty.insert(0,row[3])

    connection.close()

cakepic=PhotoImage(file="oo.png")
Label(cake,image=cakepic, bg="Black").place(x=-40,y=2)

s_no = Label(cake, text="enter s_no ", font=("Goudy Old Style", 20), fg = "black")
s_no.place(x=250,y=420)

name = Label(cake, text="enter name ", font=("Goudy Old Style", 20), fg = "black")
name.place(x=250,y=470)

qty= Label(cake, text="enter qty ", font=("Goudy Old Style", 20), fg = "black")
qty.place(x=250,y=520)

price= Label(cake, text="enter cost ", font=("Goudy Old Style", 20), fg = "black")
price.place(x=250,y=570)


b_no = Entry(cake, bg = "white" , font = ("Goudy Old Style",15))
b_no.place(x=450,y=430)

b_name = Entry(cake,bg = "white" , font = ("Goudy Old Style",15))
b_name.place(x=450,y=480)

b_qty = Entry(cake,bg = "white", font = ("Goudy Old Style",15) )
b_qty.place(x=450,y=530)

b_price = Entry(cake,bg = "white" , font = ("Goudy Old Style",15))
b_price.place(x=450,y=580)

    
#button
insert = Button(cake, text = "INSERT", fg = "black" , font = ("Goudy Old Style",15),relief= RAISED,   command = Binsert)
insert.place(x=200,y=700)

delete = Button(cake, text = "DELETE", font = ("Goudy Old Style",15), fg = "black", relief= RAISED, command=  Bdelete)
delete.place(x=300,y=700)

update = Button(cake, text = "UPDATE", font = ("Goudy Old Style",15), fg = "black", command = Bupdate)
update.place(x=400,y=700)

get = Button(cake, text = "GET", font = ("Goudy Old Style",15), fg = "black", command= Bget)
get.place(x=510,y=700)
Button(cake, text = "home", fg = "black", font = ("Goudy Old Style",15),  command=lambda: FrameRaiser(menu)).place(x=900,y=800)


Ilist = Listbox(cake, font = ("Goudy Old Style", 15) , bg = "white")
Ilist.place(x=750,y=400)
Bshow()

#_______________________________________beverages______________________________________

def Vinsert():
    s_no = v_no.get()
    drinks = v_name.get()
    price  = v_price.get()
    qty = v_qty.get()

    if(s_no==" " or drinks==" " or  price==" " or qty==" "  ):
       MessageBox.showinfo("insert status", "all fields are required")
    else:
        connection = mysql.connector.connect(host = "localhost",user="cs",passwd="hamdard", database = "whipped_bakery",auth_plugin='mysql_native_password')
        cursor = connection.cursor()
        cursor.execute("insert into beverages values('"+ s_no +"', '"+ drinks +"', '"+ price +"', '"+ qty +"')")
        cursor.execute("commit")

        v_no.delete(0,'end') 
        v_name.delete(0,'end') 
        v_qty.delete(0,'end') 
        v_price.delete(0,'end')
        Vshow() 
        MessageBox.showinfo("insert status","inserted successfully")
        connection.close()

def Vupdate():    #not working
    s_no = v_no.get()
    drinks = v_name.get()
    price  = v_price.get()
    qty = v_qty.get()

    if(s_no==" " or name==" " or  price==" " or qty==" "  ):
       MessageBox.showinfo("update status", "all fields are required")
    else:
        connection = mysql.connector.connect(host = "localhost",user="cs",passwd="hamdard", database = "whipped_bakery",auth_plugin='mysql_native_password')
        cursor = connection.cursor()
        cursor.execute("update cake set drinks = '" + v_name + "', qty= '" + qty + "',price = '" + price + "' where s_no = '"+ v_no +"'")
        cursor.execute("commit")

        v_no.delete(0,'end') 
        v_name.delete(0,'end') 
        v_qty.delete(0,'end') 
        v_price.delete(0,'end')
        Vshow() 
        MessageBox.showinfo("update status","updated successfully")
        connection.close()


def Vdelete():
    if(v_no.get() == ""):
       MessageBox.showinfo("delete status", "all fields are required")
    else:
        connection = mysql.connector.connect(host = "localhost",user="cs",passwd="hamdard", database = "whipped_bakery",auth_plugin='mysql_native_password')
        cursor = connection.cursor()
        cursor.execute("delete from beverages where s_no ='"+ v_no .get()+"'")
        cursor.execute("commit")

        
        v_no.delete(0,'end') 
        v_name.delete(0,'end') 
        v_qty.delete(0,'end') 
        v_price.delete(0,'end')
        Vshow() 
        MessageBox.showinfo("delete status","deleted successfully")
        connection.close()

def Vshow():
    connection = mysql.connector.connect(host = "localhost",user="cs",passwd="hamdard", database = "whipped_bakery",auth_plugin='mysql_native_password')
    cursor = connection.cursor()
    cursor.execute("select * from beverages")
    rows = cursor.fetchall()
    Ilist.delete(0,Ilist.size())

    for row in rows:
        insertdata = str(row[0] + ' ' + row[1])
        Ilist.insert(Ilist.size() + 1, insertdata)

    connection.close() 

def Vget():
    if(v_no.get() == ""):
        MessageBox.showinfo("fetch status", "ID is compulsory to delete")
    else:
        connection = mysql.connector.connect(host = "localhost" ,user="cs",passwd="hamdard",  database = "whipped_bakery",auth_plugin='mysql_native_password')
        cursor = connection.cursor()
        cursor.execute("select * from beverages where s_no = '"+ v_no.get() + "'")
    rows = cursor.fetchall()
    Vshow()

    for row in rows:
        v_name. insert(0,row[1])
        v_price. insert(0,row[2])
        v_qty.insert(0,row[3])

    connection.close()

beveragepic=PhotoImage(file="BEV.png")
Label(beverage,image=beveragepic, bg="Black").place(x=-20,y=1)

s_no = Label(beverage, text="enter s_no ", font=("Goudy Old Style", 20), fg = "black")
s_no.place(x=250,y=420)

name = Label(beverage, text="enter name ", font=("Goudy Old Style", 20), fg = "black")
name.place(x=250,y=470)

qty= Label(beverage, text="enter qty ", font=("Goudy Old Style", 20), fg = "black")
qty.place(x=250,y=520)

price= Label(beverage, text="enter cost ", font=("Goudy Old Style", 20), fg = "black")
price.place(x=250,y=570)


v_no = Entry(beverage, bg = "white" , font = ("Goudy Old Style",15))
v_no.place(x=450,y=430)

v_name = Entry(beverage,bg = "white" , font = ("Goudy Old Style",15))
v_name.place(x=450,y=480)

v_qty = Entry(beverage,bg = "white", font = ("Goudy Old Style",15) )
v_qty.place(x=450,y=530)

v_price = Entry(beverage,bg = "white" , font = ("Goudy Old Style",15))
v_price.place(x=450,y=580)

    
#button
insert = Button(beverage, text = "INSERT", fg = "black" , font = ("Goudy Old Style",15),relief= RAISED,   command = Vinsert)
insert.place(x=200,y=700)

delete = Button(beverage, text = "DELETE", font = ("Goudy Old Style",15), fg = "black", relief= RAISED, command=  Vdelete)
delete.place(x=300,y=700)

update = Button(beverage, text = "UPDATE", font = ("Goudy Old Style",15), fg = "black", command = Vupdate)
update.place(x=400,y=700)

get = Button(beverage, text = "GET", font = ("Goudy Old Style",15), fg = "black", command= Vget)
get.place(x=510,y=700)
Button(beverage, text = "home", fg = "black", font = ("Goudy Old Style",15),  command=lambda: FrameRaiser(menu)).place(x=900,y=800)


Ilist = Listbox(beverage, font = ("Goudy Old Style", 15) , bg = "white")
Ilist.place(x=750,y=400)
Vshow()

#__________________________________about__________________________________________

aboutpic=PhotoImage(file="LLL.png")

Label(about,image= aboutpic, bg="Black").place(x=-10,y=0) 


new = 1
new2 = 2
new3 = 3
url = "http://127.0.0.1:5501/whippedbakery.html"
qrl = "https://www.instagram.com/whip.pedbakery/"
prl = "https://www.twitter.com/Whippedbakery2/"

def openweb():
    webbrowser.open(url,new=new)
    

def openweb2():
    webbrowser.open(qrl,new=new2)
    

def openweb3():
    webbrowser.open(prl,new=new3)

Btn = Button(about, text = "www.whippedbakery.com",command=openweb,fg="dark orange",bg="white", relief= RAISED, width=28, font = ("Goudy Old Style", 20)).place(x=90,y = 630)

Atn = Button(about, text = "whip.pedbakery",command=openweb2,fg="dark orange",bg="white", relief= RAISED, width=20, font = ("Goudy Old Style", 20)).place(x=750,y = 630)

Ctn = Button(about, text = "Whippedbakery2",command=openweb3,fg="dark orange",bg="white", relief= RAISED, width=20, font = ("Goudy Old Style", 20)).place(x=1150,y = 630)

Button(about, text = "HOME", font = ("Goudy Old Style",20), fg = "black", command = lambda: FrameRaiser(menu)).place(x=120,y=730)






root.mainloop()