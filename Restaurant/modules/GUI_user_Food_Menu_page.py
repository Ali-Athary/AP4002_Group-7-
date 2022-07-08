import tkinter
from tkinter import font, ttk
from PIL import ImageTk, Image  
import os
import sys
import jdatetime
from modules import Food, functions, UserAndManager

class Food_item_UI_images():
    def __init__(self):
        background_img = Image.open(os.path.join(sys.path[0], "resources\panels\\food_item_base.png")).convert("RGBA")
        self.background = ImageTk.PhotoImage(background_img)

        plus_img = Image.open(os.path.join(sys.path[0], "resources\icons\\plus.png")).convert("RGBA")
        self.plus = ImageTk.PhotoImage(plus_img.resize((40,40), Image.ANTIALIAS))

        minus_img = Image.open(os.path.join(sys.path[0], "resources\icons\\minus.png")).convert("RGBA")
        self.minus = ImageTk.PhotoImage(minus_img.resize((40,40), Image.ANTIALIAS))

        buy_img = Image.open(os.path.join(sys.path[0], "resources\icons\\buy_button.png")).convert("RGBA")
        self.buy = ImageTk.PhotoImage(buy_img)

class Food_menu_panel(tkinter.Label):
    def __init__(self, root, color_palette, _user:UserAndManager.User, cart_page):
        global user
        user = _user
        self.cart_page = cart_page
        self.color_palette = color_palette
        img = Image.open(os.path.join(sys.path[0], "resources\panels\\user_food_menu_panel.png")).convert("RGBA")
        image = ImageTk.PhotoImage(img)

        super().__init__(root, image=image, bg=color_palette[4], bd=0)
        self.image = image

        #top bar

        self.top_bar = Food_manu_top_bar(self, color_palette)
        self.top_bar.show()

        #food items frame

        self.food_frame = Food_Item_ScrollableFrame(self, color_palette)
        self.food_frame.place(x=20, y=100)

        self.item_ui_image = Food_item_UI_images()

        self.items = []

        food_list = Food.Food.food_list
        for food in food_list:
            self.add_food_to_list(food)

    def add_food_to_list(self, food:Food.Food):
        #item frame

        frame = tkinter.Frame(self.food_frame.scrollable_frame, width=980, height=200, bg=self.color_palette[3])
        frame.pack()

        self.items.append(frame)

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

        tkinter.Label(frame, text=food.name, fg="white", bg=self.color_palette[2], font=font_dasnevis_2).place(x=940, y=30, anchor=tkinter.NE)

        #price 

        price_frame = tkinter.Frame(frame, width=160, height=40, bg=self.color_palette[2])
        price_frame.place(x=940, y=120, anchor=tkinter.NE)

        tkinter.Label(price_frame, text=functions.turn_int_to_price(food.price), fg="white",
         bg=self.color_palette[2], font=font_dasnevis_0).grid(row=0, column=1)
        tkinter.Label(price_frame, text="تومان", fg="white",
         bg=self.color_palette[2], font=font_dasnevis_0).grid(row=0, column=0, padx=6)

        #descriptiona

        descriptiona_frame = tkinter.Frame(frame, width=300, height=120, bg=self.color_palette[2])
        descriptiona_frame.pack_propagate(0)
        descriptiona_frame.place(x=740, y=40, anchor=tkinter.NE)

        ingrediente = food.discription

        f = tkinter.Frame(descriptiona_frame, bg=self.color_palette[2])
        f.pack(expand=True, fill="none")

        for line in ingrediente:
            tkinter.Label(f, text=line, bg=self.color_palette[2], font=font_dasnevis_0).pack()

        #count

        count = 0

        count_label = tkinter.Label(frame, text=count, font=font_dasnevis_1, fg="white", bg=self.color_palette[2])
        count_label.place(x=330, y=60, anchor=tkinter.CENTER)

        #number left

        left = food.amount

        left_label = tkinter.Label(frame, text=f"تعداد {left} عدد باقی مانده", font=font_dasnevis_0, fg="white", bg=self.color_palette[2])
        left_label.place(x=330, y=100, anchor=tkinter.CENTER)

        #plus button

        def plus_buuton():
            nonlocal count, left
            nonlocal count_label, left_label
            if(left > 0):
                count += 1
                left -= 1
                count_label.configure(text=count)
                left_label.configure(text=f"تعداد {left} عدد باقی مانده")

        plus_button = tkinter.Button(frame, image=self.item_ui_image.plus, bg=self.color_palette[2],
         highlightthickness=0, bd=0, activebackground=self.color_palette[2], command=plus_buuton)
        plus_button.image = self.item_ui_image.plus
        plus_button.place(x=330+50, y=60, anchor=tkinter.CENTER)

        #minus button

        def minus_buuton():
            nonlocal count, left
            nonlocal count_label, left_label
            if(count > 0):
                count -= 1
                left += 1
                count_label.configure(text=count)
                left_label.configure(text=f"تعداد {left} عدد باقی مانده")

        minus_button = tkinter.Button(frame, image=self.item_ui_image.minus, bg=self.color_palette[2],
         highlightthickness=0, bd=0, activebackground=self.color_palette[2], command=minus_buuton)
        minus_button.image = self.item_ui_image.minus
        minus_button.place(x=330-50, y=60, anchor=tkinter.CENTER)

        #buy button

        def buy():
            nonlocal count
            nonlocal count_label, left_label
            user.add_food_to_order_list(food, count, self.top_bar.get_date())
            count = 0
            count_label.configure(text=count)
            left_label.configure(text=f"تعداد {food.amount} عدد باقی مانده")
            self.cart_page.update_page()


        minus_button = tkinter.Button(frame, image=self.item_ui_image.buy, bg=self.color_palette[2],
         highlightthickness=0, bd=0, activebackground=self.color_palette[2], command=buy)
        minus_button.image = self.item_ui_image.buy
        minus_button.place(x=330, y=145, anchor=tkinter.CENTER)

        #image

        food_img = food.picture
        food_image = food_img.resize((200,200), Image.ANTIALIAS)
        mask_img = Image.open(os.path.join(sys.path[0], "resources\panels\\food_image_mask.png")).convert("RGBA")
        food_image.paste(mask_img, (0, 0), mask_img)
        food_image_with_mask = ImageTk.PhotoImage(food_image)

        image_label = tkinter.Label(frame, image=food_image_with_mask, highlightthickness=0, bd=0)
        image_label.image = food_image_with_mask
        image_label.place(x=0,y=0)

    def update_page(self):
        for item in self.items:
            item.pack_forget()
        self.items = []

        self.item_ui_image = Food_item_UI_images()

        food_list = Food.Food.food_list
        for food in food_list:
            self.add_food_to_list(food)

    def show(self):
        self.place(x=20, y=20)

    def hide(self):
        self.place_forget()
    
