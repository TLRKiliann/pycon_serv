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
        self.root.geometry("770x700+300+0")
        self.root.resizable(width=False, height=False)

        MainFrame = Frame(self.root, bd=10, width=770, height=False, relief=RIDGE, bg='RoyalBlue3')
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd=7, width=770, height=100, relief=RIDGE)
        TitleFrame.grid(row=0, column=0)
        TopFrame3 = Frame(MainFrame, bd=5, width=770, height=500, relief=RIDGE)
        TopFrame3.grid(row=1, column=0)

        LeftFrame = Frame(TopFrame3, bd=5, width=600, height=400, padx=2, relief=RIDGE, bg='RoyalBlue3')
        LeftFrame.pack(side=LEFT)
        LeftFrame1 = Frame(LeftFrame, bd=5, width=600, height=180, padx=2, relief=RIDGE)
        LeftFrame1.pack(side=TOP, padx=0, pady=0)

        RightFrame1 = Frame(TopFrame3, bd=5, width=100, height=400, padx=2, relief=RIDGE, bg="RoyalBlue3")
        RightFrame1.pack(side=RIGHT)
        RightFramelo = Frame(RightFrame1, bd=5, width=90, height=300, padx=2, pady=2, relief=RIDGE)
        RightFramelo.pack(side=TOP)
        #------------------
        self.lbltitle = Label(TitleFrame, font=('arial', 40, 'bold'), text='MySQL Connection', bd=7)
        self.lbltitle.grid(row=0, column=0, padx=132)

        self.lblStudentID = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Student ID", bd=7)
        self.lblStudentID.grid(row=1, column=0, sticky=W, padx=5)
        self.entStudentID = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left')
        self.entStudentID.grid(row=1, column=1, sticky=W, padx=5)

        self.lblFirstname = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Firstname", bd=7)
        self.lblFirstname.grid(row=2, column=0, sticky=W, padx=5)
        self.entFirstname = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left')
        self.entFirstname.grid(row=2, column=1, sticky=W, padx=5)

        self.lblSurname = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Surname", bd=7)
        self.lblSurname.grid(row=3, column=0, sticky=W, padx=5)
        self.entSurname = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left')
        self.entSurname.grid(row=3, column=1, sticky=W, padx=5)

        self.lblAddress = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Address", bd=7)
        self.lblAddress.grid(row=4, column=0, sticky=W, padx=5)
        self.entAddress = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left')
        self.entAddress.grid(row=4, column=1, sticky=W, padx=5)

        self.lblGender = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Gender", bd=7)
        self.lblGender.grid(row=5, column=0, sticky=W, padx=5)
        self.cboGender = ttk.Combobox(LeftFrame1, font=('arial', 12, 'bold'), width=42, state="readonly")
        self.cboGender['values'] = ('', 'Female', 'Male')
        self.cboGender.current(0)
        self.cboGender.grid(row=5, column=1, sticky=W, padx=5)

        self.lblMobile = Label(LeftFrame1, font=('arial', 12, 'bold'), text="Mobile", bd=7)
        self.lblMobile.grid(row=6, column=0, sticky=W, padx=5)
        self.entMobile = Entry(LeftFrame1, font=('arial', 12, 'bold'), bd=5, width=44, justify='left')
        self.entMobile.grid(row=6, column=1, sticky=W, padx=5)


        #------------------



        scroll_y=Scrollbar(LeftFrame, orient=VERTICAL)

        self.student_records=ttk.Treeview(LeftFrame, height=12, columns=("stdid",
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

if __name__=='__main__':
    root = Tk()
    application = ConnectorDB(root)
    root.mainloop()
