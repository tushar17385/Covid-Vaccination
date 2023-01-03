# main form
from inspect import FrameInfo
from logging import root
import tkinter as tk
from tkinter import *

w = 1200
h = 650
class mainform:
    def __init__(self, master):
        self.master = master
        # ----------- CENTER FORM ------------- #
        # ws = self.master.winfo_screenwidth()
        # hs = self.master.winfo_screenheight()
        # x = (ws-w)
        # y = (hs-h)
        # self.master.geometry("%dx%d+%d+%d" % (w, h, x, y))
        self.master.geometry("1200x600")

        # ----------- MENU ------------- #

        self.frame = tk.Frame(self.master)
        self.menubar = Menu(self.frame)
        # self.products = Menu(self.menubar)
        # self.products.add_command(label="Add")
        # self.products.add_command(label="Edit")
        # self.products.add_command(label="Remove")

        # self.menubar.add_cascade(menu=self.products, label="Product")

        # self.categories = Menu(self.menubar)
        # self.categories.add_command(label="Add")
        # self.categories.add_command(label="Edit")
        # self.categories.add_command(label="Remove")

        # self.menubar.add_cascade(menu=self.categories, label="Category")

        self.frame.pack()

        # ------------------------------ #

        self.master.config(menu=self.menubar, bg="#ecf0f1")
        self.lbl = tk.Label(self.master, text='Vaccination Center', font=('verdana',15, 'bold'), fg='#2A2C2B',bg="#ecf0f1")
        self.lbl.place(rely=0.5, relx=0.2, anchor=CENTER)


    # mainframe = tk.Frame(root, width=w, height=h)
    # centerframe = tk.Frame(mainframe, width=w, height=h)
    # center_contentframe = tk.Frame(centerframe, padx=15, pady=15, highlightbackgroun='black', highlightcolor='black', highlightthickness=2)
    # vaccine_center = tk.Entry(FrameInfo, font=('Verdana',14), width=22)
    # vaccine_center.grid(row=0, column=1)

    # frame1= tk.frame
       
        