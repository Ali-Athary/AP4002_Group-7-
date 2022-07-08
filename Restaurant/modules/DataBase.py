import sqlite3
import os, sys
from PIL import Image
import time
from modules import UserAndManager
from modules import Food
import hashlib
from io import BytesIO

class DB:
    def __init__(self, path):
        if os.path.exists(path):
            self.con = sqlite3.connect(path)
            self.cur = self.con.cursor()
        else:
            self.con = sqlite3.connect(path)
            self.cur = self.con.cursor()

            # user table
            self.cur.execute('''
            CREATE TABLE user
            (
                name TEXT, 
                last_name TEXT, 
                id TEXT, 
                email TEXT PRIMARY KEY,
                phone TEXT,
                picture BLOB,
                user_id TEXT
            )
            ''')

            # food table
            self.cur.execute('''
            CREATE TABLE food
            (
                food_id INTEGER,
                name TEXT, 
                price INTEGER, 
                orginal_price INTEGER,
                picture BLOB, 
                discription TEXT,
                count INTEGER
            ) 
            ''')

            # last order table
            self.cur.execute('''
            CREATE TABLE last_order
            (
                user_id TEXT,
                food_data TEXT
            )
            ''') # food_data : |food_id$name$date$count|

            # users password table
            self.cur.execute('''
            CREATE TABLE password(
                user_id TEXT,
                password TEXT
            )
            ''')
            
            # admins data table
            self.cur.execute('''
            CREATE TABLE admin
            (
                name TEXT, 
                last_name TEXT, 
                id TEXT, 
                email TEXT,
                phone TEXT,
                picture BLOB,
                personal_id TEXT PRIMARY KEY,
                password TEXT
            )
            ''')

            # creating manager account
            self.cur.execute('''
            INSERT INTO admin(name, last_name, email, personal_id, password) VALUES(
                "name", "last_name", "email@mail.com", "p12345678", "password"
            )
            ''')

            # restaurant data
            self.cur.execute(
                '''
                CREATE TABLE restaurant_data
                (
                    owner_name TEXT,
                    owner_last_name TEXT,
                    district TEXT,
                    restaurant_address TEXT,
                    menu_pic BLOB
                )
                '''
            )
            self.cur.execute(
                '''
                INSERT INTO restaurant_data VALUES (
                    ?, ?, ?, ?, ?
                )
                '''
            ,('نام', 'نام خانوادگی', 'hakimie', 'address', self.image_to_bin(Image.open(os.path.join(sys.path[0], "resources\panels\menu_image.jpg")))))

            self.cur.execute('''
            CREATE TABLE discount(
                offcode TEXT,
                off_value INTEGER
            )
            ''')
        
            # opinion
            self.cur.execute('''
            CREATE TABLE opinion(
                text TEXT,
                viewed INTEGER
            )
            ''')
        self.con.commit()
    
    def create_account(self, name, l_name, 
        id, phone, email : str, password):
        'create a user account'

        # user_id is constant for all users
        user_id = email[:email.find('@')] + \
        email[email.find('@') + 1:email.find('.')] + \
        email[email.find('.') + 1:] + str(int(time.time()))

        # put records in user table
        self.cur.execute('''
        INSERT INTO user(name, last_name, id, email, phone, user_id) VALUES
        (?, ?, ?, ?, ?, ?)
        ''', (name, l_name, id, email, phone, user_id))

        # create user_id_log table which stores previous purchases 
        self.cur.execute(f'''
        CREATE TABLE {user_id}_food_log(
            purchase_number INTEGER,
            food_id TEXT,
            name TEXT,
            date TEXT,
            count INTEGER,
            price INTEGER,
            original_price INTEGER
        )
        ''')
        self.cur.execute(f'''
        CREATE TABLE {user_id}_order_log(
            purchase_number INTEGER,
            total_price INTEFER,
            orginal_price INTEGER,
            date TEXT,
            off_code TEXT,
            off_value INTEGER,
            confirm INTEGER
        )
        ''')
        self.cur.execute('''
        INSERT INTO last_order VALUES (?, ?)
        ''', (user_id, ''))
        # add a record to password table
        self.cur.execute('''
        INSERT INTO password VALUES (?, ?)
        ''', (user_id, hashlib.sha224(bytes(password, 'utf-8')).hexdigest()))
        self.con.commit()

    def change_account_info(self, new_name, new_l_name, 
        new_id, new_phone, new_email, email):
        # changes accounts info on data base
        user_id = self.get_user_id(email)
        self.cur.execute('''
        UPDATE user
        SET name = ?,
        last_name = ?,
        id = ?,
        phone = ?,
        email = ?
        WHERE user_id = ?
        ''', (new_name, new_l_name, new_id, new_phone, new_email, user_id))
        self.con.commit()
    
    def change_password(self, email, old_password, new_password):
        # changes password directly
        user_id = self.get_user_id(email)
        hashed_pass = self.cur.execute('''
        SELECT * FROM password WHERE user_id = ?
        ''', (user_id, )).fetchone()[1]
        if hashlib.sha224(bytes(old_password, 'utf-8')).hexdigest() == hashed_pass:
            self.cur.execute('''
            UPDATE password SET password = ? WHERE user_id = ?
            ''', (hashlib.sha224(bytes(new_password, 'utf-8')).hexdigest(), user_id))
            self.con.commit()
            return 0 # password changed successfully
        else:
            return 1 # password did not change
    
    def reset_password(self, email, id, phone):
        user_id = self.get_user_id(email)
        # generate new password
        # email it
        # save the hash
        self.con.commit() 

    def get_user_obj(self, email, password):
        'logging in to user account'
        user_id = self.cur.execute('''
        SELECT user_id FROM user WHERE email = ?
        ''', (email, )).fetchone()
        if(user_id != None):
            user_id = user_id[0]
            user_pass = self.cur.execute('''
            SELECT password FROM password WHERE user_id = ?
            ''', (user_id, )).fetchone()
            if user_pass[0] == hashlib.sha224(bytes(password, 'utf-8')).hexdigest():
                data = self.cur.execute('''
                SELECT * from user WHERE user_id = ?
                ''', (user_id, )).fetchone()
                return UserAndManager.User(data[0], data[1], data[2], 
                data[3], data[4], data[5], user_id, self)
            else:
                return 'نام کاربری یا رمز عبور اشتباه است'
        else:
            return 'نام کاربری یا رمز عبور اشتباه است'

    def get_manager_obj(self, personal_id, password):
        'logging in to manager account'
        user_pass = self.cur.execute('''
        SELECT password FROM admin WHERE personal_id = ?
        ''', (personal_id, )).fetchone()
        if user_pass != None and user_pass[0] == password:
            x = self.cur.execute('''
                SELECT * FROM admin WHERE personal_id = ?
                ''', (personal_id, )).fetchone()
            return UserAndManager.Manager(personal_id, *x[:6], self)
        else:
            return 'نام کاربری یا رمز عبور اشتباه است'
    
    def change_manager_info(self, personal_id, name, l_name, phone, email):
        'change manager account info'
        self.cur.execute('''
            UPDATE admin
            SET name = ?,
                last_name = ?,
                phone = ?,
                email = ?
            WHERE personal_id = ?
        ''', (name, l_name, phone, email, personal_id))
        self.con.commit()

    def change_manager_password(self, personal_id, password, new_pass):
        'change manager acounts password'
        user_pass = self.cur.execute(
            '''
            SELECT password FROM admin WHERE personal_id = ?
            ''', (personal_id, )
        )[0]
        if user_pass == password:
            self.cur.execute(
                '''
                UPDATE admin SET password = ? WHERE personal_id = ?
                ''', (new_pass, personal_id)
            )
            return 0 # successfull
        else:
            return 1 # not successfull
        
    def create_food(self, food_id, name, price, original_price, picture, discription1, discription2, count):
        'create a new food'
        discription = self.discription_list_to_str(discription1, discription2)
        picture = self.image_to_bin(picture)
        self.cur.execute('''
            INSERT INTO food VALUES(
                ?, ?, ?, ?, ?, ?, ?
            )
        ''', (food_id, name, price, original_price, picture, discription, count))
        self.con.commit()

    def change_food_amount(self, food_id, changes : int):
        '''changes food amount in the data-base
            returns 0 if it was successful
            otherwise returns 1
        '''
        if changes > 0:
            # add
            amount = self.cur.execute('''
                SELECT count FROM food WHERE food_id = ?
            ''', (food_id, )).fetchone()[0]
            self.cur.execute('''
                UPDATE food
                SET count = ?
                WHERE food_id = ?
            ''', (amount + changes, food_id))
            self.con.commit()
            return 0
        elif changes < 0:
            # buy food
            amount = self.cur.execute('''
                SELECT count FROM food WHERE food_id = ?
            ''', (food_id, )).fetchone()[0]
            if amount + changes < 0:
                self.con.commit()
                return 1
            else:
                self.cur.execute('''
                    UPDATE food
                    SET count = ?
                    WHERE food_id = ?
                ''', (amount + changes, food_id))
                self.con.commit()
                return 0

    def get_foods_obj(self):
        'get all food objs'
        food_list = []
        table = self.get_table_data('food')
        for _ in table:
            food_list.append(Food.Food(_[0], _[1], _[2], _[3], 
            self.bin_to_image(_[4]), 
            self.discription_str_to_list(_[5])[0], 
            self.discription_str_to_list(_[5])[1],
            _[6]))
        return food_list
    
    def get_user_log(self, email):
        'get all order log of an account'
        user_id = self.get_user_id(email)
        log_list = []
        temp_list_foods = self.cur.execute(f"""
            SELECT * FROM {user_id}_food_log
        """).fetchall()
        temp_list_orders = self.cur.execute(f"""
            SELECT * FROM {user_id}_order_log
        """).fetchall()
        p_n_max = 0
        for i in temp_list_foods:
            if i[0] > p_n_max:
                p_n_max = i[0]
        for i in range(p_n_max + 1, 0, -1):
            food_list = []
            for record in temp_list_foods:
                if record[0] == i - 1:
                    food_list.append(Food.FoodLog(*record[1:]))
            for order in temp_list_orders:
                if order[0] == i - 1:
                    log_list.append(Food.OrderLog(food_list, order[1], order[2], order[3], order[4], order[5], order[6], order[0]))
            
        return log_list
        # returns a list that includes orderlog objects 
        # that each of them has a foodlists attr which is a
        # list that includes foodlog objects  
    
    def update_user_log(self, email, order_log : Food.OrderLog):
        'add a new order-log to db'
        user_id = self.get_user_id(email)
        temp = self.cur.execute(f"""
            SELECT * FROM {user_id}_order_log
        """).fetchall()
        p_n_max = 0
        for record in temp:
            if record[0] > p_n_max:
                p_n_max = record[0]
        self.cur.execute(f"""
            INSERT INTO {user_id}_order_log VALUES
            (
                ?, ?, ?, ?, ?, ?, ?
            )
        """, (p_n_max + 1, order_log.total_price, order_log.original_price, order_log.date, order_log.off_code, order_log.off_value, order_log.confirm))
        for food in order_log.food_log_list:
            self.cur.execute(f'''
                INSERT INTO {user_id}_food_log VALUES(
                    ?, ?, ?, ?, ?, ?, ?
                )
            ''', (p_n_max + 1, food.food_id, food.name, food.date, food.count, food.price, food.original_price))

        self.con.commit()
    
    def delete_food(self, food_id):
        'delete a food'
        self.cur.execute('''
        DELETE FROM food WHERE food_id = ?
        ''', (food_id, ))
        self.con.commit()

    def get_table_data(self, table):
        'get a tables data'
        table = self.cur.execute(f'''
            SELECT * FROM {table}
            ''').fetchall()
        self.con.commit()
        return table
        
    def get_user_id(self, email):
        'get user id of an account'
        return self.cur.execute('''
        SELECT user_id FROM user WHERE email = ?
        ''', (email, )).fetchone()[0]
    
    def update_user_profile(self, user_id, picture : Image.Image):
        'update users profile'
        self.cur.execute(
            '''
            UPDATE user
            SET picture = ?
            WHERE user_id = ?
            ''', (self.image_to_bin(picture), user_id)
        )
        self.con.commit()
    
    def update_manager_profile(self, personal_id, picture : Image.Image):
        'update managers profile'
        self.cur.execute(
            '''
            UPDATE admin
            SET picture = ?
            WHERE personal_id = ?
            ''', (self.image_to_bin(picture), personal_id)
        )
        self.con.commit()


    def update_menu(self, menu : Image.Image):
        'update menu pic'
        self.cur.execute(
            '''
            UPDATE restaurant_data
            SET menu_pic = ?
            WHERE rowid = ?
            ''', (self.image_to_bin(menu), 0)
        )
        self.con.commit()
    
    def update_restaurant_data(self, name, l_name,
            district, address):
        'update restaurant data'
        self.cur.execute(
            '''
            UPDATE restaurant_data
            SET owner_name = ?,
                owner_last_name = ?,
                district = ?,
                restaurant_address = ?
            ''', (name, l_name, district, address)
        )
        self.con.commit()

    def close(self):
        'close connection'
        self.con.close()
    
    @staticmethod
    def discription_list_to_str(discription1, discription2):
        return discription1 + '|' + discription2
    @staticmethod
    def discription_str_to_list(discription_str : str):
        return discription_str.split('|')
    @staticmethod
    def image_to_bin(image: Image.Image):
        try:
            image.save(os.path.join(sys.path[0], "database\\temp.jpg"))
            with open(os.path.join(sys.path[0], "database\\temp.jpg"), 'rb') as file:
                bin_image = file.read()
            os.system('del ' + os.path.join(sys.path[0], "database\\temp.jpg"))
            os.system('rm ' + os.path.join(sys.path[0], "database\\temp.jpg"))
            return bin_image
        except TypeError:
            return None
    @staticmethod
    def bin_to_image(bin : bytes):
        try:
            return Image.open(BytesIO(bin))
        except TypeError:
            return None

    def update_last_order(self, user_id, food_data):
        'update last order for the next session'
        self.cur.execute('''
        UPDATE last_order
        SET food_data = ?
        WHERE user_id = ?
        ''', (food_data, user_id))
    
    def add_discount_code(self, code, value):
        'add a new discount code'
        self.cur.execute('''
        INSERT INTO discount VALUES(?, ?)
        ''', (code, value))

    def get_discount_value(self, code):
        'get the value of a discount code'
        value =  self.cur.execute('''
        SELECT off_value FROM discount WHERE 
        offcode = ?
        ''', (code, )).fetchone()
        if value != None:
            return value[0]

    def use_discount(self, code) -> int:
        'use the discount code'
        value = self.cur.execute('''
        SELECT off_value FROM discount WHERE 
        offcode = ?
        ''', (code, )).fetchone()
        if value == None:
            return 0
        self.cur.execute('''
        DELETE FROM discount WHERE offcode = ?
        ''', (code, ))
        self.con.commit()
        return value[0]

    def add_opinion(self, text):
        'add comment'
        self.cur.execute(
            '''
            INSERT INTO opinion VALUES(
                ?, ?
            )
            ''', (text, 0)
        )
        self.con.commit()

    def view_opinion(self):
        'view all new comments'
        table = self.get_table_data('opinion')
        self.cur.execute(
            '''
            UPDATE SET viewed = 1
            '''
        )
        self.con.commit()
        opinions = []
        for _ in table:
            if _[1] == 0:
                opinions.append(_[0])
        return opinions
    
    def confirm_order(self, email, purchase_number):
        'confirm the order'
        user_id = self.get_user_id(email)
        self.cur.execute(
            f'''
            UPDATE {user_id}_order_log
            SET confirm = 1
            WHERE purchase_number = ?
            ''', (purchase_number)
        )
        ...
        self.con.commit()
    
    def today_order_log(self, date):
        'get todays order logs'
        total_price = 0
        total_original_price = 0
        total_discount = 0
        temp_list = []
        user_table = self.get_table_data('user')
        for row in user_table:
            email = row[3]
            for log in self.get_user_log(email):
                if log.date == date:
                    total_price += log.total_price
                    total_original_price += log.original_price
                    total_discount += log.off_value
                    for food_log in log.food_log_list:
                        for _ in temp_list:
                            if _.food_id == food_log.food_id:
                                _.count += food_log.count
                                break
                        else:
                            temp_list.append(food_log)        
        return Food.OrderLog(temp_list, total_price, 
            total_original_price, date,
            off_value = total_discount)

    def get_user_name_email_list(self):
        temp = []
        table = self.get_table_data('user')
        for row in table:
            temp.append((row[0], row[3]))
        return temp