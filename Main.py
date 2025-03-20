from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk
import os
from time import strftime
from datetime import datetime
from Student import Student
from Train import Train
from Face_Recognition import Face_Recognition
from Attendance import Attendance
from Developer import Developer
from Help import Help


class Advanced_Attendance_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x720+0+0")
        self.root.resizable(0, 0)
        self.root.title("ADVANCED ATTENDANCE SYSTEM")

        # First image
        img = Image.open(
            r"D:\Life time Projects\3rd sem projects\Python\Advanced-Attendance-System-main\ADVANCED ATTENDANCE SYSTEM\Project_Images\Main1.png")
        img = img.resize((426, 130), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=426, height=130)

        # Second image
        img1 = Image.open(
            r"D:\Life time Projects\3rd sem projects\Python\Advanced-Attendance-System-main\ADVANCED ATTENDANCE SYSTEM\Project_Images\Main2.png")
        img1 = img1.resize((426, 130), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=426, y=0, width=426, height=130)

        # Third image
        img2 = Image.open(
            r"D:\Life time Projects\3rd sem projects\Python\Advanced-Attendance-System-main\ADVANCED ATTENDANCE SYSTEM\Project_Images\Main3.png")
        img2 = img2.resize((428, 130), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=852, y=0, width=428, height=130)

        # Background image
        img3 = Image.open(r"D:\Life time Projects\3rd sem projects\Python\Advanced-Attendance-System-main\ADVANCED ATTENDANCE SYSTEM\Project_Images\MainBg.png")
        img3 = img3.resize((1280, 590), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1280, height=590)

        title_lbl = Label(bg_img, text="WELCOME TO ADVANCED ATTENDANCE SYSTEM", font=(
            "times new roman", 32, "bold"), bg="DarkBlue", fg="red")
        title_lbl.place(x=0, y=0, width=1280, height=45)

        # Time
        def time():
            string = strftime('%x \n%A')
            lbl.config(text=string)
            string1 = strftime('%I:%M:%S %p')
            lbl1.config(text=string1)
            lbl1.after(1000, time)

        lbl = Label(title_lbl, font=('times new roman', 15, 'bold'),
                    background='DarkBlue', foreground='White')
        lbl.place(x=0, y=-4, width=99, height=50)

        lbl1 = Label(title_lbl, font=('times new roman', 14, 'bold'),
                     background='DarkBlue', foreground='White')
        lbl1.place(x=1170, y=-10, width=110, height=50)

        time()

        # Student button
        img4 = Image.open(
            r"D:\Life time Projects\3rd sem projects\Python\Advanced-Attendance-System-main\ADVANCED ATTENDANCE SYSTEM\Project_Images\MainStudent.png")
        img4 = img4.resize((250, 200), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4,
                    command=self.student_details, cursor="hand2")
        b1.place(x=80, y=50, width=250, height=200)

        b1_1 = Button(bg_img, text="Student Registration", command=self.student_details,
                      cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=80, y=250, width=250, height=40)

        # Photos button
        img9 = Image.open(
            r"D:\Life time Projects\3rd sem projects\Python\Advanced-Attendance-System-main\ADVANCED ATTENDANCE SYSTEM\Project_Images\MainPhotos.png")
        img9 = img9.resize((250, 200), Image.Resampling.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b2 = Button(bg_img, image=self.photoimg9,
                    cursor="hand2", command=self.open_img)
        b2.place(x=380, y=50, width=250, height=200)

        b2_1 = Button(bg_img, text="Photo Samples", cursor="hand2", command=self.open_img, font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b2_1.place(x=380, y=250, width=250, height=40)

        # Train button
        img8 = Image.open(
            r"D:\Life time Projects\3rd sem projects\Python\Advanced-Attendance-System-main\ADVANCED ATTENDANCE SYSTEM\Project_Images\MainTrain.png")
        img8 = img8.resize((250, 200), Image.Resampling.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b3 = Button(bg_img, image=self.photoimg8,
                    cursor="hand2", command=self.train_data)
        b3.place(x=680, y=50, width=250, height=200)

        b3_1 = Button(bg_img, text="Train Data", cursor="hand2", command=self.train_data, font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b3_1.place(x=680, y=250, width=250, height=40)

        # Face Recognition button
        img5 = Image.open(
            r"D:\Life time Projects\3rd sem projects\Python\Advanced-Attendance-System-main\ADVANCED ATTENDANCE SYSTEM\Project_Images\MainFace.png")
        img5 = img5.resize((250, 200), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b4 = Button(bg_img, image=self.photoimg5,
                    cursor="hand2", command=self.face_data)
        b4.place(x=980, y=50, width=250, height=200)

        b4_1 = Button(bg_img, text="Face Recognition", cursor="hand2", command=self.face_data, font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b4_1.place(x=980, y=250, width=250, height=40)

        # Attendance button
        img6 = Image.open(
            r"D:\Life time Projects\3rd sem projects\Python\Advanced-Attendance-System-main\ADVANCED ATTENDANCE SYSTEM\Project_Images\MainAttendance.png")
        img6 = img6.resize((250, 200), Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b5 = Button(bg_img, image=self.photoimg6,
                    cursor="hand2", command=self.attendance_data)
        b5.place(x=80, y=320, width=250, height=200)

        b5_1 = Button(bg_img, text="Attendance Record", cursor="hand2", command=self.attendance_data, font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b5_1.place(x=80, y=500, width=250, height=40)

        # Developer button
        img10 = Image.open(
            r"D:\Life time Projects\3rd sem projects\Python\Advanced-Attendance-System-main\ADVANCED ATTENDANCE SYSTEM\Project_Images\MainDeveloper.png")
        img10 = img10.resize((250, 200), Image.Resampling.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b6 = Button(bg_img, image=self.photoimg10,
                    cursor="hand2", command=self.developer_data)
        b6.place(x=380, y=320, width=250, height=200)

        b6_1 = Button(bg_img, text="Developer", cursor="hand2", command=self.developer_data, font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b6_1.place(x=380, y=500, width=250, height=40)

        # Help button
        img7 = Image.open(
            r"D:\Life time Projects\3rd sem projects\Python\Advanced-Attendance-System-main\ADVANCED ATTENDANCE SYSTEM\Project_Images\MainHelp.png")
        img7 = img7.resize((250, 200), Image.Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b7 = Button(bg_img, image=self.photoimg7,
                    cursor="hand2", command=self.helper_data)
        b7.place(x=680, y=320, width=250, height=200)

        b7_1 = Button(bg_img, text="Help Desk", cursor="hand2", command=self.helper_data, font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b7_1.place(x=680, y=500, width=250, height=40)

        # Exit button
        img11 = Image.open(
            r"D:\Life time Projects\3rd sem projects\Python\Advanced-Attendance-System-main\ADVANCED ATTENDANCE SYSTEM\Project_Images\MainExit.png")
        img11 = img11.resize((250, 200), Image.Resampling.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b8 = Button(bg_img, image=self.photoimg11,
                    cursor="hand2", command=self.IExit)
        b8.place(x=980, y=320, width=250, height=200)

        b8_1 = Button(bg_img, text="Exit", cursor="hand2", command=self.IExit, font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b8_1.place(x=980, y=500, width=250, height=40)

    def open_img(self):
        os.startfile(r"D:\Life time Projects\3rd sem projects\Python\Advanced-Attendance-System-main\ADVANCED ATTENDANCE SYSTEM\Data")

    def IExit(self):
        self.IExit = tkinter.messagebox.askyesno(
            "Face Recognition", "Exit this project?", parent=self.root)
        if self.IExit:
            self.root.destroy()

    # Function buttons
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def helper_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Advanced_Attendance_System(root)
    root.mainloop()