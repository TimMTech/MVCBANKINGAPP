from tkinter import Frame, Label, Button
from PIL import Image, ImageTk
from Observables import LARGE_FONT, MEDIUM_FONT
import tkinter as tk
import Database


class PersonalDetails(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.root = master
        self.database = Database.Accounts()
        self.root.title("Personal Details")
        self.root.geometry("1250x700+0+0")
        self.root.config(bg='white')

        # ======Login Frame==========
        frame4 = Frame(self.root, bg='white')
        frame4.place(x=480, y=100, width=700, height=500)

        # ======Right Panel Image========
        self.img = Image.open("Images/loginimage.png")
        self.img = self.img.resize((400, 400))
        self.right = ImageTk.PhotoImage(self.img)
        self.panel = Label(self.root, image=self.right)
        self.panel.image = self.right
        self.panel.place(x=775, y=140, width=375, height=375)

        # =============Title===============
        Label(frame4, text="PERSONAL INFORMATION", font=LARGE_FONT, bg='white', fg='green').place(x=80, y=0)

        # -------------------------------Row 1
        Label(frame4, text="First Name", font=MEDIUM_FONT, bg='white', fg='gray').place(x=50, y=50)

        # -------------------------------Row 2
        Label(frame4, text="Last Name", font=MEDIUM_FONT, bg='white', fg='gray').place(x=50, y=150)

        # -------------------------------Row 3
        Label(frame4, text="Contact", font=MEDIUM_FONT, bg='white', fg='gray').place(x=50, y=250)

        # -------------------------------Row 4
        Label(frame4, text="Email", font=MEDIUM_FONT, bg='white', fg='gray').place(x=50, y=350)

        # ===========Options===============
        Button(frame4, text="Previous", bd=0, cursor='hand2',
               command=lambda: self.master.switch_frame("AccountPage")).place(x=400, y=430, width=180)
