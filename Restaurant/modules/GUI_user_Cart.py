import tkinter
from tkinter import font, ttk
from PIL import ImageTk, Image  
import os
import sys
import jdatetime
from modules import Food, functions, UserAndManager

class Cart_Item_UI_images():
    def __init__(self) -> None:
        plus_img = Image.open(os.path.join(sys.path[0], "resources\icons\\plus.png")).convert("RGBA")
        self.plus = ImageTk.PhotoImage(plus_img.resize((32,32), Image.ANTIALIAS))

        minus_img = Image.open(os.path.join(sys.path[0], "resources\icons\\minus.png")).convert("RGBA")
        self.minus = ImageTk.PhotoImage(minus_img.resize((32,32), Image.ANTIALIAS))

        thrascan_img = Image.open(os.path.join(sys.path[0], "resources\icons\\trash-bin.png")).convert("RGBA")
        self.trash_can = ImageTk.PhotoImage(thrascan_img.resize((48,48), Image.ANTIALIAS))

        change_img = Image.open(os.path.join(sys.path[0], "resources\icons\\cart_item_change_button.png")).convert("RGBA")
        self.change = ImageTk.PhotoImage(change_img)

class Cart_panel(tkinter.Label):
    def __init__(self, root, color_palette, _user:UserAndManager.User):
        global user
        user = _user
        self.color_palette = color_palette
        img = Image.open(os.path.join(sys.path[0], "resources\panels\\user_food_menu_panel.png")).convert("RGBA")
        image = ImageTk.PhotoImage(img)

        super().__init__(root, image=image, bg=color_palette[4], bd=0)
        self.image = image

        self.ui_images = Cart_Item_UI_images()

        #top bar

        self.top_bar = Cart_top_bar(self, color_palette)
        self.top_bar.show()

        #items frame

        self.item_frame = Item_ScrollableFrame(self, color_palette)
        self.item_frame.place(x=20, y=100)

        self.items = []

        for i in range(4):
            self.Add_cart_item("1401/04/1", [1,2,3])

    def Add_cart_item(self, date, items):
        # farme for items in each day

        frame = tkinter.Frame(self.item_frame.scrollable_frame, width=980, height=400, bg=self.color_palette[3])
        frame.pack(pady=8)

        self.items.append(frame)

        font1 = font.Font(family="Mj_Flow", size=19)
        font2 = font.Font(family="Dast Nevis", size=19)
        
        # header

        header_frame = tkinter.Frame(frame, width=980, height=60, bg=self.color_palette[3])
        header_frame.pack(pady=10)

        header_img = Image.open(os.path.join(sys.path[0], "resources\panels\\cart_item_header.png")).convert("RGBA")
        header_image = ImageTk.PhotoImage(header_img)

        Header_label_backgroung = tkinter.Label(header_frame, image=header_image, bg=self.color_palette[3])
        Header_label_backgroung.image = header_image
        Header_label_backgroung.place(x=0, y=0)

        # date 

        date_font = font.Font(family="Dast Nevis", size=24)

        date_frame = tkinter.Frame(header_frame, width=230, height=40, bg=self.color_palette[4])
        date_frame.pack_propagate(0)
        date_frame.place(x=12, y=12)
        tkinter.Label(date_frame, text=date, bg=self.color_palette[4], font=date_font).pack(expand=True, fill="none")

        # column name

        column_name_frame = tkinter.Frame(frame, width=960, height=60, bg=self.color_palette[3])
        column_name_frame.pack_propagate(0)
        column_name_frame.pack(pady=10)

        tkinter.Label(column_name_frame, text="نام محصول", font=font1, width=12,
         bg=self.color_palette[3]).pack(side=tkinter.RIGHT, padx=4)
        tkinter.Label(column_name_frame, text="", font=font2, bg=self.color_palette[3]).pack(side=tkinter.RIGHT)
        tkinter.Label(column_name_frame, text="قیمت (تومان)", font=font1, width=8,
         bg=self.color_palette[3]).pack(side=tkinter.RIGHT, padx=4)
        tkinter.Label(column_name_frame, text="", font=font2, bg=self.color_palette[3]).pack(side=tkinter.RIGHT)
        tkinter.Label(column_name_frame, text="قیمت کل (تومان)", font=font1, width=10,
         bg=self.color_palette[3]).pack(side=tkinter.RIGHT, padx=4)
        tkinter.Label(column_name_frame, text="", font=font2, bg=self.color_palette[3]).pack(side=tkinter.RIGHT)
        tkinter.Label(column_name_frame, text="تعداد", font=font1, width=16,
         bg=self.color_palette[3]).pack(side=tkinter.RIGHT, padx=4)
        tkinter.Label(column_name_frame, text="", font=font2, bg=self.color_palette[3]).pack(side=tkinter.RIGHT)
        tkinter.Label(column_name_frame, text="حذف", font=font1, width=6,
         bg=self.color_palette[3]).pack(side=tkinter.RIGHT, padx=4)


        # purchase items

        for item in items:
            if(isinstance(item, Food.FoodLog)):
                # item frame
                cart_food_item(frame, self.color_palette, self.ui_images, self, item)
                
            
    def update_page(self):        
        for item in self.items:
            item.pack_forget()
        self.items = []

        d = user.get_last_order_dict()
        for key in d.keys():
            self.Add_cart_item(key, d[key])

        self.top_bar.update_price()

    def show(self):
        self.place(x=20, y=20)

    def hide(self):
        self.place_forget()

