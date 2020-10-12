import tkinter as tk
import os
import BruteForceIp as bfip


def checking_file():
    '''
    checking if a folder exists
    '''
    if not os.path.exists('screenshots'):
        os.mkdir("screenshots")


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.l1 = tk.Label(self)
        self.l1.config(text="Вводить в формате: 12.32.23.12\n или 12.32.23.0/24 для диапазона ip")
        self.l1.grid(row=1, column=0)

        self.ent = tk.Entry(self, width=35)
        self.ent.grid(row=2, column=0, ipadx=10, ipady=6, padx=10, pady=10)

        self.get_ip = tk.Button(self)
        self.get_ip["text"] = "Поиск"
        self.get_ip["command"] = self.start_working
        self.get_ip.grid(row=3, column=0, ipadx=93, ipady=6, padx=10, pady=10)

        self.open_file = tk.Button(self)
        self.open_file["text"] = "Показать скриншоты "
        self.open_file["command"] = self.open
        self.open_file.grid(row=4, column=0, ipadx=50, ipady=6, padx=10, pady=10)

        self.l2 = tk.Label(self)
        self.l2.grid(row=5, column=0)

    def open(self):
        '''
        opens the folder where screenshots are saved
        '''
        path = "screenshots"
        checking_file()
        os.startfile(os.path.realpath(path))

    def start_working(self):
        try:
            ip = self.ent.get()
            checking_file()
            bfip.brute_force_ip(ip)
            self.l2.config(text="Скрин сделан")
        except Exception as exception:
            print("что то пошло не так" + str(exception))


root = tk.Tk()
root.geometry("300x250")
app = Application(master=root)
app.mainloop()
