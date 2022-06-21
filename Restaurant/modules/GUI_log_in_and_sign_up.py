import tkinter
from tkinter import font, ttk
from PIL import ImageTk, Image  
import os
import sys

pages = []

def main(root, color_palette):
    #base frame

    base_frame = tkinter.Frame(root, bg=color_palette[4], width=1280, height=720)
    base_frame.pack_propagate(0)
    base_frame.pack(fill="none", expand=True) 

    #main frame

    img = Image.open(os.path.join(sys.path[0], "resources\panels\log_in_panel.png")).convert("RGBA")
    image = ImageTk.PhotoImage(img)

    main_frame = tkinter.Label(base_frame, image=image, bg=color_palette[4])
    main_frame.image = image
    main_frame.pack(fill="none", expand=True)            

    #log in frame and sign in frame

    log_in_frame = Log_in_page(main_frame, color_palette)
    pages.append(log_in_frame)
    sign_in_frame = Sign_in_page(main_frame, color_palette)
    pages.append(sign_in_frame)
    forgot_password_frame = Forgot_password_page(main_frame, color_palette)
    pages.append(forgot_password_frame)

    #place log in frame

    change_page(0)

def change_page(page_inex):
    for i in range(len(pages)):
        pages[i].hide()
    pages[page_inex].clear()
    pages[page_inex].show()
    
