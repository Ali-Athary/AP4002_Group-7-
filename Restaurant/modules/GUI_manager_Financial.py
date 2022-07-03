import tkinter
from tkinter import font, ttk
from PIL import ImageTk, Image  
import os
import sys
import jdatetime

class Item_UI_images():
    def __init__(self) -> None:
        header_img = Image.open(os.path.join(sys.path[0], "resources\panels\\history_item_header.png")).convert("RGBA")
        self.header  = ImageTk.PhotoImage(header_img)
        
class Information_panel(tkinter.Label):
    def __init__(self, root, color_palette):
        self.color_palette = color_palette
        img = Image.open(os.path.join(sys.path[0], "resources\panels\\simple_panel.png")).convert("RGBA")
        image = ImageTk.PhotoImage(img)

        super().__init__(root, image=image, bg=color_palette[4], bd=0)
        self.image = image

        self.ui_images = Item_UI_images()

        font1 = font.Font(family="Mj_Flow", size=19)
        font2 = font.Font(family="Dast Nevis", size=19)
        font_English = font.Font(family="Roboto", size=18)

        # general info

        info_frame = tkinter.Frame(self, width=990, height=160, bg=self.color_palette[4],
         highlightbackground=self.color_palette[2], highlightthickness=2)
        info_frame.pack_propagate(0)
        info_frame.place(x=20, y=20)

        information_frame  = tkinter.Frame(info_frame, width=990, height=160, bg=self.color_palette[4], highlightthickness=0)
        information_frame.pack(expand=True, fill="none")

        #date()

        date_frame = tkinter.Frame(information_frame, width=480, height=48, bg=self.color_palette[4])
        date_frame.pack_propagate(0)
        date_frame.grid(row=0, column=1, pady=2, padx=0)
        tkinter.Label(date_frame, text="تاریخ", font=font1, bg=self.color_palette[4]).pack(side=tkinter.RIGHT, padx=4)
        tkinter.Label(date_frame, text=":", font=font1, bg=self.color_palette[4]).pack(side=tkinter.RIGHT, padx=4)
        tkinter.Label(date_frame, text="1401/04/012", font=font2, bg=self.color_palette[4]).pack(side=tkinter.RIGHT, padx=4)

        # price

        price_frame = tkinter.Frame(information_frame, width=480, height=48, bg=self.color_palette[4])
        price_frame.pack_propagate(0)
        price_frame.grid(row=1, column=1, pady=2, padx=0)
        tkinter.Label(price_frame, text="هزینه تمام شده برای رستوران", font=font1, bg=self.color_palette[4]).pack(side=tkinter.RIGHT, padx=4)
        tkinter.Label(price_frame, text=":", font=font1, bg=self.color_palette[4]).pack(side=tkinter.RIGHT, padx=4)
        tkinter.Label(price_frame, text="236،217", font=font2, bg=self.color_palette[4]).pack(side=tkinter.RIGHT, padx=4)
        tkinter.Label(price_frame, text="تومان", font=font2, bg=self.color_palette[4]).pack(side=tkinter.RIGHT, padx=4)

        # discaount

        discaount_frame = tkinter.Frame(information_frame, width=480, height=48, bg=self.color_palette[4])
        discaount_frame.pack_propagate(0)
        discaount_frame.grid(row=1, column=0, pady=2, padx=0)
        tkinter.Label(discaount_frame, text="میزان تخفیف کل", font=font1, bg=self.color_palette[4]).pack(side=tkinter.RIGHT, padx=4)
        tkinter.Label(discaount_frame, text=":", font=font1, bg=self.color_palette[4]).pack(side=tkinter.RIGHT, padx=4)
        tkinter.Label(discaount_frame, text="25،000", font=font2, bg=self.color_palette[4]).pack(side=tkinter.RIGHT, padx=4)
        tkinter.Label(discaount_frame, text="تومان", font=font2, bg=self.color_palette[4]).pack(side=tkinter.RIGHT, padx=4)

        # final price

        final_price_frame = tkinter.Frame(information_frame, width=480, height=48, bg=self.color_palette[4])
        final_price_frame.pack_propagate(0)
        final_price_frame.grid(row=2, column=1, pady=2, padx=0)
        tkinter.Label(final_price_frame, text="میزان درآمد کل", font=font1, bg=self.color_palette[4]).pack(side=tkinter.RIGHT, padx=4)
        tkinter.Label(final_price_frame, text=":", font=font1, bg=self.color_palette[4]).pack(side=tkinter.RIGHT, padx=4)
        tkinter.Label(final_price_frame, text="211،217", font=font2, bg=self.color_palette[4]).pack(side=tkinter.RIGHT, padx=4)
        tkinter.Label(final_price_frame, text="تومان", font=font2, bg=self.color_palette[4]).pack(side=tkinter.RIGHT, padx=4)

        # profit price

        profit_frame = tkinter.Frame(information_frame, width=480, height=48, bg=self.color_palette[4])
        profit_frame.pack_propagate(0)
        profit_frame.grid(row=2, column=0, pady=2, padx=0)

        tkinter.Label(profit_frame, text="میزان سود نهایی", font=font1, bg=self.color_palette[4]).pack(side=tkinter.RIGHT, padx=4)
        tkinter.Label(profit_frame, text=":", font=font1, bg=self.color_palette[4]).pack(side=tkinter.RIGHT, padx=4)
        tkinter.Label(profit_frame, text="211،217", font=font2, bg=self.color_palette[4]).pack(side=tkinter.RIGHT, padx=4)
        tkinter.Label(profit_frame, text="تومان", font=font2, bg=self.color_palette[4]).pack(side=tkinter.RIGHT, padx=4)

        # column name

        column_name_frame = tkinter.Frame(self, width=990, height=50, bg=self.color_palette[3])
        column_name_frame.pack_propagate(0)
        column_name_frame.place(x=20, y=190)
        
        tkinter.Label(column_name_frame, text="", font=font2, bg=self.color_palette[3]).pack(side=tkinter.RIGHT, padx=3)
        tkinter.Label(column_name_frame, text="نام محصول", font=font1, width=12,
         bg=self.color_palette[3]).pack(side=tkinter.RIGHT, padx=4)
        tkinter.Label(column_name_frame, text="", font=font2, bg=self.color_palette[3]).pack(side=tkinter.RIGHT)
        tkinter.Label(column_name_frame, text="تعداد فروش", font=font1, width=8,
         bg=self.color_palette[3]).pack(side=tkinter.RIGHT, padx=4)
        tkinter.Label(column_name_frame, text="", font=font2, bg=self.color_palette[3]).pack(side=tkinter.RIGHT)
        tkinter.Label(column_name_frame, text="قیمت عرضه", font=font1, width=10,
         bg=self.color_palette[3]).pack(side=tkinter.RIGHT, padx=4)
        tkinter.Label(column_name_frame, text="", font=font2, bg=self.color_palette[3]).pack(side=tkinter.RIGHT)
        tkinter.Label(column_name_frame, text="قیمت تمام شده", font=font1, width=12,
         bg=self.color_palette[3]).pack(side=tkinter.RIGHT, padx=4)
        tkinter.Label(column_name_frame, text="", font=font2, bg=self.color_palette[3]).pack(side=tkinter.RIGHT)
        tkinter.Label(column_name_frame, text="سود نهایی", font=font1, width=10,
         bg=self.color_palette[3]).pack(side=tkinter.RIGHT, padx=4)
        tkinter.Label(column_name_frame, text="", font=font2, bg=self.color_palette[3]).pack(side=tkinter.RIGHT)

        #items frame

        self.item_frame = Item_ScrollableFrame(self, color_palette)
        self.item_frame.place(x=20, y=255)

        for i in range(14):
            pass
            self.Add_cart_item("1401/04/1", [1,2,3])

        tkinter.Frame(self.item_frame.scrollable_frame, width=980, height=140, bg=self.color_palette[3]).pack()

    def Add_cart_item(self, date, items):

        font1 = font.Font(family="Mj_Flow", size=19)
        font2 = font.Font(family="Dast Nevis", size=19)

        item_frame = tkinter.Frame(self.item_frame.scrollable_frame, width=980, height=60, bg=self.color_palette[4],
            highlightbackground=self.color_palette[2], highlightthickness=2)
        item_frame.pack_propagate(0)
        item_frame.pack(pady=6)

        tkinter.Label(item_frame, text="سیب زمینی سرخ کرده", font=font2, width=12,
            bg=self.color_palette[4]).pack(side=tkinter.RIGHT, padx=4)
        tkinter.Label(item_frame, text="", font=font2, bg=self.color_palette[2]).pack(side=tkinter.RIGHT)
        tkinter.Label(item_frame, text="12", font=font2, width=8,
            bg=self.color_palette[4]).pack(side=tkinter.RIGHT, padx=4)
        tkinter.Label(item_frame, text="", font=font2, bg=self.color_palette[2]).pack(side=tkinter.RIGHT)
        tkinter.Label(item_frame, text="241،000", font=font2, width=10,
            bg=self.color_palette[4]).pack(side=tkinter.RIGHT, padx=4)
        tkinter.Label(item_frame, text="", font=font2, bg=self.color_palette[2]).pack(side=tkinter.RIGHT)
        tkinter.Label(item_frame, text="191،456", font=font2, width=12,
            bg=self.color_palette[4]).pack(side=tkinter.RIGHT, padx=4)
        tkinter.Label(item_frame, text="", font=font2, bg=self.color_palette[2]).pack(side=tkinter.RIGHT)
        tkinter.Label(item_frame, text="51،672", font=font2, width=10,
            bg=self.color_palette[4]).pack(side=tkinter.RIGHT, padx=4)
            

    def show(self):
        self.place(x=20, y=20)

    def hide(self):
        self.place_forget()

class Item_ScrollableFrame(ttk.Frame):
    def __init__(self, container, color_palette, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Vertical.TScrollbar", gripcount=0, arrowsize=30,
                background=color_palette[2], darkcolor=color_palette[1], lightcolor=color_palette[1],
                troughcolor=color_palette[4], bordercolor=color_palette[3], arrowcolor=color_palette[1],
                activerelief=tkinter.FLAT, relief=tkinter.FLAT)

        canvas = tkinter.Canvas(self, height=390, width=990, bg=color_palette[3], bd=0, highlightthickness=0)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)

        self.scrollable_frame = tkinter.Frame(canvas, bg=color_palette[3])

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")