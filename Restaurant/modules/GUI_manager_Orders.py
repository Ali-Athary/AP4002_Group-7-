import tkinter
from tkinter import font, ttk
from PIL import ImageTk, Image  
import os
import sys
import jdatetime

class Food_item_UI_images():
    def __init__(self):
        background_img = Image.open(os.path.join(sys.path[0], "resources\panels\\food_item_base.png")).convert("RGBA")
        self.background = ImageTk.PhotoImage(background_img)

        plus_img = Image.open(os.path.join(sys.path[0], "resources\icons\\plus.png")).convert("RGBA")
        self.plus = ImageTk.PhotoImage(plus_img.resize((40,40), Image.ANTIALIAS))

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

        self.top_bar = Food_manu_top_bar(self, color_palette)
        self.top_bar.show()

        #orders item frame

        self.oderes_frames = {}

        unaccepted_orders_frame = Food_Item_ScrollableFrame(self, color_palette)
        self.oderes_frames["unaccepted_orders_frame"] = unaccepted_orders_frame
        self.change_order_frame("unaccepted_orders_frame")

        accepted_orders_frame = Food_Item_ScrollableFrame(self, color_palette)
        self.oderes_frames["accepted_orders_frame"] = accepted_orders_frame
        
        completed_orders_frame = Food_Item_ScrollableFrame(self, color_palette)
        self.oderes_frames["completed_orders_frame"] = completed_orders_frame

        self.item_ui_image = Food_item_UI_images()

        for i in range(20):
            self.add_food_to_list(unaccepted_orders_frame, "پیتزا پپرونی", 140000)
            self.add_food_to_list(accepted_orders_frame, "پیتزا پپرونی", 200)
            self.add_food_to_list(completed_orders_frame, "پیتزا پپرونی", 1000)

    def add_food_to_list(self, root, name, price):
        #item frame

        frame = tkinter.Frame(root.scrollable_frame, width=980, height=200, bg=self.color_palette[3])
        frame.pack()

        #background

        background = tkinter.Label(frame, image=self.item_ui_image.background, bg=self.color_palette[3])
        background.image = self.item_ui_image.background
        background.place(x=0,y=0)

        #fonts

        font1 = font.Font(family="Mj_Flow", size=40)
        font_dasnevis_0 = font.Font(family="Dast Nevis", size=18)
        font_dasnevis_1 = font.Font(family="Dast Nevis", size=30)
        font_dasnevis_2 = font.Font(family="Dast Nevis", size=35)

        #name

        tkinter.Label(frame, text=name, fg="white", bg=self.color_palette[2], font=font_dasnevis_2).place(x=940, y=30, anchor=tkinter.NE)

        #price 

        price_frame = tkinter.Frame(frame, width=160, height=40, bg=self.color_palette[2])
        price_frame.place(x=940, y=120, anchor=tkinter.NE)

        tkinter.Label(price_frame, text=f"{str(int(price))[:-3]},{str(int(price))[-3:]}", fg="white",
         bg=self.color_palette[2], font=font_dasnevis_0).grid(row=0, column=1)
        tkinter.Label(price_frame, text="تومان", fg="white",
         bg=self.color_palette[2], font=font_dasnevis_0).grid(row=0, column=0, padx=6)

        #descriptiona

        descriptiona_frame = tkinter.Frame(frame, width=300, height=120, bg=self.color_palette[2])
        descriptiona_frame.pack_propagate(0)
        descriptiona_frame.place(x=740, y=40, anchor=tkinter.NE)

        ingrediente = ["گوشت، پنیر، قارچ، پپرونی", "سس مخصوص، خمیر مخصوص"]

        f = tkinter.Frame(descriptiona_frame, bg=self.color_palette[2])
        f.pack(expand=True, fill="none")

        for line in ingrediente:
            tkinter.Label(f, text=line, bg=self.color_palette[2], font=font_dasnevis_0).pack()

        #count

        count = 0

        count_label = tkinter.Label(frame, text=count, font=font_dasnevis_1, fg="white", bg=self.color_palette[2])
        count_label.place(x=330, y=60, anchor=tkinter.CENTER)

        #number left

        left = 10

        left_label = tkinter.Label(frame, text=f"تعداد {left} عدد باقی مانده", font=font_dasnevis_0, fg="white", bg=self.color_palette[2])
        left_label.place(x=330, y=100, anchor=tkinter.CENTER)

        #plus button

        def plus_buuton():
            nonlocal count
            nonlocal count_label
            if(left > 0):
                count += 1
                count_label.configure(text=count)

        plus_button = tkinter.Button(frame, image=self.item_ui_image.plus, bg=self.color_palette[2],
         highlightthickness=0, bd=0, activebackground=self.color_palette[2], command=plus_buuton)
        plus_button.image = self.item_ui_image.plus
        plus_button.place(x=330+50, y=60, anchor=tkinter.CENTER)

        #minus button

        def minus_buuton():
            nonlocal count
            nonlocal count_label
            if(count > 0):
                count -= 1
                count_label.configure(text=count)

        minus_button = tkinter.Button(frame, image=self.item_ui_image.minus, bg=self.color_palette[2],
         highlightthickness=0, bd=0, activebackground=self.color_palette[2], command=minus_buuton)
        minus_button.image = self.item_ui_image.minus
        minus_button.place(x=330-50, y=60, anchor=tkinter.CENTER)

        #add button

        def add():
            nonlocal count, left
            nonlocal count_label, left_label
            left += count
            count = 0
            left_label.configure(text=f"تعداد {left} عدد باقی مانده")
            count_label.configure(text=count)

        minus_button = tkinter.Button(frame, image=self.item_ui_image.add, bg=self.color_palette[2],
         highlightthickness=0, bd=0, activebackground=self.color_palette[2], command=add)
        minus_button.image = self.item_ui_image.add
        minus_button.place(x=330, y=145, anchor=tkinter.CENTER)

        #image

        food_img = Image.open(os.path.join(sys.path[0], "resources\panels\\pitza.jpg")).convert("RGBA")
        food_image = food_img.resize((200,200), Image.ANTIALIAS)
        mask_img = Image.open(os.path.join(sys.path[0], "resources\panels\\food_image_mask.png")).convert("RGBA")
        food_image.paste(mask_img, (0, 0), mask_img)
        food_image_with_mask = ImageTk.PhotoImage(food_image)

        image_label = tkinter.Label(frame, image=food_image_with_mask, highlightthickness=0, bd=0)
        image_label.image = food_image_with_mask
        image_label.place(x=0,y=0)

    def change_order_frame(self, frame_name):
        for frame in self.oderes_frames.values():
            frame.place_forget()
        self.oderes_frames[frame_name].place(x=20, y=100)
        self.top_bar.hide()
        self.top_bar.show()

    def show(self):
        self.place(x=20, y=20)

    def hide(self):
        self.place_forget()
    
class Food_manu_top_bar(tkinter.Frame):
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
        frame_dict = {Types[0]:"unaccepted_orders_frame",Types[1]:"accepted_orders_frame",Types[2]:"completed_orders_frame"}

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

class Drop_Down_Menu(tkinter.OptionMenu):
    def __init__(self, master, variable, values, font_=None, font_color="black", color1="white", color2="blue"):
        super().__init__(master, variable, *values)
        self.config(font=font_, fg=font_color, bg=color2, activebackground=color1, activeforeground=font_color,
         highlightthickness=0, bd=0, indicatoron=0)
        self["menu"].config(font=font_, fg=font_color, bg=color1, activebackground=color2, 
         activeforeground=font_color, relief=tkinter.FLAT, bd=0)

class Food_Item_ScrollableFrame(ttk.Frame):
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