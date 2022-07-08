import tkinter
from tkinter import font, ttk
from PIL import ImageTk, Image
import os, sys
from modules import val_functions

pages = []

def close_page():
    base_frame.pack_forget()

def main(root, color_palette, db):
    global DB
    DB = db

    #base frame
    global base_frame

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

    user_log_in_frame = User_Log_in_page(main_frame, color_palette, root)
    pages.append(user_log_in_frame)
    sign_in_frame = Sign_up_page(main_frame, color_palette)
    pages.append(sign_in_frame)
    forgot_password_frame = Forgot_password_page(main_frame, color_palette)
    pages.append(forgot_password_frame)
    manager_log_in_frame = Manager_Log_in_page(main_frame, color_palette, root)
    pages.append(manager_log_in_frame)

    #place log in frame

    change_page(0)

    return

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
        self.place(x=400,y=30)

    def hide(self):
        self.place_forget()

class User_Log_in_page(Page):
    def __init__(self, root, color_palette, main_root):
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
        password_entry = tkinter.Entry(entry_frame, font=font_English, width=22, textvariable=self.password_var, show='●',
         highlightthickness=0, bd=0)
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

        def loggin():
            user = DB.get_user_obj(self.email_var.get(), self.password_var.get())
            if(isinstance(user, str)):
                self.display_error_message(user)
            else:
                close_page()
                main_root.open_user_app(user)
                


        tkinter.Button(button_frame, text="ورود", font=font_persian, width=26, bg=color_palette[4],
        activebackground=color_palette[3], highlightthickness=0, bd=0, command=loggin).grid(row=0, column=0, columnspan=3)
        
        #sign up button 

        tkinter.Button(button_frame, text="ثبت نام", font=font_persian, fg='#292a73', command=lambda:change_page(1),
        bg=color_palette[3], highlightthickness=0, bd=0, activebackground=color_palette[3]).grid(row=1, column=2, pady=8)

        #forgot password button 

        tkinter.Button(button_frame, text="فراموشی رمز عبور", font=font_persian, fg='#292a73', command=lambda:change_page(2),
        bg=color_palette[3], highlightthickness=0, bd=0, activebackground=color_palette[3]).grid(row=1, column=0, pady=8)

        #manager log in button 

        tkinter.Button(button_frame, text="ورود مدیر", font=font_persian, fg='#292a73', command=lambda:change_page(3),
         bg=color_palette[3], highlightthickness=0, bd=0, activebackground=color_palette[3]).grid(row=1, column=1, pady=8)

    def clear(self):
        for entry in self.entries:
            entry.delete(0, 'end')

    def display_error_message(self, text):
        self.error_label.configure(text=text)

class Manager_Log_in_page(Page):
    def __init__(self, root, color_palette, main_root):
        super().__init__(root, width=415, height=430, bg=color_palette[3])
        self.pack_propagate(0)

        frame = tkinter.Frame(self, bg=color_palette[3])
        frame.pack(fill="none", expand=True)

        font1 = font.Font(family="Mj_Flow", size=24)
        font2 = font.Font(family="Dast Nevis", size=14)

        #top label

        tkinter.Label(frame, text="ورود به حساب مدرییت", font=font1, bg=color_palette[3]).pack()
        tkinter.Label(frame, text="اطلاعات خود را وارد کنید", font=font2, bg=color_palette[3]).pack(pady=8)

        #entry frame

        entry_frame = tkinter.Frame(frame, bg=color_palette[3])
        entry_frame.pack(pady=22)
        font_English = font.Font(family="Roboto", size=12)
        font_persian = font.Font(family="Mj_Flow", size=16)
        self.entries = []
    
        #manager id
        
        tkinter.Label(entry_frame, text="شماره پرسنلی", font=font_persian, bg=color_palette[3]).grid(row=0, column=1, padx=12, pady=4)
        self.manager_id_var = tkinter.StringVar()
        manager_id_entry = tkinter.Entry(entry_frame, font=font_English, width=22, textvariable=self.manager_id_var,
         highlightthickness=0, bd=0)
        manager_id_entry.grid(row=0, column=0, padx=12, pady=4)
        self.entries.append(manager_id_entry)

        #password
        
        tkinter.Label(entry_frame, text="رمز عبور", font=font_persian, bg=color_palette[3]).grid(row=1, column=1, padx=12, pady=4)
        self.password_var = tkinter.StringVar()
        password_entry = tkinter.Entry(entry_frame, font=font_English, width=22, textvariable=self.password_var, show='●',
         highlightthickness=0, bd=0)
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

        def loggin():
            admin = DB.get_manager_obj(self.manager_id_var.get(), self.password_var.get())
            if(isinstance(admin, str)):
                self.display_error_message(admin)
            else:
                close_page()
                main_root.open_manager_app(admin)

        #log in button

        tkinter.Button(button_frame, text="ورود", font=font_persian, width=26, bg=color_palette[4],
        activebackground=color_palette[3], highlightthickness=0, bd=0, command=loggin).grid(row=0, column=0, columnspan=3)

        #sign up button 

        tkinter.Button(button_frame, text="ثبت نام", font=font_persian, fg='#292a73', command=lambda:change_page(1),
        bg=color_palette[3], highlightthickness=0, bd=0, activebackground=color_palette[3]).grid(row=1, column=2, pady=8)

        #forgot password button 

        tkinter.Button(button_frame, text="فراموشی رمز عبور", font=font_persian, fg='#292a73', command=lambda:change_page(2),
        bg=color_palette[3], highlightthickness=0, bd=0, activebackground=color_palette[3]).grid(row=1, column=0, pady=8)

        #user log in button 

        tkinter.Button(button_frame, text="ورود کاربر", font=font_persian, fg='#292a73', command=lambda:change_page(0),
         bg=color_palette[3], highlightthickness=0, bd=0, activebackground=color_palette[3]).grid(row=1, column=1, pady=8)

    def clear(self):
        for entry in self.entries:
            entry.delete(0, 'end')

    def display_error_message(self, text):
        self.error_label.configure(text=text)

