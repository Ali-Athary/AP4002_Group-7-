import tkinter
from tkinter import font, ttk
from PIL import ImageTk, Image  
import os
import sys
import jdatetime
from modules import Food, functions, UserAndManager

class Order_item_UI_images():
    def __init__(self):
        background_img = Image.open(os.path.join(sys.path[0], "resources\panels\\order_item_base.png")).convert("RGBA")
        self.background = ImageTk.PhotoImage(background_img)

        view_img = Image.open(os.path.join(sys.path[0], "resources\icons\\view_buuton.png")).convert("RGBA")
        self.view = ImageTk.PhotoImage(view_img)

        close_img = Image.open(os.path.join(sys.path[0], "resources\icons\\close.png")).convert("RGBA")
        self.close = ImageTk.PhotoImage(close_img)

        send_img = Image.open(os.path.join(sys.path[0], "resources\icons\\send.png")).convert("RGBA")
        self.send = ImageTk.PhotoImage(send_img)
        
        add_img = Image.open(os.path.join(sys.path[0], "resources\icons\\add.png")).convert("RGBA")
        self.add = ImageTk.PhotoImage(add_img)

class Orders_panel(tkinter.Label):
    def __init__(self, root, color_palette, _admin:UserAndManager.Manager):
        global admin, main_panel
        admin = _admin
        main_panel = self
        self.color_palette = color_palette
        img = Image.open(os.path.join(sys.path[0], "resources\panels\\user_food_menu_panel.png")).convert("RGBA")
        image = ImageTk.PhotoImage(img)
        self.item_ui_image = Order_item_UI_images()

        super().__init__(root, image=image, bg=color_palette[4], bd=0)
        self.image = image

        #top bar

        self.top_bar = Orders_top_bar(self, color_palette)
        self.top_bar.show()

        #header 

        self.orders_header = Orders_header(self, color_palette)
        self.orders_header.show()

        #orders item frame

        self.oderes_frames = {}

        all_orders_frame = Order_Item_ScrollableFrame(self, color_palette, x=20, y=160)
        self.oderes_frames["total"] = all_orders_frame
        self.change_order_frame("total")

        unaccepted_orders_frame = Order_Item_ScrollableFrame(self, color_palette, x=20, y=160)
        self.oderes_frames["unaccepted_orders_frame"] = unaccepted_orders_frame
        
        completed_orders_frame = Order_Item_ScrollableFrame(self, color_palette, x=20, y=160)
        self.oderes_frames["completed_orders_frame"] = completed_orders_frame

        global items
        items = []
        
        self.update_page()

    def change_order_frame(self, frame_name):
        for frame in self.oderes_frames.values():
            frame.hide()
        self.oderes_frames[frame_name].show()
        self.top_bar.hide()
        self.top_bar.show()
        self.orders_header.hide()
        self.orders_header.show()

    def show_detail(self, order):
        self.detail_page = Orders_Detail_panel(self, self.color_palette, order)
        self.detail_page.show()

    def update_page(self):
        global items
        for item in items:
            item.pack_forget()

        all_orders = admin.get_all_orders()
        for order in all_orders:
            self.oderes_frames["total"].add_item(order)

        all_orders = admin.get_not_confirmed_orders()
        for order in all_orders:
            self.oderes_frames["unaccepted_orders_frame"].add_item(order)

        all_orders = admin.get_confirmed_orders()
        for order in all_orders:
            self.oderes_frames["completed_orders_frame"].add_item(order)

    def hide_detail(self):
        self.detail_page.hide()
        del self.detail_page

    def show(self):
        self.place(x=20, y=20)

    def hide(self):
        self.place_forget()
    
