import tkinter 
from modules import GUI_log_in_and_sign_up, GUI_user
 
color_palette = ["#361d32", "#543c52", "#f55951", "#f1e8e6", "#edd2cb"]

class App(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.state('zoomed')
        self.configure(bg= color_palette[4])
        self.title("Restaurant")

        #GUI_log_in_and_sign_up.main(self, color_palette)
        GUI_user.main(self, color_palette)

        self.mainloop()        


if __name__ == "__main__":
    app = App()