class Page(tkinter.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clear(self):
        pass

    def show(self):
        self.place(x=400,y=35)

    def hide(self):
        self.place_forget()

class Log_in_page(Page):
    def __init__(self, root, color_palette):
        super().__init__(root, width=415, height=430, bg=color_palette[3])
        self.pack_propagate(0)

        frame = tkinter.Frame(self, bg=color_palette[3])
        frame.pack(fill="none", expand=True)

        font1 = font.Font(family="Mj_Flow", size=24)
        font2 = font.Font(family="Dast Nevis", size=14)

        #top label

        tkinter.Label(frame, text="ورود به حساب کاربری", font=font1, bg=color_palette[3]).pack()
        tkinter.Label(frame, text="اطلاعات خود را وارد کنید", font=font2, bg=color_palette[3]).pack(pady=8)

        #entry frame

        entry_frame = tkinter.Frame(frame, bg=color_palette[3])
        entry_frame.pack(pady=22)
        font_English = font.Font(family="Roboto", size=12)
        font_persian = font.Font(family="Mj_Flow", size=16)
        self.entries = []
    
        #email
        
        tkinter.Label(entry_frame, text="ایمیل", font=font_persian, bg=color_palette[3]).grid(row=0, column=1, padx=12, pady=4)
        self.email_var = tkinter.StringVar()
        email_entry = tkinter.Entry(entry_frame, font=font_English, width=22, textvariable=self.email_var,
         highlightthickness=0, bd=0)
        email_entry.grid(row=0, column=0, padx=12, pady=4)
        self.entries.append(email_entry)

        #password
        
        tkinter.Label(entry_frame, text="رمز عبور", font=font_persian, bg=color_palette[3]).grid(row=1, column=1, padx=12, pady=4)
        self.password_var = tkinter.StringVar()
        password_entry = tkinter.Entry(entry_frame, font=font_English, width=22, textvariable=self.password_var, show='●')
        password_entry.pack_propagate(0)
        password_entry.grid(row=1, column=0, padx=12, pady=4)
        self.entries.append(password_entry)
        
        #eye button (show password characters)

        eye_img = Image.open(os.path.join(sys.path[0], "resources\icons\eye.png")).convert("RGBA")
        eye_image = ImageTk.PhotoImage(eye_img.resize((26,26), Image.ANTIALIAS))

        def eye_on_click(event):
            password_entry.configure(show='')

        def eye_on_release(event):
            password_entry.configure(show='●')

        eye_button = tkinter.Button(password_entry, image=eye_image, bg=color_palette[4],
        highlightthickness=0, bd=0, activebackground=color_palette[3])
        eye_button.image = eye_image

        eye_button.bind("<ButtonPress>", eye_on_click)
        eye_button.bind("<ButtonRelease>", eye_on_release)

        #show and hide eye button
        
        def show_hide_eye(sv):
            if(len(sv.get()) == 0):
                eye_button.pack_forget()
            else:
                eye_button.pack(side=tkinter.RIGHT)

        self.password_var.trace("w", lambda name, index, mode, sv=self.password_var: show_hide_eye(sv))

        #error message 

        self.error_label = tkinter.Label(frame, font=font2, bg=color_palette[3], fg='#f55951')
        self.error_label.pack()

        #button frame

        button_frame = tkinter.Frame(frame, bg=color_palette[3])
        button_frame.pack(pady=12)
        font_persian = font.Font(family="Mj_Flow", size=14)

        #log in button

        tkinter.Button(button_frame, text="ورود", font=font_persian, width=26, bg=color_palette[4],
        activebackground=color_palette[3], highlightthickness=0, bd=0).grid(row=0, column=0, columnspan=2)
        
        #sign in button 

        tkinter.Button(button_frame, text="ثبت نام", font=font_persian, fg='#292a73', command=lambda:change_page(1),
        bg=color_palette[3], highlightthickness=0, bd=0, activebackground=color_palette[3]).grid(row=1, column=1, pady=8)

        #forgot password button 

        tkinter.Button(button_frame, text="فراموشی رمز عبور", font=font_persian, fg='#292a73', command=lambda:change_page(2),
        bg=color_palette[3], highlightthickness=0, bd=0, activebackground=color_palette[3]).grid(row=1, column=0, pady=8)

    def clear(self):
        for entry in self.entries:
            entry.delete(0, 'end')

    def display_error_message(self, text):
        self.error_label.configure(text=text)

class Sign_in_page(Page):
    def __init__(self, root, color_palette):
        super().__init__(root, width=415, height=430, bg=color_palette[3])
        self.pack_propagate(0)

        frame = tkinter.Frame(self, bg=color_palette[3])
        frame.pack(fill="none", expand=True)

        font1 = font.Font(family="Mj_Flow", size=24)
        font2 = font.Font(family="Dast Nevis", size=14)

        #top label

        tkinter.Label(frame, text="ثبت نام", font=font1, bg=color_palette[3]).pack()

        #entry frame

        entry_frame = tkinter.Frame(frame, bg=color_palette[3])
        entry_frame.pack()
        font_English = font.Font(family="Roboto", size=12)
        font_persian = font.Font(family="Mj_Flow", size=16)
        pady = 1
        self.entries = []

        #full name
        
        tkinter.Label(entry_frame, text="نام و نام خانوادگی", font=font_persian, bg=color_palette[3]).grid(row=0, column=1, padx=12, pady=pady)
        self.full_nam_var = tkinter.StringVar()
        full_nam_entry = tkinter.Entry(entry_frame, font=font_English, width=22, textvariable=self.full_nam_var)
        full_nam_entry.grid(row=0, column=0, padx=12, pady=pady)
        self.entries.append(full_nam_entry)

        #phone number
        
        tkinter.Label(entry_frame, text="شماره تماس", font=font_persian, bg=color_palette[3]).grid(row=1, column=1, padx=12, pady=pady)
        self.phone_number_var = tkinter.StringVar()
        phone_number_entry = tkinter.Entry(entry_frame, font=font_English, width=22, textvariable=self.phone_number_var)
        phone_number_entry.grid(row=1, column=0, padx=12, pady=pady)
        self.entries.append(phone_number_entry)

        #email
        
        tkinter.Label(entry_frame, text="ایمیل", font=font_persian, bg=color_palette[3]).grid(row=2, column=1, padx=12, pady=pady)
        self.email_var = tkinter.StringVar()
        email_entry = tkinter.Entry(entry_frame, font=font_English, width=22, textvariable=self.email_var)
        email_entry.grid(row=2, column=0, padx=12, pady=pady)
        self.entries.append(email_entry)

        #id
        
        tkinter.Label(entry_frame, text="کد ملی", font=font_persian, bg=color_palette[3]).grid(row=3, column=1, padx=12, pady=pady)
        self.id_var = tkinter.StringVar()
        id_entry = tkinter.Entry(entry_frame, font=font_English, width=22, textvariable=self.id_var)
        id_entry.grid(row=3, column=0, padx=12, pady=pady)
        self.entries.append(id_entry)

        #password
        
        tkinter.Label(entry_frame, text="رمز عبور", font=font_persian, bg=color_palette[3]).grid(row=4, column=1, padx=12, pady=pady)
        self.password_var = tkinter.StringVar()
        password_entry = tkinter.Entry(entry_frame, font=font_English, width=22, textvariable=self.password_var, show='●')
        password_entry.grid(row=4, column=0, padx=12, pady=pady)
        self.entries.append(password_entry)

        #password confirm
        
        tkinter.Label(entry_frame, text="تکرار رمز عبور", font=font_persian, bg=color_palette[3]).grid(row=5, column=1, padx=12, pady=pady)
        self.password_confirm_var = tkinter.StringVar()
        password_confirm_var = tkinter.Entry(entry_frame, font=font_English, width=22, textvariable=self.password_confirm_var, show='●')
        password_confirm_var.grid(row=5, column=0, padx=12, pady=pady)
        self.entries.append(password_confirm_var)

        #message 

        self.message_label = tkinter.Label(frame, text="\n", font=font2, bg=color_palette[3])
        self.message_label.pack()

        #button frame

        button_frame = tkinter.Frame(frame, bg=color_palette[3])
        button_frame.pack(pady=12)
        font_persian = font.Font(family="Mj_Flow", size=14)

        #sign in button

        tkinter.Button(button_frame, text="ثبت نام", font=font_persian, width=16, bg=color_palette[4],
        activebackground=color_palette[3], highlightthickness=0, bd=0).grid(row=0, column=1, padx=10)
        
        #log in button 

        tkinter.Button(button_frame, text="ورود به حساب کاربری", font=font_persian, fg='#292a73', command=lambda:change_page(0),
        bg=color_palette[3], highlightthickness=0, bd=0, activebackground=color_palette[3]).grid(row=0, column=0, padx=10)

    def clear(self):
        for entry in self.entries:
            entry.delete(0, 'end')

    def display_error_message(self, text):
        self.message_label.configure(text=text, fg='#f55951')

    def display_confirm_message(self, text):
        self.message_label.configure(text=text, fg='#00b300')
    
class Forgot_password_page(Page):
    def __init__(self, root, color_palette):
        super().__init__(root, width=415, height=430, bg=color_palette[3])
        self.pack_propagate(0)

        frame = tkinter.Frame(self, bg=color_palette[3])
        frame.pack(fill="none", expand=True)

        font1 = font.Font(family="Mj_Flow", size=24)
        font2 = font.Font(family="Dast Nevis", size=14)

        #top label

        tkinter.Label(frame, text="فراموشی رمز عبور", font=font1, bg=color_palette[3]).pack()
        tkinter.Label(frame, text="ایمیل خور را وارد کنید", font=font2, bg=color_palette[3]).pack(pady=8)

        #entry frame

        entry_frame = tkinter.Frame(frame, bg=color_palette[3])
        entry_frame.pack(pady=22)
        font_English = font.Font(family="Roboto", size=12)
        font_persian = font.Font(family="Mj_Flow", size=16)
        self.entries = []
    
        #email
        
        tkinter.Label(entry_frame, text="ایمیل", font=font_persian, bg=color_palette[3]).grid(row=0, column=1, padx=12, pady=4)
        self.email_var = tkinter.StringVar()
        email_entry = tkinter.Entry(entry_frame, font=font_English, width=22, textvariable=self.email_var)
        email_entry.grid(row=0, column=0, padx=12, pady=4)
        self.entries.append(email_entry)

        #message 

        self.message_label = tkinter.Label(frame, font=font2, bg=color_palette[3])
        self.message_label.pack()

        #button frame

        button_frame = tkinter.Frame(frame, bg=color_palette[3])
        button_frame.pack(pady=12)
        font_persian = font.Font(family="Mj_Flow", size=14)

        #Send button

        tkinter.Button(button_frame, text="ارسال", font=font_persian, width=26, bg=color_palette[4],
        activebackground=color_palette[3], highlightthickness=0, bd=0).grid(row=0, column=0, columnspan=2)
        
        #sign in button 

        tkinter.Button(button_frame, text="ثبت نام", font=font_persian, fg='#292a73', command=lambda:change_page(1),
        bg=color_palette[3], highlightthickness=0, bd=0, activebackground=color_palette[3]).grid(row=1, column=1, pady=8)

        #log in button 

        tkinter.Button(button_frame, text="ورود", font=font_persian, fg='#292a73', command=lambda:change_page(0),
        bg=color_palette[3], highlightthickness=0, bd=0, activebackground=color_palette[3]).grid(row=1, column=0, pady=8)

    def clear(self):
        for entry in self.entries:
            entry.delete(0, 'end')

    def display_message(self, text):
        self.error_label.configure(text=text)
