# main form
from inspect import FrameInfo
from logging import root
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import mysql.connector

connection = mysql.connector.connect(host='localhost', user='root', port='3306', password='', database='covid')
c = connection.cursor()

w = 1200
h = 650
class mainform:
    # headerframe = tk.Frame(root, highlightbackgroun='black', highlightcolor='black', highlightthickness=2, bg='#3E71BB', width=w, height=70)
    # close_button = tk.Button(headerframe, text='x', borderwidth=1, relief='solid', font=('Verdana',12))
    # headerframe.pack()
    # close_button.pack()
    # close_button.place(x=410, y=10)
    # def close_win():
    #     root.destroy()
    # close_button['command'] = close_win



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

        # self.frame = tk.Frame(self.master)
        # self.menubar = Menu(dself.frame)
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

        

        # ------------------------------ #

        # # self.master.config(menu=self.menubar, bg="#ecf0f1")
        # self.center = tk.Frame(self.master)
        # self.regi = tk.Frame(self.master, width=w, height=h)
        # self.lbl = tk.Label(self.master, text='Vaccination Center', font=('verdana',15, 'bold'), fg='#2A2C2B',bg="#ecf0f1")
        # self.lbl.place(rely=0.5, relx=0.2, anchor=CENTER)
        # self.lbl1 = tk.Entry(self.master, font=('Verdana',16))
        # self.lbl1.place(rely=0.5, relx=0.5, anchor=CENTER)
        # # self.lbl1.grid(row=0, column=0, pady=10)
        # # self.lbl1.grid(row=0, column=1)
        # search_button = tk.Button(self.master,text="Search",font=('Verdana',16), padx=25, pady=10, width=25)
        # search_button.place(rely=0.8, relx=0.5, anchor=CENTER)
        # # search_button.grid(row=2, column=0, columnspan=2, pady=40)
    
        # def center(frame):
        #     frame.tkraise()    
        #     name = self.lbl1.get().strip()
        #     vals = (name,)
        #     select_query = "SELECT * FROM `vaccinationcenter` WHERE `name` = %s"
        #     c.execute(select_query, vals)
        #     # vaccenter = c.fetchone()
        #     # if vaccenter is not None:
                

                

        #     else:
        #         messagebox.showwarning('Error','wrong Center name')

        # search_button['command'] = center
        # self.master.pack()

        
        self.registerframe = tk.Frame(self.master, width=w, height=h)

        # self.register_contentframe = tk.Frame(self.registerframe, padx=15, pady=15, highlightbackgroun='black', highlightcolor='black', highlightthickness=2)

        name_label_rg = tk.Label(self.registerframe, text='Name:', font=('Verdana',14) )
        phone_label_rg = tk.Label(self.registerframe, text='Phone:', font=('Verdana',14))
        gender_label_rg = tk.Label(self.registerframe, text='Gender:', font=('Verdana',14) )
        
        name_entry_rg = tk.Entry(self.registerframe, font=('Verdana',14), width=22)
        phone_entry_rg = tk.Entry(self.registerframe, font=('Verdana',14), width=22)


        center_label_rg = tk.Label(self.registerframe, text='Vaccination Center:', font=('Verdana',14) )
        radiosframe = tk.Frame(self.registerframe)
        center = StringVar()
        center.set('solapur')
        solapur_radiobutton = tk.Radiobutton(radiosframe, text='solapur', font=('Verdana',14),  variable=center, value='solapur')
        sangli_radiobutton = tk.Radiobutton(radiosframe, text='sangli', font=('Verdana',14),  variable=center, value='sangli')
        center_label_rg.grid(row=6, column=0, pady=6, sticky='e')
        radiosframe.grid(row=6, column=1)
        solapur_radiobutton.grid(row=0, column=0)
        sangli_radiobutton.grid(row=0, column=1)



        radiosframe = tk.Frame(self.registerframe)
        gender = StringVar()
        gender.set('Male')
        male_radiobutton = tk.Radiobutton(radiosframe, text='Male', font=('Verdana',14),  variable=gender, value='Male')
        female_radiobutton = tk.Radiobutton(radiosframe, text='Female', font=('Verdana',14),  variable=gender, value='Female')

        register_button = tk.Button(self.registerframe,text="Register For Vaccine", font=('Verdana',16), bg='#2980b9',fg='#fff', padx=25, pady=10, width=25)

        #mainframe.pack(fill='both', expand=1)
        #registerframe.pack(fill='both', expand=1)
        self.registerframe.pack(fill='both', expand=1)

        name_label_rg.grid(row=0, column=0, pady=5, sticky='e')
        name_entry_rg.grid(row=0, column=1)

        phone_label_rg.grid(row=4, column=0, pady=5, sticky='e')
        phone_entry_rg.grid(row=4, column=1)

        gender_label_rg.grid(row=5, column=0, pady=5, sticky='e')
        radiosframe.grid(row=5, column=1)
        male_radiobutton.grid(row=0, column=0)
        female_radiobutton.grid(row=0, column=1)


        register_button.grid(row=7, column=0, columnspan=2, pady=20)

