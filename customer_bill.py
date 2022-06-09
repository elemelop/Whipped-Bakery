#from tkinter import*
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
import math
class Customer_bill:
    
    def __init__(self,root):
        
        self.root = root
        self.root.geometry("1450x800+0+0")
        self.root.title("Customer Billing")
        title = Label(self.root, text = "Customer Billing", relief = GROOVE,bd = 5,font=("ILoveGlitter", 30),bg = "#bdc7eb", fg = "black")
        title.pack(fill = X)

        ABC1 = LabelFrame(self.root, text = "Customer Details", font = ("times new roman",15,"bold"), fg = "white",bg ="#bdc7eb")
        ABC1.place(x=0,y=60,relwidth = 1)

        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        #self.search_bill = StringVar()
        
        #===============================Customer Details========================== 
        customername_lbl = Label(ABC1, text = "Customer Name ",font =("Calibri",15) ,fg = "black", bg = "#bdc7eb")
        customername_lbl.grid(row=0,column = 0,pady = 5,padx = 10)
        customername_txt = Entry(ABC1,textvariable=self.c_name,font = ("Calibri",15))
        customername_txt.grid(row = 0,column= 1)

        customerphone_lbl = Label(ABC1, text = "Phone Number ", font = ("Calibri",15), fg = "black", bg ="#bdc7eb")
        customerphone_lbl.grid(row=0, column=2,padx=40)
        customerphone_txt = Entry(ABC1,textvariable=self.c_phone,font = ("Calibri",15))
        customerphone_txt.place(x=550,y=7)

        customerbill_lbl = Label(ABC1, text = "Bill No. ", font = ("Calibri",15), fg = "black", bg ="#bdc7eb")
        customerbill_lbl.grid(row=0, column=3,padx=210)
        customerbill_txt = Entry(ABC1,textvariable=self.bill_no,font = ("Calibri",15))
        customerbill_txt.place(x=870,y=7)

        
        #===============================================================================

        #=====================================VARIABLES============================
        self.Latta = IntVar()
        self.Iced_Latta = IntVar()
        self.Vale_Coffee = IntVar()
        self.Cappuccino = IntVar()
        self.African_Coffee = IntVar()

        self.Butterscotch = IntVar()
        self.Pineapple = IntVar()
        self.Strawberry = IntVar()
        self.Blackforest = IntVar()
        self.Turkishdelight = IntVar()

        self.balloons = IntVar()
        self.banners = IntVar()
        self.confetti = IntVar()
        self.Streamers = IntVar()

        #================================Adorn==========================================
        ABC2 = LabelFrame(self.root, text = "Adorn", font = ("times new roman",15,"bold"), fg = "white",bg ="#bdc7eb")
        ABC2.place(x=3,y=130,width = 325, height =380)

        balloons_lbl = Label(ABC2, text = "Balloons ", font = ("Calibri",15), fg = "black", bg ="#bdc7eb")
        balloons_lbl.grid(row=0, column=0,padx=10,pady=10,sticky="w")
        balloons_txt = Entry(ABC2,textvariable=self.balloons,font = ("Calibri",15),width=10)
        balloons_txt.place(x=130,y=12)

        banners_lbl = Label(ABC2, text = "Banners ", font = ("Calibri",15), fg = "black", bg ="#bdc7eb")
        banners_lbl.grid(row=1, column=0,padx=10,pady=10,sticky="w")
        banners_txt = Entry(ABC2,textvariable=self.banners,font = ("Calibri",15),width=10)
        banners_txt.place(x=130,y=58)

        confetti_lbl = Label(ABC2, text = "Confetti ", font = ("Calibri",15), fg = "black", bg ="#bdc7eb")
        confetti_lbl.grid(row=2, column=0,padx=10,pady=10,sticky="w")
        confetti_txt = Entry(ABC2,textvariable=self.confetti,font = ("Calibri",15),width=10)
        confetti_txt.place(x=130,y=108)

        Streamers_lbl = Label(ABC2, text = "Streamers ", font = ("Calibri",15), fg = "black", bg ="#bdc7eb")
        Streamers_lbl.grid(row=3, column=0,padx=10,pady=9,sticky="w")
        Streamers_txt = Entry(ABC2,textvariable=self.Streamers,font = ("Calibri",15),width=10)
        Streamers_txt.place(x=130,y=158)

        #=============================Cake=================================
        ABC3 = LabelFrame(self.root,text="Cake",font=("times new roman",15,"bold"), fg = "white",bg ="#bdc7eb")
        ABC3.place(x=330,y=130,width=325,height=380)

        Butterscotch_lbl = Label(ABC3, text = "Butterscotch ", font = ("Calibri",15), fg = "black", bg ="#bdc7eb")
        Butterscotch_lbl.grid(row=0, column=0,padx=10,pady=10,sticky="w")
        Butterscotch_txt = Entry(ABC3,textvariable=self.Butterscotch,font = ("Calibri",15),width=10)
        Butterscotch_txt.place(x=150,y=12)

        Pineapple_lbl = Label(ABC3, text = "Pineapple ", font = ("Calibri",15), fg = "black", bg ="#bdc7eb")
        Pineapple_lbl.grid(row=1, column=0,padx=10,pady=10,sticky="w")
        Pineapple_txt = Entry(ABC3,textvariable=self.Pineapple,font = ("Calibri",15),width=10)
        Pineapple_txt.place(x=150,y=58)

        Strawberry_lbl = Label(ABC3, text = "Strawberry ", font = ("Calibri",15), fg = "black", bg ="#bdc7eb")
        Strawberry_lbl.grid(row=2, column=0,padx=10,pady=10,sticky="w")
        Strawberry_txt = Entry(ABC3,textvariable=self.Strawberry,font = ("Calibri",15),width=10)
        Strawberry_txt.place(x=150,y=108)

        Blackforest_lbl = Label(ABC3, text = "Blackforest ", font = ("Calibri",15), fg = "black", bg ="#bdc7eb")
        Blackforest_lbl.grid(row=3, column=0,padx=10,pady=10,sticky="w")
        Blackforest_txt = Entry(ABC3,textvariable=self.Blackforest,font = ("Calibri",15),width=10)
        Blackforest_txt.place(x=150,y=158)

        Turkishdelight_lbl = Label(ABC3, text = "Turkishdelight ", font = ("Calibri",15), fg = "black", bg ="#bdc7eb")
        Turkishdelight_lbl.grid(row=4, column=0,padx=10,pady=10,sticky="w")
        Turkishdelight_txt = Entry(ABC3,textvariable=self.Turkishdelight,font = ("Calibri",15),width=10)
        Turkishdelight_txt.place(x=150,y=210)

        """balloons_lbl = Label(ABC2, text = "Balloons ", font = ("Calibri",15), fg = "black", bg ="#bdc7eb")
        balloons_lbl.grid(row=0, column=0,padx=10,pady=10,sticky="w")
        balloons_txt = Entry(ABC2,font = ("Calibri",15),width=10)
        balloons_txt.place(x=100,y=12)"""

        #==========================Beverage==========================
        ABC4 = LabelFrame(self.root,text="Beverage",font=("times new roman",15,"bold"), fg = "white",bg ="#bdc7eb")
        ABC4.place(x=658,y=130,width=325,height=380)

        Latta_lbl = Label(ABC4, text = "Latta ", font = ("Calibri",15), fg = "black", bg ="#bdc7eb")
        Latta_lbl.grid(row=0, column=0,padx=10,pady=10,sticky="w")
        Latta_txt = Entry(ABC4,textvariable=self.Latta,font = ("Calibri",15),width=10)
        Latta_txt.place(x=150,y=12)

        Iced_Latta_lbl = Label(ABC4, text = "Iced Latta", font = ("Calibri",15), fg = "black", bg ="#bdc7eb")
        Iced_Latta_lbl.grid(row=1, column=0,padx=10,pady=10,sticky="w")
        Iced_Latta_txt = Entry(ABC4,textvariable=self.Iced_Latta,font = ("Calibri",15),width=10)
        Iced_Latta_txt.place(x=150,y=58)

        Vale_Coffee_lbl = Label(ABC4, text = "Vale Coffee", font = ("Calibri",15), fg = "black", bg ="#bdc7eb")
        Vale_Coffee_lbl.grid(row=2, column=0,padx=10,pady=10,sticky="w")
        Vale_Coffee_txt = Entry(ABC4,textvariable=self.Vale_Coffee,font = ("Calibri",15),width=10)
        Vale_Coffee_txt.place(x=150,y=108)

        Cappuccino_lbl = Label(ABC4, text = "Cappuccino", font = ("Calibri",15), fg = "black", bg ="#bdc7eb")
        Cappuccino_lbl.grid(row=3, column=0,padx=10,pady=10,sticky="w")
        Cappuccino_txt = Entry(ABC4,textvariable=self.Cappuccino,font = ("Calibri",15),width=10)
        Cappuccino_txt.place(x=150,y=158)

        African_Coffee_lbl = Label(ABC4, text = "African Coffee", font = ("Calibri",15), fg = "black", bg ="#bdc7eb")
        African_Coffee_lbl.grid(row=4, column=0,padx=10,pady=10,sticky="w")
        African_Coffee_txt = Entry(ABC4,textvariable=self.African_Coffee,font = ("Calibri",15),width=10)
        African_Coffee_txt.place(x=150,y=210)
        #====================================================================================

        #=======================Bill Area=======================================
        """ABC5 = Frame(self.root,bd=10,relief=GROOVE)
        ABC5.place(x=990,y=130,height=385,width=400)

        bill_title=Label(ABC5,text="BILL AREA",font=("Calibri",15),relief=GROOVE)
        #bill_title.grid(row=0,column=0)
        bill_title.pack(fill=X)

        scroll = Scrollbar(ABC5,orient=VERTICAL)
        self.txtarea = Text(ABC5, yscrollcommand = scroll.set)
        scroll.pack(side = RIGHT, fill = Y)
        scroll.config(command = self.txtarea.yview)
        self.txtarea.pack(fill = BOTH, expand = 1)"""

        #=======================================================================

        self.cake_price = StringVar()
        self.adorn_price = StringVar()
        self.beverage_price = StringVar()

        self.cake_tax = StringVar()
        self.adorn_tax = StringVar()
        self.beverage_tax = StringVar()


        ABC6 = LabelFrame(self.root,relief=GROOVE,text="BILL",bg="#bdc7eb",font=("times new roman",20,"bold"),fg="white")
        ABC6.place(x=3,y=515,width=1435,height=320)

        a1_lbl = Label(ABC6,text="  Total Adorn Price ", bg="#bdc7eb",font=("times new roman",20),fg="black").grid(row=0,column=0)
        a1_txt=Entry(ABC6,textvariable=self.adorn_price,font=("times new roman",20),fg="black",width=10)
        a1_txt.place(x=250,y=3)

        a2_lbl = Label(ABC6,text="Total Cake Price ", bg="#bdc7eb",font=("times new roman",20),fg="black").grid(row=2,column=0,pady=50)
        a2_txt=Entry(ABC6,textvariable=self.cake_price,font=("times new roman",20),fg="black",width=10)
        a2_txt.place(x=250,y=90)

        a3_lbl = Label(ABC6,text="  Total Beverage Price ", bg="#bdc7eb",font=("times new roman",20),fg="black").grid(row=3,column=0)
        a3_txt=Entry(ABC6,textvariable=self.beverage_price,font=("times new roman",20),fg="black",width=10)
        a3_txt.place(x=250,y=177)

        b1_lbl = Label(ABC6,text="  Adorn Tax ", bg="#bdc7eb",font=("times new roman",20),fg="black").grid(row=0,column=1)
        b1_txt=Entry(ABC6,textvariable=self.adorn_tax,font=("times new roman",20),fg="black",width=10)
        b1_txt.place(x=600,y=3)

        b2_lbl = Label(ABC6,text="Cake Tax ", bg="#bdc7eb",font=("times new roman",20),fg="black").grid(row=2,column=1,pady=50,padx=200)
        b2_txt=Entry(ABC6,textvariable=self.cake_tax,font=("times new roman",20),fg="black",width=10)
        b2_txt.place(x=600,y=90)

        b3_lbl = Label(ABC6,text="  Beverage Tax ", bg="#bdc7eb",font=("times new roman",20),fg="black").grid(row=3,column=1)
        b3_txt=Entry(ABC6,textvariable=self.beverage_tax,font=("times new roman",20),fg="black",width=10)
        b3_txt.place(x=600,y=177)

       #============================TOTAL===============================
        def total():
            self.total_cake_price=(
                                    (self.Butterscotch.get()*250)+
                                    (self.Pineapple.get()*200)+
                                    (self.Strawberry.get()*350)+
                                    (self.Blackforest.get()*550)+
                                    (self.Turkishdelight.get()*450)
                                    )
            self.cake_price.set(str(self.total_cake_price))
            self.cake_tax.set(str(self.total_cake_price*0.25))

            self.total_adorn_price=(
                                     (self.balloons.get()*100)+
                                     (self.banners.get()*100)+
                                     (self.confetti.get()*100)+
                                     (self.Streamers.get()*100))
            self.adorn_price.set(str(self.total_adorn_price))
            self.adorn_tax.set(str(self.total_adorn_price*0.25))

            self.total_beverage_price=(
                                        (self.Latta.get()*240)+
                                        (self.Iced_Latta.get()*340)+
                                        (self.Vale_Coffee.get()*200)+
                                        (self.Cappuccino.get()*280)+
                                        (self.African_Coffee.get()*300))
            self.beverage_price.set(str(self.total_beverage_price))
            self.beverage_tax.set(str(self.total_beverage_price*0.25))


        
        #======================================EXIT=======================================
        def iExit():
            iExit = messagebox.askyesno("Customer Billing","Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        #================================================================================  
        #==================================RESET=================================
        def Reset():
            #self.txtarea.delete("1.0", END)
            self.Latta.set("0")
            self.Iced_Latta.set("0")
            self.Vale_Coffee.set("0")
            self.Cappuccino.set("0")
            self.African_Coffee.set("0")
            self.Butterscotch.set("0")
            self.Pineapple.set("0")
            self.Strawberry.set("0")
            self.Blackforest.set("0")
            self.Turkishdelight.set("0")
            self.balloons.set("0")
            self.banners.set("0")
            self.confetti.set("0")
            self.Streamers.set("0")
            self.adorn_price.set("")
            self.beverage_price.set("")
            self.cake_price.set("")
            self.cake_tax.set("")
            self.adorn_tax.set("")
            self.beverage_tax.set("")
            self.c_name.set("")
            self.c_phone.set("")
            self.bill_no.set("")

        #==============================BUTTONS FRAME===========================
        ABC7 = LabelFrame(self.root,relief=SUNKEN,bg="#bdc7eb")
        ABC7.place(x=809,y=540,width=620,height=110)

        total_button = Button(ABC7,padx=12,pady=25,command=total,text="TOTAL",font=("times new roman",20),bg="white")
        total_button.grid(row=0,column=0,pady=5,padx=2)

        Generate_button = Button(ABC7,padx=5,pady=25,text="GENERATE BILL",font=("times new roman",20),bg="white")
        Generate_button.grid(row=0,column=1,pady=5,padx=2)

        Reset_button = Button(ABC7,padx=12,pady=25,text="RESET",command=Reset,font=("times new roman",20),bg="white")
        Reset_button.grid(row=0,column=2,pady=5,padx=2)

        Exit_button = Button(ABC7,command=iExit,padx=12,pady=25,text="EXIT",font=("times new roman",20),bg="white")
        Exit_button.grid(row=0,column=3,pady=5,padx=2)
        #===========================================================================


        



        


root = Tk()
app = Customer_bill(root)
root.mainloop()