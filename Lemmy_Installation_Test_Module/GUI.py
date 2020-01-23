import tkinter as tk
from tkinter import ttk
from CaseCreator import CaseCreator


class GUI:

    def __init__(self):
        self.master = tk.Tk()
        self.master.title('Test av ledningsägarmodul')
        self.master.geometry('500x300')
        self.label_style = ttk.Style()
        self.label_style.configure("BW.TLabel", foreground="black", background="white")
        self.button_style = ttk.Style()
        self.button_style.configure('W.TButton', font=('calibri', 10, 'bold', 'underline'), foreground='red')
        tk.Label(self.master, text="Url till ledningsägarmodul: ").grid(row=0)
        tk.Label(self.master, text="Användarnamn: ").grid(row=1)
        tk.Label(self.master, text="Lösenord: ").grid(row=2)

        self.base_url_input = tk.Entry(self.master)

        self.selected_base_url = tk.StringVar(self.master)
        self.default_value = self.selected_base_url.set("https://test.ledningskollen.se/ella/api/v4/")

        self.base_url_selector = tk.OptionMenu(self.master, self.default_value,
                                               "https://test.ledningskollen.se/ella/api/v2/",
                                               "https://test.ledningskollen.se/ella/api/v3/").grid(row=0, column=1)

        self.username_entry = tk.Entry(self.master)
        self.password_input = tk.Entry(self.master, show="*")

        #self.base_url_input.grid(row=0, column=1)
        self.username_entry.grid(row=1, column=1)
        self.password_input.grid(row=2, column=1)

        self.close_button = tk.Button(self.master, text='Stäng',  command=self.master.quit) \
            .grid(row=3, column=0,
                  sticky=tk.W,
                  pady=4)
        self.run_test_button = tk.Button(self.master, text='Generera Test',
                                         command=lambda: self.generate_test(self.selected_base_url.get(),
                                                                            self.username_entry.get(),
                                                                            self.password_input.get())).grid(row=3,
                                                                                                             column=1,
                                                                                                             sticky=tk.W,
                                                                                                             pady=4)
        self.output_window = tk.Text(self.master, height=10, width=70).grid(row=4, column=2)

        tk.mainloop()

    def generate_test(self, base_url, username, password):
        if base_url == '':
            print('base url is required!')
        elif username == '':
            print('username is required!')
        elif password == '':
            print('password is required!')
        else:
            cases = CaseCreator(base_url=base_url, username=username, password=password)
            return cases
