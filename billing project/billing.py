import random
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
import sqlite3
import datetime as dt
from tkinter import messagebox as ms
import os

root=Tk()
root.geometry("990x830")
root.maxsize(height=750,width=990)
root.title("billing 'kiran'")

date=dt.date.today()
ran_num = random.randint(1,1000000)


#___________________________sql area_________________________________
con=sqlite3.connect("bill.db")
c=con.cursor()
# c.execute("create table if not exists product1(code int,name text,qty int,price int)")
# c.execute("create table if not exists bills(bill_no int,date text,name text,qty int,total int)")
# c.execute("create table if not exists daybill(bill_no int,date text,qty int,total int)")


#c.execute("insert into product values(20,'mango',50)")
#c.execute("insert into bills values(10000,'15/05/2022','kiran',5,50000)")
#c.execute("insert into daybill values(1,'23/05/2022',5,50000)")

#con.commit()


#________________________frem no 1____________________________________________
f1=Frame(relief=RIDGE,borderwidth=2)
f1.place(x=5,y=5,width=450,height=180)




#label
f1l1=Label(f1,text="Date :",font="Vardana 10 bold")
f1l1.place(x=10,y=5)

f1l2=Label(f1,text="Bill Number :",font="Vardana 10 bold")
f1l2.place(x=200,y=5)

f1l3=Label(f1,text="Name of bill :",font="Vardana 10 bold")
f1l3.place(x=5,y=40)

f1l4=Label(f1,text="Contact Number :",font="Vardana 10 bold")
f1l4.place(x=5,y=80)

#entry
f1e1=Entry(f1,font="Vardana 10 bold",width=15)
f1e1.place(x=70,y=5)
f1e1.insert(END,date)

f1e2=Entry(f1,font="Vardana 10 bold",width=15)
f1e2.place(x=300,y=5)
f1e2.insert(END,ran_num)

f1e3=Entry(f1,font="Vardana 10 bold",width=20)
f1e3.place(x=100,y=40)



f1e4=Entry(f1,font="Vardana 10 bold",width=20)
f1e4.place(x=120,y=80)
#combobox
pymethod=["Cash","Net banking"]
com1=Combobox(f1,values=pymethod,font="Vardana 10 bold",state="readonly")
com1.place(x=280,y=40)
com1.set("Pyment Method",)






#_________________________________frem no 1.5 _________________________________________________________
def add_item():
    itemid=f1_5e1.get()
    itemname=f1_5e2.get()
    itemqty=f1_5e3.get()
    itemprice=f1_5e4.get()

    if itemid=="" or itemname=="" or itemqty=="" or itemprice=="":
        ms.showerror("error","fill someting")
    else:
        c.execute(f"insert into product1 values({itemid},'{itemname}',{itemqty},{itemprice})")
        con.commit()

    f1_5e1.delete(0, END)
    f1_5e2.delete(0, END)
    f1_5e3.delete(0, END)
    f1_5e4.delete(0, END)

root.bind("<Return>", add_item)


def delete_item():
    itemname=f1_5e2.get()
    if  itemname == "":
        ms.showerror("error", "fill someting")
    else:
        c.execute(f"delete from product1 where name='{itemname}'")
        con.commit()

    f1_5e1.delete(0, END)
    f1_5e2.delete(0, END)
    f1_5e3.delete(0, END)
    f1_5e4.delete(0, END)

f1_5=Frame(relief=RIDGE,borderwidth=2)
f1_5.place(x=500,y=5,width=480,height=180)
# Label
f1_5l1=Label(f1_5,text="Add and Delete Item in the stock",font="Vardana 10 bold")
f1_5l1.place(x=5,)

f1_5l2=Label(f1_5,text="Item Code :",font="Vardana 10 bold")
f1_5l2.place(x=5,y=40)

f1_5l3=Label(f1_5,text="Item Name :",font="Vardana 10 bold")
f1_5l3.place(x=5,y=100)

f1_5l4=Label(f1_5,text="Qty :",font="Vardana 10 bold")
f1_5l4.place(x=250,y=40)

f1_5l5=Label(f1_5,text="Price :",font="Vardana 10 bold")
f1_5l5.place(x=250,y=100)
# entry
f1_5e1=Entry(f1_5,font="Vardana 10 bold")
f1_5e1.place(x=90,y=40)

f1_5e2=Entry(f1_5,font="Vardana 10 bold")
f1_5e2.place(x=90,y=100)


f1_5e3=Entry(f1_5,font="Vardana 10 bold")
f1_5e3.place(x=300,y=40)

f1_5e4=Entry(f1_5,font="Vardana 10 bold")
f1_5e4.place(x=300,y=100)
#Button
f1_5b1=Button(f1_5,text="Add Item",font="Vardana 10 bold",command=add_item)
f1_5b1.place(x=40,y=140)

f1_5b1=Button(f1_5,text="Delete Item",font="Vardana 10 bold",command=delete_item)
f1_5b1.place(x=120,y=140)

