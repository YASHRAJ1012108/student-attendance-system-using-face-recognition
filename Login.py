from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from Main import Advanced_Attendance_System
import re

def main():
    win = Tk()
    app = Login_window(win)
    win.mainloop()

class Login_window:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x720+0+0")  # Changed
        self.root.resizable(0, 0)
        self.root.title("LOGIN")
        self.var_txtuser = StringVar()
        self.var_txtpass = StringVar()

        # ====================Title=====================
        title_lbl = Label(self.root, text="ADVANCED ATTENDANCE SOFTWARE", font=(
            "times new roman", 30, "bold"), bg="DarkBlue", fg="White")
        title_lbl.place(x=0, y=0, width=1280, height=40)  # Width changed

        # ===================Background Image===========================
        img_top = Image.open(r"D:\Life time Projects\3rd sem projects\Python\Advanced-Attendance-System-main\ADVANCED ATTENDANCE SYSTEM\Project_Images\RegisterBG.jpg")
        img_top = img_top.resize((1280, 680), Image.Resampling.LANCZOS)  # Changed
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=40, width=1280, height=680)  # Adjusted

        frame = Frame(self.root, bg="White")
        frame.place(x=415, y=100, width=450, height=500)  # Position changed

        img1 = Image.open(r"D:\Life time Projects\3rd sem projects\Python\Advanced-Attendance-System-main\ADVANCED ATTENDANCE SYSTEM\Project_Images\LoginIcon.jpg")
        img1 = img1.resize((130, 130), Image.Resampling.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg="white", borderwidth=0)
        lblimg1.place(x=575, y=110, width=130, height=130)  # Position changed

        get_str = Label(frame, text="Get Started!!", font=(
            "times new roman", 20, "bold"), fg="DarkBlue", bg="White")
        get_str.place(x=160, y=130)

        # label
        username = Label(frame, text="Username", font=(
            "times new roman", 18, "bold"), fg="DarkBlue", bg="White")
        username.place(x=70, y=195)

        self.txtuser = ttk.Entry(frame, textvariable=self.var_txtuser, 
                               font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=225, width=300)

        password = Label(frame, text="Password", font=(
            "times new roman", 18, "bold"), fg="DarkBlue", bg="White")
        password.place(x=70, y=271)

        self.txtpass = ttk.Entry(frame, textvariable=self.var_txtpass, show='*',
                               font=("times new roman", 15, "bold"))
        self.txtpass.place(x=40, y=300, width=300)

        # ===========================Icon Images========================
        img2 = Image.open(r"D:\Life time Projects\3rd sem projects\Python\Advanced-Attendance-System-main\ADVANCED ATTENDANCE SYSTEM\Project_Images\LoginIcon2.jpg")
        img2 = img2.resize((30, 30), Image.Resampling.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        Label(frame, image=self.photoimage2, bg="White", borderwidth=0).place(x=40, y=195, width=30, height=30)

        img3 = Image.open(r"D:\Life time Projects\3rd sem projects\Python\Advanced-Attendance-System-main\ADVANCED ATTENDANCE SYSTEM\Project_Images\PasswordIcon.jpg")
        img3 = img3.resize((30, 30), Image.Resampling.LANCZOS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        Label(frame, image=self.photoimage3, bg="white", borderwidth=0).place(x=40, y=271, width=30, height=30)

        # login_button
        img0 = Image.open(r"D:\Life time Projects\3rd sem projects\Python\Advanced-Attendance-System-main\ADVANCED ATTENDANCE SYSTEM\Project_Images\LoginButton1.jpg")
        img0 = img0.resize((200, 65), Image.Resampling.LANCZOS)
        self.photoimage0 = ImageTk.PhotoImage(img0)
        Button(frame, image=self.photoimage0, command=self.login,
              borderwidth=0, cursor="hand2").place(x=200, y=390, width=200)

        # register_button
        img4 = Image.open(r"D:\Life time Projects\3rd sem projects\Python\Advanced-Attendance-System-main\ADVANCED ATTENDANCE SYSTEM\Project_Images\RegisterButton1.png")
        img4 = img4.resize((200, 60), Image.Resampling.LANCZOS)
        self.photoimage4 = ImageTk.PhotoImage(img4)
        Button(frame, image=self.photoimage4, bg="white", 
              command=lambda: [self.register_window(), self.reset_data()], 
              borderwidth=0, cursor="hand2").place(x=20, y=450, width=200)  # Position changed

        # forget_button
        Button(frame, text="Forget Password", 
              command=lambda: [self.forget_password_window(), self.reset_one()], 
              font=("times new roman", 15, "bold"), borderwidth=0, 
              fg="Red", bg="White").place(x=10, y=410, width=200)  # Position changed

        Checkbutton(frame, text="Show Password", command=self.show_password, 
                   font=("times new roman", 15, "bold"), fg="DarkBlue", 
                   bg="White").place(x=20, y=340, width=200)

    # ======================Keep all methods unchanged below======================
    def show_password(self):
        if self.txtpass.cget('show') == '*':
            self.txtpass.config(show='')
        else:
            self.txtpass.config(show='*')

    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register_window(self.new_window)

    def reset_data(self):
        self.var_txtuser.set("")
        self.var_txtpass.set("")

    def reset_one(self):
        self.var_txtpass.set("")

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All Fields are Required !!")
        else:
            # Email format validation
            if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', self.txtuser.get()):
                messagebox.showerror("Error", "Invalid Email Format!")
                return
            conn = mysql.connector.connect(
                host="localhost", username="root", password="Yash1012108@", 
                database="advanced_attendance_system")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where Email=%s and Password=%s ", 
                             (self.txtuser.get(), self.txtpass.get()))
            row = my_cursor.fetchone()
            if row is None:
                messagebox.showerror("Invalid", "Invalid Credentials !!")
            else:
                if messagebox.askyesno("YesNo", "Access Only Admin"):
                    self.new_window = Toplevel(self.root)
                    self.app = Advanced_Attendance_System(self.new_window)
                    messagebox.showinfo("Success", "LOGIN SUCCESSFUL !!", parent=self.new_window)
                    messagebox.showinfo("Success", "Welcome to ADVANCED ATTENDANCE SOFTWARE !!", parent=self.new_window)
            conn.close()


    def reset_pass(self):
        if self.combo_security_Q.get() == "Select":
            messagebox.showerror("Error", "Select Security Question", parent=self.root2)
        elif self.txt_securityA.get() == "":
            messagebox.showerror("Error", "Please Enter the Answer", parent=self.root2)
        elif self.txt_new_password.get() == "":
            messagebox.showerror("Error", "Please Enter the New Password", parent=self.root2)
        else:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="Yash1012108@", 
                database="advanced_attendance_system")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where Email=%s and SecurityQ=%s and SecurityA=%s",
                             (self.txtuser.get(), self.combo_security_Q.get(), self.txt_securityA.get()))
            if my_cursor.fetchone() is None:
                messagebox.showerror("Error", "Please Enter Correct Answer", parent=self.root2)
            else:
                my_cursor.execute("update register set Password =%s where Email=%s",
                                 (self.txt_new_password.get(), self.txtuser.get()))
                conn.commit()
                messagebox.showinfo("Info", "Your Password has been Reset, Please Login with New Password", parent=self.root2)
                self.root2.destroy()
            conn.close()

    def forget_password_window(self):
        if self.txtuser.get() == "":
            messagebox.showerror("Error", "Please Enter the Email Address to Reset the Password ")
        else:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="Yash1012108@", 
                database="advanced_attendance_system")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where Email=%s", (self.txtuser.get(),))
            if my_cursor.fetchone() is None:
                messagebox.showerror("My Error", "Please Enter the Valid User Name")
            else:
                self.root2 = Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("452x552+400+100")  # Position centered
                self.root2.resizable(0, 0)
                Label(self.root2, text="Forget Password", font=(
                    "times new roman", 20, "bold"), fg="White", bg="DarkBlue").place(x=0, y=10, relwidth=1)
                Label(self.root2, text="Select Security Questions", font=(
                    "times new roman", 15, "bold"), bg="white", fg="Darkblue").place(x=110, y=100)
                self.combo_security_Q = ttk.Combobox(self.root2, font=(
                    "times new roman", 15, "bold"), state="readonly")
                self.combo_security_Q["values"] = (
                    "Select", "Your Birth Place", "Your Favourite Space", "Your Pet Name")
                self.combo_security_Q.place(x=110, y=140, width=250)
                self.combo_security_Q.current(0)
                Label(self.root2, text="Security Answer", font=(
                    "times new roman", 15, "bold"), bg="white", fg="DarkBlue").place(x=110, y=215)
                self.txt_securityA = ttk.Entry(self.root2, font=("times new roman", 15))
                self.txt_securityA.place(x=110, y=250, width=250)
                Label(self.root2, text="New Password", font=(
                    "times new roman", 15, "bold"), bg="white", fg="DarkBlue").place(x=110, y=315)
                self.txt_new_password = ttk.Entry(self.root2, font=("times new roman", 15))
                self.txt_new_password.place(x=110, y=350, width=250)
                Button(self.root2, text="Reset", command=self.reset_pass, font=(
                    "times new roman", 15, "bold"), fg="white", bg="DarkBlue").place(x=100, y=400, width=270)
            conn.close()

