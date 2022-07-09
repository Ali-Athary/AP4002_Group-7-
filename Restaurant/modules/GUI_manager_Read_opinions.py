import tkinter
from tkinter import font, ttk
from PIL import ImageTk, Image  
import os
import sys
import jdatetime
from modules import Food, functions, UserAndManager

class Item_UI_images():
    def __init__(self) -> None:
        header_img = Image.open(os.path.join(sys.path[0], "resources\panels\\history_item_header.png")).convert("RGBA")
        self.header  = ImageTk.PhotoImage(header_img)
        
class Opinion_panel(tkinter.Label):
    def __init__(self, root, color_palette, _admin:UserAndManager.Manager):
        global admin
        admin = _admin
        self.color_palette = color_palette
        img = Image.open(os.path.join(sys.path[0], "resources\panels\\simple_panel.png")).convert("RGBA")
        image = ImageTk.PhotoImage(img)

        super().__init__(root, image=image, bg=color_palette[4], bd=0)
        self.image = image

        self.ui_images = Item_UI_images()

        font1 = font.Font(family="Mj_Flow", size=19)
        font2 = font.Font(family="Dast Nevis", size=30)
        font_English = font.Font(family="Roboto", size=18)

        # title

        title_frame = tkinter.Frame(self, width=900, height=60, bg=self.color_palette[3],
         highlightthickness=0, bd=0)
        title_frame.pack_propagate(0)
        title_frame.place(x=20, y=20)
        
        tkinter.Label(title_frame, text="نظرات کاربر ها", bg=self.color_palette[3], font=font2).pack(side=tkinter.RIGHT)


        #items frame

        self.item_frame = Item_ScrollableFrame(self, color_palette)
        self.item_frame.place(x=20, y=100)

        opinion_list = admin.view_comments()
        for opinion in opinion_list:
            self.item_frame.add_item(opinion)

    def Add_cart_item(self, food_log):
        if(isinstance(food_log, Food.FoodLog)):

            font1 = font.Font(family="Mj_Flow", size=19)
            font2 = font.Font(family="Dast Nevis", size=19)

            item_frame = tkinter.Frame(self.item_frame.scrollable_frame, width=980, height=60, bg=self.color_palette[4],
                highlightbackground=self.color_palette[2], highlightthickness=2)
            item_frame.pack_propagate(0)
            item_frame.pack(pady=6)

            tkinter.Label(item_frame, text=food_log.name, font=font2, width=12,
                bg=self.color_palette[4]).pack(side=tkinter.RIGHT, padx=4)
            tkinter.Label(item_frame, text="", font=font2, bg=self.color_palette[2]).pack(side=tkinter.RIGHT)
            tkinter.Label(item_frame, text=food_log.count, font=font2, width=8,
                bg=self.color_palette[4]).pack(side=tkinter.RIGHT, padx=4)
            tkinter.Label(item_frame, text="", font=font2, bg=self.color_palette[2]).pack(side=tkinter.RIGHT)
            tkinter.Label(item_frame, text=functions.turn_int_to_price(food_log.price * food_log.count), font=font2, width=10,
                bg=self.color_palette[4]).pack(side=tkinter.RIGHT, padx=4)
            tkinter.Label(item_frame, text="", font=font2, bg=self.color_palette[2]).pack(side=tkinter.RIGHT)
            tkinter.Label(item_frame, text=functions.turn_int_to_price(food_log.original_price * food_log.count), font=font2, width=12,
                bg=self.color_palette[4]).pack(side=tkinter.RIGHT, padx=4)
            tkinter.Label(item_frame, text="", font=font2, bg=self.color_palette[2]).pack(side=tkinter.RIGHT)
            tkinter.Label(item_frame, text=functions.turn_int_to_price((food_log.price - food_log.original_price) * food_log.count), font=font2, width=10,
                bg=self.color_palette[4]).pack(side=tkinter.RIGHT, padx=4)
            

    def show(self):
        self.place(x=20, y=20)

    def hide(self):
        self.place_forget()

class Item_ScrollableFrame(ttk.Frame):
    def __init__(self, container, color_palette, *args, **kwargs):
        self.color_palette = color_palette
        super().__init__(container, *args, **kwargs)
        
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Vertical.TScrollbar", gripcount=0, arrowsize=30,
                background=color_palette[2], darkcolor=color_palette[1], lightcolor=color_palette[1],
                troughcolor=color_palette[4], bordercolor=color_palette[3], arrowcolor=color_palette[1],
                activerelief=tkinter.FLAT, relief=tkinter.FLAT)

        canvas = tkinter.Canvas(self, height=550, width=990, bg=color_palette[3], bd=0, highlightthickness=0)
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
    
    def add_item(self, opinion):
        #item frame

        frame = tkinter.Frame(self.scrollable_frame, width=980, height=200, bg=self.color_palette[3],
         highlightthickness=0, bd=0)
        frame.pack(pady=6)

        font1 = font.Font(family="Mj_Flow", size=20)
        font2 = font.Font(family="Dast Nevis", size=20)
        font_english = font.Font(family="Roboto", size=20)

        #info frame

        info_frame = tkinter.Frame(frame, width=980, height=60, bg=self.color_palette[4],
         highlightthickness=0, bd=0)
        info_frame.pack_propagate(0)
        info_frame.pack()
        
        #name

        tkinter.Label(info_frame, text=" ", bg=self.color_palette[4], font=font1).pack(side=tkinter.RIGHT, padx=4)
        tkinter.Label(info_frame, text="نام کاربر", bg=self.color_palette[4], font=font1).pack(side=tkinter.RIGHT)
        tkinter.Label(info_frame, text=":", bg=self.color_palette[4], font=font1).pack(side=tkinter.RIGHT, padx=4)
        tkinter.Label(info_frame, text=opinion[2], bg=self.color_palette[4], font=font1).pack(side=tkinter.RIGHT)

        #date

        tkinter.Label(info_frame, text=" ", bg=self.color_palette[4], font=font1).pack(side=tkinter.LEFT, padx=4)
        tkinter.Label(info_frame, text="1401/04/18", bg=self.color_palette[4], font=font1).pack(side=tkinter.LEFT)
        tkinter.Label(info_frame, text=":", bg=self.color_palette[4], font=font1).pack(side=tkinter.LEFT, padx=4)
        tkinter.Label(info_frame, text=opinion[1], bg=self.color_palette[4], font=font1).pack(side=tkinter.LEFT)

        #text

        text_box = tkinter.Text(frame, height=9, width=68, font=font1, bg="white", highlightthickness=0, bd=0)
        text_box.tag_configure('tag-right', justify='right')
        text_box.insert('end', opinion[0], 'tag-right')
        text_box.config(state='disabled')
        text_box.pack()
