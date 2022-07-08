from modules import DataBase
from PIL import Image
from modules import Food
from modules import val_functions
import sys , os

class Manager:
    def __init__(self, personal_id, name, l_name, 
    id, email, phone, picture : bytes, db):
        self.personal_id = personal_id
        self.name = name
        self.l_name = l_name
        self.id = id
        self.email = email
        self.phone = phone 
        self.picture = DataBase.DB.bin_to_image(picture)
        if(self.picture == None):
            self.picture = Image.open(os.path.join(sys.path[0], "resources\panels\default_profile_picture.jpg")).convert("RGBA")
        if isinstance(db, DataBase.DB):
            self.db = db
        Food.Food.load_foods(self.db)

        self.get_owner_data()
        
    def change_account_info(self, name, l_name, phone, email):
        var = val_functions.change_acc_info_val(name, l_name, self.id,
            phone, email, self.db, self.email)
        if var == True:
            self.db.change_manager_info(self.personal_id, name,
                l_name, phone, email)
            self.name = name
            self.l_name = l_name
            self.phone = phone
            self.email = email
        else:
            return var
        
    def change_password(self, password, new_pass, confirm_pass):
        var = val_functions.password_validation(new_pass, confirm_pass)
        if var == True :
            if self.db.change_manager_password(self.personal_id, password, new_pass) == 0:
                return 0
            else:
                return 'رمزعبور نادرست است'
        else: return var
    
    def change_profile_pic(self, picture : Image.Image):
        self.picture = picture
        self.db.update_manager_profile(self.personal_id, picture)

    def change_menu_pic(self, pic):
        self.restaurant_menu = pic
        self.db.update_menu(pic)
    
    def change_owner_info(self, new_name, new_l_name,
            new_district, new_addrss):
        v1 = val_functions.name_val(new_name)
        v2 = val_functions.l_name_val(new_l_name)
        if v1 == True:
            if v2 == True:
                self.db.update_restaurant_data(new_name, new_l_name,
                        new_district, new_addrss)
                self.get_owner_data()
            else:
                return v2
        else:
            return v1

    def get_owner_data(self):
        row = self.db.get_table_data('restaurant_data')[0]
        self.manager_name = row[0]
        self.manager_last_name = row[1]
        self.restaurant_district = row[2]
        self.restaurant_address = row[3]
        self.restaurant_menu = self.db.bin_to_image(row[4])

    def create_food(self, name, price, discription1, discription2, picture : Image.Image):
        Food.Food.add_food(name, int(price), picture,
            discription1, discription2, self.db)
    
    def change_food_amount(self, food : Food.Food, count):
        food.update_food(count, self.db)

    def delete_food(self, food : Food.Food):
        Food.Food.delete_food(food, self.db)
    
    def view_comments(self):
        ...
    
class User:
    def __init__(self, name, l_name, id, email, phone, picture : bytes, user_id, db):
        self.name = name 
        self.l_name = l_name
        self.id = id
        self.email = email
        self.phone = phone
        self.picture = DataBase.DB.bin_to_image(picture)
        if(self.picture == None):
            self.picture = Image.open(os.path.join(sys.path[0], "resources\panels\default_profile_picture.jpg")).convert("RGBA")
        self.user_id = user_id
        self.db = db

        Food.Food.load_foods(self.db)

        self.off_code = ''
        self.last_order = self.get_last_order()
        self.order_log = self.get_order_log()

    def add_food_to_order_list(self, food : Food.Food, count, date):
        'select food from the menu'
        if food.amount - count < 0:
            return 'ناموفق'
        food.amount -= count
        self.last_order.append(Food.FoodLog(food.food_id, food.name, date , count, food.price))
        self.total_price = self.get_total_price()
        return 0

    def confirm_order(self, date):
        'confirm the order'
        i = []
        for index, foodlog in enumerate(self.last_order):
            for foodobj in Food.Food.food_list:
                if foodobj.food_id == foodlog.food_id:
                    if foodobj.update_food(-foodlog.count, self.db) != 0:
                        i.append(index)
        temp_food = []
        for index, food in enumerate(self.last_order):
            if index not in i:
                temp_food.append(food)
                
        order_log = Food.OrderLog(temp_food, self.get_total_price(), date, self.off_code, self.db.use_discount(self.off_code))
        self.db.update_user_log(self.email, order_log)
        self.order_log = self.db.get_user_log()
        self.last_order = []
        self.save_last_order()

    def get_last_order(self):
        'get the last order from data-base'
        table = self.db.get_table_data('last_order')
        for _ in table:
            if _[0] == self.user_id:
                last_order = _[1]
                break
        last_order = last_order.split('|')
        if len(last_order) == 1:
            return []
        else:
            return list(map(lambda x: Food.FoodLog(*x.split('$')), last_order))

    def save_last_order(self):
        'save the unfinished order to the data-base'
        food_data = ''
        for food in self.last_order:
            food_data += f'{food.food_id}${food.name}${food.date}${food.count}|'
        if len(food_data) != 0:
            return food_data[:-1]
        else:
            return ''

    def remove_from_last_order(self, foodlog : Food.FoodLog):
        'remove a food log from last order'
        self.last_order.remove(foodlog)
        for food_obj in Food.Food.food_list:
            if food_obj.food_id == foodlog.food_id:
                food_obj.amount += foodlog.count

    def get_total_price(self):
        x = 0
        for _ in self.last_order:
            x += _.count * _.price
        return x

    def purchasable_price(self):
        v =  self.get_total_price() - self.db.get_discount_value(self.off_code)
        if v < 0:
            return 0
        return v
    
    def apply_discount(self, code):
        self.off_code = code

    def get_order_log(self):
        return self.db.get_user_log(self.email)

    def change_account_info(self, name, l_name, phone, email):
        var = val_functions.change_acc_info_val(name,
        l_name, self.id, phone, email, self.db, self.email)
        if var == True:
            self.db.change_account_info(name, l_name, self.id,
            phone, email, self.email)
            self.name = name
            self.l_name = l_name
            self.phone = phone
            self.email = email
        else:
            return var

    def change_password(self, password, new_password, confirm_pass):
        var = val_functions.password_validation(new_password, confirm_pass)
        if var == True:
            if self.db.change_password(self.email, password, new_password) == 0:
                return 0 # successfully changed
            else: return 'رمز عبور نادرست است'
        else: return var

    def change_profile_pic(self, picture : Image.Image):
        self.picture = picture
        self.db.update_user_profile(self.user_id, picture)

    def submit_opinion(self, text : str):
        self.db.add_opinion(text)

    def get_last_order_dict(self):
        last_order_dict = {}
        for foodlog in self.last_order:
            if foodlog.date in last_order_dict.keys():
                last_order_dict[foodlog.date].append(foodlog)
            else:
                last_order_dict[foodlog.date] = [foodlog]
        return last_order_dict
    