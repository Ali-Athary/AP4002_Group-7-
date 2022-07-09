from modules import DataBase
from PIL import Image
from modules import Food
from modules import val_functions
import sys , os
from io import BytesIO

class Manager:
    def __init__(self, personal_id, name, l_name, 
    id, email, phone, picture : bytes, db):
        self.personal_id = personal_id
        self.name = name
        self.l_name = l_name
        self.id = id
        self.email = email
        self.phone = phone 
        if(picture == None):
            self.picture = Image.open(os.path.join(sys.path[0], "resources\panels\default_profile_picture.jpg")).convert("RGBA")
        else:
            self.picture = DataBase.DB.bin_to_image(picture)
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

    def create_food(self, name, price, original_price, discription1, discription2, picture : Image.Image):
        Food.Food.add_food(name, int(price), int(original_price), picture,
            discription1, discription2, self.db)
    
    def change_food_amount(self, food : Food.Food, count):
        food.update_food(count, self.db)

    def delete_food(self, food : Food.Food):
        Food.Food.delete_food(food, self.db)
    
    def view_comments(self):
        'returns a list of text, date, senders_name pair'
        return self.db.view_opinion()
    
    def create_discount_code(self, code, value):
        self.db.add_discount_code(code, value)
    
    def get_today_order_log(self, date):
        return self.db.today_order_log(date)
    
    def get_confirmed_orders(self):
        name_and_email = self.db.get_user_name_email_list()
        full_orders_list = []
        for name, email in name_and_email:
            orders = self.db.get_user_log(email)
            for order in orders:
                if order.confirm:
                    full_order = Food.FullOrderLog(
                        order.food_log_list,
                        order.total_price,
                        order.original_price,
                        order.date,
                        email, name, confirm= order.confirm,
                        purchase_number= order.purchase_number
                    )
                    full_orders_list.append(full_order)
        return sorted(full_orders_list, key = lambda x : x.date)
    
    def get_not_confirmed_orders(self):
        name_and_email = self.db.get_user_name_email_list()
        full_orders_list = []
        for name, email in name_and_email:
            orders = self.db.get_user_log(email)
            for order in orders:
                if not order.confirm:
                    full_order = Food.FullOrderLog(
                        order.food_log_list,
                        order.total_price,
                        order.original_price,
                        order.date,
                        email, name, confirm= order.confirm,
                        purchase_number= order.purchase_number
                    )
                    full_orders_list.append(full_order)
        return sorted(full_orders_list, key = lambda x : x.date)
    
    def get_all_orders(self):
        name_and_email = self.db.get_user_name_email_list()
        full_orders_list = []
        for name, email in name_and_email:
            orders = self.db.get_user_log(email)
            for order in orders:
                full_order = Food.FullOrderLog(
                    order.food_log_list,
                    order.total_price,
                    order.original_price,
                    order.date,
                    email, name, confirm= order.confirm,
                    purchase_number= order.purchase_number
                )
                full_orders_list.append(full_order)
        return sorted(full_orders_list, key = lambda x : x.date)
    
    def confirm_order(self, full_order : Food.FullOrderLog, date):
        self.db.confirm_order(full_order.user_email, 
            full_order.purchase_number, date)

class User:
    def __init__(self, name, l_name, id, email, phone, picture : bytes, user_id, db):
        self.name = name 
        self.l_name = l_name
        self.id = id
        self.email = email
        self.phone = phone
        if(picture == None):
            self.picture = Image.open(os.path.join(sys.path[0], "resources\panels\default_profile_picture.jpg")).convert("RGBA")
        else:
            self.picture = DataBase.DB.bin_to_image(picture)
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
        for _ in self.last_order:
            if (_.food_id == food.food_id and _.date == date):
                _.count += count
                break
        else:
            self.last_order.append(Food.FoodLog(food.food_id, food.name, date , count, food.price, food.original_price))
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
                
        order_log = Food.OrderLog(temp_food, self.get_total_price(), self.get_orginal_price(), date, self.off_code, self.db.use_discount(self.off_code))
        self.db.update_user_log(self.email, order_log)
        self.order_log = self.db.get_user_log(self.email)
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
        if last_order == ['']:
            last_order = []
        else:
            last_order = list(map(lambda x: Food.FoodLog(*x.split('$')), last_order))

        i_list = []
        for i, log in enumerate(last_order):
            for food in Food.Food.food_list:
                if food.food_id == log.food_id:
                    if food.amount - log.count >= 0:
                        food.amount -= log.count
                    else:
                        i_list.append(i)
        for _ in i_list:
            last_order.pop(_)
        
        return last_order

    def save_last_order(self):
        'save the unfinished order to the data-base'
        food_data = ''
        for food in self.last_order:
            food_data += f'{food.food_id}${food.name}${food.date}${food.count}${food.price}${food.original_price}|'
        if len(food_data) != 0:
            self.db.update_last_order(self.user_id, food_data[:-1])
        else:
            return self.db.update_last_order(self.user_id, '')

    def remove_from_last_order(self, foodlog : Food.FoodLog, count = -1):
        'remove a food log from last order or decrease the amount of it'
        if count == -1 or foodlog.count == count:
            self.last_order.remove(foodlog)
            for food_obj in Food.Food.food_list:
                if food_obj.food_id == foodlog.food_id:
                    food_obj.amount += foodlog.count
        else:
            foodlog.count -= count
            for food_obj in Food.Food.food_list:
                if food_obj.food_id == foodlog.food_id:
                    food_obj.amount += count  

    def get_total_price(self):
        x = 0
        for _ in self.last_order:
            x += _.count * _.price
        return x
    
    def get_orginal_price(self):
        x = 0
        for _ in self.last_order:
            x += _.count * _.original_price
        return x

    def purchasable_price(self):
        try:
            v =  self.get_total_price() - self.db.get_discount_value(self.off_code)
        except TypeError:
            v = self.get_total_price()
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

    def submit_opinion(self, text : str, date):
        self.db.add_opinion(text, date, self.name + ' ' + self.l_name)

    def get_last_order_dict(self):
        last_order_dict = {}
        for foodlog in self.last_order:
            if foodlog.date in last_order_dict.keys():
                last_order_dict[foodlog.date].append(foodlog)
            else:
                last_order_dict[foodlog.date] = [foodlog]
        return last_order_dict
    