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

if __name__=='__main__':
    root = Tk()
    application = ConnectorDB(root)
    root.mainloop()