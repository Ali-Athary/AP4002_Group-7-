import tkinter
from tkinter import font, ttk
from PIL import ImageTk, Image  
import os
import sys
import jdatetime

class Order_item_UI_images():
    def __init__(self):
        background_img = Image.open(os.path.join(sys.path[0], "resources\panels\\order_item_base.png")).convert("RGBA")
        self.background = ImageTk.PhotoImage(background_img)

        view_img = Image.open(os.path.join(sys.path[0], "resources\icons\\view_buuton.png")).convert("RGBA")
        self.view = ImageTk.PhotoImage(view_img)

        minus_img = Image.open(os.path.join(sys.path[0], "resources\icons\\minus.png")).convert("RGBA")
        self.minus = ImageTk.PhotoImage(minus_img.resize((40,40), Image.ANTIALIAS))

        add_img = Image.open(os.path.join(sys.path[0], "resources\icons\\add.png")).convert("RGBA")
        self.add = ImageTk.PhotoImage(add_img)

class Orders_panel(tkinter.Label):
    def __init__(self, root, color_palette):
        self.color_palette = color_palette
        img = Image.open(os.path.join(sys.path[0], "resources\panels\\user_food_menu_panel.png")).convert("RGBA")
        image = ImageTk.PhotoImage(img)

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

        unpaid_orders_frame = Order_Item_ScrollableFrame(self, color_palette)
        self.oderes_frames["unpaid_orders_frame"] = unpaid_orders_frame
        self.change_order_frame("unpaid_orders_frame")

        unaccepted_orders_frame = Order_Item_ScrollableFrame(self, color_palette)
        self.oderes_frames["unaccepted_orders_frame"] = unaccepted_orders_frame
        
        completed_orders_frame = Order_Item_ScrollableFrame(self, color_palette)
        self.oderes_frames["completed_orders_frame"] = completed_orders_frame

        for i in range(20):
            self.oderes_frames["unpaid_orders_frame"].add_item("علی اطهری", "12,140,433", "1401/04/14", "-")
            self.oderes_frames["unaccepted_orders_frame"].add_item("علی اطهری", "140،123", "1401/04/14", "1401/04/15")
            self.oderes_frames["completed_orders_frame"].add_item("علی اطهری", "140،123", "1401/04/14", "1401/04/15")
            pass

    def change_order_frame(self, frame_name):
        for frame in self.oderes_frames.values():
            frame.hide()
        self.oderes_frames[frame_name].show()
        self.top_bar.hide()
        self.top_bar.show()
        self.orders_header.hide()
        self.orders_header.show()

    def show(self):
        self.place(x=20, y=20)

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

        Types = ["در انتظار تسویه حساب", "در انتظار ارسال", "ارسال شده"]
        frame_dict = {Types[0]:"unpaid_orders_frame",Types[1]:"unaccepted_orders_frame",Types[2]:"completed_orders_frame"}

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

class Order_Item_ScrollableFrame(ttk.Frame):
    def __init__(self, container, color_palette, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        self.item_ui_image = Order_item_UI_images()
        self.color_palette = color_palette
        
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Vertical.TScrollbar", gripcount=0, arrowsize=30,
                background=color_palette[2], darkcolor=color_palette[1], lightcolor=color_palette[1],
                troughcolor=color_palette[4], bordercolor=color_palette[3], arrowcolor=color_palette[1],
                activerelief=tkinter.FLAT, relief=tkinter.FLAT)

        canvas = tkinter.Canvas(self, height=520, width=990, bg=color_palette[3], bd=0, highlightthickness=0)
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

    def add_item(self, user_name, order_price, order_date, sent_date):
        frame = tkinter.Frame(self.scrollable_frame, width=980, height=90, bg=self.color_palette[1])
        frame.pack_propagate(0)
        frame.pack(pady=4)

        #background 
        
        background = tkinter.Label(frame, image=self.item_ui_image.background, bg=self.color_palette[3])
        background.image = self.item_ui_image.background
        background.place(x=0, y=0)

        #info

        font1 = font.Font(family="Mj_Flow", size=20)
        font2 = font.Font(family="Dast Nevis", size=20)
        font3 = font.Font(family="Mj_Flow", size=20)

        # user name

        tkinter.Label(frame, text=user_name, bg=self.color_palette[3], font=font1, width=12).pack(side=tkinter.RIGHT, padx=10)
        tkinter.Label(frame, text="", bg=self.color_palette[2], font=font1).pack(side=tkinter.RIGHT)

        # order price

        tkinter.Label(frame, text=order_price, bg=self.color_palette[3], font=font2, width=10).pack(side=tkinter.RIGHT)
        tkinter.Label(frame, text="", bg=self.color_palette[2], font=font1).pack(side=tkinter.RIGHT)

        # order date

        tkinter.Label(frame, text=order_date, bg=self.color_palette[3], font=font2, width=9).pack(side=tkinter.RIGHT)
        tkinter.Label(frame, text="", bg=self.color_palette[2], font=font1).pack(side=tkinter.RIGHT)

        # sent date

        tkinter.Label(frame, text=sent_date, bg=self.color_palette[3], font=font2, width=9).pack(side=tkinter.RIGHT)
        tkinter.Label(frame, text="", bg=self.color_palette[2], font=font1).pack(side=tkinter.RIGHT)

        # view button

        view_button = tkinter.Button(frame, image=self.item_ui_image.view, bg=self.color_palette[3],
         activebackground=self.color_palette[3], highlightthickness=0, bd=0)
        view_button.image = self.item_ui_image.view
        view_button.pack(side=tkinter.RIGHT, padx=26)
    def show(self):
        self.place(x=20, y=160)
    
    def hide(self):
        self.place_forget()

   