class Register_window:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x720+0+0")  # Changed
        self.root.resizable(0, 0)
        self.root.title("REGISTER")
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        # ==================BG image=========================
        self.bg = ImageTk.PhotoImage(
            file=r"D:\Life time Projects\3rd sem projects\Python\Advanced-Attendance-System-main\ADVANCED ATTENDANCE SYSTEM\Project_Images\RegisterBg.jpg")
        Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # ==================left image=========================
        self.bg1 = ImageTk.PhotoImage(
            file=r"D:\Life time Projects\3rd sem projects\Python\Advanced-Attendance-System-main\ADVANCED ATTENDANCE SYSTEM\Project_Images\Register1.png")
        Label(self.root, image=self.bg1).place(x=30, y=100, width=400, height=500)  # Adjusted

        # ===============main Frame===============================
        frame = Frame(self.root, bg="white")
        frame.place(x=450, y=100, width=750, height=500)  # Adjusted

        Label(frame, text="REGISTER HERE", font=(
            "times new roman", 20, "bold"), fg="darkgreen", bg="white").place(x=20, y=20)

        # =======================row1========================
        Label(frame, text="First Name", font=(
            "times new roman", 15, "bold"), bg="white", fg="DarkBlue").place(x=50, y=90)
        self.fname_entry = ttk.Entry(frame, textvariable=self.var_fname, 
                                   font=("times new roman", 15, "bold"))
        self.fname_entry.place(x=50, y=120, width=300)  # Width increased

        Label(frame, text="Last Name", font=(
            "times new roman", 15, "bold"), bg="white", fg="DarkBlue").place(x=400, y=90)  # Position changed
        self.txt_lname = ttk.Entry(frame, textvariable=self.var_lname, 
                                 font=("times new roman", 15, "bold"))
        self.txt_lname.place(x=400, y=120, width=300)  # Position & width changed

        # ============================row2======================
        Label(frame, text="Contact Number", font=(
            "times new roman", 15, "bold"), bg="white", fg="DarkBlue").place(x=50, y=170)
        self.txt_contact = ttk.Entry(frame, textvariable=self.var_contact, 
                                   font=("times new roman", 15, "bold"))
        self.txt_contact.place(x=50, y=200, width=300)  # Width increased

        Label(frame, text="Email", font=(
            "times new roman", 15, "bold"), bg="white", fg="DarkBlue").place(x=400, y=170)  # Position changed
        self.txt_email = ttk.Entry(frame, textvariable=self.var_email, 
                                 font=("times new roman", 15, "bold"))
        self.txt_email.place(x=400, y=200, width=300)  # Position & width changed

        # =====================row3================================
        Label(frame, text="Select Security Questions", font=(
            "times new roman", 15, "bold"), bg="white", fg="DarkBlue").place(x=50, y=240)
        self.combo_security_Q = ttk.Combobox(frame, textvariable=self.var_securityQ, 
                                           font=("times new roman", 15, "bold"), state="readonly")
        self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your Favourite Space", "Your Pet Name")
        self.combo_security_Q.place(x=50, y=270, width=300)  # Width increased
        self.combo_security_Q.current(0)

        Label(frame, text="Security Answer", font=(
            "times new roman", 15, "bold"), bg="white", fg="DarkBlue").place(x=400, y=240)  # Position changed
        self.txt_security = ttk.Entry(frame, textvariable=self.var_securityA, 
                                    font=("times new roman", 15))
        self.txt_security.place(x=400, y=270, width=300)  # Position & width changed

        # ===========================row4=========================
        Label(frame, text="Password", font=(
            "times new roman", 15, "bold"), bg="white", fg="DarkBlue").place(x=50, y=310)
        self.txt_pswd = ttk.Entry(frame, textvariable=self.var_pass, 
                                font=("times new roman", 15))
        self.txt_pswd.place(x=50, y=340, width=300)  # Width increased

        Label(frame, text="Confirm Password", font=(
            "times new roman", 15, "bold"), bg="white", fg="DarkBlue").place(x=400, y=310)  # Position changed
        self.confirm_pswd = ttk.Entry(frame, textvariable=self.var_confpass, 
                                    font=("times new roman", 15))
        self.confirm_pswd.place(x=400, y=340, width=300)  # Position & width changed

        # =========================checkButton==========================
        self.var_check = IntVar()
        Checkbutton(frame, variable=self.var_check, 
                   text="I Agree The Terms & Conditions", 
                   font=("times new roman", 15, "bold"), 
                   fg="DarkBlue", bg="White").place(x=50, y=390)

        # ==========================buttons==============================
        img = Image.open(r"D:\Life time Projects\3rd sem projects\Python\Advanced-Attendance-System-main\ADVANCED ATTENDANCE SYSTEM\Project_Images\RegisterButton2.jpg")
        img = img.resize((200, 70), Image.Resampling.LANCZOS)
        self.photoimage = ImageTk.PhotoImage(img)
        Button(frame, image=self.photoimage, command=self.register_data,
              borderwidth=0, cursor="hand2").place(x=50, y=430, width=200)  # Position adjusted

        img1 = Image.open(r"D:\Life time Projects\3rd sem projects\Python\Advanced-Attendance-System-main\ADVANCED ATTENDANCE SYSTEM\Project_Images\LoginButton2.png")
        img1 = img1.resize((200, 60), Image.Resampling.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        Button(frame, image=self.photoimage1, command=self.return_login,
              borderwidth=0, cursor="hand2").place(x=400, y=440, width=200)  # Position changed

    def register_data(self):
        # Check all required fields
        if (self.var_fname.get() == "" or self.var_lname.get() == "" or 
            self.var_contact.get() == "" or self.var_email.get() == "" or 
            self.var_securityQ.get() == "Select" or self.var_securityA.get() == "" or 
            self.var_pass.get() == "" or self.var_confpass.get() == ""):
            messagebox.showerror("Error", "All Fields Are Required", parent=self.root)
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Password & Confirm Password must be same", parent=self.root)
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree our terms and conditions", parent=self.root)
        elif len(self.var_contact.get()) != 10 or not self.var_contact.get().isdigit():
            messagebox.showerror("Error", "Invalid Mobile Number (10 digits required)", parent=self.root)
        elif not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', self.var_email.get()):
            messagebox.showerror("Error", "Invalid Email Format", parent=self.root)
        elif not self.var_fname.get().isalpha() or not self.var_lname.get().isalpha():
            messagebox.showerror("Error", "Name must contain only letters", parent=self.root)
        else:
            # Password strength validation
            password = self.var_pass.get()
            if len(password) < 8:
                messagebox.showerror("Error", "Password must be at least 8 characters", parent=self.root)
                return
            if not re.search(r'[A-Z]', password):
                messagebox.showerror("Error", "Password must contain an uppercase letter", parent=self.root)
                return
            if not re.search(r'[a-z]', password):
                messagebox.showerror("Error", "Password must contain a lowercase letter", parent=self.root)
                return
            if not re.search(r'[0-9]', password):
                messagebox.showerror("Error", "Password must contain a digit", parent=self.root)
                return

            conn = mysql.connector.connect(
                host="localhost", username="root", password="Yash1012108@", 
                database="advanced_attendance_system")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where Email=%s", (self.var_email.get(),))
            if my_cursor.fetchone() is not None:
                messagebox.showerror("Error", "User Already Exist, Please Try With Another Email", parent=self.root)
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get(),
                    self.var_pass.get()))
                conn.commit()
                messagebox.showinfo("Success", "Registered Successfully !!", parent=self.root)
                # Clear fields
                self.var_check.set(0)
                self.var_fname.set("")
                self.var_lname.set("")
                self.var_email.set("")
                self.var_contact.set("")
                self.var_securityA.set("")
                self.var_securityQ.set("Select")
                self.var_confpass.set("")
                self.var_pass.set("")
            conn.close()

    def return_login(self):
        self.root.destroy()

if __name__ == "__main__":
    main()