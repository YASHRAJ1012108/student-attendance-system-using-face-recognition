from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2
import re



class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1280x720+0+5")  # Changed geometry
        self.root.resizable(0, 0)
        self.root.title("ADVANCED ATTENDANCE SYSTEM")

        # ======================================Variables=======================================
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_div = StringVar()
        self.var_usn = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        self.var_search = StringVar()
        self.var_searchcombo = StringVar()

        def click(event):
            dob_entry.config(state=NORMAL)
            dob_entry.delete(0, END)

        # firstimage
        img = Image.open(
            r"D:\Life time Projects\3rd sem projects\Python\Advanced-Attendance-System-main\ADVANCED ATTENDANCE SYSTEM\Project_Images\Student1.png")
        img = img.resize((426, 100), Image.Resampling.LANCZOS)  # Adjusted size
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=426, height=100)  # Adjusted placement

        # secondimage
        img1 = Image.open(
            r"D:\Life time Projects\3rd sem projects\Python\Advanced-Attendance-System-main\ADVANCED ATTENDANCE SYSTEM\Project_Images\Student2.png")
        img1 = img1.resize((426, 100), Image.Resampling.LANCZOS)  # Adjusted size
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=426, y=0, width=426, height=100)  # Adjusted placement

        # thirdimage
        img2 = Image.open(
            r"D:\Life time Projects\3rd sem projects\Python\Advanced-Attendance-System-main\ADVANCED ATTENDANCE SYSTEM\Project_Images\Student3.png")
        img2 = img2.resize((428, 100), Image.Resampling.LANCZOS)  # Adjusted size
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=852, y=0, width=428, height=100)  # Adjusted placement

        # backgroundimage
        img3 = Image.open(r"D:\Life time Projects\3rd sem projects\Python\Advanced-Attendance-System-main\ADVANCED ATTENDANCE SYSTEM\Project_Images\StudentBg.jpg")
        img3 = img3.resize((1280, 620), Image.Resampling.LANCZOS)  # Adjusted size
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=100, width=1280, height=620)  # Adjusted placement

        # Main Frame
        title_lbl = Label(bg_img, text="STUDENT REGISTERATION", font=(
            "times new roman", 35, "bold"), bg="DarkBlue", fg="White")
        title_lbl.place(x=-2, y=-2, width=1280, height=40)  # Adjusted width

        main_frame = Frame(bg_img, bd=2, bg="DarkBlue")
        main_frame.place(x=0, y=40, width=1274, height=532)  # Adjusted dimensions

        # left label frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                text="Student Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=5, y=5, width=630, height=520)  # Adjusted dimensions

        img_left = Image.open(
            r"D:\Life time Projects\3rd sem projects\Python\Advanced-Attendance-System-main\ADVANCED ATTENDANCE SYSTEM\Project_Images\Student4.png")
        img_left = img_left.resize((625, 100), Image.Resampling.LANCZOS)  # Adjusted size
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=1, y=0, width=625, height=100)  # Adjusted placement

        # Current_course
        current_course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE,
                                          text="Current Course Information", font=("times new roman", 12, "bold"))
        current_course_frame.place(x=1, y=105, width=625, height=100)  # Adjusted placement

        # Department
        dep_label = Label(current_course_frame, text="Department", font=(
            "times new roman", 12, "bold"), bg="white")  # Reduced font size
        dep_label.grid(row=0, column=0, padx=8, sticky=W)  # Adjusted padding

        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=(
            "times new roman", 12, "bold"), state="readonly", width=22)  # Reduced font size
        dep_combo["values"] = ("Select Department", "Aerospace Engineering", "Artificial Intelligence And Machine Learning", "Automobile Engineering", "Computer Science And Engineering", "Computer Engineering", "Civil Engineering",
                               "Chemical Engineering", "Electronics And Communication Engineering", "Electrical AND Electronics Engineering", "Industrial Engineering", "Information Science And Engineering", "Mechanical Engineering")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=5, sticky=W)  # Adjusted padding

        # Course
        course_label = Label(current_course_frame, text="Course", font=(
            "times new roman", 12, "bold"), bg="white")  # Reduced font size
        course_label.grid(row=0, column=2, padx=15, sticky=W)  # Adjusted padding

        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, font=(
            "times new roman", 12, "bold"), state="readonly", width=22)  # Reduced font size
        course_combo["values"] = (
            "Select Course", "B.E.", "M.tech", "B.BA", "M.BA", "B.com")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=5, sticky=W)  # Adjusted padding

        # Year
        year_label = Label(current_course_frame, text="Batch-Year",
                           font=("times new roman", 12, "bold"), bg="white")  # Reduced font size
        year_label.grid(row=1, column=0, padx=8, sticky=W)  # Adjusted padding

        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=(
            "times new roman", 12, "bold"), state="readonly", width=22)  # Reduced font size
        year_combo["values"] = ("Select Year", "2019-20",
                                "2020-21", "2021-22", "2022-23")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=5, sticky=W)  # Adjusted padding

        # Semester
        semester_label = Label(current_course_frame, text="Semester", font=(
            "times new roman", 12, "bold"), bg="white")  # Reduced font size
        semester_label.grid(row=1, column=2, padx=15, sticky=W)  # Adjusted padding

        semester_combo = ttk.Combobox(current_course_frame, textvariable=self.var_sem, font=(
            "times new roman", 12, "bold"), state="readonly", width=22)  # Reduced font size
        semester_combo["values"] = (
            "Select Semester", "I", "II", "III", "IV", "V", "VI", "VII", "VIII")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=5, sticky=W)  # Adjusted padding

        # Class_Student_Information
        class_student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE,
                                         text="Class Student Information", font=("times new roman", 12, "bold"))
        class_student_frame.place(x=1, y=205, width=625, height=290)  # Adjusted placement

        # Student_ID
        student_Id_label = Label(class_student_frame, text="Student ID", font=(
            "times new roman", 12, "bold"), bg="white")  # Reduced font size
        student_Id_label.grid(row=0, column=0, padx=8, pady=3, sticky=W)  # Adjusted padding

        student_Id_entry = ttk.Entry(
            class_student_frame, textvariable=self.var_id, width=18, font=("times new roman", 12, "bold"))  # Reduced font size
        student_Id_entry.grid(row=0, column=1, padx=8, pady=3, sticky=W)  # Adjusted padding

        # Student_Name
        studentName_label = Label(class_student_frame, text="Student Name", font=(
            "times new roman", 12, "bold"), bg="white")  # Reduced font size
        studentName_label.grid(row=0, column=2, padx=35, pady=3, sticky=W)  # Adjusted padding

        studentName_entry = ttk.Entry(
            class_student_frame, textvariable=self.var_name, width=18, font=("times new roman", 12, "bold"))  # Reduced font size
        studentName_entry.grid(row=0, column=3, padx=8, pady=3, sticky=W)  # Adjusted padding

        # Class_Division
        class_div_label = Label(class_student_frame, text="Class Division", font=(
            "times new roman", 12, "bold"), bg="white")  # Reduced font size
        class_div_label.grid(row=1, column=0, padx=8, pady=3, sticky=W)  # Adjusted padding

        div_combo = ttk.Combobox(class_student_frame, textvariable=self.var_div, font=(
            "times new roman", 12, "bold"), state="readonly", width=16)  # Reduced font size
        div_combo["values"] = ("Select Division ", "A", "B", "C", "D", "E")
        div_combo.current(0)
        div_combo.grid(row=1, column=1, padx=8, pady=3, sticky=W)  # Adjusted padding

        # USN
        usn_label = Label(class_student_frame, text="USN", font=(
            "times new roman", 12, "bold"), bg="white")  # Reduced font size
        usn_label.grid(row=1, column=2, padx=35, pady=3, sticky=W)  # Adjusted padding

        usn_entry = ttk.Entry(class_student_frame, textvariable=self.var_usn, width=18, font=(
            "times new roman", 12, "bold"))  # Reduced font size
        usn_entry.grid(row=1, column=3, padx=8, pady=3, sticky=W)  # Adjusted padding

        # Gender
        gender_label = Label(class_student_frame, text="Gender", font=(
            "times new roman", 12, "bold"), bg="white")  # Reduced font size
        gender_label.grid(row=2, column=0, padx=8, pady=3, sticky=W)  # Adjusted padding

        gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender, font=(
            "times new roman", 12, "bold"), state="readonly", width=16)  # Reduced font size
        gender_combo["values"] = ("Select Gender", "Male", "Female", "Others")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=8, pady=3, sticky=W)  # Adjusted padding

        # DOB
        dob_label = Label(class_student_frame, text="D.O.B", font=(
            "times new roman", 12, "bold"), bg="white")  # Reduced font size
        dob_label.grid(row=2, column=2, padx=35, pady=3, sticky=W)  # Adjusted padding

        dob_entry = ttk.Entry(class_student_frame, textvariable=self.var_dob, width=18, font=(
            "times new roman", 12, "bold"))  # Reduced font size
        dob_entry.insert(0, "DD/MM/YYYY")
        dob_entry.config(state=DISABLED)
        dob_entry.bind("<Button-1>", click)
        dob_entry.grid(row=2, column=3, padx=8, pady=3, sticky=W)  # Adjusted padding

        # Email
        email_label = Label(class_student_frame, text="Email", font=(
            "times new roman", 12, "bold"), bg="white")  # Reduced font size
        email_label.grid(row=3, column=0, padx=8, pady=3, sticky=W)  # Adjusted padding

        email_entry = ttk.Entry(class_student_frame, textvariable=self.var_email, width=18, font=(
            "times new roman", 12, "bold"))  # Reduced font size
        email_entry.grid(row=3, column=1, padx=8, pady=3, sticky=W)  # Adjusted padding

        # Phone_No
        phone_label = Label(class_student_frame, text="Phone No.", font=(
            "times new roman", 12, "bold"), bg="white")  # Reduced font size
        phone_label.grid(row=3, column=2, padx=35, pady=3, sticky=W)  # Adjusted padding

        phone_entry = ttk.Entry(class_student_frame, textvariable=self.var_phone, width=18, font=(
            "times new roman", 12, "bold"))  # Reduced font size
        phone_entry.grid(row=3, column=3, padx=8, pady=3, sticky=W)  # Adjusted padding

        # Address
        address_label = Label(class_student_frame, text="Address", font=(
            "times new roman", 12, "bold"), bg="white")  # Reduced font size
        address_label.grid(row=4, column=0, padx=8, pady=3, sticky=W)  # Adjusted padding

        address_entry = ttk.Entry(class_student_frame, textvariable=self.var_address, width=18, font=(
            "times new roman", 12, "bold"))  # Reduced font size
        address_entry.grid(row=4, column=1, padx=8, pady=3, sticky=W)  # Adjusted padding

        # Teacher_Name
        teacherName_label = Label(class_student_frame, text="Teacher Name", font=(
            "times new roman", 12, "bold"), bg="white")  # Reduced font size
        teacherName_label.grid(row=4, column=2, padx=35, pady=3, sticky=W)  # Adjusted padding

        teacherName_entry = ttk.Entry(
            class_student_frame, textvariable=self.var_teacher, width=18, font=("times new roman", 12, "bold"))  # Reduced font size
        teacherName_entry.grid(row=4, column=3, padx=8, pady=3, sticky=W)  # Adjusted padding

        # Radio_buttons
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(
            class_student_frame, variable=self.var_radio1, text="Take Photo Sample", value="Yes")
        radiobtn1.grid(row=6, column=0, pady=3)  # Adjusted padding

        radiobtn2 = ttk.Radiobutton(
            class_student_frame, variable=self.var_radio1, text="No Photo Sample", value="No")
        radiobtn2.grid(row=6, column=1, pady=3)  # Adjusted padding

        # 1st Buttons_Frame
        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=180, width=620, height=35)  # Adjusted width to 620

        save_btn = Button(btn_frame, text="Save", command=self.add_data, width=15, font=(
            "times new roman", 12, "bold"), bg="DarkBlue", fg="white")
        save_btn.grid(row=0, column=0, padx=2, pady=2)

        update_btn = Button(btn_frame, text="Update", command=self.update_data, width=15, font=(
            "times new roman", 12, "bold"), bg="DarkBlue", fg="white")
        update_btn.grid(row=0, column=1, padx=2, pady=2)

        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, width=15, font=(
            "times new roman", 12, "bold"), bg="DarkBlue", fg="white")
        delete_btn.grid(row=0, column=2, padx=2, pady=2)

        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=15, font=(
            "times new roman", 12, "bold"), bg="DarkBlue", fg="white")
        reset_btn.grid(row=0, column=3, padx=2, pady=2)

        # 2nd Buttons_Frame
        btn_frame1 = Frame(class_student_frame, bd=2, relief=RIDGE)
        btn_frame1.place(x=0, y=215, width=620, height=35)  # Adjusted width to 620

        take_photo_btn = Button(btn_frame1, command=self.generate_dataset, text="Take Photo Sample", width=30, font=(
            "times new roman", 12, "bold"), bg="DarkBlue", fg="white")
        take_photo_btn.grid(row=0, column=0, padx=2, pady=2)

        update_photo_btn = Button(btn_frame1, command=self.generate_dataset, text="Update Photo Sample", width=30, font=(
            "times new roman", 12, "bold"), bg="DarkBlue", fg="white")
        update_photo_btn.grid(row=0, column=1, padx=2, pady=2)

        # Right label frame
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                 text="Student Details", font=("times new roman", 12, "bold"))
        right_frame.place(x=640, y=5, width=629, height=520)  # Adjusted x and width

        img_right = Image.open(
            r"D:\Life time Projects\3rd sem projects\Python\Advanced-Attendance-System-main\ADVANCED ATTENDANCE SYSTEM\Project_Images\Student5.png")
        img_right = img_right.resize((625, 130), Image.Resampling.LANCZOS)  # Adjusted size
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(right_frame, image=self.photoimg_right)
        f_lbl.place(x=1, y=0, width=625, height=130)  # Adjusted placement

        # Search System
        search_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE,
                                  text="Search System", font=("times new roman", 12, "bold"))
        search_frame.place(x=1, y=135, width=625, height=80)  # Adjusted width

        # Search Combo
        search_combo = ttk.Combobox(search_frame, textvariable=self.var_searchcombo, font=(
            "times new roman", 12, "bold"), state="readonly", width=15)
        search_combo["values"] = ("Select", "Usn", "Name")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        search_entry = ttk.Entry(search_frame, textvariable=self.var_search, width=18, font=(
            "times new roman", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        search_btn = Button(search_frame, text="Search", command=self.search_data, width=10, font=(
            "times new roman", 12, "bold"), bg="DarkBlue", fg="white")
        search_btn.grid(row=0, column=3, padx=5, pady=5)

        showAll_btn = Button(search_frame, text="Show All", command=self.fetch_data, width=10, font=(
            "times new roman", 12, "bold"), bg="DarkBlue", fg="white")
        showAll_btn.grid(row=0, column=4, padx=5, pady=5)

        # Table Frame
        table_frame = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=1, y=220, width=625, height=285)  # Adjusted placement

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, columns=("dep", "course", "year", "sem", "id", "name", "div", "usn", "gender",
                                          "dob", "email", "phone", "address", "teacher", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Batch-Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="Student ID")
        self.student_table.heading("name", text="Student Name")
        self.student_table.heading("div", text="Class Division")
        self.student_table.heading("usn", text="USN")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="D.O.B")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone No.")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher Name")
        self.student_table.heading("photo", text="PhotoSampleStatus")

        self.student_table.column("dep", width=180)
        self.student_table.column("course", width=130)
        self.student_table.column("year", width=130)
        self.student_table.column("sem", width=130)
        self.student_table.column("id", width=130)
        self.student_table.column("name", width=180)
        self.student_table.column("div", width=130)
        self.student_table.column("usn", width=140)
        self.student_table.column("gender", width=130)
        self.student_table.column("dob", width=130)
        self.student_table.column("email", width=130)
        self.student_table.column("phone", width=130)
        self.student_table.column("address", width=180)
        self.student_table.column("teacher", width=180)
        self.student_table.column("photo", width=140)


        self.student_table["show"] = "headings"
        # style=ttk.Style()
        # style.theme_use("default")

        # style.configure("Treeview",background="#707070")

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

        # ===========================================Function Declaration================================================

        # ===========================================Function Declaration================================================

    def add_data(self):
        # Department, Course, Year, Semester, Division, Gender Validation
        if self.var_dep.get() == "Select Department" or \
        self.var_course.get() == "Select Course" or \
        self.var_year.get() == "Select Year" or \
        self.var_sem.get() == "Select Semester" or \
        self.var_div.get() == "Select Division" or \
        self.var_gender.get() == "Select Gender":
            messagebox.showerror("Error", "Please select all required fields.", parent=self.root)
            return

        # Name Validation
        if not self.var_name.get().strip():
            messagebox.showerror("Error", "Name cannot be empty.", parent=self.root)
            return
        if not re.match(r'^[A-Za-z\s]+$', self.var_name.get().strip()):
            messagebox.showerror("Error", "Name can only contain letters and spaces.", parent=self.root)
            return

        # Date of Birth (DOB) Validation
        if not self.var_dob.get().strip():
            messagebox.showerror("Error", "Date of Birth cannot be empty.", parent=self.root)
            return
        if not re.match(r'^\d{2}/\d{2}/\d{4}$', self.var_dob.get().strip()):
            messagebox.showerror("Error", "Date of Birth must be in DD/MM/YYYY format.", parent=self.root)
            return
        # Additional DOB plausibility checks can be added here

        # Email Validation
        if not self.var_email.get().strip():
            messagebox.showerror("Error", "Email cannot be empty.", parent=self.root)
            return
        if not re.match(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', self.var_email.get().strip()):
            messagebox.showerror("Error", "Invalid email format.", parent=self.root)
            return

        # Phone Number Validation
        if not self.var_phone.get().strip():
            messagebox.showerror("Error", "Phone number cannot be empty.", parent=self.root)
            return
        if not re.match(r'^\d{10}$', self.var_phone.get().strip()):
            messagebox.showerror("Error", "Phone number must be 10 digits.", parent=self.root)
            return

        # Address Validation
        if not self.var_address.get().strip():
            messagebox.showerror("Error", "Address cannot be empty.", parent=self.root)
            return

        # Teacher Name Validation
        if not self.var_teacher.get().strip():
            messagebox.showerror("Error", "Teacher name cannot be empty.", parent=self.root)
            return
        if not re.match(r'^[A-Za-z\s]+$', self.var_teacher.get().strip()):
            messagebox.showerror("Error", "Teacher name can only contain letters and spaces.", parent=self.root)
            return

        # USN Validation
        if not self.var_usn.get().strip():
            messagebox.showerror("Error", "USN cannot be empty.", parent=self.root)
            return
        # Add specific USN format validation if required



        # If all validations pass, proceed to add data to the database
        try:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="Yash1012108@", database="advanced_attendance_system")
            my_cursor = conn.cursor()
            my_cursor.execute("INSERT INTO student (Department, Course, Year, Semester, ID, Name, Division, USN, Gender, DOB, Email, Phone, Address, Teacher, PhotoSample) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                self.var_dep.get(),
                self.var_course.get(),
                self.var_year.get(),
                self.var_sem.get(),
                self.var_id.get(),
                self.var_name.get(),
                self.var_div.get(),
                self.var_usn.get(),
                self.var_gender.get(),
                self.var_dob.get(),
                self.var_email.get(),
                self.var_phone.get(),
                self.var_address.get(),
                self.var_teacher.get(),
                self.var_radio1.get()
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Student details have been added successfully!", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
        # =======================================fetch data=============================================

    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="Yash1012108@", database="advanced_attendance_system")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # ===================================================get cursor=================================================
    # ===================================================get cursor=================================================
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        if not cursor_focus:  # Check if any item is selected
            return
        
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        
        # Validate data before setting variables
        if not data or len(data) < 15:
            messagebox.showwarning("Warning", "Incomplete or corrupt data record", parent=self.root)
            self.reset_data()
            return

        try:
            self.var_dep.set(data[0])
            self.var_course.set(data[1])
            self.var_year.set(data[2])
            self.var_sem.set(data[3])
            self.var_id.set(data[4])
            self.var_name.set(data[5])
            self.var_div.set(data[6])
            self.var_usn.set(data[7])
            self.var_gender.set(data[8])
            self.var_dob.set(data[9])
            self.var_email.set(data[10])
            self.var_phone.set(data[11])
            self.var_address.set(data[12])
            self.var_teacher.set(data[13])
            self.var_radio1.set(data[14])
        except IndexError as ie:
            messagebox.showerror("Data Error", f"Missing data field: {str(ie)}", parent=self.root)
            self.reset_data()
        except Exception as e:
            messagebox.showerror("Error", f"Unexpected error: {str(e)}", parent=self.root)
            self.reset_data()

    # update function
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_course.get() == "Select Course" or self.var_year.get() == "Select Year" or self.var_sem.get() == "Select Semester" or self.var_address.get() == "" or self.var_name.get() == "" or self.var_id.get() == "" or self.var_course == "" or self.var_div == "" or self.var_dob == "" or self.var_email == "" or self.var_gender == "" or self.var_usn == "":
            messagebox.showerror(
                "Error", "All Fields are Required", parent=self.root)

        else:
            try:
                update = messagebox.askyesno(
                    "Update", "Do you want to update this Student Details ??", parent=self.root)
                if update > 0:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="Yash1012108@", database="advanced_attendance_system")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Department=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Usn=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where ID =%s", (

                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_name.get(),
                        self.var_div.get(),
                        self.var_usn.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_id.get()
                    ))
                else:
                    if not update:
                        return
                messagebox.showinfo(
                    "Success", "Student Details Updated Successfully!!", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due TO:{str(es)}", parent=self.root)

    # Delete Function

    def delete_data(self):
        if self.var_id.get() == "":
            messagebox.showerror(
                "Error", "Student ID must be Required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno(
                    "Student Delete Page", "Do you want to Delete this Student Details ??", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="Yash1012108@", database="advanced_attendance_system")
                    my_cursor = conn.cursor()
                    sql = "delete from student where ID=%s"
                    val = (self.var_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Delete", "Student Details Deleted Successfully !!", parent=self.root)

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due TO:{str(es)}", parent=self.root)

    # Reset Button
    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_sem.set("Select Semester"),
        self.var_id.set(""),
        self.var_name.set("")
        self.var_div.set("Select Division")
        self.var_usn.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("DD/MM/YYYY")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    # search

    def search_data(self):
        if self.var_searchcombo.get() == "Select":
            messagebox.showerror(
                "Error", "Select Combo Option", parent=self.root)
        elif self.var_search.get() == "":
            messagebox.showerror(
                "Error", "Fill the Search Field", parent=self.root)

        else:

            try:

                conn = mysql.connector.connect(
                    host="localhost", username="root", password="Yash1012108@", database="advanced_attendance_system")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student where " + str(
                    self.var_searchcombo.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                data = my_cursor.fetchall()

                if len(data) != 0:
                    self.student_table.delete(
                        *self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("", END, values=i)
                    conn.commit()

                else:
                    messagebox.showerror(
                        "Error", "Data Not Found", parent=self.root)
                conn.close()
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due To :{str(es)}", parent=self.root)


# ==================================================Generate data set or Take photo samples===================================================

    def generate_dataset(self):
        if (self.var_dep.get() == "Select Department" 
            or self.var_course.get() == "Select Course" 
            or self.var_year.get() == "Select Year" 
            or self.var_sem.get() == "Select Semester" 
            or self.var_name.get() == "" 
            or self.var_id.get() == "" 
            or self.var_div.get() == "Select Division" 
            or self.var_dob.get() == "DD/MM/YYYY" 
            or self.var_email.get() == "" 
            or self.var_gender.get() == "Select Gender" 
            or self.var_usn.get() == ""):
            messagebox.showerror("Error", "All Fields are Required", parent=self.root)
        else:
            try:
                # Check if student exists in the database
                conn = mysql.connector.connect(
                    host="localhost", 
                    username="root", 
                    password="Yash1012108@", 
                    database="advanced_attendance_system"
                )
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * FROM student WHERE ID=%s", (self.var_id.get(),))
                existing = my_cursor.fetchone()
                conn.close()

                if not existing:
                    messagebox.showerror("Error", "Student not found. Please save the student first.", parent=self.root)
                    return

                # Capture photos
                face_classifier = cv2.CascadeClassifier(
                    r"D:\Life time Projects\3rd sem projects\Python\Advanced-Attendance-System-main\ADVANCED ATTENDANCE SYSTEM\haarcascade_frontalface_default.xml"
                )

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    for (x, y, w, h) in faces:
                        return img[y:y+h, x:x+w]
                    return None

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(
                            my_frame), (450, 450), fx=0.5, fy=0.5)
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = r"D:\Life time Projects\3rd sem projects\Python\Advanced-Attendance-System-main\ADVANCED ATTENDANCE SYSTEM/Data/user." + \
                            str(self.var_id.get()) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50),
                                    cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break

                cap.release()
                cv2.destroyAllWindows()

                # Update PhotoSample status to "Yes" after capturing images
                conn = mysql.connector.connect(
                    host="localhost", 
                    username="root", 
                    password="Yash1012108@", 
                    database="advanced_attendance_system"
                )
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "UPDATE student SET PhotoSample=%s WHERE ID=%s",
                    ("Yes", self.var_id.get())
                )
                conn.commit()
                conn.close()

                self.var_radio1.set("Yes")  # Update radio button to "Yes"
                messagebox.showinfo("Success", "Photos captured and status updated successfully!", parent=self.root)
                self.fetch_data()  # Refresh the table data

            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
