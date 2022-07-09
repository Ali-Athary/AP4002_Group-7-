from modules import DataBase
from PIL import Image

class Food:
    '''each food is an object of this class
    after logging in all food-data will be
    loaded from data-base with Food.load_foods
    and will be saved in Food.food_list
    '''
    food_list = []
    def __init__(self, food_id, name, price, original_price,
    picture, discription1, discription2, amount):
        '''initial method of food class
        a food object has food_id, name, price, picture
        , discription and amount attribiute'''
        self.food_id = int(food_id)
        self.name = name
        self.price = int(price)
        self.original_price = original_price
        self.picture = picture
        self.discription = [discription1, discription2]
        self.amount = int(amount)

    @classmethod
    def add_food(cls, name, price, original_price, picture : Image.Image, discription1, discription2, db):
        'adds a new food to both list and data-base'
        food_id = 0
        for food in cls.food_list:
            if food.food_id > food_id:
                food_id = food.food_id
        food = Food(food_id + 1, name, price, original_price, picture, discription1, discription2, 0)
        cls.food_list.insert(0, food)
        db.create_food(food_id + 1, name, price, original_price, picture, discription1, discription2, 0)

    def update_food(self, changes, db):
        'changes the amount of food'
        if db.change_food_amount(self.food_id, changes) == 0:
            if changes > 0:
                self.amount += changes
            return 0
        else:
            if changes < 0:
                food_table = db.get_table_data('food')
                for data_base_food in food_table:
                    if data_base_food[0] == self.food_id:
                        self.amount = data_base_food[6]
            return 'ناموفق'

    @classmethod
    def load_foods(cls, db):
        'loads all foods and save the in cls.food_list'
        cls.food_list = db.get_foods_obj()

    @classmethod
    def reload_foods(cls, db):
        'reload all foods'
        food_table = db.get_table_data('food')
        for data_base_food in food_table:
            for food_obj in cls.food_list:
                if data_base_food[0] == food_obj.food_id:
                    food_obj.amount = data_base_food[6]
                    break
    
    @classmethod
    def delete_food(cls, food, db):
        cls.food_list.remove(food)
        db.delete_food(food.food_id)
        
    def __repr__(self) -> str:
        return f"Food obj | id = {self.food_id}, \
        name = {self.name}, price = {self.price}, \
        original price : {self.original_price} \
        discriptions : \n \
        {self.discription[0]}\n \
        {self.discription[1]}"

class OrderLog:
    'order log is a record of a successfull purchase that includes a list of foodlogs'
    def __init__(self, food_log_list, total_price, original_price, date, off_code = None, off_value = 0, confirm = '', purchase_number = 0):
        self.food_log_list = food_log_list
        self.total_price = int(total_price)
        self.original_price = int(original_price)
        self.off_code = off_code
        self.off_value = int(off_value)
        self.date = date
        self.confirm = confirm
        self.purchase_number = purchase_number
    def __repr__(self) -> str:
        return f"OrderLog object | total price : {self.total_price}, date : {self.date} \n \
            food list : \n \
            {self.food_log_list}"
      
class FullOrderLog(OrderLog):
    def __init__(self, food_log_list, total_price, original_price, date, user_email, user_name, off_code=None, off_value=0, confirm='', purchase_number = 0):
        super().__init__(food_log_list, total_price, original_price, date, off_code, off_value, confirm, purchase_number)
        self.user_email = user_email
        self.user_name = user_name
        
class FoodLog:
    'foodlog object is a food record that purchased or is in the last order'
    def __init__(self, food_id, name, date, count, price, original_price):
        self.name = name
        self.date = date
        self.count = int(count)
        self.price = int(price)
        self.original_price = int(original_price)
        self.food_id = int(food_id)
    def __repr__(self) -> str:
        return f"FoodLog object | name : {self.name}, date : {self.date}, count : {self.count}, price : {self.price}"
