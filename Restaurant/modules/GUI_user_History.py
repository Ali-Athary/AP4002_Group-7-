import tkinter
from tkinter import font, ttk
from PIL import ImageTk, Image  
import os
import sys
import jdatetime

class History_Item_UI_images():
    def __init__(self) -> None:
        header_img = Image.open(os.path.join(sys.path[0], "resources\panels\\history_item_header.png")).convert("RGBA")
        self.header  = ImageTk.PhotoImage(header_img)
        
class History_panel(tkinter.Label):
    def __init__(self, root, color_palette):
        self.color_palette = color_palette
        img = Image.open(os.path.join(sys.path[0], "resources\panels\\simple_panel.png")).convert("RGBA")
        image = ImageTk.PhotoImage(img)

        super().__init__(root, image=image, bg=color_palette[4], bd=0)
        self.image = image

        self.ui_images = History_Item_UI_images()

        #items frame

        self.item_frame = Item_ScrollableFrame(self, color_palette)
        self.item_frame.place(x=20, y=20)

        for i in range(4):
            self.Add_cart_item("1401/04/1", [1,2,3])

        tkinter.Frame(self.item_frame.scrollable_frame, width=980, height=140, bg=self.color_palette[3]).pack()

    def Add_cart_item(self, date, items):
        # farme for items in each day

        frame = tkinter.Frame(self.item_frame.scrollable_frame, width=980, height=400, bg=self.color_palette[3])
        frame.pack(pady=8)

        font1 = font.Font(family="Mj_Flow", size=19)
        font2 = font.Font(family="Dast Nevis", size=19)
        font_English = font.Font(family="Roboto", size=18)
        
        # header

        header_frame = tkinter.Frame(frame, width=980, height=60, bg=self.color_palette[3])
        header_frame.pack(pady=10)

        Header_label_backgroung = tkinter.Label(header_frame, image=self.ui_images.header, bg=self.color_palette[3])
        Header_label_backgroung.image = self.ui_images.header
        Header_label_backgroung.place(x=0, y=0)

        # date 

        date_font1 = font.Font(family="Mj_Flow", size=22)
        date_font2 = font.Font(family="Dast Nevis", size=22)

        date_frame = tkinter.Frame(header_frame, width=280, height=40, bg=self.color_palette[4])
        date_frame.pack_propagate(0)
        date_frame.place(x=808, y=32, anchor=tkinter.CENTER)
        
        tkinter.Label(date_frame, text="تاریخ خرید", bg=self.color_palette[4], font=date_font1).pack(side=tkinter.RIGHT)
        tkinter.Label(date_frame, text=":", bg=self.color_palette[4], font=date_font1).pack(side=tkinter.RIGHT, padx=8)
        tkinter.Label(date_frame, text=date, bg=self.color_palette[4], font=date_font2).pack(side=tkinter.RIGHT)

        # general info

        purchase_info_frame = tkinter.Frame(frame, width=960, height=160, bg=self.color_palette[4],
         highlightbackground=self.color_palette[2], highlightthickness=2)
        purchase_info_frame.pack_propagate(0)
        purchase_info_frame.pack(pady=10)

        # price

        price_frame = tkinter.Frame(purchase_info_frame, width=950, height=53, bg=self.color_palette[4])
        price_frame.pack_propagate(0)
        price_frame.pack()
        tkinter.Label(price_frame, text="قیمت کل", font=font1, bg=self.color_palette[4]).pack(side=tkinter.RIGHT, padx=4)
        tkinter.Label(price_frame, text=":", font=font1, bg=self.color_palette[4]).pack(side=tkinter.RIGHT, padx=4)
        tkinter.Label(price_frame, text="236،217", font=font2, bg=self.color_palette[4]).pack(side=tkinter.RIGHT, padx=4)
        tkinter.Label(price_frame, text="تومان", font=font2, bg=self.color_palette[4]).pack(side=tkinter.RIGHT, padx=4)

        # discaount

        discaount_frame = tkinter.Frame(purchase_info_frame, width=950, height=53, bg=self.color_palette[4])
        discaount_frame.pack_propagate(0)
        discaount_frame.pack()

        tkinter.Label(discaount_frame, text="کد تخفیف", font=font1, bg=self.color_palette[4]).pack(side=tkinter.RIGHT, padx=4)
        tkinter.Label(discaount_frame, text=":", font=font1, bg=self.color_palette[4]).pack(side=tkinter.RIGHT, padx=4)
        tkinter.Label(discaount_frame, text="AS2D23", font=font_English, bg=self.color_palette[4]).pack(side=tkinter.RIGHT, padx=4)

        tkinter.Label(discaount_frame, text="", font=font2, bg=self.color_palette[4]).pack(side=tkinter.RIGHT, padx=40)

        tkinter.Label(discaount_frame, text="مقدار تخفیف", font=font1, bg=self.color_palette[4]).pack(side=tkinter.RIGHT, padx=4)
        tkinter.Label(discaount_frame, text=":", font=font1, bg=self.color_palette[4]).pack(side=tkinter.RIGHT, padx=4)
        tkinter.Label(discaount_frame, text="25،000", font=font2, bg=self.color_palette[4]).pack(side=tkinter.RIGHT, padx=4)
        tkinter.Label(discaount_frame, text="تومان", font=font2, bg=self.color_palette[4]).pack(side=tkinter.RIGHT, padx=4)

        # final price

        final_price_frame = tkinter.Frame(purchase_info_frame, width=950, height=53, bg=self.color_palette[4])
        final_price_frame.pack_propagate(0)
        final_price_frame.pack()

        tkinter.Label(final_price_frame, text="قیمت نهای (با احتساب تخفیف)", font=font1, bg=self.color_palette[4]).pack(side=tkinter.RIGHT, padx=4)
        tkinter.Label(final_price_frame, text=":", font=font1, bg=self.color_palette[4]).pack(side=tkinter.RIGHT, padx=4)
        tkinter.Label(final_price_frame, text="211،217", font=font2, bg=self.color_palette[4]).pack(side=tkinter.RIGHT, padx=4)
        tkinter.Label(final_price_frame, text="تومان", font=font2, bg=self.color_palette[4]).pack(side=tkinter.RIGHT, padx=4)

        # column name

        column_name_frame = tkinter.Frame(frame, width=960, height=50, bg=self.color_palette[3])
        column_name_frame.pack_propagate(0)
        column_name_frame.pack(pady=2)

        tkinter.Label(column_name_frame, text="نام محصول", font=font1, width=12,
         bg=self.color_palette[3]).pack(side=tkinter.RIGHT, padx=4)
        tkinter.Label(column_name_frame, text="", font=font2, bg=self.color_palette[3]).pack(side=tkinter.RIGHT)
        tkinter.Label(column_name_frame, text="قیمت (تومان)", font=font1, width=10,
         bg=self.color_palette[3]).pack(side=tkinter.RIGHT, padx=4)
        tkinter.Label(column_name_frame, text="", font=font2, bg=self.color_palette[3]).pack(side=tkinter.RIGHT)
        tkinter.Label(column_name_frame, text="تعداد", font=font1, width=8,
         bg=self.color_palette[3]).pack(side=tkinter.RIGHT, padx=4)
        tkinter.Label(column_name_frame, text="", font=font2, bg=self.color_palette[3]).pack(side=tkinter.RIGHT)
        tkinter.Label(column_name_frame, text="قیمت کل (تومان)", font=font1, width=12,
         bg=self.color_palette[3]).pack(side=tkinter.RIGHT, padx=4)
        tkinter.Label(column_name_frame, text="", font=font2, bg=self.color_palette[3]).pack(side=tkinter.RIGHT)
        tkinter.Label(column_name_frame, text="تاریخ", font=font1, width=10,
         bg=self.color_palette[3]).pack(side=tkinter.RIGHT, padx=4)


        # purchase items

        for item in items:
            # item frame

            item_frame = tkinter.Frame(frame, width=960, height=60, bg=self.color_palette[4],
             highlightbackground=self.color_palette[2], highlightthickness=2)
            item_frame.pack_propagate(0)
            item_frame.pack(pady=6)

            tkinter.Label(item_frame, text="سیب زمینی سرخ کرده", font=font2, width=12,
             bg=self.color_palette[4]).pack(side=tkinter.RIGHT, padx=4)
            tkinter.Label(item_frame, text="", font=font2, bg=self.color_palette[2]).pack(side=tkinter.RIGHT)
            tkinter.Label(item_frame, text="62،324", font=font2, width=10,
             bg=self.color_palette[4]).pack(side=tkinter.RIGHT, padx=4)
            tkinter.Label(item_frame, text="", font=font2, bg=self.color_palette[2]).pack(side=tkinter.RIGHT)
            tkinter.Label(item_frame, text="2", font=font2, width=8,
             bg=self.color_palette[4]).pack(side=tkinter.RIGHT, padx=4)
            tkinter.Label(item_frame, text="", font=font2, bg=self.color_palette[2]).pack(side=tkinter.RIGHT)
            tkinter.Label(item_frame, text="123،456", font=font2, width=12,
             bg=self.color_palette[4]).pack(side=tkinter.RIGHT, padx=4)
            tkinter.Label(item_frame, text="", font=font2, bg=self.color_palette[2]).pack(side=tkinter.RIGHT)
            tkinter.Label(item_frame, text="1401/4/4", font=font2, width=10,
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

        canvas = tkinter.Canvas(self, height=680, width=990, bg=color_palette[3], bd=0, highlightthickness=0)
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