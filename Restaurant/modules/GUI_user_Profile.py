import tkinter
from tkinter import font, ttk, filedialog
from PIL import ImageTk, Image  
import os
import sys
import jdatetime

class Profile_panel(tkinter.Label):
    def __init__(self, root, color_palette):
        self.color_palette = color_palette
        img = Image.open(os.path.join(sys.path[0], "resources\panels\\simple_panel.png")).convert("RGBA")
        image = ImageTk.PhotoImage(img)

        super().__init__(root, image=image, bg=color_palette[4], bd=0)
        self.image = image
        self.pack_propagate(0)

        font1 = font.Font(family="Mj_Flow", size=18)
        font2 = font.Font(family="Dast Nevis", size=20)
        font_english = font.Font(family="Roboto", size=20)

        # profile picture

        picture_frame = tkinter.Frame(self, width=256, height=400, bg=self.color_palette[3]) 
        picture_frame.place(x=40, y=60) 

        # picture image

        picture_mask_image = Image.open(os.path.join(sys.path[0], "resources\panels\profile_page_picture_mask.png"))
        picture_img = Image.open(os.path.join(sys.path[0], "resources\panels\default_profile_picture.jpg"))
        picture_img = picture_img.resize((256,256), Image.ANTIALIAS)
        picture_img.paste(picture_mask_image, (0, 0), picture_mask_image)
        picture_image = ImageTk.PhotoImage(picture_img)
        profile_image_label = tkinter.Label(picture_frame, image=picture_image, bg=color_palette[3],
         highlightthickness=0, bd=0)
        profile_image_label.image = picture_image
        profile_image_label.grid(row=0, column=0, columnspan=2)

        # changge pichture

        def choose_picture():
            file_directory = filedialog.askopenfilename(title='select', filetypes=[
                    ("image", ".jpeg"),
                    ("image", ".png"),
                    ("image", ".jpg"),
                ])
            print(file_directory)

        tkinter.Label(picture_frame, text="تغییر تصویر", font=font1, bg=self.color_palette[3]).grid(row=1, column=1)

        choose_img = Image.open(os.path.join(sys.path[0], "resources\icons\choose.png"))
        picture_image = ImageTk.PhotoImage(choose_img)

        choose_picture_button = tkinter.Button(picture_frame, image=picture_image, bg=self.color_palette[3],
         activebackground=self.color_palette[3], highlightthickness=0, bd=0, command=lambda:choose_picture())
        choose_picture_button.image = picture_image
        choose_picture_button.grid(row=1, column=0)

        # information

        info_background_img = Image.open(os.path.join(sys.path[0], "resources\panels\profile_info_background.png"))
        info_background_image = ImageTk.PhotoImage(info_background_img)

        information_background = tkinter.Label(self, image=info_background_image, bg=self.color_palette[3]) 
        information_background.image = info_background_image
        information_background.place(x=1060-40, y=40, anchor=tkinter.NE) 

        info_frame = tkinter.Frame(information_background, width=600, height=520, bg=self.color_palette[3])
        info_frame.place(x=340, y=300, anchor=tkinter.CENTER)

        # first name

        tkinter.Label(info_frame, text="نام", font=font1, bg=self.color_palette[3]).grid(row=0, column=1, padx=8, pady=8)

        first_name_var = tkinter.StringVar()
        first_name_var.set("نام")
        first_name_entry =tkinter.Entry(info_frame, textvariable=first_name_var, width=26, justify=tkinter.CENTER,
         font=font1, bg=self.color_palette[4], disabledforeground="black", disabledbackground=self.color_palette[3],
         highlightthickness=0, bd=0,  highlightbackground=self.color_palette[4], highlightcolor=self.color_palette[2])
        first_name_entry.config(state="disable")
        first_name_entry.grid(row=0, column=0, padx=8, pady=8)

        # last name

        tkinter.Label(info_frame, text="نام خانوادگی", font=font1, bg=self.color_palette[3]).grid(row=1, column=1, padx=8, pady=8)

        last_name_var = tkinter.StringVar()
        last_name_var.set("نام خانوادگی")
        last_name_entry = tkinter.Entry(info_frame, textvariable=last_name_var, width=26, justify=tkinter.CENTER,
         font=font1, bg=self.color_palette[4], disabledforeground="black", disabledbackground=self.color_palette[3],
         highlightthickness=0, bd=0,  highlightbackground=self.color_palette[4], highlightcolor=self.color_palette[2])
        last_name_entry.config(state="disable")
        last_name_entry.grid(row=1, column=0, padx=8, pady=8)

        # phone number

        tkinter.Label(info_frame, text="شماره تماس", font=font1, bg=self.color_palette[3]).grid(row=2, column=1, padx=8, pady=8)
        
        phone_number_var = tkinter.StringVar()
        phone_number_var.set("09...")        
        phone_number_entry = tkinter.Entry(info_frame, textvariable=phone_number_var,  width=22, justify=tkinter.CENTER,
         font=font_english, bg=self.color_palette[4], disabledforeground="black", disabledbackground=self.color_palette[3],
         highlightthickness=0, bd=0,  highlightbackground=self.color_palette[4], highlightcolor=self.color_palette[2])
        phone_number_entry.config(state="disable")
        phone_number_entry.grid(row=2, column=0, padx=8, pady=8)

        # email

        tkinter.Label(info_frame, text="ایمیل", font=font1, bg=self.color_palette[3]).grid(row=3, column=1, padx=8, pady=8)
        
        email_var = tkinter.StringVar()
        email_var.set("email") 
        email_entry = tkinter.Entry(info_frame, width=22, textvariable=email_var, justify=tkinter.CENTER,
         font=font_english, bg=self.color_palette[4], disabledforeground="black", disabledbackground=self.color_palette[3],
         highlightthickness=0, bd=0, highlightbackground=self.color_palette[4], highlightcolor=self.color_palette[2])
        email_entry.config(state="disable")
        email_entry.grid(row=3, column=0, padx=8, pady=8)

        #     eddit

        confirm_img = Image.open(os.path.join(sys.path[0], "resources\icons\confirm.png"))
        confirm_image = ImageTk.PhotoImage(confirm_img)

        confirm_button = tkinter.Button(info_frame, image=confirm_image, font=font1, bg=self.color_palette[3],
         highlightthickness=0, bd=0, activebackground=self.color_palette[3], command=lambda:confirm())
        confirm_button.image = confirm_image

        def eddit():
            first_name_entry.config(state="normal", highlightthickness=1)
            last_name_entry.config(state="normal", highlightthickness=1)
            phone_number_entry.config(state="normal", highlightthickness=1)
            email_entry.config(state="normal", highlightthickness=1)
            confirm_button.grid(row=4, column=0, padx=8)

        def confirm():
            first_name_entry.config(state="disable", highlightthickness=0)
            last_name_entry.config(state="disable", highlightthickness=0)
            phone_number_entry.config(state="disable", highlightthickness=0)
            email_entry.config(state="disable", highlightthickness=0)
            confirm_button.grid_forget()

        eddit_img = Image.open(os.path.join(sys.path[0], "resources\icons\eddit.png"))
        eddit_image = ImageTk.PhotoImage(eddit_img)

        eddit_button = tkinter.Button(info_frame, image=eddit_image, font=font1, bg=self.color_palette[3],
         highlightthickness=0, bd=0, activebackground=self.color_palette[3], command=lambda:eddit())
        eddit_button.image = eddit_image
        eddit_button.grid(row=4, column=1, padx=8)

        #change password 

        change_password_panel = Change_password_panel(self, self.color_palette)

        change_passwword_img = Image.open(os.path.join(sys.path[0], "resources\icons\change_password.png"))
        change_passwword_image = ImageTk.PhotoImage(change_passwword_img)

        change_passwword_button = tkinter.Button(info_frame, image=change_passwword_image, font=font1, bg=self.color_palette[3],
         highlightthickness=0, bd=0, activebackground=self.color_palette[3], command=lambda:change_password_panel.show())
        change_passwword_button.image = change_passwword_image
        change_passwword_button.grid(row=5, column=1, padx=8)

    def show(self):
        self.place(x=20, y=20)

    def hide(self):
        self.place_forget()