class Sign_up_page(Page):
    def __init__(self, root, color_palette):
        super().__init__(root, width=415, height=440, bg=color_palette[3])
        self.pack_propagate(0)

        frame = tkinter.Frame(self, bg=color_palette[3])
        frame.pack(fill="none", expand=True)

        font1 = font.Font(family="Mj_Flow", size=22)
        font2 = font.Font(family="Dast Nevis", size=14)

        #top label

        tkinter.Label(frame, text="ثبت نام", font=font1, bg=color_palette[3]).pack()

        #entry frame

        entry_frame = tkinter.Frame(frame, bg=color_palette[3])
        entry_frame.pack()
        font_English = font.Font(family="Roboto", size=12)
        font_persian = font.Font(family="Mj_Flow", size=16)
        pady = 0
        self.entries = []

        #first name
        
        tkinter.Label(entry_frame, text="نام", font=font_persian, bg=color_palette[3]).grid(row=0, column=1, padx=12, pady=pady)
        self.first_nam_var = tkinter.StringVar()
        first_nam_entry = tkinter.Entry(entry_frame, font=font_English, width=22, textvariable=self.first_nam_var, justify=tkinter.RIGHT,
         highlightthickness=0, bd=0)
        first_nam_entry.grid(row=0, column=0, padx=12, pady=pady)
        self.entries.append(first_nam_entry)

        #last name
        
        tkinter.Label(entry_frame, text="نام خانوادگی", font=font_persian, bg=color_palette[3]).grid(row=1, column=1, padx=12, pady=pady)
        self.last_nam_var = tkinter.StringVar()
        last_nam_entry = tkinter.Entry(entry_frame, font=font_English, width=22, textvariable=self.last_nam_var, justify=tkinter.RIGHT,
         highlightthickness=0, bd=0)
        last_nam_entry.grid(row=1, column=0, padx=12, pady=pady)
        self.entries.append(last_nam_entry)

        #phone number
        
        tkinter.Label(entry_frame, text="شماره تماس", font=font_persian, bg=color_palette[3]).grid(row=2, column=1, padx=12, pady=pady)
        self.phone_number_var = tkinter.StringVar()
        phone_number_entry = tkinter.Entry(entry_frame, font=font_English, width=22, textvariable=self.phone_number_var,
         highlightthickness=0, bd=0)
        phone_number_entry.grid(row=2, column=0, padx=12, pady=pady)
        self.entries.append(phone_number_entry)

        #email
        
        tkinter.Label(entry_frame, text="ایمیل", font=font_persian, bg=color_palette[3]).grid(row=3, column=1, padx=12, pady=pady)
        self.email_var = tkinter.StringVar()
        email_entry = tkinter.Entry(entry_frame, font=font_English, width=22, textvariable=self.email_var,
         highlightthickness=0, bd=0)
        email_entry.grid(row=3, column=0, padx=12, pady=pady)
        self.entries.append(email_entry)

        #id
        
        tkinter.Label(entry_frame, text="کد ملی", font=font_persian, bg=color_palette[3]).grid(row=4, column=1, padx=12, pady=pady)
        self.id_var = tkinter.StringVar()
        id_entry = tkinter.Entry(entry_frame, font=font_English, width=22, textvariable=self.id_var,
         highlightthickness=0, bd=0)
        id_entry.grid(row=4, column=0, padx=12, pady=pady)
        self.entries.append(id_entry)

        #password
        
        tkinter.Label(entry_frame, text="رمز عبور", font=font_persian, bg=color_palette[3]).grid(row=5, column=1, padx=12, pady=pady)
        self.password_var = tkinter.StringVar()
        password_entry = tkinter.Entry(entry_frame, font=font_English, width=22, textvariable=self.password_var, show='●',
         highlightthickness=0, bd=0)
        password_entry.grid(row=5, column=0, padx=12, pady=pady)
        self.entries.append(password_entry)

        #password confirm
        
        tkinter.Label(entry_frame, text="تکرار رمز عبور", font=font_persian, bg=color_palette[3]).grid(row=6, column=1, padx=12, pady=pady)
        self.password_confirm_var = tkinter.StringVar()
        password_confirm_var = tkinter.Entry(entry_frame, font=font_English, width=22, textvariable=self.password_confirm_var, show='●',
         highlightthickness=0, bd=0)
        password_confirm_var.grid(row=6, column=0, padx=12, pady=pady)
        self.entries.append(password_confirm_var)

        #message 

        self.message_label = tkinter.Label(frame, text=" ", font=font2, bg=color_palette[3])
        self.message_label.pack()

        #button frame

        button_frame = tkinter.Frame(frame, bg=color_palette[3])
        button_frame.pack(pady=12)
        font_persian = font.Font(family="Mj_Flow", size=14)

        #sign up button

        def Sign_UP():
            val = val_functions.create_account_val(self.first_nam_var.get(), self.last_nam_var.get(), self.id_var.get(),
             self.phone_number_var.get(), self.email_var.get(), self.password_var.get(), self.password_confirm_var.get(), DB)
            if(val == True):
                self.display_error_message(" ")
                self.display_confirm_message("ثبت نام با موفقیت انجام شد")
                DB.create_account(self.first_nam_var.get(), self.last_nam_var.get(), self.id_var.get(),
                 self.phone_number_var.get(), self.email_var.get(), self.password_var.get())
            else:
                self.display_error_message(val)

        tkinter.Button(button_frame, text="ثبت نام", font=font_persian, width=16, bg=color_palette[4],
        activebackground=color_palette[3], highlightthickness=0, bd=0, command=Sign_UP).grid(row=0, column=1, padx=10)
        
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
        entry_frame.pack(pady=12)
        font_English = font.Font(family="Roboto", size=12)
        font_persian = font.Font(family="Mj_Flow", size=16)
        self.entries = []
    
        #email
        
        tkinter.Label(entry_frame, text="ایمیل", font=font_persian, bg=color_palette[3]).grid(row=0, column=1, padx=12)
        self.email_var = tkinter.StringVar()
        email_entry = tkinter.Entry(entry_frame, font=font_English, width=22, textvariable=self.email_var,
         highlightthickness=0, bd=0)
        email_entry.grid(row=0, column=0, padx=12)
        self.entries.append(email_entry)

        #phone number
        
        tkinter.Label(entry_frame, text="شماره تماس", font=font_persian, bg=color_palette[3]).grid(row=1, column=1, padx=12)
        self.phone_number_var = tkinter.StringVar()
        phone_number_entry = tkinter.Entry(entry_frame, font=font_English, width=22, textvariable=self.phone_number_var,
         highlightthickness=0, bd=0)
        phone_number_entry.grid(row=1, column=0, padx=12)
        self.entries.append(phone_number_entry)

        #id
        
        tkinter.Label(entry_frame, text="کد ملی", font=font_persian, bg=color_palette[3]).grid(row=2, column=1, padx=12)
        self.id_var = tkinter.StringVar()
        id_entry = tkinter.Entry(entry_frame, font=font_English, width=22, textvariable=self.id_var,
         highlightthickness=0, bd=0)
        id_entry.grid(row=2, column=0, padx=12)
        self.entries.append(id_entry)

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