#_________________________________fream no 2______________________________________
f2=Frame(relief=RIDGE,borderwidth=2)
f2.place(x=5,y=190,width=975,height=290)

#serch

scr=Scrollbar(f2)

scr.pack(fill=Y,side=RIGHT)

#product treeview
column="Item code","Item name","qty","Price"
tre=ttk.Treeview(f2,show='headings',column=column,yscrollcommand=scr.set)

tre.column("Item code",width=215,anchor="w")
tre.column("Item name",width=400,anchor="w")
tre.column("Price",width=100,anchor="w")
tre.column("Price",width=180,anchor="w")


tre.heading("Item code",text="Item code",anchor="w")
tre.heading("Item name",text="Item name",anchor="w")
tre.heading("qty",text="Qty",anchor="w")
tre.heading("Price",text="Price",anchor="w")

# show all func
def show_all():
    try:
        for i in tre.get_children():
            tre.delete(i)
        c.execute("SELECT * from product1")
        ra=c.fetchall()
        for i in ra:
            tre.insert('',"end",text="", values=(f"{i[0]}",f"{i[1]}",f"{i[2]}",f"{i[3]}"))
    except:
        pass

#serch func
def search_item():
    try:
        en=f2e1.get()
        if en=="":
            ms.showerror("error","emty search box")
        else:
            for i in tre.get_children():
                tre.delete(i)
            c.execute(f"select * from product1 where name like '{en}%'")
            ra=c.fetchall()
            for i in ra:
                tre.insert('', "end", text="", values=(f"{i[0]}", f"{i[1]}", f"{i[2]}",f"{i[3]}"))
        f2e1.delete(0,END)
    except:
        pass

tre.pack()

scr.config(command=tre.yview())

#func feach data in treeview

# fill in the entry box

lis_name=[]
lisqty=[]
listotal=[]

def itemfeach():
    try:
        tu=tre.focus()
        name=tre.item(tu,'values')[1]
        pri=tre.item(tu,'values')[3]

        # aapending name area
        lis_name.append(name)

        # price inset area
        cal_price = int(pri) * var_add_qty.get()
        listotal.append(cal_price)
        f3e4.delete(0, END)
        f3e4.insert(END, sum(listotal))

        #qty insert area
        lisqty.append(int(var_add_qty.get()))
        f3e1.delete(0, END)
        f3e1.insert(END,sum(lisqty))


    except:
        ms.showerror("erorr","fill qty")
    f2e2.delete(0,END)



var_add_qty=IntVar()

#Lable
f2l1=Label(f2,text="Search Item \n search by code",font="Vardana 10 bold")
f2l1.place(x=30,y=240)

f2l2=Label(f2,text="|\n|\n|\n",font="Vardana 10 bold")
f2l2.place(x=480,y=230)

f2l3=Label(f2,text="billing input",font="Vardana 10 ")
f2l3.place(x=490,y=250)

f2l4=Label(f2,text="Qty :",font="Vardana 10 bold")
f2l4.place(x=650,y=228)

# entry
f2e1=Entry(f2,width=20,font="Vardana 10 bold")
f2e1.place(x=170,y=250)

f2e2=Entry(f2,width=10,font="Vardana 10 bold",textvariable=var_add_qty)
f2e2.place(x=610,y=250)

#button
f2b1=Button(f2,text="Search",font="Vardana 10 bold",width=5,command=search_item)
f2b1.place(x=320,y=250)

f2b2=Button(f2,text="show all ",font="Vardana 10 bold",width=10,command=show_all)
f2b2.place(x=380,y=250)

f2b3=Button(f2,text="add",font="Vardana 10 bold",width=8,command=itemfeach)
f2b3.place(x=700,y=250)
#____________________________frem3_________________________________________________

#creat for , for loop
f3=Frame(relief=RIDGE,borderwidth=2)
f3.place(x=5,y=490,width=975,height=220)

lis_bil_total=[]

def cal_bill():
    #entry get total
    tu1= (float(vartax.get()) + float(vartotal.get()))- float(vardiscount.get())
    lis_bil_total.append(tu1)

    vartax.set(0)
    vartotal.set(0)
    vardiscount.set(0)

#text box