class cart_food_item(tkinter.Frame):
    def __init__(self, root, color_palette, ui_images, main_root, item:Food.FoodLog):
        self.main_root = main_root
        self.color_palette = color_palette
        self.ui_images = ui_images
        super().__init__(root, width=960, height=100, bg=self.color_palette[4],
         highlightbackground=self.color_palette[2], highlightthickness=2)
        self.pack_propagate(0)
        self.pack(pady=10)

        font1 = font.Font(family="Mj_Flow", size=19)
        font2 = font.Font(family="Dast Nevis", size=19)

        # info frame

        item_info_frame = tkinter.Frame(self, width=580, height=90, bg=self.color_palette[4])
        item_info_frame.pack_propagate(0)
        item_info_frame.pack(side=tkinter.RIGHT)

        tkinter.Label(item_info_frame, text=item.name, font=font2, width=12,
        bg=self.color_palette[4]).pack(side=tkinter.RIGHT, padx=4)
        tkinter.Label(item_info_frame, text="", font=font2, bg=self.color_palette[2]).pack(side=tkinter.RIGHT)
        tkinter.Label(item_info_frame, text=functions.turn_int_to_price(item.price), font=font2, width=8,
        bg=self.color_palette[4]).pack(side=tkinter.RIGHT, padx=4)
        tkinter.Label(item_info_frame, text="", font=font2, bg=self.color_palette[2]).pack(side=tkinter.RIGHT)
        tkinter.Label(item_info_frame, text=functions.turn_int_to_price(item.price * item.count), font=font2, width=10,
        bg=self.color_palette[4]).pack(side=tkinter.RIGHT, padx=4)
        tkinter.Label(item_info_frame, text="", font=font2, bg=self.color_palette[2]).pack(side=tkinter.RIGHT)

        # adjust frame

        item_adjust_frame = tkinter.Frame(self, width=380, height=90, bg=self.color_palette[4])
        item_adjust_frame.pack_propagate(0)
        item_adjust_frame.pack(side=tkinter.LEFT, padx=5)

        # count adjustment
        
        count_frame = tkinter.Frame(item_adjust_frame, width=220, height=40, bg=self.color_palette[4])
        count_frame.place(x=240, y=20, anchor=tkinter.CENTER)
        
        count_label = tkinter.Label(count_frame, text=item.count, font=font2, bg=self.color_palette[4])
        count_label.grid(row=0, column=1, padx=32)

        count = item.count

        def plus():
            nonlocal count, item
            nonlocal count_label, plus_button, change_count_button, minus_button
            count += 1
            if(count == item.count):
                plus_button.config(state="disable")
                change_count_button.config(state="disable")
            if(count > 0):
                minus_button.config(state="normal")
            count_label.configure(text=count)

        plus_button = tkinter.Button(count_frame, image=self.ui_images.plus, bg=self.color_palette[4],
        highlightthickness=0, bd=0, activebackground=self.color_palette[4], command=plus)
        plus_button.image = self.ui_images.plus
        plus_button.config(state="disable")
        plus_button.grid(row=0, column=2)
        
        def minus():
            nonlocal count, item
            nonlocal count_label, plus_button, change_count_button, minus_button
            count -= 1
            if(count == 0):
                minus_button.config(state="disable")
            if(count < item.count):
                plus_button.config(state="normal")
                change_count_button.config(state="normal")
            count_label.configure(text=count)

        minus_button = tkinter.Button(count_frame, image=self.ui_images.minus, bg=self.color_palette[4],
        highlightthickness=0, bd=0, activebackground=self.color_palette[4], command=minus)
        minus_button.image = self.ui_images.minus
        minus_button.grid(row=0, column=0)

        # change count button

        def change():
            nonlocal count
            if(count == 0):
                user.remove_from_last_order(item)
            else:
                pass
            self.main_root.update_page()

        change_count_button = tkinter.Button(item_adjust_frame, image=self.ui_images.change, bg=self.color_palette[4],
        highlightthickness=0, bd=0, activebackground=self.color_palette[4], command=change)
        change_count_button.config(state="disable")
        change_count_button.place(x=240, y=70, anchor=tkinter.CENTER)

        #delete button

        def delete():
            user.remove_from_last_order(item)
            self.main_root.update_page()

        delete_button = tkinter.Button(item_adjust_frame, image=self.ui_images.trash_can, bg=self.color_palette[4],
        highlightthickness=0, bd=0, activebackground=self.color_palette[4], command=delete)
        delete_button.image = self.ui_images.trash_can
        delete_button.pack(side=tkinter.LEFT, padx=18)

        tkinter.Label(item_adjust_frame, text="", font=font2, bg=self.color_palette[2]).pack(side=tkinter.LEFT, padx=8)

