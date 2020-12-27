from home import *
from tkinter import*
from PIL import ImageTk              #import kar isko
from tkinter import messagebox
class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(True, True)
        self.bg=ImageTk.PhotoImage(file="/home/shrutim/Downloads/29303524-row-of-books-grungy-background-free-copy-space.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=680,y=160,height=340,width=500)

        title=Label(Frame_login,text="         LOGIN        ",font=("Georgia",30,"bold"),fg="#000000",bg="#e6ac00").place(x=90,y=30)

        lbl_user=Label(Frame_login, text="Username", font=("Goudy", 15, "bold"), fg="black", bg="white").place(x=90,
                                                                                                                  y=100)
        self.txt_user=Entry(Frame_login,font=("times new roman",15),bg="lightgray", fg="black")
        self.txt_user.place(x=90,y=140,width=350,height=35)
        lbl_pass = Label(Frame_login, text="Password", font=("Goudy", 15, "bold"), fg="#000000", bg="white").place(x=90,
                                                                                                                y=180)
        self.txt_pass = Entry(Frame_login, show="*", font=("times new roman", 15), bg="lightgray", fg="black")
        self.txt_pass.place(x=90, y=210, width=350, height=35)

        forget=Button(Frame_login,text="Forget Password?",bg="white",fg="#e6ac00",bd=0,font=("times new roman",12)).place(x=90,y=270)
        Login_btn= Button(self.root,command=self.login, text="Login", bg="#e6ac00", fg="white",font=("times new roman", 20)).place(x=850,y=490,width=180,height=40)
    def login(self):
        if self.txt_pass.get()==""or self.txt_user.get()=="":
            messagebox.showerror("ERROR","All fields are required",parent=self.root)
        elif self.txt_pass.get()!="123456"or self.txt_user.get()!="sonal":
            messagebox.showerror("ERROR", "Invalid Username/Password", parent=self.root)
        else:
            #messagebox.showinfo("Welcome","Login Sucessful!",parent=self.root)
            hm()

            


root=Tk()
obj=Login(root)

root.mainloop()
