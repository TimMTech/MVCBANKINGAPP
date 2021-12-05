from tkinter import Frame, Label, Button
from tkinter import messagebox
from PIL import Image, ImageTk
from Observables import LARGE_FONT, MEDIUM_FONT
import tkinter as tk
import Database

"""
Finish the rest of AccountDash.  
Create Personal Details
Create Deposit
Create Withdraw
"""


class AccountDash(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.root = master
        self.database = Database.Accounts()
        self.root.title("Login Page")
        self.root.geometry("1250x700+0+0")
        self.root.config(bg='white')

        # ======Account Dash Frame=========
        frame3 = Frame(self.root, bg='white')
        frame3.place(x=480, y=100, width=700, height=500)

        # ========Right Image============
        self.img = Image.open("Images/investment.png")
        self.img = self.img.resize((400, 400))
        self.right = ImageTk.PhotoImage(self.img)
        self.panel = Label(self.root, image=self.right)
        self.panel.image = self.right
        self.panel.place(x=775, y=140, width=375, height=350)

        # ========Title==============
        Label(frame3, text="ACCOUNT DASHBOARD", font=LARGE_FONT, bg='white', fg='green').place(x=80, y=0)

        # -----------------------Row 1
        Label(frame3, text="Choose What's Right For You", font=MEDIUM_FONT, bg='white', fg='green').place(x=80, y=80)

        # =========Options==============
        Button(frame3, text="Personal Details", bd=0, cursor='hand2',
               command=lambda: self.personalDetails()).place(x=60, y=160, width=180)
        Button(frame3, text="Deposit", bd=0, cursor='hand2',
               command='').place(x=60, y=240, width=180)
        Button(frame3, text="Withdraw", bd=0, cursor='hand2',
               command='').place(x=60, y=320, width=180)
        Button(frame3, text="Sign Out", bd=0, cursor='hand2',
               command=lambda: self.successLogout()).place(x=60, y=400, width=180)

    def successLogout(self):
        messagebox.showinfo("Success", "Logged Out Successfully", parent=self.root)
        self.master.switch_frame("LoginPage")

    def personalDetails(self):
        pass
