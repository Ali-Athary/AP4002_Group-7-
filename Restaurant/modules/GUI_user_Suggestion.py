from time import sleep
import tkinter
from tkinter import font, ttk
from PIL import ImageTk, Image  
import os
import sys
import jdatetime
import threading
from modules import Food, functions, UserAndManager

class Suggestion_panel(tkinter.Label):
    def __init__(self, root, color_palette, _user:UserAndManager.User):
        global user
        user = _user
        self.color_palette = color_palette
        img = Image.open(os.path.join(sys.path[0], "resources\panels\\simple_panel.png")).convert("RGBA")
        image = ImageTk.PhotoImage(img)

        super().__init__(root, image=image, bg=color_palette[4], bd=0)
        self.image = image
        self.pack_propagate(0)

        font1 = font.Font(family="Mj_Flow", size=24)
        font2 = font.Font(family="Dast Nevis", size=24)

        # title 

        title_frame = tkinter.Frame(self, width=1000, height=80, bg=self.color_palette[3])
        title_frame.pack_propagate(0)
        title_frame.pack(pady=10)
        tkinter.Label(title_frame, text="نظرات خود را برای بهبود عملکرد ما در کادر زیر بنویسید",
         font=font2, bg=self.color_palette[3]).pack(side=tkinter.RIGHT, padx=20)

        #text box frame

        text_background_img = Image.open(os.path.join(sys.path[0], "resources\panels\\suggestion_tex_background.png")).convert("RGBA")
        text_background_image = ImageTk.PhotoImage(text_background_img)

        text_frame = tkinter.Label(self, image = text_background_image, bg=self.color_palette[3])
        text_frame.image = text_background_image
        text_frame.pack()

        text_box = tkinter.Text(text_frame, height=9, width=52, font=font1, bg="#e2e2e2", highlightthickness=0, bd=0)
        
        text_box.tag_configure('tag-right', justify='right')

        def Right_to_Left(key):
            if key.keycode in [8, 13, 32, 48, 49, 50, 51, 52, 53, 54, 55, 
            56, 57, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 
            77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 
            186, 187, 188, 189, 190, 191, 192, 219, 220, 221, 222]:
                text_str =  text_box.get("1.0",tkinter.END)
                if(key.char != '\n'):
                    text_str = text_str[:-1]
                text_box.delete("1.0", tkinter.END)
                text_box.insert('end', text_str, 'tag-right')

        text_box.place(x=960/2, y=30, anchor=tkinter.N)
        text_box.bind("<KeyRelease>", Right_to_Left)

        #submit

        def submit():
            opinion = text_box.get("1.0",tkinter.END)
            user.submit_opinion(opinion)

        submit_img = Image.open(os.path.join(sys.path[0], "resources\icons\\submit.png")).convert("RGBA")
        submit_image = ImageTk.PhotoImage(submit_img)

        submit_complete_button = tkinter.Button(self, bg=color_palette[3], image=submit_image,
         highlightthickness=0, bd=0, activebackground=color_palette[3], command=submit)
        submit_complete_button.image = submit_image
        submit_complete_button.pack()

    def update_page(self):
        pass

    def show(self):
        self.place(x=20, y=20)

    def hide(self):
        self.place_forget()