class Orders_Detail_panel(tkinter.Label):
    def __init__(self, root, color_palette, order:Food.FullOrderLog):
        self.color_palette = color_palette
        img = Image.open(os.path.join(sys.path[0], "resources\panels\\simple_panel.png")).convert("RGBA")
        image = ImageTk.PhotoImage(img)
        self.item_ui_image = root.item_ui_image

        super().__init__(root, image=image, bg=color_palette[4], bd=0)
        self.image = image
        self.grid_propagate(0)

        #info frame

        font1 = font.Font(family="Mj_Flow", size=20)
        font2 = font.Font(family="Dast Nevis", size=20)
        font1_english = font.Font(family="Roboto", size=22)

        frame = tkinter.Frame(self, width=880, height=190, bg=color_palette[4], highlightbackground=color_palette[2],
         highlightthickness=2)
        frame.grid_propagate(0)
        frame.place(x=160, y=40)

        #order date 

        f = tkinter.Frame(frame, width=435, height=60, bg=color_palette[4])
        f.pack_propagate(0)
        f.grid(row=0, column=1)

        tkinter.Label(f, text="تاریخ سفارش", font=font1, bg=color_palette[4]).pack(side=tkinter.RIGHT, padx=8)
        tkinter.Label(f, text=":", font=font1, bg=color_palette[4]).pack(side=tkinter.RIGHT, padx=8)
        tkinter.Label(f, text=order.date, font=font2, bg=color_palette[4]).pack(side=tkinter.RIGHT, padx=8)

        #sent date
        
        f = tkinter.Frame(frame, width=435, height=60, bg=color_palette[4])
        f.pack_propagate(0)
        f.grid(row=0, column=0)

        tkinter.Label(f, text="تاریخ ارسال", font=font1, bg=color_palette[4]).pack(side=tkinter.RIGHT, padx=8)
        tkinter.Label(f, text=":", font=font1, bg=color_palette[4]).pack(side=tkinter.RIGHT, padx=8)
        tkinter.Label(f, text=order.confirm, font=font2, bg=color_palette[4]).pack(side=tkinter.RIGHT, padx=8)

        #user name
        
        f = tkinter.Frame(frame, width=435, height=60, bg=color_palette[4])
        f.pack_propagate(0)
        f.grid(row=1, column=1)

        tkinter.Label(f, text="نام کاربر", font=font1, bg=color_palette[4]).pack(side=tkinter.RIGHT, padx=8)
        tkinter.Label(f, text=":", font=font1, bg=color_palette[4]).pack(side=tkinter.RIGHT, padx=8)
        tkinter.Label(f, text=order.user_name, font=font1, bg=color_palette[4]).pack(side=tkinter.RIGHT, padx=8)

        #final price

        f = tkinter.Frame(frame, width=435, height=60, bg=color_palette[4])
        f.pack_propagate(0)
        f.grid(row=1, column=0)

        tkinter.Label(f, text="قیمت نهایی", font=font1, bg=color_palette[4]).pack(side=tkinter.RIGHT, padx=8)
        tkinter.Label(f, text=":", font=font1, bg=color_palette[4]).pack(side=tkinter.RIGHT, padx=8)
        tkinter.Label(f, text=functions.turn_int_to_price(order.total_price - order.off_value), font=font2, bg=color_palette[4]).pack(side=tkinter.RIGHT, padx=8)
        tkinter.Label(f, text="تومان", font=font2, bg=color_palette[4]).pack(side=tkinter.RIGHT, padx=8)

        #discount code

        f = tkinter.Frame(frame, width=435, height=60, bg=color_palette[4])
        f.pack_propagate(0)
        f.grid(row=2, column=1)

        tkinter.Label(f, text="کد تخفیف", font=font1, bg=color_palette[4]).pack(side=tkinter.RIGHT, padx=8)
        tkinter.Label(f, text=":", font=font1, bg=color_palette[4]).pack(side=tkinter.RIGHT, padx=8)
        tkinter.Label(f, text=order.off_code, font=font1_english, bg=color_palette[4]).pack(side=tkinter.RIGHT, padx=8)

        #discount amount

        f = tkinter.Frame(frame, width=435, height=60, bg=color_palette[4])
        f.pack_propagate(0)
        f.grid(row=2, column=0)

        tkinter.Label(f, text="مقدار تخفیف", font=font1, bg=color_palette[4]).pack(side=tkinter.RIGHT, padx=8)
        tkinter.Label(f, text=":", font=font1, bg=color_palette[4]).pack(side=tkinter.RIGHT, padx=8)
        tkinter.Label(f, text=functions.turn_int_to_price(order.off_value), font=font2, bg=color_palette[4]).pack(side=tkinter.RIGHT, padx=8)
        tkinter.Label(f, text="تومان", font=font2, bg=color_palette[4]).pack(side=tkinter.RIGHT, padx=8)

        #columns names

        column_name_frame = tkinter.Frame(self, width=960, height=50, bg=self.color_palette[3])
        column_name_frame.pack_propagate(0)
        column_name_frame.place(x=50,y=240)

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

        #detail items 

        self.item_frame = Detail_Item_ScrollableFrame(self, color_palette, width=960, height=360, x=50, y=300)
        self.item_frame.show()
        food_list = order.food_log_list
        for food in food_list:
            self.item_frame.add_item(food)

        #button frame

        button_frame = tkinter.Frame(self, bg=color_palette[3], bd=0, highlightthickness=0)
        button_frame.place(x=28, y=46)

        #close button

        close_button = tkinter.Button(button_frame, image=self.item_ui_image.close, bg=color_palette[3],
         activebackground=color_palette[3], bd=0, highlightthickness=0, command=root.hide_detail)
        close_button.image = self.item_ui_image.close
        close_button.grid(row=0, column=0)


        #send button

        if(order.confirm == ""):
            def send():
                admin.confirm_order(order, functions.get_date())
                root.hide_detail()
                main_panel.update_page()

            send_button = tkinter.Button(button_frame, image=self.item_ui_image.send, bg=color_palette[3],
            activebackground=color_palette[3], bd=0, highlightthickness=0, command=send)
            send_button.image = self.item_ui_image.send
            send_button.grid(row=1, column=0)

    def show(self):
        self.place(x=0, y=0)

    def hide(self):
        self.place_forget()

