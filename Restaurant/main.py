import tkinter 
from modules import GUI_log_in_and_sign_up, GUI_user, GUI_manager, DataBase
import os, sys
 
color_palette = ["#361d32", "#543c52", "#f55951", "#f1e8e6", "#edd2cb"]

class App(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.state('zoomed')
        self.configure(bg= color_palette[4])
        self.title("Restaurant")

        db = DataBase.DB(os.path.join(sys.path[0], "database/database.db"))

        GUI_log_in_and_sign_up.main(self, color_palette, db)

        self.mainloop()        
 
    def open_user_app(self, user):
        GUI_user.main(self, color_palette, user)

    def open_manager_app(self, admin):
        GUI_manager.main(self, color_palette, admin)


if __name__ == "__main__":
    app = App()