def print():
    top=Tk()
    def akki():
        tu = textb.get(1.0, END)
        # save the text file
        with open(f"billsprit.txt", "w") as k:
            k.write(f"{tu}")
        #print resipt
        os.startfile('C:\\Users\\Aai\\Desktop\\billing project\\billsprit.txt','print')
        top.destroy()

    if len(lis_name)==0:
        ms.showerror("erorr","do not print emty bill")
        top.destroy()
    else:
        textb=Text(top,height=40,width=120,font="Vardana 10 ")
        textb.insert(END,f"SONAWANE SOFFTWER\n\n")
        textb.insert(END,"-"*100)
        textb.insert(END,f"\nDate : {date}\n")
        textb.insert(END,"-"*100)
        textb.insert(END,f"\nitem\t\t\tQTY\t\tPRICE\n")
        for i in zip(lis_name,lisqty,listotal):
            textb.insert(END, f"\n{i[0]}\t\t\t{i[1]}\t\t{i[2]}\n")
        textb.insert(END,"-"*100)
        textb.insert(END, f"\n\t\t\tsub qty\t\tsub total\n")
        textb.insert(END, f"\n\t\t\t{sum(lisqty)}\t\t{vartotal.get()}\n")
        textb.insert(END,"-"*100)
        textb.insert(END, f"\nthanks for visiting our store ")
        textb.pack()

        # insert bills in sql data
        c.execute(f"insert into daybill values({ran_num},'{date}',{varqty.get()},{vartotal.get()})")
        con.commit()

        #clear the list
        lis_name.clear()
        listotal.clear()
        lisqty.clear()
        lis_bil_total.clear()

        #clear the entry box
        vartax.set(0)
        vartotal.set(0)
        vardiscount.set(0)
        varqty.set(0)


        topb1 = Button(top, text="Print", font="Vardana 10 bold", width=8, command=akki)
        topb1.pack()

def allbills():
    top1=Toplevel()
    top1.maxsize(600,300)
    top1.minsize(600, 300)
    ra=c.execute('select * from daybill')

    scr = Scrollbar(top1)

    scr.pack(fill=Y, side=RIGHT)

    # product treeview
    column = "Bill No", "Date", "qty", "Price"
    tre = ttk.Treeview(top1, show='headings', column=column, yscrollcommand=scr.set)

    tre.column("Bill No", width=120, anchor="w")
    tre.column("Date", width=120, anchor="w")
    tre.column("qty", width=140, anchor="w")
    tre.column("Price", width=180, anchor="w")

    tre.heading("Bill No", text="Bill No", anchor="w")
    tre.heading("Date", text="Date", anchor="w")
    tre.heading("qty", text="Qty", anchor="w")
    tre.heading("Price", text="Price", anchor="w")
    for i in ra:
        tre.insert('', "end", text="", values=(f"{i[0]}", f"{i[1]}", f"{i[2]}", f"{i[3]}"))
    tre.pack()
    scr.config(command=tre.yview())

    top1l = Label(top1, text="Search",font="Vardana 10 bold")
    top1l.place(x=100, y=250)

    top1e=Entry(top1,bg='yellow')
    top1e.place(x=200,y=250)

    def show_me():
        c.execute("select * from daybill")
        ra2=c.fetchall()
        for i in tre.get_children():
            tre.delete(i)
        for i in ra2:
            tre.insert('', "end", text="", values=(f"{i[0]}", f"{i[1]}", f"{i[2]}", f"{i[3]}"))

    def billser():
        c.execute(f"select * from daybill where bill_no={top1e.get()}")
        ra1=c.fetchall()
        for i in tre.get_children():
            tre.delete(i)
        for i in ra1:
            tre.insert('', "end", text="", values=(f"{i[0]}", f"{i[1]}", f"{i[2]}", f"{i[3]}"))
        top1e.delete(0,END)

    top1b=Button(top1,text="Search",font="Vardana 10 bold",command=billser)
    top1b.place(x=350,y=250)

    top2b = Button(top1, text="all bills", font="Vardana 10 bold", command=show_me)
    top2b.place(x=420, y=250)


varqty=IntVar()
vartax=IntVar()
vardiscount=IntVar()
vartotal=IntVar()

#lalbel
f3l1=Label(f3,text="Total Qty :",font="Vardana 10 bold")
f3l1.place(x=5,y=10)

f3l2=Label(f3,text="Tax :",font="Vardana 10 bold")
f3l2.place(x=5,y=50)

f3l3=Label(f3,text="Discount :",font="Vardana 10 bold")
f3l3.place(x=5,y=90)

f3l3=Label(f3,text="Total Rs. :",font="Vardana 10 bold")
f3l3.place(x=5,y=130)

#entry
f3e1=Entry(f3,width=20,font="Vardana 10 bold",textvariable=varqty)
f3e1.place(x=100,y=10)

f3e2=Entry(f3,width=20,font="Vardana 10 bold",textvariable=vartax)
f3e2.place(x=100,y=50)

f3e3=Entry(f3,width=20,font="Vardana 10 bold",textvariable=vardiscount)
f3e3.place(x=100,y=90)

f3e4=Entry(f3,width=20,font="Vardana 10 bold",textvariable=vartotal)
f3e4.place(x=100,y=130)
#button
f3b1=Button(f3,text="Print",font="Vardana 10 bold",width=8,command=print)
f3b1.place(x=880,y=10)

f3b2=Button(f3,text="bills",font="Vardana 10 bold",width=8,command=allbills)
f3b2.place(x=880,y=60)


root.mainloop()