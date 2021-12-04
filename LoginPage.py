from tkinter import Frame, Label, Entry, Button
from tkinter import messagebox
from PIL import Image, ImageTk
from Observables import LARGE_FONT, MEDIUM_FONT
import tkinter as tk
import Database


class Login(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.root = master
        self.database = Database.Accounts()
        self.root.title("Login Page")
        self.root.geometry("1250x700+0+0")
        self.root.config(bg='white')

        # ======Login Frame==========
        frame2 = Frame(self.root, bg='white')
        frame2.place(x=480, y=100, width=700, height=500)

        # ======Right Panel Image========
        self.img = Image.open("Images/loginimage.png")
        self.img = self.img.resize((400, 400))
        self.right = ImageTk.PhotoImage(self.img)
        self.panel = Label(self.root, image=self.right)
        self.panel.image = self.right
        self.panel.place(x=775, y=140, width=375, height=375)

        # ========Title==========
        Label(frame2, text="LOGIN HERE", font=LARGE_FONT, bg='white', fg='green').place(x=80, y=0)

        # ------------------------Row 1

        Label(frame2, text="EMAIL ADDRESS", font=MEDIUM_FONT, bg='white', fg='gray').place(x=50, y=150)
        self.email = Entry(frame2, font=MEDIUM_FONT, bg='lightgray')
        self.email.place(x=50, y=180, width=200)

        # -------------------------Row 2

        Label(frame2, text="Password", font=MEDIUM_FONT, bg='white', fg='gray').place(x=50, y=250)
        self.txt_password = Entry(frame2, font=MEDIUM_FONT, bg='lightgray', show='*')
        self.txt_password.place(x=50, y=280, width=200)

        # ----------Login Success----------------
        Button(frame2, text="Sign In", bd=0, cursor='hand2',
               command=lambda: self.login()).place(x=250, y=430, width=180)
        Button(frame2, text="New Account?", bd=0, cursor='hand2',
               command=lambda: master.switch_frame("RegisterPage")).place(x=250, y=460, width=180)

    def login(self):
        fields = [self.email.get(),
                  self.txt_password.get()]
        for entries in fields:
            if entries == "":
                messagebox.showerror("Error", "All Fields Are Required", parent=self.root)
                return
            if self.database.file_read(self.email.get(), self.txt_password.get()):
                messagebox.showinfo("Success", "Logged In", parent=self.root)
                self.master.switch_frame("AccountPage")
                return
            messagebox.showinfo("Error", "Email or Password Does Not Match", parent=self.root)
            return
