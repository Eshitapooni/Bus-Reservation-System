
from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
import mysql.connector as mysql
import sqlite3
from Splash_screen import *
root=Tk()
root.title('Seat Reservation')

root.geometry('800x800')


Label(root,text="Bus Reservation System",font="Arial 20",fg="White",bg="blue").grid(row=0,column=1)

img=PhotoImage(file="C:\\Users\\eshit\\Desktop\\PYTHON PROJECT BUS\\unnamed.png")
Label(root,image=img).grid(row=1,column=1)

def add_bus():
    top=Toplevel()
    top.title('Add Bus')
    img=PhotoImage(file="C:\\Users\\eshit\\Desktop\\PYTHON PROJECT BUS\\unnamed.png")
    Label(top,image=img).grid(row=0,column=1)
    Label(top,text="Bus Operator Details",font="ARIAL 14",fg="White",bg="Red").grid(row=1,column=1)

    con=mysql.connect(host="localhost",user="root",password="xyz(Type your own password)",database="python_project")
    c=con.cursor()



    def add():

        """name=,
        contact_no=,
        address=,
        op_Id=,
        bus_Type=,
        fromp=,
        topp=,
        dt=,
        seats=,
        fare=,
        dep_Time=,
        arr_Time="""

        con=mysql.connect(host="localhost",user="root",password="xyz(Type your own password)",database="python_project")
        c=con.cursor()

        c.execute("INSERT INTO Bus_Info VALUES (' "+Name.get()+"','"+Contact_No.get()+"','"+Address.get()+"','"+Op_Id.get()+"','"+Bus_Type.get()+"','"+Fromp.get()+"','"+Topp.get()+"','" +Dt.get()+"','"+ Seats.get()+"','"+Fare.get()+"','" +Dep_Time.get()+"','" +Arr_Time.get()+"')")
        

        c.execute("commit");
        

        con.close();

        Name.delete(0,END)
        Contact_No.delete(0,END)
        Address.delete(0,END)
        Op_Id.delete(0,END)
        Bus_Type.delete(0,END)
        Fromp.delete(0,END)
        Topp.delete(0,END)
        Dt.delete(0,END)
        Seats.delete(0,END)
        Fare.delete(0,END)
        Dep_Time.delete(0,END)
        Arr_Time.delete(0,END)
        messagebox.showinfo("Status", "Bus Added Successfully")
        top.destroy()



        
    Name=Entry(top,width=30)
    Name.grid(row=2,column=2,padx=20)
    Contact_No=Entry(top,width=30)
    Contact_No.grid(row=3,column=2,padx=20)
    Address=Entry(top,width=30)
    Address.grid(row=4,column=2,padx=20)            
    Op_Id=Entry(top,width=30)
    Op_Id.grid(row=5,column=2,padx=20)
    Bus_Type=Entry(top,width=30)
    Bus_Type.grid(row=6,column=2,padx=20)
    Fromp=Entry(top,width=30)
    Fromp.grid(row=7,column=2,padx=20)
    Topp=Entry(top,width=30)
    Topp.grid(row=8,column=2,padx=20)
    Dt=Entry(top,width=30)
    Dt.grid(row=9,column=2,padx=20)
    Seats=Entry(top,width=30)
    Seats.grid(row=10,column=2,padx=20)
    Fare=Entry(top,width=30)
    Fare.grid(row=11,column=2,padx=20)
    Dep_Time=Entry(top,width=30)
    Dep_Time.grid(row=12,column=2,padx=20)
    Arr_Time=Entry(top,width=30)
    Arr_Time.grid(row=13,column=2,padx=20)


    nmlabel=Label(top,text="NAME",font = "ARIAL 12")
    nmlabel.grid(row=2,column=0)
    cnolabel=Label(top,text="CONTACT NO",font = "ARIAL 12")
    cnolabel.grid(row=3,column=0)
    adrslabel=Label(top,text="ADDRESS",font = "ARIAL 12")
    adrslabel.grid(row=4,column=0)
    Oplabel=Label(top,text="OPERATOR ID",font = "ARIAL 12")
    Oplabel.grid(row=5,column=0)
    BTypelabel=Label(top,text="BUS TYPE",font = "ARIAL 12")
    BTypelabel.grid(row=6,column=0)
    Fromlabel=Label(top,text="FROM",font = "ARIAL 12")
    Fromlabel.grid(row=7,column=0)
    Tolabel=Label(top,text="TO",font = "ARIAL 12")
    Tolabel.grid(row=8,column=0)
    Dtlabel=Label(top,text="DATE",font = "ARIAL 12")
    Dtlabel.grid(row=9,column=0)
    Stlabel=Label(top,text="SEATS",font = "ARIAL 12")
    Stlabel.grid(row=10,column=0)
    Frlabel=Label(top,text="FARE",font = "ARIAL 12")
    Frlabel.grid(row=11,column=0)
    DTlabel=Label(top,text="DEPARTURE TIME",font = "ARIAL 12")
    DTlabel.grid(row=12,column=0)
    ATlabel=Label(top,text="ARRIVAL TIME",font = "ARIAL 12")
    ATlabel.grid(row=13,column=0)


    add_btn=Button(top,text="Add Bus",fg="Black",bg="Cyan",command=add)
    add_btn.grid(row=14,column=0,columnspan=2,padx=5,pady=5,ipadx=100)




    con.commit()




    con.close()
    


    top.mainloop()