class Orders_top_bar(tkinter.Frame):
    def __init__(self, root, color_palette):
        super().__init__(root, width=1000, height=60, bg=color_palette[3])
        self.pack_propagate(0)

        font1 = font.Font(family="Mj_Flow", size=25)
        font2 = font.Font(family="Dast Nevis", size=30)
        font3 = font.Font(family="Mj_Flow", size=20)

        # Date

        tkinter.Label(self, text="سفارشات", bg=color_palette[3], font=font1).pack(side=tkinter.RIGHT, padx=30)

        # choose order type

        frame = tkinter.Frame(self, height=60, width=380, bg=color_palette[3])
        frame.pack_propagate(0)
        frame.pack(side=tkinter.LEFT, padx=20)

        tkinter.Label(frame, text="نوع سفارشات", font=font3, bg=color_palette[3]).pack(side=tkinter.RIGHT, padx=2)
        tkinter.Label(frame, text=":", font=font3, bg=color_palette[3]).pack(side=tkinter.RIGHT, padx=2)

        Types = ["کل", "در انتظار ارسال", "ارسال شده"]
        frame_dict = {Types[0]:"total",Types[1]:"unaccepted_orders_frame",Types[2]:"completed_orders_frame"}

        order_type_var = tkinter.StringVar()
        order_type_var.set(Types[0])

        order_type_menu = Drop_Down_Menu(frame, order_type_var, Types, font_=font3,
         font_color=color_palette[0], color1=color_palette[3], color2=color_palette[4])
        order_type_menu.pack(side=tkinter.RIGHT, padx=2)

        order_type_var.trace("w", lambda x, y, z:root.change_order_frame(frame_dict[order_type_var.get()]))

    def show(self):
        self.place(x=30, y=8)

    def hide(self):
        self.place_forget()

class Orders_header(tkinter.Frame):
    def __init__(self, root, color_palette):
        super().__init__(root, width=1010, height=66, bg=color_palette[3])
        self.pack_propagate(0)

        font1 = font.Font(family="Mj_Flow", size=20)
        font2 = font.Font(family="Dast Nevis", size=30)
        font3 = font.Font(family="Mj_Flow", size=20)

        tkinter.Label(self, text="   ", bg=color_palette[3], font=font1).pack(side=tkinter.RIGHT)
        tkinter.Label(self, text="نام کاربر", bg=color_palette[3], font=font1).pack(side=tkinter.RIGHT, padx=90)
        tkinter.Label(self, text="هزینه سفارش", bg=color_palette[3], font=font1).pack(side=tkinter.RIGHT, padx=20)
        tkinter.Label(self, text="تاریخ سفارش", bg=color_palette[3], font=font1).pack(side=tkinter.RIGHT, padx=30)
        tkinter.Label(self, text="تاریخ ارسال", bg=color_palette[3], font=font1).pack(side=tkinter.RIGHT, padx=30)
        tkinter.Label(self, text="جزییات سفارش", bg=color_palette[3], font=font1).pack(side=tkinter.RIGHT, padx=30)
        

    def show(self):
        self.place(x=20, y=90)

    def hide(self):
        self.place_forget()

class Drop_Down_Menu(tkinter.OptionMenu):
    def __init__(self, master, variable, values, font_=None, font_color="black", color1="white", color2="blue"):
        super().__init__(master, variable, *values)
        self.config(font=font_, fg=font_color, bg=color2, activebackground=color1, activeforeground=font_color,
         highlightthickness=0, bd=0, indicatoron=0)
        self["menu"].config(font=font_, fg=font_color, bg=color1, activebackground=color2, 
         activeforeground=font_color, relief=tkinter.FLAT, bd=0)