class Change_password_panel(tkinter.Frame):
    def __init__(self, root, color_palette):
        self.color_palette = color_palette
        super().__init__(root, width=1020, height=640, bg=color_palette[3], bd=0)
        self.pack_propagate(0)

        font1 = font.Font(family="Mj_Flow", size=18)
        font2 = font.Font(family="Dast Nevis", size=20)
        font_english = font.Font(family="Roboto", size=20)

        #middle frame

        img = Image.open(os.path.join(sys.path[0], "resources\panels\\profile_info_background.png")).convert("RGBA")
        image = ImageTk.PhotoImage(img)

        background = tkinter.Label(self, image=image, bg=self.color_palette[3], bd=0)
        background.image = image
        background.pack_propagate(0)
        background.pack(expand=True, fill="none")

        frame = tkinter.Frame(background, bg=self.color_palette[3])
        frame.pack(expand=True, fill="none")

        #current password

        tkinter.Label(frame, text="رمز عبور فعلی", font=font1, bg=self.color_palette[3]).grid(row=0, column=1, padx=8, pady=8)
        
        current_password_var = tkinter.StringVar()
        current_password_entry = tkinter.Entry(frame, textvariable=current_password_var,  width=22, show='●',
         font=font_english, highlightcolor=self.color_palette[4], highlightthickness=0, bd=0)
        current_password_entry.grid(row=0, column=0, padx=8, pady=28)

        #new password

        tkinter.Label(frame, text="رمز عبور جدید", font=font1, bg=self.color_palette[3]).grid(row=1, column=1, padx=8, pady=8)
        
        new_password_var = tkinter.StringVar()
        new_password_entry = tkinter.Entry(frame, textvariable=new_password_var,  width=22, show='●',
         font=font_english, highlightcolor=self.color_palette[4], highlightthickness=0, bd=0)
        new_password_entry.grid(row=1, column=0, padx=8, pady=8)

        #new password confirm

        tkinter.Label(frame, text="تکرار رمز عبور جدید", font=font1, bg=self.color_palette[3]).grid(row=2, column=1, padx=8, pady=8)
        
        new_password_confirm_var = tkinter.StringVar()
        new_password_confirm_entry = tkinter.Entry(frame, textvariable=new_password_confirm_var,  width=22, show='●',
         font=font_english, highlightcolor=self.color_palette[4], highlightthickness=0, bd=0)
        new_password_confirm_entry.grid(row=2, column=0, padx=8, pady=8)

        #error massage

        error_message = tkinter.Label(frame, text=" \n ", font=font2, fg=self.color_palette[2], bg=self.color_palette[3])
        error_message.grid(row=3, column=0, columnspan=2, padx=8, pady=8)

        #confirm button

        def confirm():
            current_password_var.set("")
            new_password_var.set("")
            new_password_confirm_var.set("")
            self.hide()

        confirm_img = Image.open(os.path.join(sys.path[0], "resources\icons\confirm.png"))
        confirm_image = ImageTk.PhotoImage(confirm_img)

        confirm_button = tkinter.Button(frame, image=confirm_image, bg=self.color_palette[3],
         highlightthickness=0, bd=0, activebackground=self.color_palette[3], command=confirm)
        confirm_button.image = confirm_image
        confirm_button.grid(row=4, column=1, padx=8, pady=8)



    def show(self):
        self.place(x=20, y=20)

    def hide(self):
        self.place_forget()