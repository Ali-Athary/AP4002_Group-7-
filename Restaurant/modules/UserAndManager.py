from modules import DataBase
from PIL import Image
from modules import Food
from modules import val_functions

class Manager:
    def __init__(self, personal_id, name, l_name, 
    id, email, phone, picture):
        self.personal_id = personal_id
        self.name = name
        self.l_name = l_name
        self.id = id
        self.email = email
        self.phone = phone 
        self.picture = picture

class User:
    def __init__(self, name, l_name, id, email, phone, picture : Image.Image, user_id, db : DataBase.DB):
        self.name = name 
        self.l_name = l_name
        self.id = id
        self.email = email
        self.phone = phone
        self.picture = picture
        self.user_id = user_id
        self.db = db
        Food.Food.load_foods(self.db)
        self.last_order = self.get_last_order()
        self.order_log = self.get_order_log()
        self.total_price = self.get_total_price()
    def add_food_to_order_list(self, food : Food.Food, count, date):
        'select food from the menu'
        if food.amount - count < 0:
            return 'ناموفق'
        food.amount -= count
        self.last_order.append(Food.FoodLog(food.food_id, food.name, date , count, food.price))
        self.total_price = self.get_total_price()
        return 0
    def confirm_order(self, date, off_code):
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
        total_price = 0
        for food in temp_food:
            total_price += food.count * food.price
        order_log = Food.OrderLog(temp_food, total_price, date, off_code, self.db.discount_value(off_code))
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

    def get_order_log(self):
        return self.db.get_user_log(self.email)

    def change_account_info(self, name, l_name, phone, email):
        var = val_functions.change_acc_info_val(name,
        l_name, self.id, phone, email, self.db, self.email)
        if var == True:
            self.db.change_account_info(name, l_name, self.id,
            phone, email, self.email)
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
        ...
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
    