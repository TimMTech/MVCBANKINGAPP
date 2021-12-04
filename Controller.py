import tkinter as tk
from RegisterPage import Register
from LoginPage import Login
from AccountPage import AccountDash

pages = {
    "RegisterPage": Register,
    "LoginPage": Login,
    "AccountPage": AccountDash
}


class Controller(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame("RegisterPage")

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
