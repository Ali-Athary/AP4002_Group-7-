import sqlite3
import os
from PIL import ImageTk, Image
import time
import UserAndManager
import Food

class DB:
    def __init__(self, path):
        if os.path.exists(path):
            self.con = sqlite3.connect(path)
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
                picture BLOB
                user_id TEXT
            )
            ''')

            # food table
            self.cur.execute('''
            CREATE TABLE food
            (
                food_id TEXT
                name TEXT, 
                price INTEGER, 
                picture BLOB, 
                discription TEXT
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
            ''')

            # users password table
            self.cur.execute('''
            CREATE TABLE password(
                user_id TEXT,
                password INTEGER
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
                picture BLOB
                personal_id TEXT PRIMARY KEY
                password TEXT
            )
            ''')

            # creating manager account
            self.cur.execute('''
            INSERT INTO admin(name, last_name, email, personal_id, password) VALUES(
                "name", "last_name", "email@mail.com", "p12345678", "password"
            )
            ''')
        self.con.commit()

    def create_account(self, name, l_name, 
        id, phone, email : str, password):

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
            date TEXT,
            count INTEGER,
            price INTEGER
        )
        ''')
        self.cur.execute(f'''
        CREATE TABLE {user_id}_order_log(
            purchase_number INTEGER,
            total_price INTEFER,
            off_code TEXT,
            off_value INTEGER,
            date TEXT
        )
        ''')

        # add a record to password table
        self.cur.execute('''
        INSERT INTO password VALUES (?, ?)
        ''', (user_id, hash(password)))
        self.con.commit()
    
    def change_account_info(self, new_name, new_l_name, 
        new_id, new_phone, new_email, email):
        # changes accounts info on data base
        user_id = self.get_user_id(email)
        self.cur.execute('''
        UPDATE user
        SET name = ?,
        l_name = ?,
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
        if hash(old_password) == hashed_pass:
            self.cur.execute('''
            UPDATE password SET password = ? WHERE user_id = ?
            ''', (hash(new_password), user_id))
            self.con.commit()
            return 0 # password changed successfully
        else:
            return 1 # password did not change
    
    def reset_password(self, email):
        user_id = self.get_user_id(email)
        # generate new password
        # email it
        # save the hash
        self.con.commit() 

    def get_user_obj(self, email, password):
        user_pass = self.cur.execute('''
        SELECT pasword FROM user WHERE email = ?
        ''', (email, )).fetchone()
        if user_pass != None and user_pass[0] == hash(password):
            user_id = self.get_user_id(email)
            return UserAndManager.User(user_id)
        else:
            return 'نام کاربری یا رمز عبور اشتباه است'

    def get_manager_obj(self, personal_id, password):
        user_pass = self.cur.execute('''
        SELECT pasword FROM admin WHERE personal_id = ?
        ''', (personal_id, )).fetchone()
        if user_pass != None and user_pass[0] == password:
            return UserAndManager.Manager(personal_id)
        else:
            return 'نام کاربری یا رمز عبور اشتباه است'
    
    def create_food(self):
        self.con.commit()

    def change_food_amount(self, food_id, changes):
        self.con.commit()

    def get_foods_obj(self, food_id):
        return []
    
    def get_user_log(self, email):
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
        for i in range(p_n_max, 0):
            food_list = []
            for record in temp_list_foods:
                if record(0) == i:
                    food_list.append(Food.FoodLog(*record[1:]))
            for order in temp_list_orders:
                if order[0] == i:
                    log_list.append(Food.OrderLog(food_list, order[1], order[2], order[3], order[4]))
            
        return log_list
        # returns a list that includes orderlog objects 
        # that each of them has a foodlists attr which is a
        # list that includes foodlog objects  
    
    def update_user_log(self, email, order_log : Food.OrderLog):
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
                ?, ?, ?, ?, ?
            )
        """, (p_n_max + 1, order_log.total_price, order_log.off_code, order_log.off_value, order_log.date))
        for food in order_log.foods_list:
            self.cur.execute(f'''
                INSERT INTO {user_id}_food_log VALUES(
                    ?, ?, ?, ?, ?
                )
            ''', (p_n_max, food.food_id, food.date, food.count, food.price))

        self.con.commit()
        
    def get_table_data(self, table):
        return self.cur.execute(f'''
            SELECT * FROM {table}
            ''').fetchall()
        
    def get_user_id(self, email):
        return self.cur.execute('''
        SELECT user_id FROM user WHERE email = ?
        ''', (email, )).fetchone()[0]

    def close(self):
        self.con.close()