class Food_manu_top_bar(tkinter.Frame):
    def __init__(self, root, color_palette):
        super().__init__(root, width=1000, height=60, bg=color_palette[3])
        self.grid_propagate(0)

        font1 = font.Font(family="Mj_Flow", size=25)
        font2 = font.Font(family="Dast Nevis", size=30)

        # Date

        date_frame = tkinter.Frame(self, width=200, height=55, bg=color_palette[3])
        date_frame.grid_propagate(0)
        date_frame.place(x=0,y=0)

        # year

        tkinter.Label(date_frame, text = f"{jdatetime.datetime.now().year}/", font=font2, fg=color_palette[0],
         bg=color_palette[3]).grid(row=0, column=0)

        # month

        self.month_var = tkinter.StringVar()

        self.months = [jdatetime.datetime.now().month, (jdatetime.datetime.now() + jdatetime.timedelta(days=30)).month]
        self.month_var.set(self.months[0])
        month_menu = Drop_Down_Menu(date_frame, self.month_var, self.months, font_=font2,
         font_color=color_palette[0], color1=color_palette[3], color2=color_palette[4])
        month_menu.grid(row=0, column=1)

        tkinter.Label(date_frame, text = f"/", font=font2, fg=color_palette[0],
         bg=color_palette[3]).grid(row=0, column=2)

        # day

        self.day_var = tkinter.StringVar()
        self.days1 = [str(x) for x in range(jdatetime.datetime.now().day, jdatetime.j_days_in_month[self.months[0]] + 1)]
        self.day_var.set(self.days1[0])
        self.day_menu1 = Drop_Down_Menu(date_frame, self.day_var, self.days1, font_=font2,
         font_color=color_palette[0], color1=color_palette[3], color2=color_palette[4])
        self.day_menu1.grid(row=0, column=3)

        self.days2 = [str(x) for x in range(1, jdatetime.j_days_in_month[self.months[1]] + 1)]
        self.day_menu2 = Drop_Down_Menu(date_frame, self.day_var, self.days2, font_=font2,
         font_color=color_palette[0], color1=color_palette[3], color2=color_palette[4])

        #change month

        self.month_var.trace("w", lambda x, y, z:self.change_month())

        # Search

        search_frame = tkinter.Frame(self, width=240, height=60, bg="yellow")
        search_frame.pack_propagate(0)
        search_frame.place(x=1000,y=0, anchor=tkinter.NE)

        # sreach button

        sreach_img = Image.open(os.path.join(sys.path[0], "resources\icons\search.png")).convert("RGBA")
        sreach_image = ImageTk.PhotoImage(sreach_img)

        sreach_button = tkinter.Button(search_frame, bg=color_palette[3], image=sreach_image,
         highlightthickness=0, bd=0)
        sreach_button.image = sreach_image
        sreach_button.pack(fill="none", expand=True) 

    def get_date(self):
        return f"{jdatetime.datetime.now().year}/{self.month_var.get()}/{self.day_var.get()}"

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