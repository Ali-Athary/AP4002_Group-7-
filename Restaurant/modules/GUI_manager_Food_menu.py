import tkinter
from tkinter import font, ttk, filedialog
from PIL import ImageTk, Image  
import os
import sys
import jdatetime

class Item_UI_images():
    def __init__(self):
        background_img = Image.open(os.path.join(sys.path[0], "resources\panels\\food_item_base.png")).convert("RGBA")
        self.background = ImageTk.PhotoImage(background_img.resize((720,200), Image.ANTIALIAS))

        delete_img = Image.open(os.path.join(sys.path[0], "resources\icons\\trash-bin.png")).convert("RGBA")
        self.delete = ImageTk.PhotoImage(delete_img.resize((64,64), Image.ANTIALIAS))

class Food_menu_panel(tkinter.Label):
    def __init__(self, root, color_palette):
        self.color_palette = color_palette
        img = Image.open(os.path.join(sys.path[0], "resources\panels\\user_food_menu_panel.png")).convert("RGBA")
        image = ImageTk.PhotoImage(img)

        super().__init__(root, image=image, bg=color_palette[4], bd=0)
        self.image = image

        #top bar

        top_bar = Food_inventory_top_bar(self, color_palette)
        top_bar.show()

        #food items frame

        self.food_frame = Food_Item_ScrollableFrame(self, color_palette)
        self.food_frame.place(x=20, y=100)

        self.item_ui_image = Item_UI_images()

        for i in range(20):
            self.add_food_to_list("پیتزا پپرونی", 140000)

        #add food panel

        self.add_panel = Add_food_panel(self, color_palette)

    def add_food_to_list(self, name, price):
        #item frame

        frame = tkinter.Frame(self.food_frame.scrollable_frame, width=980, height=200, bg=self.color_palette[3])
        frame.pack()

        #background

        background = tkinter.Label(frame, image=self.item_ui_image.background, bg=self.color_palette[3])
        background.image = self.item_ui_image.background
        background.place(x=260,y=0)

        #fonts

        font1 = font.Font(family="Mj_Flow", size=20)
        font_dasnevis_0 = font.Font(family="Dast Nevis", size=18)
        font_dasnevis_1 = font.Font(family="Dast Nevis", size=30)
        font_dasnevis_2 = font.Font(family="Dast Nevis", size=35)

        #button frame

        price_frame = tkinter.Frame(frame, width=160, height=140, bg=self.color_palette[3])
        price_frame.pack_propagate(0)
        price_frame.place(x=180, y=30, anchor=tkinter.NE)

        delete_button = tkinter.Button(price_frame, image=self.item_ui_image.delete, bg=self.color_palette[3],
         activebackground=self.color_palette[3], highlightthickness=0, bd=0)
        delete_button.image = self.item_ui_image.delete
        delete_button.pack(pady=12)

        tkinter.Label(price_frame, text="حذف", bg=self.color_palette[3], font=font1).pack(pady=12)

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

        #image

        food_img = Image.open(os.path.join(sys.path[0], "resources\panels\\pitza.jpg")).convert("RGBA")
        food_image = food_img.resize((200,200), Image.ANTIALIAS)
        mask_img = Image.open(os.path.join(sys.path[0], "resources\panels\\food_image_mask.png")).convert("RGBA")
        food_image.paste(mask_img, (0, 0), mask_img)
        food_image_with_mask = ImageTk.PhotoImage(food_image)

        image_label = tkinter.Label(frame, image=food_image_with_mask, highlightthickness=0, bd=0)
        image_label.image = food_image_with_mask
        image_label.place(x=200,y=0)

    def show(self):
        self.place(x=20, y=20)

    def hide(self):
        self.place_forget()

