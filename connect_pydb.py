#!/usr/bin/python3
#! -*- encoding:Utf-8 -*-


from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import pymysql


class ConnectorDB:
    def __init__(self, root):
        self.root = root
        titlespace = ""
        self.root.title(102 * titlespace + "MySql Connection")
        self.root.geometry("800x700+300+0")
        self.root.resizable(width=False, height=False)

        MainFrame = Frame(self.root, bd=10, width=770, height=700, relief=RIDGE, bg='RoyalBlue3')
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd=7, width=770, height=100, relief=RIDGE)
        TitleFrame.grid(row=0, column=0)
        TopFrame3 = Frame(MainFrame, bd=5, width=770, height=500, relief=RIDGE)
        TopFrame3.grid(row=1, column=0)

        LeftFrame = Frame(TopFrame3, bd=5, width=600, height=400, padx=2, relief=RIDGE, bg='RoyalBlue3')
        LeftFrame.pack(side=LEFT)
        LeftFrame1 = Frame(LeftFrame, bd=5, width=600, height=180, padx=12, pady=9, relief=RIDGE)
        LeftFrame1.pack(side=TOP)

        RightFrame1 = Frame(TopFrame3, bd=5, width=100, height=400, padx=2, relief=RIDGE, bg="RoyalBlue3")
        RightFrame1.pack(side=RIGHT)
        RightFramelo = Frame(RightFrame1, bd=5, width=90, height=300, padx=2, pady=2, relief=RIDGE)
        RightFramelo.pack(side=TOP)

        #------------------

        StudentID = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        Address = StringVar()
        Gender = StringVar()
        Mobile = StringVar()

        #------------------

        def iExit():
            iExit = tkinter.messagebox.askyesno('MySQL connection', 'Confirm if you want to exit ?')
            if iExit > 0:
                root.destroy()
                return

        def Reset():
            self.entStudentID.delete(0, END)
            self.entFirstname.delete(0, END)
            self.entSurname.delete(0, END)
            self.entAddress.delete(0, END)
            Gender.set("")
            self.entMobile.delete(0, END)

        #------------------

        self.lbltitle = Label(TitleFrame, font=('arial', 40, 'bold'), text='MySQL Connection', bd=7)
        self.lbltitle.grid(row=0, column=0, padx=132)

        self.lblStudentID = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Student ID", bd=7)
        self.lblStudentID.grid(row=1, column=0, sticky=W, padx=5)
        self.entStudentID = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
            textvariable=StudentID)
        self.entStudentID.grid(row=1, column=1, sticky=W, padx=5)

        self.lblFirstname = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Firstname", bd=7)
        self.lblFirstname.grid(row=2, column=0, sticky=W, padx=5)
        self.entFirstname = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
            textvariable=Firstname)
        self.entFirstname.grid(row=2, column=1, sticky=W, padx=5)

        self.lblSurname = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Surname", bd=7)
        self.lblSurname.grid(row=3, column=0, sticky=W, padx=5)
        self.entSurname = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
            textvariable=Surname)
        self.entSurname.grid(row=3, column=1, sticky=W, padx=5)

        self.lblAddress = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Address", bd=7)
        self.lblAddress.grid(row=4, column=0, sticky=W, padx=5)
        self.entAddress = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
            textvariable=Address)
        self.entAddress.grid(row=4, column=1, sticky=W, padx=5)

        self.lblGender = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Gender", bd=7)
        self.lblGender.grid(row=5, column=0, sticky=W, padx=5)
        self.cboGender = ttk.Combobox(LeftFrame1, font=('arial', 12, 'bold'), width=43, state="readonly")
        self.cboGender['values'] = ('', 'Female', 'Male')
        self.cboGender.current(0)
        self.cboGender.grid(row=5, column=1, sticky=W, padx=5)

        self.lblMobile = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Mobile", bd=7)
        self.lblMobile.grid(row=6, column=0, sticky=W, padx=5)
        self.entMobile = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left',
            textvariable=Mobile)
        self.entMobile.grid(row=6, column=1, sticky=W, padx=5)

        #------------------ ok

        scroll_y=Scrollbar(LeftFrame, orient=VERTICAL)

        self.student_records=ttk.Treeview(LeftFrame, height=14, columns=("stdid",
            "firstname", "surname", "address", "gender", "mobile"),yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.student_records.heading("stdid", text="StudentID.")
        self.student_records.heading("firstname", text="Firstname")
        self.student_records.heading("surname", text="Surname")
        self.student_records.heading("address", text="Address")
        self.student_records.heading("gender", text="Gender")
        self.student_records.heading("mobile", text="Mobile")

        self.student_records['show']="headings"

        self.student_records.column("stdid", width=70)
        self.student_records.column("firstname", width=70)
        self.student_records.column("surname", width=70)
        self.student_records.column("address", width=70)
        self.student_records.column("gender", width=70)
        self.student_records.column("mobile", width=70)

        self.student_records.pack(fill=BOTH, expand=1)

        #------------------

        self.btnAddNew = Button(RightFramelo, font=('arial', 16, 'bold'), text="Add New", bd=4, 
            padx=24, pady=1, width=8, height=2).grid(row=0, column=0, padx=1)

        self.btnDisplay = Button(RightFramelo, font=('arial', 16, 'bold'), text="Display", bd=4, 
            padx=24, pady=1, width=8, height=2).grid(row=1, column=0, padx=1)

        self.btnUpdate = Button(RightFramelo, font=('arial', 16, 'bold'), text="Update", bd=4, 
            padx=24, pady=1, width=8, height=2).grid(row=2, column=0, padx=1)

        self.btnDelete = Button(RightFramelo, font=('arial', 16, 'bold'), text="Delete", bd=4, 
            padx=24, pady=1, width=8, height=2).grid(row=3, column=0, padx=1)

        self.btnSearch = Button(RightFramelo, font=('arial', 16, 'bold'), text="Search", bd=4, 
            padx=24, pady=1, width=8, height=2).grid(row=4, column=0, padx=1)

        self.btnReset = Button(RightFramelo, font=('arial', 16, 'bold'), text="Reset", bd=4, 
            padx=24, pady=1, width=8, height=2, command=Reset).grid(row=5, column=0, padx=1)

        self.btnExit = Button(RightFramelo, font=('arial', 16, 'bold'), text="Exit", bd=4, 
            padx=24, pady=1, width=8, height=2, command=iExit).grid(row=6, column=0, padx=1)

if __name__=='__main__':
    root = Tk()
    application = ConnectorDB(root)
    root.mainloop()
