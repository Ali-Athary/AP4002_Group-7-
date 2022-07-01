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

        # menu picture

        picture_frame = tkinter.Frame(self, width=256, height=620, bg=self.color_palette[3]) 
        picture_frame.grid_propagate(0)
        picture_frame.place(x=40, y=40) 

        tkinter.Label(picture_frame, text="تصویر منو رستوران", font=font1, bg=self.color_palette[3]).grid(row=0, column=0, columnspan=2, padx=8, pady=8)

        # menu image

        menu_img = Image.open(os.path.join(sys.path[0], "resources\panels\menu.jpg"))
        menu_img = menu_img.resize((256,int((menu_img.height/menu_img.width)*256)), Image.ANTIALIAS)
        if(menu_img.height > 512):
            menu_img = menu_img.resize((int((menu_img.width/menu_img.height)*512),512), Image.ANTIALIAS)

        menu_image = ImageTk.PhotoImage(menu_img)
        menu_image_label = tkinter.Label(picture_frame, image=menu_image, bg=color_palette[3],
         highlightthickness=0, bd=0)
        menu_image_label.image = menu_image
        menu_image_label.grid(row=1, column=0, columnspan=2)

        # change pichture

        def choose_picture():
            file_directory = filedialog.askopenfilename(title='select', filetypes=[
                    ("image", ".jpeg"),
                    ("image", ".png"),
                    ("image", ".jpg"),
                ])
            print(file_directory)

        tkinter.Label(picture_frame, text="تغییر تصویر", font=font1, bg=self.color_palette[3]).grid(row=2, column=1)

        choose_img = Image.open(os.path.join(sys.path[0], "resources\icons\choose.png"))
        picture_image = ImageTk.PhotoImage(choose_img)

        choose_picture_button = tkinter.Button(picture_frame, image=picture_image, bg=self.color_palette[3],
         activebackground=self.color_palette[3], highlightthickness=0, bd=0, command=lambda:choose_picture())
        choose_picture_button.image = picture_image
        choose_picture_button.grid(row=2, column=0)

        # information

        info_background_img = Image.open(os.path.join(sys.path[0], "resources\panels\profile_info_background.png"))
        info_background_image = ImageTk.PhotoImage(info_background_img)

        information_background = tkinter.Label(self, image=info_background_image, bg=self.color_palette[3]) 
        information_background.image = info_background_image
        information_background.place(x=1060-40, y=40, anchor=tkinter.NE) 

        info_frame = tkinter.Frame(information_background, width=600, height=520, bg=self.color_palette[3])
        info_frame.place(x=340, y=300, anchor=tkinter.CENTER)

        # first name

        tkinter.Label(info_frame, text=" نام مدیر", font=font1, bg=self.color_palette[3]).grid(row=0, column=1, padx=8, pady=8)

        first_name_var = tkinter.StringVar()
        first_name_var.set("نام")
        first_name_entry =tkinter.Entry(info_frame, textvariable=first_name_var, width=26, justify=tkinter.CENTER,
         font=font1, bg=self.color_palette[4], disabledforeground="black", disabledbackground=self.color_palette[3],
         highlightthickness=0, bd=0,  highlightbackground=self.color_palette[4], highlightcolor=self.color_palette[2])
        first_name_entry.config(state="disable")
        first_name_entry.grid(row=0, column=0, padx=8, pady=8)

        # last name

        tkinter.Label(info_frame, text="نام خانوادگی مدیر", font=font1, bg=self.color_palette[3]).grid(row=1, column=1, padx=8, pady=8)

        last_name_var = tkinter.StringVar()
        last_name_var.set("نام خانوادگی")
        last_name_entry = tkinter.Entry(info_frame, textvariable=last_name_var, width=26, justify=tkinter.CENTER,
         font=font1, bg=self.color_palette[4], disabledforeground="black", disabledbackground=self.color_palette[3],
         highlightthickness=0, bd=0,  highlightbackground=self.color_palette[4], highlightcolor=self.color_palette[2])
        last_name_entry.config(state="disable")
        last_name_entry.grid(row=1, column=0, padx=8, pady=8)

        # area

        tkinter.Label(info_frame, text="منطقه رستوران", font=font1, bg=self.color_palette[3]).grid(row=2, column=1, padx=8, pady=8)
        
        area_var = tkinter.StringVar()
        area_var.set("حکیمیه")        
        area_entry = tkinter.Entry(info_frame, textvariable=area_var,  width=22, justify=tkinter.CENTER,
         font=font_english, bg=self.color_palette[4], disabledforeground="black", disabledbackground=self.color_palette[3],
         highlightthickness=0, bd=0,  highlightbackground=self.color_palette[4], highlightcolor=self.color_palette[2])
        area_entry.config(state="disable")
        area_entry.grid(row=2, column=0, padx=8, pady=8)

        # address

        tkinter.Label(info_frame, text="آدرس رستوران", font=font1, bg=self.color_palette[3]).grid(row=3, column=1, padx=8, pady=8)
        
        address_var = tkinter.StringVar()
        address_var.set("تهران، حکیمیه، خیابان") 
        address_entry = tkinter.Entry(info_frame, width=22, textvariable=address_var, justify=tkinter.CENTER,
         font=font_english, bg=self.color_palette[4], disabledforeground="black", disabledbackground=self.color_palette[3],
         highlightthickness=0, bd=0, highlightbackground=self.color_palette[4], highlightcolor=self.color_palette[2])
        address_entry.config(state="disable")
        address_entry.grid(row=3, column=0, padx=8, pady=8)

        #     eddit

        confirm_img = Image.open(os.path.join(sys.path[0], "resources\icons\confirm.png"))
        confirm_image = ImageTk.PhotoImage(confirm_img)

        confirm_button = tkinter.Button(info_frame, image=confirm_image, font=font1, bg=self.color_palette[3],
         highlightthickness=0, bd=0, activebackground=self.color_palette[3], command=lambda:confirm())
        confirm_button.image = confirm_image

        def eddit():
            first_name_entry.config(state="normal", highlightthickness=1)
            last_name_entry.config(state="normal", highlightthickness=1)
            area_entry.config(state="normal", highlightthickness=1)
            address_entry.config(state="normal", highlightthickness=1)
            confirm_button.grid(row=4, column=0, padx=8)

        def confirm():
            first_name_entry.config(state="disable", highlightthickness=0)
            last_name_entry.config(state="disable", highlightthickness=0)
            area_entry.config(state="disable", highlightthickness=0)
            address_entry.config(state="disable", highlightthickness=0)
            confirm_button.grid_forget()

        eddit_img = Image.open(os.path.join(sys.path[0], "resources\icons\eddit.png"))
        eddit_image = ImageTk.PhotoImage(eddit_img)

        eddit_button = tkinter.Button(info_frame, image=eddit_image, font=font1, bg=self.color_palette[3],
         highlightthickness=0, bd=0, activebackground=self.color_palette[3], command=lambda:eddit())
        eddit_button.image = eddit_image
        eddit_button.grid(row=4, column=1, padx=8)

    def show(self):
        self.place(x=20, y=20)

    def hide(self):
        self.place_forget()