#------------------------Check if name already exist--------------------#
        # def check_username(name):
        #     name = name_entry_rg.get().strip()
        #     vals = (name,)
        #     select1_query = "SELECT * FROM `registration1` WHERE `name` = %s"
        #     c.execute(select1_query, vals)
        #     name = c.fetchone()
        #     if name is not None:
        #         return True
        #     else:
        #         return False

        def register():
            # reg_max = c.execute("SELECT MAX(regi_no) AS reg_max FROM `registration1`")
            name = name_entry_rg.get().strip() # remove white space
            phone = phone_entry_rg.get().strip()
            gdr = gender.get()
            gdr1 = center.get()
            
            
            
            if len(name) > 0 and len(phone) > 0:
                # if check_username(name) == False: 
                    vals = (name, phone, gdr, gdr1)
                    insert_query = "INSERT INTO `registration1`(`name`,`phone`,`gender`,`center`) VALUES (%s,%s,%s,%s)"
                    # select_query = "SELECT MAX(regi_no) AS reg_max  FROM registration1"
                    # c.execute(select_query)
                    c.execute(insert_query, vals)
                    # name = c.fetchone()
                    # if name is not None:
                    connection.commit()
                    messagebox.showinfo('Register','your registration has been done successfully')
                    # else:
                    #     messagebox.showwarning('Error','wrong name')
                # else:
                #     messagebox.showwarning('Duplicate Username','This Name Already Exists, try another one')
            else:
                messagebox.showwarning('Empty Fields','make sure to enter all the information')
        
        register_button['command'] = register




       








        # def check_centername(vaccenter):
        #     vaccenter = self.lbl1.get().strip()
        #     vals = (self.lbl1,)
        #     select_query = "SELECT * FROM `vaccinationcenter` WHERE `name` = %s"
        #     c.execute(select_query, vals)
        #     vaccenter = c.fetchone()
        #     if vaccenter is not None:
        #         return True
        #     else:
        #         return False


        # if check_centername(self.lbl1) == False: 
        #     # vals = (self.lbl1)
        #     # insert_query = "INSERT INTO `vaccinationcenter`"
        #     # c.execute(insert_query, vals)
        #     connection.commit()
        #     messagebox.showinfo('Register','Center Found Successfully')
        # else:
        #     messagebox.showwarning('Duplicate center','Try Another Center')   

   
    #    def Search():
    #         self.frame.forget()
    #         registerframe.pack(fill="both", expand=1)
    #         title_label['text'] = 'Register'
    #         title_label['bg'] = '#27ae60'
        # registerframe = tk.Frame(mainframe, width=w, height=h)
        # self.register_contentframe = tk.Frame(registerframe, padx=15, pady=15, highlightbackgroun='black', highlightcolor='black', highlightthickness=2, )


    #     go_register_label.bind("<Button-1>", lambda page: Search())
       
       
       