def search_Bus():
    
    top=Toplevel()
    top.title('Search Bus')
    img=PhotoImage(file="C:\\Users\\eshit\\Desktop\\PYTHON PROJECT BUS\\unnamed.png")
    Label(top,image=img).grid(row=1,column=1)
    Label(top,text="Search Bus ",font="Arial 20",fg="Blue",bg="Pink").grid(row=0,column=1)

    def search_b():
        
        def end_book():
            messagebox.showinfo("Status", "Seats Booked Successfully")
            board.destroy()
            top.destroy()

        def book_d():

            v1=IntVar()
            v2=IntVar()
            v3=IntVar()
            v4=IntVar()
            v5=IntVar()
            v6=IntVar()
            v7=IntVar()
            v8=IntVar()
            v9=IntVar()
            v10=IntVar()
            v11=IntVar()
            v12=IntVar()
            v13=IntVar()
            v14=IntVar()
            v15=IntVar()
            
            cb1=Checkbutton(board,text="1",variable=v1,onvalue=1,offvalue=0,state=ACTIVE)
            cb1.grid(row=50,column=1)
            cb2=Checkbutton(board,text="2",variable=v2,onvalue=1,offvalue=0,state=ACTIVE)
            cb2.grid(row=50,column=2)
            cb3=Checkbutton(board,text="3",variable=v3,onvalue=1,offvalue=0,state=ACTIVE)
            cb3.grid(row=50,column=3)
            cb4=Checkbutton(board,text="4",variable=v4,onvalue=1,offvalue=0,state=ACTIVE)
            cb4.grid(row=50,column=4)
            cb5=Checkbutton(board,text="5",variable=v5,onvalue=1,offvalue=0,state=ACTIVE)
            cb5.grid(row=50,column=5)
            cb6=Checkbutton(board,text="6",variable=v6,onvalue=1,offvalue=0,state=ACTIVE)
            cb6.grid(row=55,column=1)
            cb7=Checkbutton(board,text="7",variable=v7,onvalue=1,offvalue=0,state=ACTIVE)
            cb7.grid(row=55,column=2)
            cb8=Checkbutton(board,text="8",variable=v8,onvalue=1,offvalue=0,state=ACTIVE)
            cb8.grid(row=55,column=3)
            cb9=Checkbutton(board,text="9",variable=v9,onvalue=1,offvalue=0,state=ACTIVE)
            cb9.grid(row=55,column=4)
            cb10=Checkbutton(board,text="10",variable=v10,onvalue=1,offvalue=0,state=ACTIVE)
            cb10.grid(row=55,column=5)
            cb11=Checkbutton(board,text="11",variable=v11,onvalue=1,offvalue=0,state=ACTIVE)
            cb11.grid(row=60,column=1)
            cb12=Checkbutton(board,text="12",variable=v12,onvalue=1,offvalue=0,state=ACTIVE)
            cb12.grid(row=60,column=2)
            cb13=Checkbutton(board,text="13",variable=v13,onvalue=1,offvalue=0,state=ACTIVE)
            cb13.grid(row=60,column=3)
            cb14=Checkbutton(board,text="14",variable=v14,onvalue=1,offvalue=0,state=ACTIVE)
            cb14.grid(row=60,column=4)
            cb15=Checkbutton(board,text="15",variable=v15,onvalue=1,offvalue=0,state=ACTIVE)
            cb15.grid(row=60,column=5)

            eb=Button(board,text="Book Seats",font="Arial 10",bg="Cyan",fg="Black",command=end_book)
            eb.grid(row=65,column=3)
            
            
        
        a=b1.get()
        b=b2.get()
        c=b3.get()
        d=b4.get()


        if ((a=='') or (b=='')or(c=='')or(d=='')):
            messagebox.showerror(title="Error",message="Fields can't be empty!!")
        elif(b==c):
            messagebox.showerror(title="Error",message="Source and destination can't be same")

        else:
            con=mysql.connect(host="localhost",user="root",password="xyz(Type your password)",database="python_project")
            cur=con.cursor()
            cur.execute("select Name,Bus_Type,Fromp,Topp,Date,Seats,Fare,Dep_Time,Arr_Time from Bus_Info where Bus_Type='"+str(b1.get())+"' and Fromp='"+str(b2.get())+"' and Topp='"+str(b3.get())+"' and Date='"+str(b4.get())+"'")
            s=cur.fetchall()
            y=3
            x=0

        
            if len(s) == 0:
                messagebox.showerror(title="Sorry",message="Bus not available")

            else:
                board = Tk()
                board.title("Reserve Bus Seats")
                
                
                Label(board,text="Search Bus ",font="Arial 20",fg="Orange",bg="Purple").grid(row=0,column=4)

                Label(board,text="Name",font="Bold 14").grid(row=1,column=0)
                Label(board,text="Bus Type",font="Bold 14").grid(row=1,column=1)
                Label(board,text="From",font="Bold 14").grid(row=1,column=2)
                Label(board,text="To",font="Bold 14").grid(row=1,column=3)
                Label(board,text="Date",font="Bold 14").grid(row=1,column=4)
                Label(board,text="Seats Available",font="Bold 14").grid(row=1,column=5)
                Label(board,text="Fare",font="Bold 14").grid(row=1,column=6)
                Label(board,text="Departure Time",font="Bold 14").grid(row=1,column=7)
                Label(board,text="Arrival Time",font="Bold 14").grid(row=1,column=8)

            
            
                c=3
                e=1
                cnstt=15
                v=IntVar()
                for i in s:
                    k=1
                    x=0
                    while(k<=9):
                        if(k==6):
                            Label(board,text=str(cnstt)).grid(row=y,column=x)
                        else:   
                            Label(board,text=str(i[x])).grid(row=y,column=x)
                        x=x+1
                        k=k+1
                    y=y+1
                    Radiobutton(board,text="",variable=v,value=e).grid(row=c,column=10)
                    c=c+1
                    e=e+1


                Button(board,text="Book Seats",font="Arial 14",bg="Pink",fg="Red",command=book_d).grid(row=c,column=4)

        
                cur.execute("commit");
        

                con.close();
        
            
        

    Label(top,text="Bus Type").grid(row=2,column=1)
    b1=ttk.Combobox(top,height=10,width=30,values=["Ac","Non Ac","Sleeper"])
    b1.grid(row=2,column=2)

    Label(top,text="From").grid(row=3,column=1)
    b2=Entry(top,width=30)
    b2.grid(row=3,column=2)

    Label(top,text="To").grid(row=4,column=1)
    b3=Entry(top,width=30)
    b3.grid(row=4,column=2)

    Label(top,text="Date in format DD-MM-YY").grid(row=5,column=1)
    b4=Entry(top,width=30)
    b4.grid(row=5,column=2)

    k=Button(top,text="Search Bus",font="Arial 16",bg="green",fg="white",command=search_b).grid(row=6,column=1)
    

    

    

    top.mainloop()
 



   
x=Button(root,text="Add Bus",font="Arial 16",bg="green",fg="white",command=add_bus)
x=x.grid(row=20,column=0)
y=Button(root,text="Search Bus",font="Arial 16",bg="green",fg="white",command=search_Bus)
y=y.grid(row=20,column=160)


root.mainloop()
