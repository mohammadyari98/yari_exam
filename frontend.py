from tkinter import *  
from tkinter import messagebox  
from backend import Database  # تصحیح نام کلاس  

db = Database('C:/Users/M.Yari/Desktop/Mohammad Yari/Payghahe Dade.db')  

# Func: ثبت نام  
def sabt():  
    a = ent_fname.get()  
    b = ent_lname.get()  
    c = ent_email.get()  
    d = ent_pas.get()  
    if len(c) == 0 or len(d) == 0:  
        messagebox.showerror("Error", "Email or Password not valid!")  
    elif len(d) < 8:  
        messagebox.showerror("Error", "The password should not be less than 8 characters.")  
    else:  
        db.insert_record(a, b, c, d)  
        messagebox.showinfo("Welcome", "Registration is done.")  
        ent_fname.delete(0, END)  
        ent_lname.delete(0, END)  
        ent_email.delete(0, END)  
        ent_pas.delete(0, END)  
        ent_fname.focus_set()  

# Func: ورود  
def vorod():  
    c = ent_email.get()  
    d = ent_pas.get()  
    user = db.select_record(c, d)  
    if len(user) == 0:  
        messagebox.showerror("Error", "Email or password is wrong.")  
    else:  
        fname, lname = user[0][1], user[0][2]  
        win.destroy()
        root = Tk()
        root.title("welcome")  
        root.geometry("650x400+400+200")  

        lbl_wel = Label(root,text=f"Hello {fname} {lname}!",font=("B titr", 20, "bold"))                           
        lbl_wel.pack(pady=50)                         
        
        root.resizable(0, 0)  
        root.mainloop()


# Create:  
win = Tk()  
win.title("Login Form")  
win.geometry("650x400+400+200")  

# Widgets  
lbl_fname = Label(win, text="First name:", font=("B titr", 12, "bold"))  
lbl_fname.place(x=30, y=40)  

lbl_Lname = Label(win, text="Last name:", font=("B titr", 12, "bold"))  
lbl_Lname.place(x=30, y=100)  

lbl_Email = Label(win, text="Email:", font=("B titr", 12, "bold"))  
lbl_Email.place(x=30, y=160)  

lbl_pass = Label(win, text="Password:", font=("B titr", 12, "bold"))  
lbl_pass.place(x=30, y=220)  

ent_fname = Entry(win, justify="center", width=50, font=("B titr", 12, "bold"))  
ent_fname.place(x=170, y=40)  

ent_lname = Entry(win, justify="center", width=50, font=("B titr", 12, "bold"))  
ent_lname.place(x=170, y=100)  

ent_email = Entry(win, justify="center", width=50, font=("B titr", 12, "bold"))  
ent_email.place(x=170, y=160)  

ent_pas = Entry(win, justify="center", width=50, show="*", font=("B titr", 12, "bold"))  
ent_pas.place(x=170, y=220)  

star_e = Label(win, text='*', fg="red", font=("B titr", 12, "bold"))  
star_e.place(x=100, y=160)  

star_p = Label(win, text='*', fg="red", font=("B titr", 12, "bold"))  
star_p.place(x=145, y=220)  

btn_up = Button(win, text="Sign Up", width=15, command=sabt, font=("B titr", 12, "bold"))  
btn_up.place(x=120, y=280)  

btn_in = Button(win, text="Sign In", width=15, command=vorod, font=("B titr", 12, "bold"))  
btn_in.place(x=340, y=280)  

# Run  
win.resizable(0, 0)  
win.mainloop()