class ScrollableFrame(ttk.Frame):
    def __init__(self, container, color_palette, *args, width=990, height=520, x=0, y=0, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.main_root = container
        self.item_ui_image = container.item_ui_image
        self.color_palette = color_palette
        self.x = x
        self.y = y
        
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Vertical.TScrollbar", gripcount=0, arrowsize=30,
                background=color_palette[2], darkcolor=color_palette[1], lightcolor=color_palette[1],
                troughcolor=color_palette[4], bordercolor=color_palette[3], arrowcolor=color_palette[1],
                activerelief=tkinter.FLAT, relief=tkinter.FLAT)

        canvas = tkinter.Canvas(self, height=height, width=width, bg=color_palette[3], bd=0, highlightthickness=0)
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
        
    def show(self):
        self.place(x=self.x, y=self.y)
    
    def hide(self):
        self.place_forget()

class Order_Item_ScrollableFrame(ScrollableFrame):
    def add_item(self, order:Food.FullOrderLog):
        global items

        frame = tkinter.Frame(self.scrollable_frame, width=980, height=90, bg=self.color_palette[1])
        frame.pack_propagate(0)
        frame.pack(pady=4)

        items.append(frame)

        #background 
        
        background = tkinter.Label(frame, image=self.item_ui_image.background, bg=self.color_palette[3])
        background.image = self.item_ui_image.background
        background.place(x=0, y=0)

        #info

        font1 = font.Font(family="Mj_Flow", size=20)
        font2 = font.Font(family="Dast Nevis", size=20)
        font3 = font.Font(family="Mj_Flow", size=20)

        # user name

        tkinter.Label(frame, text=order.user_name, bg=self.color_palette[3], font=font1, width=12).pack(side=tkinter.RIGHT, padx=10)
        tkinter.Label(frame, text="", bg=self.color_palette[2], font=font1).pack(side=tkinter.RIGHT)

        # order price

        tkinter.Label(frame, text=order.total_price, bg=self.color_palette[3], font=font2, width=10).pack(side=tkinter.RIGHT)
        tkinter.Label(frame, text="", bg=self.color_palette[2], font=font1).pack(side=tkinter.RIGHT)

        # order date

        tkinter.Label(frame, text=order.date, bg=self.color_palette[3], font=font2, width=9).pack(side=tkinter.RIGHT)
        tkinter.Label(frame, text="", bg=self.color_palette[2], font=font1).pack(side=tkinter.RIGHT)

        # sent date

        tkinter.Label(frame, text=order.confirm, bg=self.color_palette[3], font=font2, width=9).pack(side=tkinter.RIGHT)
        tkinter.Label(frame, text="", bg=self.color_palette[2], font=font1).pack(side=tkinter.RIGHT)

        # view button

        def veiw():
            self.main_root.show_detail(order)

        view_button = tkinter.Button(frame, image=self.item_ui_image.view, bg=self.color_palette[3],
         activebackground=self.color_palette[3], highlightthickness=0, bd=0, command=veiw)
        view_button.image = self.item_ui_image.view
        view_button.pack(side=tkinter.RIGHT, padx=26)

class Detail_Item_ScrollableFrame(ScrollableFrame):
    def add_item(self, food:Food.FoodLog):
        font1 = font.Font(family="Mj_Flow", size=20)
        font2 = font.Font(family="Dast Nevis", size=20)
        font1_english = font.Font(family="Roboto", size=22)

        item_frame = tkinter.Frame(self.scrollable_frame, width=960, height=60, bg=self.color_palette[4],
         highlightbackground=self.color_palette[2], highlightthickness=2)
        item_frame.pack_propagate(0)
        item_frame.pack(pady=6)

        tkinter.Label(item_frame, text=food.name, font=font2, width=12,
            bg=self.color_palette[4]).pack(side=tkinter.RIGHT, padx=4)
        tkinter.Label(item_frame, text="", font=font2, bg=self.color_palette[2]).pack(side=tkinter.RIGHT)
        tkinter.Label(item_frame, text=functions.turn_int_to_price(food.price), font=font2, width=10,
            bg=self.color_palette[4]).pack(side=tkinter.RIGHT, padx=4)
        tkinter.Label(item_frame, text="", font=font2, bg=self.color_palette[2]).pack(side=tkinter.RIGHT)
        tkinter.Label(item_frame, text=food.count, font=font2, width=8,
            bg=self.color_palette[4]).pack(side=tkinter.RIGHT, padx=4)
        tkinter.Label(item_frame, text="", font=font2, bg=self.color_palette[2]).pack(side=tkinter.RIGHT)
        tkinter.Label(item_frame, text=functions.turn_int_to_price(food.price * food.count), font=font2, width=12,
            bg=self.color_palette[4]).pack(side=tkinter.RIGHT, padx=4)
        tkinter.Label(item_frame, text="", font=font2, bg=self.color_palette[2]).pack(side=tkinter.RIGHT)
        tkinter.Label(item_frame, text=food.date, font=font2, width=10,
            bg=self.color_palette[4]).pack(side=tkinter.RIGHT, padx=4)