class Cart_top_bar(tkinter.Frame):
    def __init__(self, root, color_palette, final_price=1456789):
        super().__init__(root, width=1010, height=60, bg=color_palette[3])
        self.grid_propagate(0)

        self.final_price = int(final_price)

        font1 = font.Font(family="Mj_Flow", size=20)
        font2 = font.Font(family="Dast Nevis", size=20)
        font_english = font.Font(family="Roboto", size=20)

        # info frame

        info_frame = tkinter.Frame(self, width=390, height=60, bg=color_palette[3])
        info_frame.pack_propagate(0)
        info_frame.place(x=1010,y=0, anchor=tkinter.NE)
        
        # purchase information

        tkinter.Label(info_frame, text="قیمت نهایی", font=font1, bg=color_palette[3]).pack(side=tkinter.RIGHT, padx=0)
        tkinter.Label(info_frame, text=":", font=font1, bg=color_palette[3]).pack(side=tkinter.RIGHT, padx=5)
        
        self.price_label = tkinter.Label(info_frame, text="0", font=font2, bg=color_palette[3])
        self.price_label.pack(side=tkinter.RIGHT, padx=0)

        self.update_price()

        tkinter.Label(info_frame, text="تومان", font=font2, bg=color_palette[3]).pack(side=tkinter.RIGHT, padx=5)

        # button frame

        button_frame = tkinter.Frame(self, width=610, height=60, bg=color_palette[3])
        button_frame.pack_propagate(0)
        button_frame.place(x=0,y=0)

        # purchase complete button

        def complete():
            user.confirm_order(functions.get_date())
            root.update_page()

        complete_img = Image.open(os.path.join(sys.path[0], "resources\icons\\cart_complete_purchase_button.png")).convert("RGBA")
        complete_image = ImageTk.PhotoImage(complete_img)

        purchase_complete_button = tkinter.Button(button_frame, bg=color_palette[3], image=complete_image,
         highlightthickness=0, bd=0, activebackground=color_palette[3], command=complete)
        purchase_complete_button.image = complete_image
        purchase_complete_button.pack(side=tkinter.LEFT)

        #discount 
        
        tkinter.Label(button_frame, text="کد تخفیف", font=font1, bg=color_palette[3]).pack(side=tkinter.RIGHT, padx=0)
        tkinter.Label(button_frame, text=":", font=font1, bg=color_palette[3]).pack(side=tkinter.RIGHT, padx=5)

        discount_code_var = tkinter.StringVar()
        tkinter.Entry(button_frame, textvariable=discount_code_var, font=font_english, bg=color_palette[4],
         highlightthickness=0, bd=0, width=12).pack(side=tkinter.RIGHT)

        def apply_discount():
            user.apply_discount(discount_code_var.get())
            self.update_price()

        complete_img = Image.open(os.path.join(sys.path[0], "resources\icons\\discount.png")).convert("RGBA")
        complete_image = ImageTk.PhotoImage(complete_img)

        purchase_complete_button = tkinter.Button(button_frame, bg=color_palette[3], image=complete_image,
         highlightthickness=0, bd=0, activebackground=color_palette[3], command=apply_discount)
        purchase_complete_button.image = complete_image
        purchase_complete_button.pack(side=tkinter.RIGHT)

    def update_price(self):
        self.final_price = user.purchasable_price()
        self.price_label.configure(text=functions.turn_int_to_price(self.final_price))

    def change_month(self):
        if(int(self.month_var.get()) == self.months[1]):
            self.day_menu1.grid_forget()
            self.day_menu2.grid(row=0, column=3)
            self.day_var.set(self.days2[0])
        else:
            self.day_menu1.grid(row=0, column=3)
            self.day_menu2.grid_forget()
            self.day_var.set(self.days1[0])

    def show(self):
        self.place(x=20, y=8)

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

        canvas = tkinter.Canvas(self, height=560, width=990, bg=color_palette[3], bd=0, highlightthickness=0)
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