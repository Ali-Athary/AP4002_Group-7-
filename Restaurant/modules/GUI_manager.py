import tkinter
from tkinter import font, ttk
from PIL import ImageTk, Image  
import os
import sys
from modules import GUI_restaurant_Profile, GUI_user_Profile

pages = {}
active_page_name = ""

def set_profile_info(**kwargs):
    global profile_info
    profile_info = Profile_info(**kwargs)

def change_page(name):
    global active_page_name, pages

    if(active_page_name == name):
        return

    pages[active_page_name].hide()
    pages[name].show()
    pages["right_menu"].hide()
    pages["right_menu"].show()

    active_page_name = name


def main(root, color_palette):
    global active_page_name, pages
    set_profile_info()

    #main frame
    img = Image.open(os.path.join(sys.path[0], "resources\panels\\main_panel_background.png")).convert("RGBA")
    image = ImageTk.PhotoImage(img)

    main_frame = tkinter.Label(root, image=image, bg=color_palette[4])
    main_frame.image = image
    main_frame.pack(fill="none", expand=True) 

    #right menu

    right_menu = Right_menu(main_frame, color_palette)
    pages["right_menu"] = right_menu
    right_menu.show()

    # user profile

    food_menu_page = GUI_user_Profile.Profile_panel(main_frame, color_palette)
    pages["user_profile"] = food_menu_page

    #restaurant profile panel

    food_menu_page = GUI_restaurant_Profile.Profile_panel(main_frame, color_palette)
    pages["restaurant_profile"] = food_menu_page

    active_page_name = "restaurant_profile"
    food_menu_page.show()

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
         activebackground=color_palette[4], highlightthickness=0, bd=0, command=lambda:change_page("user_profile"))
        profile_image_label.image = profile_image
        profile_image_label.pack()   

        #profile name

        profile_image_label = tkinter.Button(profile_frame,text=profile_info.name, font=font1, bg=color_palette[4],
         activebackground=color_palette[4], highlightthickness=0, bd=0, command=lambda:change_page("user_profile")).pack()

        #button frame

        button_frame = tkinter.Frame(self, bg=color_palette[4])
        button_frame.pack(pady=40)

        #Restaurant information button

        Restaurant_information_button = tkinter.Button(button_frame, text="اطلاعات رستوران", bg=color_palette[2], width=22, font=font1,
         activebackground=color_palette[2], highlightthickness=0, bd=0, command=lambda:change_page("restaurant_profile"))
        Restaurant_information_button.pack(pady=6)

        #inventory button

        inventory_button = tkinter.Button(button_frame, text="موجودی غذا", bg=color_palette[2], width=22, font=font1,
         activebackground=color_palette[2], highlightthickness=0, bd=0, command=lambda:change_page("cart"))
        inventory_button.pack(pady=6)

        #orders button

        orders_button = tkinter.Button(button_frame, text="سفارشات", bg=color_palette[2], width=22, font=font1,
         activebackground=color_palette[2], highlightthickness=0, bd=0, command=lambda:change_page("history"))
        orders_button.pack(pady=6)

        #Economic information button

        suggestion_button = tkinter.Button(button_frame, text="اطلاعات اقتصادی", bg=color_palette[2], width=22, font=font1,
         activebackground=color_palette[2], highlightthickness=0, bd=0, command=lambda:change_page("suggestion"))
        suggestion_button.pack(pady=6)

    def show(self):
        self.place(x=1090, y=40)

    def hide(self):
        self.place_forget()