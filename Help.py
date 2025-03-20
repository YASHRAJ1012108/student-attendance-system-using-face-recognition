from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import webbrowser
from PIL import Image, ImageTk
import mysql.connector
import cv2

class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x720+0+0")  # Changed
        self.root.resizable(0, 0)
        self.root.title("ADVANCED ATTENDANCE SYSTEM")

        title_lbl = Label(self.root, text="HELP DESK ", font=(
            "times new roman", 35, "bold"), bg="white", fg="SlateBlue")
        title_lbl.place(x=0, y=0, width=1280, height=40)  # Width changed

        img_top = Image.open(r"D:\Life time Projects\3rd sem projects\Python\Advanced-Attendance-System-main\ADVANCED ATTENDANCE SYSTEM\Project_Images\Help.jpg")
        img_top = img_top.resize((1280, 680), Image.Resampling.LANCZOS)  # Changed
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=40, width=1280, height=680)  # Adjusted

        # Developer info
        dep_label = Label(self.root, text="MAIL ID: rathodyashraj1012108@gmail.com",
                        font=("times new roman", 18, "bold"), bg="white")
        dep_label.place(x=800, y=650)  # Position adjusted

        new = 1
        url = "https://www.linkedin.com/in/yashraj-rathod-8a71652b8"
        url1 = "https://github.com/YASHRAJ1012108"

        def openweb():
            webbrowser.open(url, new=new)

        def openweb1():
            webbrowser.open(url1, new=new)
            
        Btn = Button(root, text="LinkedIn", command=openweb, font=(
            "times new roman", 15, "bold"), bg="coral", fg="Black")
        Btn.place(x=900, y=610, width=130)  # Position adjusted

        Btn1 = Button(root, text="GitHub", command=openweb1, font=(
            "times new roman", 15, "bold"), bg="coral", fg="Black")
        Btn1.place(x=1070, y=610, width=130)  # Position adjusted
        root.mainloop()

if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()