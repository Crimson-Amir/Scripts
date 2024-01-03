import os
import tkinter as tk
from tkinter import ttk, filedialog


class CleanName:
    def __init__(self, path):
        self.folder_path = path
        self.file_names = os.listdir(self.folder_path)

    def remove_from_name(self, text):
        try:
            for file in self.file_names:
                file_name = file
                for text_ in text:
                    file_name = file_name.replace(text_, '')
                os.rename(file, file_name)
            return 'OK'
        except Exception as e:
            print(e)
            return e
        finally:
            self.file_names = os.listdir(self.folder_path)

    def clean_dot(self):
        try:
            for file in self.file_names:
                last_dot = file.rindex('.')
                file_name_clean = file[:last_dot].replace('.', ' ') + file[last_dot:]
                os.rename(file, file_name_clean)
            return 'OK'
        except Exception as e:
            print(e)
            return e
        finally:
            self.file_names = os.listdir(self.folder_path)

    def return_camel_case(self):
        try:
            for file in self.file_names:
                os.rename(file, file.capitalize())
            return 'OK'
        except Exception as e:
            print(e)
            return e
        finally:
            self.file_names = os.listdir(self.folder_path)


class GUI:
    def __init__(self):
        self.path = '.'
        self.root = tk.Tk()
        self.root.title('Name Cleaner')
        self.root.geometry('200x300')

        self.button_directory = tk.Button(self.root, text='choice dir', borderwidth=1, command=self.askfordir)
        self.button_directory.pack(pady=20)

        self.var1 = tk.StringVar()
        self.var2 = tk.StringVar()

        self.lable1 = tk.Label(self.root, text="remove from names: ")
        self.lable1.pack()

        self.rfn = tk.Entry(self.root)
        self.rfn.pack()

        self.replace_dot = ttk.Checkbutton(self.root, text='Replace the dot with space', variable=self.var1, onvalue=1, offvalue=0)
        self.replace_dot.pack()
        self.cammel_case = ttk.Checkbutton(self.root, text='Convert names to camelcase', variable=self.var2, onvalue=1, offvalue=0)
        self.cammel_case.pack()

        self.commit = tk.Button(self.root, text='start clean', borderwidth=1, command=self.start)
        self.commit.pack(pady=20)

        self.root.mainloop()

    def start(self):
        self.clean = CleanName(self.path)
        if self.rfn.get():
            self.clean.remove_from_name([self.rfn.get()])
            print(f'remove {self.rfn.get()} from names!')
        if self.var1.get():
            self.clean.clean_dot()
            print(f'clean dots from names!{self.var1.get()}')
        if self.var2.get():
            self.clean.return_camel_case()
            print(f'names now cammelcase! {self.var2.get()}')
        tk.messagebox.showinfo(title='Done', message='Names Clean!')

    def askfordir(self):
        self.directory = filedialog.askdirectory()
        self.path = self.directory
        self.lable = tk.Label(self.root, text=self.directory, borderwidth=1)
        self.lable.pack()


a = GUI()
