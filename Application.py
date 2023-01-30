# Front-End of Application

import customtkinter as ctk 
import tkinter
from tkinter import *
from PIL import Image, ImageTk
from backend import  Database
from tkinter import messagebox as tm
import random

database = Database("books.db")

bb=['red','black','blue2','purple','dark green','blue','maroon1','green2']
cc=random.choice(bb)

cursors=["circle","clock","cross","dotbox","plus","spider","star"]
cd=random.choice(cursors)


class Window(object):
    def __init__(self,window):
        
        self.window = window
        
        self.window.geometry('1080x600')
 
        
        # ctk.set_appearance_mode("green")
        # ctk.set_default_color_theme("dark-blue")
        
        self.window.wm_title("Sachin's Library")
        
        frame = ctk.CTkFrame(master = window)

        frame.pack(pady=15,padx=15, fill="both", expand=True)
        '''
        label = ctk.CTkLabel(master=frame, text="Login System")
        label.pack(pady=12,padx=10)
        '''
    # Setting the College/School Logo
        
        image = Image.open("images/logo.png")
        photo = ImageTk.PhotoImage(image)
        
        label = Label(image=photo,width=230,height=150) 
        label.image = photo # keep a reference!
        label.place(x=750, y=40)
                
    # Different Labels of Application

        l0 = Label(window, text = "MY UNIVERSITY Name", width="25",height="2",
                    font=('Helvetica',20),bg='red',fg='white')
        l0.place(x=140,y=50)


        lb1 = Label(window, text = "Welcome To Sachin's Library", width="35",height="1",
                    font=('Helvetica',20),bg='Blue',fg='Yellow')
        lb1.place(x=80,y=140)        

        l1 = Label(window, text = "Book's Title", width=15,fg=cc,
                    font=("bold",14),justify=RIGHT)
        l1.place(x=80,y=250)
        
        self.Title_text = StringVar()
        self.e1 = Entry(window,width=25 ,font=('bold',13),textvariable=self.Title_text)
        self.e1.place(x=300,y=250)

        l2 = Label(window, text = "Author Name", width=15,fg=cc,
                    font=("bold",14),justify=RIGHT)
        l2.place(x=80,y=300)
        
        self.Author_text = StringVar()
        self.e2 = Entry(window,width=25,font=('bold',13),textvariable=self.Author_text)
        self.e2.place(x=300,y=300)       

        l3 = Label(window, text = "Year",fg=cc,
                    width=10, font=("bold",14),justify=RIGHT)
        l3.place(x=80,y=350)
        
        self.Year_text = StringVar()
        self.e3 = Entry(window, font=('bold',13),textvariable=self.Year_text)
        self.e3.place(x=300,y=350)        
        
        l4 = Label(window, text = "Price", width=10,fg=cc,
                    font=("bold",14),justify=RIGHT)
        l4.place(x=80,y=400)

        self.PRICE_text = StringVar()
        self.e4= Entry(window, font=('bold',13),textvariable=self.PRICE_text)
        self.e4.place(x=300,y=400)

        
    # ListBox of Entries
        
        self.list1 = Listbox(window, height=14,	cursor=cd ,width=32,bg="pale green",
                             selectbackground="green" ,
                             fg='red',font=('bold',15,))
        self.list1.place(x=650,y=220)

        self.list1.bind('<<ListboxSelect>>', self.get_selected_row)

    # now we need to attach a Scrollbar to the Listbox, and the other direction,too

    # Horizontal Scrollbar
        sb1 = Scrollbar(window)
        sb1.place(x=1008,y=525)
        self.list1.config(yscrollcommand=sb1.set)
        sb1.config(command=self.list1.yview)

    # Vertical Scrollbar
        sb2 = Scrollbar(window,orient=HORIZONTAL)
        sb2.place(x=955,y=560)
        self.list1.config(xscrollcommand=sb2.set)
        sb2.config(command=self.list1.xview)
        

    # Command Buttons of Applications 

        b4 = Button(window, text="Update selected",bg='cyan',font=('bold',12),relief=RAISED,
                    width=15,command=self.update_command )
        b4.place(x=80,y=470)

        b2 = Button(window, text="Search entry",bg='yellow',font=('bold',12),
                    width=15,command=self.search_command)
        b2.place(x=270,y=470)

    # Alert Box of New Entry
        def AddEntry():
            MsgBox = tm.askquestion ('Add New Entry','Are you sure you want to Add new Entry of this book',icon = 'warning')
            if MsgBox == 'yes':
               command = self.add_command()
        b3 = Button(window, text="Add entry",bg='orchid1',font=('bold',12),relief=RAISED,
                    width=15,command = AddEntry )
        b3.place(x=450,y=470)

        b1 =Button(window, text="View all",bg='green2',font=('bold',12),
                   width=15,command=self.view_command )
        b1.place(x=80,y=520)

    # Alert Box for Deleting Entry
        def Del():
            MsgBox = tm.askquestion ('Delete Entry','Are you sure you want to Remove the Entry of this book',icon = 'warning')
            if MsgBox == 'yes':
               command = self.delete_command()
        b5 = Button(window, text="Delete selected", bg='light blue',font=('bold',12),relief=RAISED,
                    width=15,command=Del)
        b5.place(x=270,y=520)


        # Different Fuctions assigned to each buttons above
        
        def Src():
            MsgBox = tm.showinfo ('Exit Application','Are you sure you want to exit the application',)
        
        def ExitApp():
            MsgBox = tm.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
            if MsgBox == 'yes':
               window.destroy()
        b6 = Button(window, text="Exit", bg='OliveDrab1',font=('purple',12),width=15,command=ExitApp)
        b6.place(x=450,y=520)

    def get_selected_row(self,event):   #the "event" parameter is needed b/c we've binded this function to the listbox
        try:
            index = self.list1.curselection()[0]
            self.selected_tuple = self.list1.get(index)
            self.e1.delete(0,END)
            self.e1.insert(END,self.selected_tuple[1])
            self.e2.delete(0, END)
            self.e2.insert(END,self.selected_tuple[2])
            self.e3.delete(0, END)
            self.e3.insert(END,self.selected_tuple[3])
            self.e4.delete(0, END)
            self.e4.insert(END,self.selected_tuple[4])
        except IndexError:
            pass                #in the case where the listbox is empty, the code will not execute

    def view_command(self):
        self.list1.delete(0, END)  # make sure we've cleared all entries in the listbox every time we press the View all button
        for row in database.view():
            self.list1.insert(END, row)

    def search_command(self):
        self.list1.delete(0, END)
        for row in database.search(self.Title_text.get(), self.Author_text.get(),self.Year_text.get(), self.PRICE_text.get()):
            self.list1.insert(END, row)

    def add_command(self):
        database.insert(self.Title_text.get(), self.Author_text.get(),self.Year_text.get(), self.PRICE_text.get())
        self.list1.delete(0, END)
        self.list1.insert(END, (self.Title_text.get(), self.Author_text.get(),self.Year_text.get(), self.PRICE_text.get()))

    def delete_command(self):
        database.delete(self.selected_tuple[0])
        self.view_command()

    def update_command(self):
        #be careful for the next line ---> we are updating using the texts in the entries, not the selected tuple
        database.update(self.selected_tuple[0],self.Title_text.get(), self.Author_text.get(), self.Year_text.get(), self.PRICE_text.get())
        self.view_command()

#code for the GUI (front end)
        
window = ctk.CTk()
window.iconbitmap("images/appLogo.png")
Window(window)
window.mainloop()

