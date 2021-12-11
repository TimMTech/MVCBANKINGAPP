from tkinter import Frame, Label, Button
from PIL import Image, ImageTk
from Observables import LARGE_FONT, MEDIUM_FONT
import tkinter as tk
import os


class PersonalDetails(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.root = master
        self.root.title("Personal Details")
        self.root.geometry("1250x700+0+0")
        self.root.config(bg='white')

        # ======Personal Frame==========
        frame4 = Frame(self.root, bg='white')
        frame4.place(x=480, y=100, width=700, height=500)

        # ===Left Image=====
        self.pic = Image.open("Images/bgimage.png")
        self.pic = self.pic.resize((300, 400))
        self.left = ImageTk.PhotoImage(self.pic)
        Label(self.root, image=self.left).place(x=0, y=0, width=400, height=700)
        left_txt = Label(self.root, text="BANKING APPLICATION", font=LARGE_FONT)
        left_txt.place(x=75, y=500)
        left_txt_author = Label(self.root, text="Beta by Tim Mukhamedov", font=MEDIUM_FONT)
        left_txt_author.place(x=110, y=550)

        # ======Right Panel Image========
        self.img = Image.open("Images/loginimage.png")
        self.img = self.img.resize((400, 400))
        self.right = ImageTk.PhotoImage(self.img)
        self.panel = Label(self.root, image=self.right)
        self.panel.image = self.right
        self.panel.place(x=775, y=140, width=375, height=375)

        # FILE HANDLER
        account_active = self.master.data["email"].get()
        path = '/Users/tim/PycharmProjects/MVCBANKINGAPP/Accounts/'
        file_name = account_active + ".txt"
        complete_name = os.path.join(path, file_name)
        with open(complete_name, 'r') as f:
            data = f.read()
            details = data.split('\n')
            firstname = details[0]
            lastname = details[1]
            contact = details[2]
            email = details[3]

        # =============Title===============
        Label(frame4, text="PERSONAL INFORMATION", font=LARGE_FONT, bg='white', fg='green').place(x=80, y=0)

        # -------------------------------Row 1
        Label(frame4, text="First Name", font=MEDIUM_FONT, bg='white', fg='green').place(x=50, y=30)
        Label(frame4, text=firstname, font=MEDIUM_FONT, bg='white', fg='black').place(x=50, y=50)

        # -------------------------------Row 2
        Label(frame4, text="Last Name", font=MEDIUM_FONT, bg='white', fg='green').place(x=50, y=130)
        Label(frame4, text=lastname, font=MEDIUM_FONT, bg='white', fg='black').place(x=50, y=150)

        # -------------------------------Row 3
        Label(frame4, text="Contact Number", font=MEDIUM_FONT, bg='white', fg='green').place(x=50, y=230)
        Label(frame4, text=contact, font=MEDIUM_FONT, bg='white', fg='black').place(x=50, y=250)

        # -------------------------------Row 4
        Label(frame4, text="Email", font=MEDIUM_FONT, bg='white', fg='green').place(x=50, y=330)
        Label(frame4, text=email, font=MEDIUM_FONT, bg='white', fg='black').place(x=50, y=350)

        # ===========Options===============
        Button(frame4, text="Previous", bd=0, cursor='hand2',
               command=lambda: self.master.switch_frame("AccountPage")).place(x=400, y=430, width=180)
