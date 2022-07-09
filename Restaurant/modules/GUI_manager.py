import tkinter
from tkinter import font, ttk
from PIL import ImageTk, Image  
import os
import sys
from modules import GUI_manager_Inventory, GUI_restaurant_Profile, GUI_user_Profile, GUI_manager_Orders
from modules import GUI_manager_Financial, GUI_manager_Food_menu, UserAndManager, GUI_manager_Discount, GUI_manager_Read_opinions
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

def main(root, color_palette, _admin:UserAndManager.Manager):
    global active_page_name, pages
    global admin
    admin = _admin
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

    profile_page = GUI_user_Profile.Profile_panel(main_frame, color_palette, admin, right_menu)
    pages["user_profile"] = profile_page

    active_page_name = "user_profile"
    profile_page.show()

    #restaurant profile panel

    restaurant_Profile_page = GUI_restaurant_Profile.Profile_panel(main_frame, color_palette, admin)
    pages["restaurant_profile"] = restaurant_Profile_page

    #inventory panel

    inventory_page = GUI_manager_Inventory.Food_inventory_panel(main_frame, color_palette, admin)
    pages["inventory"] = inventory_page

    #orders panel

    orders_page = GUI_manager_Orders.Orders_panel(main_frame, color_palette, admin)
    pages["orders"] = orders_page

    #orders panel

    financial_page = GUI_manager_Financial.Information_panel(main_frame, color_palette, admin)
    pages["financial"] = financial_page

    #food menu panel

    food_menu_page = GUI_manager_Food_menu.Food_menu_panel(main_frame, color_palette, admin, inventory_page)
    pages["food_menu"] = food_menu_page

    #discount panel

    discount_page = GUI_manager_Discount.Discount_panel(main_frame, color_palette, admin)
    pages["discount"] = discount_page

    #opinion page

    opinion_page = GUI_manager_Read_opinions.Opinion_panel(main_frame, color_palette, admin)
    pages["opinion"] = opinion_page

class Profile_info():
    def __init__(self, profile_name = "نام کاربری", profile_image = Image.open(os.path.join(sys.path[0], "resources\panels\default_profile_picture.jpg")).convert("RGBA")):
        self.name = profile_name
        self.image = profile_image

class Right_menu(tkinter.Frame):
    def __init__(self, root, color_palette):
        super().__init__(root, width=160, height=680, bg=color_palette[4])
        self.pack_propagate(0)

        font1 = font.Font(family="Mj_Flow", size=18)

        #profile frame

        profile_frame = tkinter.Frame(self, bg=color_palette[4])
        profile_frame.pack()

        #profile picture

        profile_frame_image = Image.open(os.path.join(sys.path[0], "resources\panels\profile_photo_mask.png"))
        profile_img = admin.picture.resize((128,128), Image.ANTIALIAS)
        profile_img.paste(profile_frame_image, (0, 0), profile_frame_image)
        profile_image = ImageTk.PhotoImage(profile_img)
        self.profile_image_label = tkinter.Button(profile_frame, image=profile_image, bg=color_palette[4],
         activebackground=color_palette[4], highlightthickness=0, bd=0, command=lambda:change_page("user_profile"))
        self.profile_image_label.image = profile_image
        self.profile_image_label.pack()   

        #profile name

        self.profile_image_label_name = tkinter.Button(profile_frame,text=admin.name + "\n" + admin.l_name, font=font1, bg=color_palette[4],
         activebackground=color_palette[4], highlightthickness=0, bd=0, command=lambda:change_page("user_profile"))
        self.profile_image_label_name.pack()

        #button frame

        button_frame = tkinter.Frame(self, bg=color_palette[4])
        button_frame.pack(pady=20)

        #Restaurant information button

        Restaurant_information_button = tkinter.Button(button_frame, text="اطلاعات رستوران", bg=color_palette[2], width=22, font=font1,
         activebackground=color_palette[2], highlightthickness=0, bd=0, command=lambda:change_page("restaurant_profile"))
        Restaurant_information_button.pack(pady=6)

        #inventory button

        inventory_button = tkinter.Button(button_frame, text="موجودی غذا", bg=color_palette[2], width=22, font=font1,
         activebackground=color_palette[2], highlightthickness=0, bd=0, command=lambda:change_page("inventory"))
        inventory_button.pack(pady=6)

        #orders button

        orders_button = tkinter.Button(button_frame, text="سفارشات", bg=color_palette[2], width=22, font=font1,
         activebackground=color_palette[2], highlightthickness=0, bd=0, command=lambda:change_page("orders"))
        orders_button.pack(pady=6)

        #financial information button

        financial_information_button = tkinter.Button(button_frame, text="اطلاعات اقتصادی", bg=color_palette[2], width=22, font=font1,
         activebackground=color_palette[2], highlightthickness=0, bd=0, command=lambda:change_page("financial"))
        financial_information_button.pack(pady=6)

        #food menu button

        food_menu_button = tkinter.Button(button_frame, text="منو غذا", bg=color_palette[2], width=22, font=font1,
         activebackground=color_palette[2], highlightthickness=0, bd=0, command=lambda:change_page("food_menu"))
        food_menu_button.pack(pady=6)

        #discaounts button

        discaounts_button = tkinter.Button(button_frame, text="تخفیف ها", bg=color_palette[2], width=22, font=font1,
         activebackground=color_palette[2], highlightthickness=0, bd=0, command=lambda:change_page("discount"))
        discaounts_button.pack(pady=6)

        #discaounts button

        discaounts_button = tkinter.Button(button_frame, text="نظرات", bg=color_palette[2], width=22, font=font1,
         activebackground=color_palette[2], highlightthickness=0, bd=0, command=lambda:change_page("opinion"))
        discaounts_button.pack(pady=6)

    def update_info(self):
        self.profile_image_label_name.configure(text=admin.name + "\n" + admin.l_name)

        profile_frame_image = Image.open(os.path.join(sys.path[0], "resources\panels\profile_photo_mask.png"))
        profile_img = admin.picture.resize((128,128), Image.ANTIALIAS)
        profile_img.paste(profile_frame_image, (0, 0), profile_frame_image)
        profile_image = ImageTk.PhotoImage(profile_img)
        self.profile_image_label.configure(image = profile_image)
        self.profile_image_label.image = profile_image

    def show(self):
        self.place(x=1090, y=25)

    def hide(self):
        self.place_forget()