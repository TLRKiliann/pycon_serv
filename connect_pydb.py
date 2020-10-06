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

        MainFrame = Frame(self.root, bd=10, width=770, height=False)



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