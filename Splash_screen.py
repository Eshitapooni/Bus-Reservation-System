from tkinter import*
root=Tk()
root.title("Python Project")
root.geometry('980x500')
x=Label(root,text="Project Title:Bus Booking System",font="Arial 20",fg="Red").grid(row=0,column=30)
y=Label(root,text="Project of Advanced Programming Lab-1 and DBMS",font="Arial 18").grid(row=1,column=30)
a=Label(root,text="------------------------------------------------",font="Arial 18",fg="blue").grid(row=3,column=30)
z=Label(root,text="Project Developed by:Eshita,191B104,B3",font="Arial 18").grid(row=5,column=30)
b=Label(root,text="Project Supervisors:Dr.Mahesh Kumar,Dr. Amit Kumar Srivastava,Dr. Nilesh Kumar Patel",font="Arial 18 ").grid(row=7,column=30)
c=Label(root,text="Make mouse movement on the screen to close",font="Arial 12",fg='green').grid(row=9,column=30)

def close(e=2):
    root.destroy()

root.bind('<Motion>',close)

root.mainloop()










