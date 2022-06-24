import tkinter
from tkinter import font, ttk
from PIL import ImageTk, Image  
import os
import sys
import jdatetime

class Suggestion_panel(tkinter.Label):
    def __init__(self, root, color_palette):
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

        text_box = tkinter.Text(self, height=10, width=55, font=font1, bg=self.color_palette[2])
        def Right_to_Left(event):
            text_box.tag_configure('tag-right', justify='right')
            text_str =  text_box.get("1.0",tkinter.END)
            text_box.delete("1.0", tkinter.END)
            text_box.insert('end', text_str, 'tag-right')
        text_box.bind("<Key>", Right_to_Left)
        text_box.pack()
    

    def show(self):
        self.place(x=20, y=20)

    def hide(self):
        self.place_forget()
