from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x720+0+0")  # Changed
        self.root.resizable(0, 0)
        self.root.title("CREATER")
        
        # Title
        title_lbl = Label(self.root, text="DEVELOPER", font=(
            "times new roman", 35, "bold"), bg="white", fg="DarkBlue")
        title_lbl.place(x=0, y=0, width=1280, height=40)  # Width changed
        
        # Background
        img_top = Image.open(r"D:\Life time Projects\3rd sem projects\Python\Advanced-Attendance-System-main\ADVANCED ATTENDANCE SYSTEM\Project_Images\DeveloperBg.png")
        img_top = img_top.resize((1280, 680), Image.Resampling.LANCZOS)  # Changed
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=40, width=1280, height=680)  # Adjusted
        
        # Developer Image
        img_top1 = Image.open(r"D:\Life time Projects\3rd sem projects\Python\Advanced-Attendance-System-main\ADVANCED ATTENDANCE SYSTEM\Project_Images\Developer.jpg")
        img_top1 = img_top1.resize((250, 250), Image.Resampling.LANCZOS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        f_lbl = Label(self.root, image=self.photoimg_top1)
        f_lbl.place(x=30, y=360, width=250, height=250)  # Y-position changed
        
        # Labels
        dep_label = Label(self.root, text="HELLO, MY NAME IS Rathod Yashraj", font=(
            "times new roman", 17, "bold"), bg="DarkBlue", fg="White")
        dep_label.place(x=30, y=620)  # Y-position changed

        dep_label = Label(self.root, text="I am student of L.J Collage.I love to do coding & improve my self and my skill day by day ", font=(
            "times new roman", 17, "bold"), fg="white", bg="red")
        dep_label.place(x=30, y=650)  # Y-position changed

if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()