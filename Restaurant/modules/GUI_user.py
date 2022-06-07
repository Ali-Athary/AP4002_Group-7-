import tkinter
from tkinter import font
from PIL import ImageTk, Image  
import os
import sys
import jdatetime

def set_profile_info(**kwargs):
    global profile_info
    profile_info = Profile_info(**kwargs)


def main(root, color_palette):
    #main frame
    set_profile_info()

    img = Image.open(os.path.join(sys.path[0], "resources\panels\\main_panel_background.png")).convert("RGBA")
    image = ImageTk.PhotoImage(img)

    main_frame = tkinter.Label(root, image=image, bg=color_palette[4])
    main_frame.image = image
    main_frame.pack(fill="none", expand=True) 

    #right menu

    right_menu = Right_menu(main_frame, color_palette)
    right_menu.show()

    right_menu = Food_menu_panel(main_frame, color_palette)
    right_menu.show()

class Profile_info():
    def __init__(self, profile_name = "نام کاربری", profile_image = Image.open(os.path.join(sys.path[0], "resources\panels\default_profile_picture.jpg")).convert("RGBA")):
        self.name = profile_name
        self.image = profile_image

class Right_menu(tkinter.Frame):
    def __init__(self, root, color_palette):
        super().__init__(root, width=160, height=640, bg=color_palette[4])
        self.pack_propagate(0)

        font1 = font.Font(family="Mj_Flow", size=20)

        #profile frame

        profile_frame = tkinter.Frame(self, bg=color_palette[4])
        profile_frame.pack()

        #profile picture

        profile_frame_image = Image.open(os.path.join(sys.path[0], "resources\panels\profile_photo_mask.png"))
        profile_img = profile_info.image.resize((128,128), Image.ANTIALIAS)
        profile_img.paste(profile_frame_image, (0, 0), profile_frame_image)
        profile_image = ImageTk.PhotoImage(profile_img)
        profile_image_label = tkinter.Button(profile_frame, image=profile_image, bg=color_palette[4],
         activebackground=color_palette[4], highlightthickness=0, bd=0)
        profile_image_label.image = profile_image
        profile_image_label.pack()   

        #profile name

        profile_image_label = tkinter.Button(profile_frame,text=profile_info.name, font=font1, bg=color_palette[4],
         activebackground=color_palette[4], highlightthickness=0, bd=0).pack()

        #button frame

        button_frame = tkinter.Frame(self, bg=color_palette[4])
        button_frame.pack(pady=40)

        #menu button

        menu_img = Image.open(os.path.join(sys.path[0], "resources\icons\menu.png")).convert("RGBA")
        menu_image = ImageTk.PhotoImage(menu_img)

        menu_button = tkinter.Button(button_frame, image=menu_image, bg=color_palette[4],
         activebackground=color_palette[4], highlightthickness=0, bd=0)
        menu_button.image = menu_image
        menu_button.grid(row=0, column=1)   

        tkinter.Label(button_frame, text="منو", font=font1, bg=color_palette[4], fg=color_palette[0]).grid(row=0, column=0)   

        #cart button

        cart_img = Image.open(os.path.join(sys.path[0], "resources\icons\cart.png")).convert("RGBA")
        cart_image = ImageTk.PhotoImage(cart_img)

        cart_button = tkinter.Button(button_frame, image=cart_image, bg=color_palette[4],
         activebackground=color_palette[4], highlightthickness=0, bd=0)
        cart_button.image = cart_image
        cart_button.grid(row=1, column=1)   

        tkinter.Label(button_frame, text="سبد خرید", font=font1, bg=color_palette[4], fg=color_palette[0]).grid(row=1, column=0)   

        #history button

        history_img = Image.open(os.path.join(sys.path[0], "resources\icons\history.png")).convert("RGBA")
        history_image = ImageTk.PhotoImage(history_img)

        history_button = tkinter.Button(button_frame, image=history_image, bg=color_palette[4],
         activebackground=color_palette[4], highlightthickness=0, bd=0)
        history_button.image = history_image
        history_button.grid(row=2, column=1)   

        tkinter.Label(button_frame, text="تاریخچه", font=font1, bg=color_palette[4], fg=color_palette[0]).grid(row=2, column=0)   

    def show(self):
        self.place(x=1090, y=40)

    def hide(self):
        self.place_forget()

class Food_menu_panel(tkinter.Label):
    def __init__(self, root, color_palette):
        img = Image.open(os.path.join(sys.path[0], "resources\panels\\user_food_menu_panel.png")).convert("RGBA")
        image = ImageTk.PhotoImage(img)

        super().__init__(root, image=image, bg=color_palette[4], bd=0)
        self.image = image

        font1 = font.Font(family="Mj_Flow", size=20)

        #top bar

        top_bar = Food_manu_top_bar(self, color_palette)
        top_bar.show()

    def show(self):
        self.place(x=20, y=20)

    def hide(self):
        self.place_forget()
    
class Food_manu_top_bar(tkinter.Frame):
    def __init__(self, root, color_palette):
        super().__init__(root, width=1000, height=60, bg=color_palette[3])

        font1 = font.Font(family="Mj_Flow", size=20)

    def show(self):
        self.place(x=30, y=2)

    def hide(self):
        self.place_forget()