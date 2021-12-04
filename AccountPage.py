from tkinter import Frame, Label, Entry, Button
from tkinter import messagebox
from PIL import Image, ImageTk
from Observables import LARGE_FONT, MEDIUM_FONT
import tkinter as tk
import Database


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

