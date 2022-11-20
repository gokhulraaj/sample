from tkinter import *
from tkinter import ttk
from tkinter import messagebox

tk=Tk()
tk.attributes("-fullscreen",True)
tk.config(bg="White")
tk.title("Server")

def out():
    tk.destroy()

def submit():
        a1=str(b1.get());
        a2=str(c1.get());

        if(a1=="username" and a2=="password"):
            a=Label(tk,text="YOUR LOGIN IS SUCCESSFUL",font=("Cooper Black",20),bg="White",fg="Red").pack()

        elif((a1==" " and a2==" ") or (a1!="username" and a2!="password")):
            messagebox.showerror("ERROR!", "INCORRECT USERNAME OR PASSWORD")
            
        
    
    
a=Label(tk,text="LOGIN PAGE",font=("Cooper Black",40),bg="White",fg="Deep sky blue").pack()
b=Label(tk,text="Username :",font=("Cooper Black",20),bg="White",fg="Deep sky blue").place(x=20,y=100)
b1=Entry(tk,font=("Cooper Black",18))
c=Label(tk,text="Password :",font=("Cooper Black",20),bg="White",fg="Deep sky blue").place(x=20,y=160)
c1=Entry(tk,font=("Cooper Black",18),show="*")
d1=Button(tk,text="Submit",font=("Cooper Black",20),bg="Deep sky blue",fg="Black",command=submit).place(x=120,y=220)
e1=Button(tk,text="  x  ",font=("Cooper Black",12),bg="Red",fg="White",command=out).place(x=1500,y=0)
b1.place(x=200,y=100)
c1.place(x=200,y=160)
tk.mainloop()

