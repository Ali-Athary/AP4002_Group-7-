from time import sleep
import tkinter
from tkinter import font, ttk
from PIL import ImageTk, Image  
import os
import sys
import jdatetime
import threading
from modules import Food, functions, UserAndManager

class Discount_panel(tkinter.Label):
    def __init__(self, root, color_palette, admin:UserAndManager.Manager):
        self.color_palette = color_palette
        img = Image.open(os.path.join(sys.path[0], "resources\panels\\simple_panel.png")).convert("RGBA")
        image = ImageTk.PhotoImage(img)

        super().__init__(root, image=image, bg=color_palette[4], bd=0)
        self.image = image
        self.pack_propagate(0)

        font1 = font.Font(family="Mj_Flow", size=24)
        font2 = font.Font(family="Dast Nevis", size=24)
        font_english = font.Font(family="Roboto", size=30)

        #middle frame

        frame = tkinter.Frame(self, bg=color_palette[3], highlightthickness=0, bd=0)
        frame.pack(expand=True, fill="none")
        
        bg_img = Image.open(os.path.join(sys.path[0], "resources\panels\\profile_info_background.png")).convert("RGBA")
        bg_image = ImageTk.PhotoImage(bg_img)

        bg_label = tkinter.Label(frame, image=bg_image, highlightthickness=0, bd=0, bg=color_palette[3])
        bg_label.image = bg_image
        bg_label.pack()


        # title 

        title_frame = tkinter.Frame(frame, width=600, height=80, bg=self.color_palette[3])
        title_frame.pack_propagate(0)
        title_frame.place(x=340, y=80, anchor=tkinter.CENTER)
        tkinter.Label(title_frame, text="ایجاد کد تخفیف",
         font=font2, bg=self.color_palette[3]).pack(side=tkinter.RIGHT, padx=20)


        #code

        code_var = tkinter.StringVar()
        tkinter.Entry(frame, textvariable=code_var, bg=color_palette[4], font=font_english,
         highlightthickness=0, bd=0).place(x=340, y=230, anchor=tkinter.CENTER)

        #value

        code_value = tkinter.StringVar()
        tkinter.Entry(frame, textvariable=code_var, bg=color_palette[4], font=font_english,
         highlightthickness=0, bd=0).place(x=340, y=310, anchor=tkinter.CENTER)

        #submit

        def submit():
            pass

        submit_img = Image.open(os.path.join(sys.path[0], "resources\icons\\confirm.png")).convert("RGBA")
        submit_image = ImageTk.PhotoImage(submit_img)

        submit_complete_button = tkinter.Button(frame, bg=color_palette[3], image=submit_image,
         highlightthickness=0, bd=0, activebackground=color_palette[3], command=submit)
        submit_complete_button.image = submit_image
        submit_complete_button.place(x=340, y=480, anchor=tkinter.CENTER)

    def update_page(self):
        pass

    def show(self):
        self.place(x=20, y=20)

    def hide(self):
        self.place_forget()
