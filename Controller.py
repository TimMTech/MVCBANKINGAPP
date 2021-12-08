import tkinter as tk

import Database


from RegisterPage import Register
from LoginPage import Login
from AccountPage import AccountDash
from PersonalPage import PersonalDetails

pages = {
    "RegisterPage": Register,
    "LoginPage": Login,
    "AccountPage": AccountDash,
    "PersonalPage": PersonalDetails
}


class Controller(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame("RegisterPage")
        self.database = Database.Accounts()

    def switch_frame(self, page_name):
        cls = pages[page_name]
        new_frame = cls(master=self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.place()


if __name__ == '__main__':
    app = Controller()
    app.mainloop()
