from tkinter import Label, Frame, Entry, Button
from tkinter import IntVar, Checkbutton, CENTER, EXCEPTION
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from Observables import LARGE_FONT, MEDIUM_FONT, COMBOBOX_FONT
import tkinter as tk
import Database


class Register(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.root = master
        self.database = Database.Accounts()
        self.root.title("Register Page")
        self.root.geometry("1250x700+0+0")
        self.root.config(bg='white')

        # ===BG Image=====
        self.bg = ImageTk.PhotoImage(file="Images/background.png")
        Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # ===Left Image=====
        self.pic = Image.open("Images/bgimage.png")
        self.pic = self.pic.resize((300, 400))
        self.left = ImageTk.PhotoImage(self.pic)
        Label(self.root, image=self.left).place(x=0, y=0, width=400, height=700)
        left_txt = Label(self.root, text="BANKING APPLICATION", font=LARGE_FONT)
        left_txt.place(x=75, y=500)
        left_txt_author = Label(self.root, text="Beta by Tim Mukhamedov", font=MEDIUM_FONT)
        left_txt_author.place(x=110, y=550)

        # ===Register Frame=====
        frame1 = Frame(self.root, bg='white')
        frame1.place(x=480, y=100, width=700, height=500)

        Label(frame1, text="REGISTER HERE", font=LARGE_FONT, bg='white', fg='green').place(x=50, y=0)

        # ----------------------Row 1

        Label(frame1, text="First Name", font=MEDIUM_FONT, bg='white', fg='gray').place(x=50, y=50)
        self.txt_firstname = Entry(frame1, font=MEDIUM_FONT, bg='lightgray')
        self.txt_firstname.place(x=50, y=80, width=200)

        Label(frame1, text="Last Name", font=MEDIUM_FONT, bg='white', fg='gray').place(x=400, y=50)
        self.txt_lastname = Entry(frame1, font=MEDIUM_FONT, bg='lightgray')
        self.txt_lastname.place(x=400, y=80, width=200)

        # ----------------------Row 2

        Label(frame1, text="Contact No", font=MEDIUM_FONT, bg='white', fg='gray').place(x=50, y=120)
        self.txt_contact = Entry(frame1, font=MEDIUM_FONT, bg='lightgray')
        self.txt_contact.place(x=50, y=150, width=200)

        Label(frame1, text="Email", font=MEDIUM_FONT, bg='white', fg='gray').place(x=400, y=120)
        self.txt_email = Entry(frame1, font=MEDIUM_FONT, bg='lightgray')
        self.txt_email.place(x=400, y=150, width=200)

        # ----------------------Row 3

        Label(frame1, text="Security Question", font=MEDIUM_FONT, bg='white', fg='gray').place(x=50, y=190)

        self.cmb_quest = ttk.Combobox(frame1, font=COMBOBOX_FONT, state='readonly', justify=CENTER)
        self.cmb_quest['values'] = ("Select", "Your First Pet Name",
                                    "Your Birth Place",
                                    "Your Best Friend's Name")
        self.cmb_quest.place(x=50, y=220, width=200)
        self.cmb_quest.current(0)

        Label(frame1, text="Answer", font=MEDIUM_FONT, bg='white', fg='gray').place(x=400, y=190)
        self.txt_answer = Entry(frame1, font=MEDIUM_FONT, bg='lightgray')
        self.txt_answer.place(x=400, y=220, width=200)

        # ---------------------Row 4

        Label(frame1, text="Password", font=MEDIUM_FONT, bg='white', fg='gray').place(x=50, y=260)
        self.txt_password = Entry(frame1, font=MEDIUM_FONT, bg='lightgray', show='*')
        self.txt_password.place(x=50, y=290, width=200)

        Label(frame1, text="Confirm Password", font=MEDIUM_FONT, bg='white', fg='gray').place(x=400,
                                                                                              y=260)
        self.txt_confirm_password = Entry(frame1, font=MEDIUM_FONT, bg='lightgray', show='*')
        self.txt_confirm_password.place(x=400, y=290, width=200)

        # ----------Terms----------
        self.var_check = IntVar()
        Checkbutton(frame1, text="I Agree to Terms & Conditions", variable=self.var_check, onvalue=1, offvalue=0,
                    font=MEDIUM_FONT,
                    bg='white').place(x=50, y=360)

        Button(frame1, text="Register", bd=0, cursor='hand2',
               command=lambda: self.register()).place(x=50, y=430, width=180)
        Button(frame1, text="Sign In", bd=0, cursor='hand2',
               command=lambda: master.switch_frame("LoginPage")).place(x=400, y=430, width=180)

    def register(self):
        fields = [self.txt_firstname.get(),
                  self.txt_lastname.get(),
                  self.txt_contact.get(),
                  self.txt_email.get(),
                  self.cmb_quest.get(),
                  self.txt_answer.get(),
                  self.txt_password.get(),
                  self.txt_confirm_password.get()]
        for entries in fields:
            if entries == "":
                messagebox.showerror("Error", "All Fields Are Required", parent=self.root)
                return
            if self.txt_password.get() != self.txt_confirm_password.get():
                messagebox.showerror("Error", "Password Does Not Match", parent=self.root)
                return
            if self.var_check.get() == 0:
                messagebox.showerror("Error", "Please Agree to Terms & Conditions", parent=self.root)
                return
        try:
            self.database.file_save(self.txt_firstname.get(),
                                    self.txt_lastname.get(),
                                    self.txt_contact.get(),
                                    self.txt_email.get(),
                                    self.cmb_quest.get(),
                                    self.txt_answer.get(),
                                    self.txt_password.get())
            messagebox.showinfo("Success", "Registration Complete", parent=self.root)
            return

        except EXCEPTION as es:
            messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)
