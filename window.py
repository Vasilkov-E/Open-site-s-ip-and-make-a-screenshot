import tkinter as tk
import os


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.ent = tk.Entry(self, width=35)
        self.ent.grid(row=1, column=0, ipadx=10, ipady=6, padx=10, pady=10)

        self.get_ip = tk.Button(self)
        self.get_ip["text"] = "Поиск"
        self.get_ip["command"] = self.start_working
        self.get_ip.grid(row=2, column=0, ipadx=93, ipady=6, padx=10, pady=10)

        self.open_file = tk.Button(self)
        self.open_file["text"] = "Показать скриншоты "
        self.open_file["command"] = self.open
        self.open_file.grid(row=3, column=0, ipadx=50, ipady=6, padx=10, pady=10)

    def open(self):
        path = "screenshots"
        os.startfile(os.path.realpath(path))

    def start_working(self):
        b = self.ent.get()
        print(str(b))


root = tk.Tk()
root.geometry("300x250")
app = Application(master=root)
app.mainloop()
