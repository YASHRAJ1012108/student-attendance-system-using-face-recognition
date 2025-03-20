from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np
import csv
from tkinter import filedialog

mydata = []

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x720+0+5")
        self.root.resizable(0, 0)
        self.root.title("ATTENDANCE DETAILS")

        # ====================Variables=====================
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()
      

        # First image
        img = Image.open(r"D:\Life time Projects\3rd sem projects\Python\Advanced-Attendance-System-main\ADVANCED ATTENDANCE SYSTEM\Project_Images\Attendance1.png")
        img = img.resize((640, 180), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=640, height=180)

        # Second image
        img1 = Image.open(r"D:\Life time Projects\3rd sem projects\Python\Advanced-Attendance-System-main\ADVANCED ATTENDANCE SYSTEM\Project_Images\Attendance2.png")
        img1 = img1.resize((640, 180), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=640, y=0, width=640, height=180)

        # Background image
        img3 = Image.open(r"D:\Life time Projects\3rd sem projects\Python\Advanced-Attendance-System-main\ADVANCED ATTENDANCE SYSTEM\Project_Images\AttendanceBg.jpg")
        img3 = img3.resize((1280, 720), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=180, width=1280, height=540)

        title_lbl = Label(bg_img, text="ATTENDANCE REPORT", font=("times new roman", 30, "bold"), bg="DarkBlue", fg="White")
        title_lbl.place(x=0, y=0, width=1280, height=40)

        main_frame = Frame(bg_img, bd=2, bg="DarkBlue")
        main_frame.place(x=1, y=40, width=1278, height=490)

        # Left label frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                              text="Student Attendance Details", font=("times new roman", 14, "bold"))
        Left_frame.place(x=5, y=5, width=630, height=475)

        img_left = Image.open(r"D:\Life time Projects\3rd sem projects\Python\Advanced-Attendance-System-main\ADVANCED ATTENDANCE SYSTEM\Project_Images\Attendance3.png")
        img_left = img_left.resize((625, 120), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=1, y=0, width=625, height=120)

        left_inside_frame = Frame(Left_frame, bd=2, relief=RIDGE, bg="white")
        left_inside_frame.place(x=0, y=120, width=626, height=325)

        # Labels and entries
        attendance_Id_label = Label(left_inside_frame, text="Attendance ID:", font=("times new roman", 12), bg="white")
        attendance_Id_label.grid(row=0, column=0, padx=8, pady=5, sticky=W)

        attendance_Id_entry = ttk.Entry(left_inside_frame, width=18, textvariable=self.var_atten_id, font=("times new roman", 12))
        attendance_Id_entry.grid(row=0, column=1, padx=8, pady=5, sticky=W)

        Dep_label = Label(left_inside_frame, text="Department:", font=("times new roman", 12), bg="white")
        Dep_label.grid(row=0, column=2, padx=8, pady=5, sticky=W)

        Dep_combo = ttk.Combobox(left_inside_frame, textvariable=self.var_atten_dep, font=("times new roman", 12), 
                                width=16, state="readonly")
        Dep_combo["values"] = ("Select Department", "Computer Science", "Mechanical", "Electrical", "Electronics", "Civil")
        Dep_combo.current(0)
        Dep_combo.grid(row=0, column=3, padx=8, pady=5, sticky=W)

        name_label = Label(left_inside_frame, text="Name:", font=("times new roman", 12), bg="white")
        name_label.grid(row=1, column=0, padx=8, pady=5, sticky=W)

        name_entry = ttk.Entry(left_inside_frame, width=18, textvariable=self.var_atten_name, font=("times new roman", 12))
        name_entry.grid(row=1, column=1, padx=8, pady=5, sticky=W)

        roll_label = Label(left_inside_frame, text="USN:", font=("times new roman", 12), bg="white")
        roll_label.grid(row=2, column=0, padx=8, pady=5, sticky=W)

        roll_entry = ttk.Entry(left_inside_frame, width=18, textvariable=self.var_atten_roll, font=("times new roman", 12))
        roll_entry.grid(row=2, column=1, padx=8, pady=5, sticky=W)

        Date_label = Label(left_inside_frame, text="Date:", font=("times new roman", 12), bg="white")
        Date_label.grid(row=1, column=2, padx=8, pady=5, sticky=W)

        Date_entry = ttk.Entry(left_inside_frame, width=18, textvariable=self.var_atten_date, font=("times new roman", 12))
        Date_entry.grid(row=1, column=3, padx=8, pady=5, sticky=W)

        time_label = Label(left_inside_frame, text="Time:", font=("times new roman", 12), bg="white")
        time_label.grid(row=2, column=2, padx=8, pady=5, sticky=W)

        time_entry = ttk.Entry(left_inside_frame, width=18, textvariable=self.var_atten_time, font=("times new roman", 12))
        time_entry.grid(row=2, column=3, padx=8, pady=5, sticky=W)

        Attendance_label = Label(left_inside_frame, text="Status:", font=("times new roman", 12), bg="white")
        Attendance_label.grid(row=3, column=0, padx=8, pady=5, sticky=W)

        self.atten_status = ttk.Combobox(left_inside_frame, width=16, textvariable=self.var_atten_attendance,
                                       font=("times new roman", 12), state="readonly")
        self.atten_status["values"] = ("Status", "Present", "Absent")
        self.atten_status.grid(row=3, column=1, padx=8, pady=5, sticky=W)
        self.atten_status.current(0)

        # Buttons Frame
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=200, width=622, height=100)

        import_btn = Button(btn_frame, text="Import CSV", command=self.importCsv, width=35, 
                          font=("times new roman", 12, "bold"), bg="DarkBlue", fg="white")
        import_btn.grid(row=0, column=0, padx=2, pady=5)

        export_btn = Button(btn_frame, text="Export CSV", command=self.exportCsv, width=35,
                          font=("times new roman", 12, "bold"), bg="DarkBlue", fg="white")
        export_btn.grid(row=0, column=1, padx=2, pady=5)

        update_btn = Button(btn_frame, text="Update", command=self.update_data, width=35,
                          font=("times new roman", 12, "bold"), bg="DarkBlue", fg="white")
        update_btn.grid(row=1, column=0, padx=2, pady=5)

        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=35,
                         font=("times new roman", 12, "bold"), bg="DarkBlue", fg="white")
        reset_btn.grid(row=1, column=1, padx=0, pady=5)

        # Right label frame
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                               text="Attendance Details", font=("times new roman", 14, "bold"))
        right_frame.place(x=640, y=5, width=630, height=475)

        table_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=618, height=430)

        # Scrollbars
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame, columns=("id", "roll", "name", "department", "time", "date", "attendance"),
                                                xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id", text="Attendance ID")
        self.AttendanceReportTable.heading("roll", text="USN")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Status")

        self.AttendanceReportTable["show"] = "headings"
        
        self.AttendanceReportTable.column("id", width=90)
        self.AttendanceReportTable.column("roll", width=110)
        self.AttendanceReportTable.column("name", width=130)
        self.AttendanceReportTable.column("department", width=150)
        self.AttendanceReportTable.column("time", width=90)
        self.AttendanceReportTable.column("date", width=90)
        self.AttendanceReportTable.column("attendance", width=100)

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)

    def fetchData(self, rows):
        self.AttendanceReportTable.delete(
            *self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)

    # import CSV
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(
            ("CSV File", "*.csv"), ("ALL File", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    # export CSV
    def exportCsv(self):

        try:
            if len(mydata) < 1:
                messagebox.showerror(
                    "No Data", "No Data is Found to Export", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(
                ("CSV File", "*.csv"), ("ALL File", "*.*")), parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo(
                    "Data Export", "Your Data is Exported to :"+os.path.basename(fln)+" successfully")
        except Exception as es:
            messagebox.showerror(
                "Error", "Exporting Cancelled !!", parent=self.root)

    def get_cursor(self, event=""):
        cursor_row = self.AttendanceReportTable.focus()
        if not cursor_row:
            return
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content.get("values", [])
        if len(rows) != 7:
            return
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])


    def reset_data(self):
        self.var_atten_id.set(""),
        self.var_atten_roll.set(""),
        self.var_atten_name.set(""),
        self.var_atten_dep.set("Select Department"),
        self.var_atten_time.set(""),
        self.var_atten_date.set(""),
        self.var_atten_attendance.set("Status")

    # update

    def update_data(self):
        id = self.var_atten_id.get()
        roll = self.var_atten_roll.get()
        name = self.var_atten_name.get()
        dep = self.var_atten_dep.get()
        time = self.var_atten_time.get()
        date = self.var_atten_date.get()
        attendn = self.var_atten_attendance.get()

        # write to csv file
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data", "No Data is Found For Updatation", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save CSV", filetypes=(("CSV file", "*.csv"), ("All File", "*.*")), parent=self.root)
            with open(fln, mode="w", newline="\n") as f:
                dict_writer = csv.DictWriter(f, fieldnames=(["Attendance ID", "USN", "Student Name", "Department", "Time", "Date", "Attendance Status"]))
                # dict_writer.writeheader()
                dict_writer.writerow({
                    "Attendance ID": id,
                    "USN": roll,
                    "Student Name": name,
                    "Department": dep,
                    "Time": time,
                    "Date": date,
                    "Attendance Status": attendn
                })
            messagebox.showinfo("Data Updated", "Your Data is Updated to " +os.path.basename(fln) + " Successfully !!", parent=self.root)
            self.reset_data()

        except Exception as es:
            messagebox.showerror("Error", "No File Is Selected For Updation", parent=self.root)
if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()