class Add_food_panel(tkinter.Frame):
    def __init__(self, root, color_palette):
        self.color_palette = color_palette
        super().__init__(root, width=1060, height=680, bg=color_palette[4], bd=0, highlightthickness=0)
        self.pack_propagate(0)

        font1 = font.Font(family="Mj_Flow", size=18)
        font2 = font.Font(family="Dast Nevis", size=20)
        font_english = font.Font(family="Roboto", size=20)

        #background
        
        img = Image.open(os.path.join(sys.path[0], "resources\panels\\simple_panel.png")).convert("RGBA")
        image = ImageTk.PhotoImage(img)

        background = tkinter.Label(self, image=image, bg=self.color_palette[3], bd=0)
        background.image = image
        background.place(x=0, y=0)

        #info frame

        img = Image.open(os.path.join(sys.path[0], "resources\panels\\profile_info_background.png")).convert("RGBA")
        image = ImageTk.PhotoImage(img)

        info_background = tkinter.Label(self, image=image, bg=self.color_palette[3], bd=0)
        info_background.image = image
        info_background.pack_propagate(0)
        info_background.place(x=530, y=340, anchor=tkinter.CENTER)

        frame = tkinter.Frame(info_background, bg=self.color_palette[3])
        frame.pack(expand=True, fill="none")

        #title

        tkinter.Label(frame, text="اضافه کردن محصول به منو", font=font1, bg=self.color_palette[3]).grid(row=0, column=0, columnspan=2, padx=8, pady=8)

        #name

        tkinter.Label(frame, text="نام محصول", font=font1, bg=self.color_palette[3]).grid(row=1, column=1, padx=8, pady=4)
        
        name_var = tkinter.StringVar()
        name_entry = tkinter.Entry(frame, textvariable=name_var,  width=22, justify=tkinter.RIGHT,
         font=font2, highlightcolor=self.color_palette[4], highlightthickness=0, bd=0)
        name_entry.grid(row=1, column=0, padx=8, pady=4)

        #price

        tkinter.Label(frame, text="قیمت (تومان)", font=font1, bg=self.color_palette[3]).grid(row=2, column=1, padx=8, pady=4)
        
        name_var = tkinter.StringVar()
        name_entry = tkinter.Entry(frame, textvariable=name_var,  width=22,
         font=font2, highlightcolor=self.color_palette[4], highlightthickness=0, bd=0)
        name_entry.grid(row=2, column=0, padx=8, pady=4)

        #description and ingredients

        tkinter.Label(frame, text="توضیحات خط اول", font=font1, bg=self.color_palette[3]).grid(row=3, column=1, padx=8, pady=4)
        
        description1_var = tkinter.StringVar()
        description1_entry = tkinter.Entry(frame, textvariable=description1_var,  width=22, justify=tkinter.RIGHT,
         font=font2, highlightcolor=self.color_palette[4], highlightthickness=0, bd=0)
        description1_entry.grid(row=3, column=0, padx=8, pady=4)

        tkinter.Label(frame, text="توضیحات خط دوم", font=font1, bg=self.color_palette[3]).grid(row=4, column=1, padx=8, pady=4)
        
        description2_var = tkinter.StringVar()
        description2_entry = tkinter.Entry(frame, textvariable=description2_var,  width=22, justify=tkinter.RIGHT,
         font=font2, highlightcolor=self.color_palette[4], highlightthickness=0, bd=0)
        description2_entry.grid(row=4, column=0, padx=8, pady=4)

        #choose picture

        def choose_picture():
            file_directory = filedialog.askopenfilename(title='select', filetypes=[
                    ("image", ".jpeg"),
                    ("image", ".png"),
                    ("image", ".jpg"),
                ])
            print(file_directory)

        tkinter.Label(frame, text="انتخاب تصویر", font=font1, bg=self.color_palette[3]).grid(row=5, column=1, padx=8, pady=4)

        choose_img = Image.open(os.path.join(sys.path[0], "resources\icons\choose.png"))
        picture_image = ImageTk.PhotoImage(choose_img)

        choose_picture_button = tkinter.Button(frame, image=picture_image, bg=self.color_palette[3],
         activebackground=self.color_palette[3], highlightthickness=0, bd=0, command=lambda:choose_picture())
        choose_picture_button.image = picture_image
        choose_picture_button.grid(row=5, column=0, padx=8, pady=4)

        #error massage

        error_message = tkinter.Label(frame, text=" \n ", font=font2, fg=self.color_palette[2], bg=self.color_palette[3])
        error_message.grid(row=6, column=0, columnspan=2, padx=8, pady=4)

        #confirm button

        def confirm():
            name_var.set("")
            description1_var.set("")
            description2_var.set("")
            self.hide()

        confirm_img = Image.open(os.path.join(sys.path[0], "resources\icons\confirm.png"))
        confirm_image = ImageTk.PhotoImage(confirm_img)

        confirm_button = tkinter.Button(frame, image=confirm_image, bg=self.color_palette[3],
         highlightthickness=0, bd=0, activebackground=self.color_palette[3], command=confirm)
        confirm_button.image = confirm_image
        confirm_button.grid(row=7, column=0, columnspan=2, padx=8, pady=4)

    def show(self):
        self.place(x=0, y=0)

    def hide(self):
        self.place_forget()

class Food_inventory_top_bar(tkinter.Frame):
    def __init__(self, root, color_palette):
        super().__init__(root, width=1000, height=60, bg=color_palette[3])
        self.pack_propagate(0)

        font1 = font.Font(family="Mj_Flow", size=25)
        font2 = font.Font(family="Dast Nevis", size=20)

        # title

        tkinter.Label(self, text="منو محصولات رستوران", bg=color_palette[3], font=font1).pack(side=tkinter.RIGHT, padx=30)

        # add button

        add_img = Image.open(os.path.join(sys.path[0], "resources\icons\plus2.png"))
        add_img = add_img.resize((60,60), Image.ANTIALIAS)
        add_image = ImageTk.PhotoImage(add_img)
        add_image_button = tkinter.Button(self, image=add_image, bg=color_palette[3],
         activebackground=color_palette[3], highlightthickness=0, bd=0, command=lambda:root.add_panel.show())
        add_image_button.image = add_image
        add_image_button.pack(side=tkinter.LEFT, padx=2)

        tkinter.Label(self, text="اضافه کردن محصول", bg=color_palette[3], font=font2).pack(side=tkinter.LEFT, padx=8)


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