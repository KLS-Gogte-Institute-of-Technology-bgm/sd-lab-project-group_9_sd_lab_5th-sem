#from login1 import
from tkinter import*
import webbrowser
from PIL import ImageTk
from tkcalendar import*
def hm():
    my_window=Tk()
    my_window.title("HOME")
    my_window.geometry("1199x600+100+50")
    my_window.resizable(True, True)
#bg = ImageTk.PhotoImage(image=PIL.Image.fromarray(file="/home/shrutim/Downloads/getty_655998316_2000149920009280219_363765.jpg"))
    bg_image=Label(my_window,bg="#11698e").place(x=0,y=0,relwidth=1,relheight=1)
    Frame_login1=Frame(my_window,bg="#cae4db")
    Frame_login1.place(x=120,y=80,height=480,width=1040)
    Frame_login2=Frame(Frame_login1,bg="white")
    Frame_login2.place(x=0,y=90,height=480,width=1040)
    l6=Label(Frame_login1,text="GOGTE INSTITUTE OF TECHNOLOGY  ", font=("Mongolian Baiti", 36), fg="black",bg="#cae4db").place(x=50,y=20)
    l1= Label(Frame_login1, text="Username         SONAL DESHMUKH ", font=("Mongolian Baiti", 13), fg="#000000", bg="white").place(x=50,y=120)
    l2= Label(Frame_login1, text="Year       ", font=("Mongolian Baiti", 13), fg="#000000", bg="white").place(x=50,y=160)
    v = IntVar()
    
    
    c1 = Radiobutton(Frame_login1, text="First year", variable=v, value=1, fg="#000000", bg="white")
    c2 = Radiobutton(Frame_login1, text="Second year", variable=v,value=2, fg="#000000", bg="white")
    c3 = Radiobutton(Frame_login1, text="Third year", variable=v, value=3,fg="#000000", bg="white")
    c4 = Radiobutton(Frame_login1, text="Fourth year", variable=v, value=4,fg="#000000", bg="white")
    #b1 = Button(my_window, text="Submit",command=submit)
    c1.place(x=180,y=160)
    c2.place(x=280,y=160)
    c3.place(x=400,y=160)
    c4.place(x=500,y=160)
    #b1.place(x=580,y=280)
    l3= Label(Frame_login1,text="Course Name      ", font=("Mongolian Baiti", 13), fg="#000000", bg="white").place(x=50,y=200)
    txt_user1=Entry(Frame_login1 ,font=("Mongolian Baiti",15),bg="#fff2df")
    txt_user1.place(x=180,y=200)
    l4= Label(Frame_login1,text="Course Code       ", font=("Mongolian Baiti", 13), fg="#000000", bg="white").place(x=50,y=240)
    txt_user2=Entry(Frame_login1,font=("Mongolian Baiti",15),bg="#fff2df")
    txt_user2.place(x=180,y=240)
    L5= Label(Frame_login1, text="Date         ", font=("Mongolian Baiti", 13), fg="#000000", bg="white").place(x=50,y=280)
    cal = DateEntry(Frame_login1, width=12, year=2020, month=12, day=25,background='black', foreground='white', borderwidth=2)
    cal.place(x=180,y=280)

    
    
    l6= Label(Frame_login1, text="Link           ", font=("Mongolian Baiti", 13), fg="#000000", bg="white").place(x=50,y=320)
    txt_user3=Label(Frame_login1,text="barcodescanner.edu/GIT",font=("Mongolian Baiti",15),fg="blue",bg="white")
    txt_user3.place(x=180,y=320)
    b2=Button(Frame_login1, text="Generate    ",bg="black").place(x=50,y=360,width=120)
    



    my_window.mainloop()


