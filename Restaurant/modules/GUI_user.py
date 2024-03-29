import tkinter
from tkinter import font, ttk
from PIL import ImageTk, Image  
import os
import sys
from modules import GUI_user_Food_Menu_page, GUI_user_Cart, GUI_user_History, GUI_user_Suggestion, GUI_user_Profile
from modules import Food, functions, UserAndManager

pages = {}
active_page_name = ""

def set_profile_info(User):
    global profile_info
    profile_info = Profile_info(User)

def change_page(name):
    global active_page_name, pages

    if(active_page_name == name):
        return
   
    pages[active_page_name].hide()
    pages[name].show()
    pages["right_menu"].hide()
    pages["right_menu"].show()

    pages[name].update_page()

    active_page_name = name

def on_close_app(root):
    User.save_last_order()
    root.destroy()

def main(root, color_palette, user:UserAndManager.User):
    global active_page_name, pages, User
    User = user
    root.protocol("WM_DELETE_WINDOW",lambda:on_close_app(root))
    #main frame
    set_profile_info(user)

    img = Image.open(os.path.join(sys.path[0], "resources\panels\\main_panel_background.png")).convert("RGBA")
    image = ImageTk.PhotoImage(img)

    main_frame = tkinter.Label(root, image=image, bg=color_palette[4])
    main_frame.image = image
    main_frame.pack(fill="none", expand=True) 

    #right menu

    right_menu = Right_menu(main_frame, color_palette)
    pages["right_menu"] = right_menu
    right_menu.show()

    #cart panel

    cart_page = GUI_user_Cart.Cart_panel(main_frame, color_palette, User)
    pages["cart"] = cart_page

    #food menu panel

    food_menu_page = GUI_user_Food_Menu_page.Food_menu_panel(main_frame, color_palette, User, cart_page)
    pages["food_menu"] = food_menu_page

    active_page_name = "food_menu"
    food_menu_page.show()

    #history panel

    history_page = GUI_user_History.History_panel(main_frame, color_palette, User)
    pages["history"] = history_page

    #suggestion panel

    history_page = GUI_user_Suggestion.Suggestion_panel(main_frame, color_palette, User)
    pages["suggestion"] = history_page

    #profile panel

    history_page = GUI_user_Profile.Profile_panel(main_frame, color_palette, User, right_menu)
    pages["profile"] = history_page

    

class Profile_info():
    def __init__(self, user):
        self.name = user.name
        self.image = user.picture

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
        self.profile_image_label = tkinter.Button(profile_frame, image=profile_image, bg=color_palette[4],
         activebackground=color_palette[4], highlightthickness=0, bd=0, command=lambda:change_page("profile"))
        self.profile_image_label.image = profile_image
        self.profile_image_label.pack()   

        #profile name

        self.profile_image_label_name = tkinter.Button(profile_frame,text=User.name + "\n" + User.l_name, font=font1, bg=color_palette[4],
         activebackground=color_palette[4], highlightthickness=0, bd=0, command=lambda:change_page("profile"))
        self.profile_image_label_name.pack()

        #button frame

        button_frame = tkinter.Frame(self, bg=color_palette[4])
        button_frame.pack(pady=40)

        #menu button

        menu_img = Image.open(os.path.join(sys.path[0], "resources\icons\menu.png")).convert("RGBA")
        menu_image = ImageTk.PhotoImage(menu_img)

        menu_button = tkinter.Button(button_frame, image=menu_image, bg=color_palette[4],
         activebackground=color_palette[4], highlightthickness=0, bd=0, command=lambda:change_page("food_menu"))
        menu_button.image = menu_image
        menu_button.grid(row=0, column=1)   

        tkinter.Label(button_frame, text="منو", font=font1, bg=color_palette[4], fg=color_palette[0]).grid(row=0, column=0)   

        #cart button

        cart_img = Image.open(os.path.join(sys.path[0], "resources\icons\cart.png")).convert("RGBA")
        cart_image = ImageTk.PhotoImage(cart_img)

        cart_button = tkinter.Button(button_frame, image=cart_image, bg=color_palette[4],
         activebackground=color_palette[4], highlightthickness=0, bd=0, command=lambda:change_page("cart"))
        cart_button.image = cart_image
        cart_button.grid(row=1, column=1)   

        tkinter.Label(button_frame, text="سبد خرید", font=font1, bg=color_palette[4], fg=color_palette[0]).grid(row=1, column=0)   

        #history button

        history_img = Image.open(os.path.join(sys.path[0], "resources\icons\history.png")).convert("RGBA")
        history_image = ImageTk.PhotoImage(history_img)

        history_button = tkinter.Button(button_frame, image=history_image, bg=color_palette[4],
         activebackground=color_palette[4], highlightthickness=0, bd=0, command=lambda:change_page("history"))
        history_button.image = history_image
        history_button.grid(row=2, column=1)   

        tkinter.Label(button_frame, text="تاریخچه", font=font1, bg=color_palette[4], fg=color_palette[0]).grid(row=2, column=0)  

        #suggestion button

        suggestion_img = Image.open(os.path.join(sys.path[0], "resources\icons\letter.png")).convert("RGBA")
        suggestion_image = ImageTk.PhotoImage(suggestion_img)

        suggestion_button = tkinter.Button(button_frame, image=suggestion_image, bg=color_palette[4],
         activebackground=color_palette[4], highlightthickness=0, bd=0, command=lambda:change_page("suggestion"))
        suggestion_button.image = suggestion_image
        suggestion_button.grid(row=3, column=1)   

        tkinter.Label(button_frame, text="نظر دهی", font=font1, bg=color_palette[4], fg=color_palette[0]).grid(row=3, column=0)    

    def update_info(self):
        self.profile_image_label_name.configure(text=User.name + "\n" + User.l_name)

        profile_frame_image = Image.open(os.path.join(sys.path[0], "resources\panels\profile_photo_mask.png"))
        profile_img = User.picture.resize((128,128), Image.ANTIALIAS)
        profile_img.paste(profile_frame_image, (0, 0), profile_frame_image)
        profile_image = ImageTk.PhotoImage(profile_img)
        self.profile_image_label.configure(image = profile_image)
        self.profile_image_label.image = profile_image

    def show(self):
        self.place(x=1090, y=40)

    def hide(self):
        self.place_forget()