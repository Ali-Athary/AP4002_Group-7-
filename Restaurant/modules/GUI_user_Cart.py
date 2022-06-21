import tkinter
from tkinter import font, ttk
from PIL import ImageTk, Image  
import os
import sys
import jdatetime

class Cart_panel(tkinter.Label):
    def __init__(self, root, color_palette):
        self.color_palette = color_palette
        img = Image.open(os.path.join(sys.path[0], "resources\panels\\user_food_menu_panel.png")).convert("RGBA")
        image = ImageTk.PhotoImage(img)

        super().__init__(root, image=image, bg=color_palette[4], bd=0)
        self.image = image

    def show(self):
        self.place(x=20, y=20)

    def hide(self):
        self.place_forget()