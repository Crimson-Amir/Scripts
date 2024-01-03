import tkinter as tk
from tkinter import ttk
from web_scraping import Scrap
import re

english_currency = {
    "دلار": "Dollar",
    "یورو": "euro",
    "درهمامارات": "AED Emirates",
    "پوندانگلیس": "British pound",
    "لیرترکیه": "Turkish Lira",
    "فرانکسوئیس": "Switzerland Frank",
    "یوانچین": "Chinese Yuan",
    "ینژاپن(100ین)": "Japan Yen",
    "وونکرهجنوبی": "South Korean Won",
    "دلارکانادا": "Canadian Dollar",
    "دلاراسترالیا": "Australian dollar",
    "دلارنیوزیلند": "New Zealand Dollar",
    "دلارسنگاپور": "Singapore Dollar",
    "روپیههند": "Indian Rupee",
    "روپیهپاکستان": "Pakistani Rupee",
    "دینارعراق": "Iraqi Dinar",
    "پوندسوریه": "Syrian Pound",
    "افغانی": "Afghan",
    "کروندانمارک": "Danish Krone",
    "کرونسوئد": "Swedish Krona",
    "کروننروژ": "Norwegian Krone",
    "ریالعربستان": "Saudi Rial",
    "ریالقطر": "Qatar Rial",
    "ریالعمان": "Oman Rial",
    "دینارکویت": "Kuwaiti Dinar",
    "دیناربحرین": "Bahrain Dinar",
    "رینگیتمالزی": "Malaysian Ringgit",
    "باتتایلند": "Thai baht",
    "دلارهنگکنگ": "Hong Kong Dollar",
    "روبلروسیه": "Russian ruble",
    "مناتآذربایجان": "Azerbaijani Manat",
    "درامارمنستان": "Armenian Drama",
    "لاریگرجستان": "Georgia truck",
    "سومقرقیزستان": "Third Kyrgyzstan",
    "سامانیتاجیکستان": "Tajikistan Samani",
    "مناتترکمنستان": "Turkmenistan Manat",
}


class GUI(Scrap):
    def __init__(self):
        super().__init__('https://www.tgju.org/currency')
        self.root = tk.Tk()
        self.root.title("Rial Converter")
        self.root.geometry("500x600")
        self.tab_control = ttk.Notebook(master=self.root)

        self.tab_1 = ttk.Frame(self.tab_control, padding=10)
        self.tab_2 = ttk.Frame(self.tab_control, padding=10)

        self.tab_control.pack(expand=1, fill="both")
        self.c = self.get_currency()
        self.price_list = [f"{value['name'].replace(value['name'], english_currency[value['name'].replace(' ', '')])}: {value['price']} Rial" for value in self.c]

    def show_currency(self):
        self.tab_control.add(self.tab_1, text="Web Scraping")
        self.text_box = tk.Text(self.tab_1, height=20)
        self.text_box.pack(fill=tk.X)
        self.text_box.insert(tk.END, "\n".join(self.price_list))

        self.button_frame = tk.Frame(self.tab_1)
        self.button_frame.pack()

        self.entry = ttk.Entry(self.button_frame, width=30)
        self.entry.pack(pady=5, side="right")

        ttk.Button(self.button_frame, text="Refresh", command=self.refresh).pack(pady=5, padx=5, side="left")
        ttk.Button(self.button_frame, text="Search", command=self.search).pack(pady=5, padx=10, side="left")

        self.result_text_box = tk.Text(self.tab_1, height=10)
        self.result_text_box.pack(pady=5, fill=tk.X)

    def converter(self):
        self.tab_control.add(self.tab_2, text="Currency Convert")
        self.clicked = tk.StringVar()
        self.clicked.set("SELECT")

        self.frame_for_input = tk.Frame(self.tab_2)
        self.frame_for_input.pack()
        tk.Label(self.frame_for_input, text="input").pack(side="right", padx=7)
        self.rial = tk.Entry(self.frame_for_input, width=37)
        self.rial.pack()

        self.frame_for_convert = tk.Frame(self.tab_2)
        self.frame_for_convert.pack()

        self.button_conert = tk.Button(self.frame_for_convert, text="Convert", command=self.calculat)
        self.button_conert.pack(side="left", pady=5)
        self.button_conert.configure(width=10)

        self.drop = tk.OptionMenu(self.frame_for_convert, self.clicked, *self.price_list)
        self.drop.pack(side="left", pady=5, padx=2)
        self.drop.configure(width=25)

        self.frame_for_entry = tk.Frame(self.tab_2)
        self.frame_for_entry.pack()
        self.output = tk.Text(self.frame_for_entry, width=48)
        self.output.pack()
        self.output.configure(height=20)

        self.frame_for_butt = tk.Frame(self.tab_2)
        self.frame_for_butt.pack()

        self.button_clear = tk.Button(self.frame_for_butt, text="Clear", command=self.clear_text)
        self.button_clear.pack(side="left", pady=5)
        self.button_clear.configure(width=17)

        self.button_refresh = tk.Button(self.frame_for_butt, text="Refresh Currency", command=self.refresh)
        self.button_refresh.pack(side="left", pady=5, padx=2)
        self.button_refresh.configure(width=17)

    def refresh(self):
        self.c = self.get_currency()
        self.price_list = [f"{value['name'].replace(value['name'], english_currency[value['name'].replace(' ', '')])}: {value['price']} Rial" for value in self.c]
        self.text_box.delete("1.0", tk.END)
        self.text_box.insert(tk.END, "\n".join(self.price_list))

        self.drop['menu'].delete(0, 'end')
        for option in self.price_list:git push
            self.drop['menu'].add_command(label=option, command=tk._setit(self.clicked, option))

    def search(self):
        self.q = self.entry.get()
        self.res = [res for res in self.price_list if self.q in res.lower()]
        self.result_text_box.insert(tk.END, "\n".join(self.res))
        self.result_text_box.configure(fg="red")

    def clear_text(self):
        self.output.delete("1.0", tk.END)

    def calculat(self):
        self.user_input = int(self.rial.get())
        self.currency = re.findall(r'\d+', str(self.clicked.get()))
        self.end = "".join(self.currency)
        self.toman = int(self.end) / 10
        r = self.user_input * int(self.end)
        t = self.user_input * int(self.toman)
        self.converted = f"{r:,} R ({t:,})"
        self.output.insert(tk.END, f"{self.converted}\n")
