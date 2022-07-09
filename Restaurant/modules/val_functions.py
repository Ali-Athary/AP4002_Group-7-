'''
This mudule includes all validation functions
they return true if all given datas are in the 
currect form, otherwise they return the 
error message in a string form
'''

from modules import DataBase

def name_val(name): 
    # validates name
    l = [1570, 1574, 1575, 1576, 1578, 
    1579, 1580, 1581, 1582, 1583, 1584, 
    1585, 1586, 1587, 1588, 1589, 1590, 
    1591, 1592, 1593, 1594, 1601, 1602, 
    1604, 1605, 1606, 1607, 1608, 1610, 
    1662, 1670, 1705, 1711, 32]
    if len(name) == 0:
        return 'نام معتبر نیست'
    for c in name:
        if ord(c) not in l:
            return 'نام معتبر نیست'
    else:
        return True

def l_name_val(l_name): 
    # validates last name
    l = [1570, 1574, 1575, 1576, 1578, 
    1579, 1580, 1581, 1582, 1583, 1584, 
    1585, 1586, 1587, 1588, 1589, 1590, 
    1591, 1592, 1593, 1594, 1601, 1602, 
    1604, 1605, 1606, 1607, 1608, 1610, 
    1662, 1670, 1705, 1711, 32]
    if len(l_name) == 0:
        return 'نام خانوادگی معتبر نیست'
    for c in l_name:
        if ord(c) not in l:
            return 'نام خانوادگی معتبر نیست'
    else: return True

def id_val(id : str):
    # validates id
    if(id == None):
        return True
    if not id.isdigit() or len(id) != 10:
        return 'کدملی معتبر نیست'
    else: return True

def phone_number_val(phone : str):
    # validates phone number
    if not ((phone[:5] == '+9809' and len(phone[5:]) == 9 and phone[5:].isdigit()) 
            or (phone[:5] == '00989' and len(phone[5:]) == 9 and phone[5:].isdigit()) 
            or (phone[:1] == '9' and len(phone) == 10 and phone.isdigit()) 
            or (phone[:2] == '09' and len(phone) == 11 and phone.isdigit())):
                return 'شماره تلفن معتبر نیست'
    else: return True

def email_val(email : str):
    # validates email address
    dot_l = []
    for i, _ in enumerate(email):
        if _ == '.':
            dot_l.append(i)
    if not (len(dot_l) > 0 and email.count('@') == 1
    and email.find('@') < dot_l[-1] 
    and email[0] != '@' and email[-1] != '.'):
        return 'ادرس ایمیل معتبر نیست'
    else : return True

def account_existance_val(email, db : DataBase.DB):
    ''' checks if any account with the given email
     exists or not
    '''
    users = db.get_table_data('user')
    for  user in users:
        if user[3] == email:
            return 'حساب کاربری موجود است'
    else : return True

def create_account_val(name, l_name, id : str, phone : str, email : str, password : str, confirm_pass : str, db: DataBase.DB):
    ' validates data for creating an account '
    val = (name_val(name), 
    l_name_val(l_name), id_val(id), phone_number_val(phone),
    email_val(email), account_existance_val(email, db), password_validation(password, confirm_pass)
    )
    for _ in val:
        if _ != True:
            return _
    else : return True



def change_acc_info_val(name, l_name, id : str, phone, email, db: DataBase.DB, old_email):
    'validates data for changing accounts info'
    if email == old_email:
        val = (name_val(name), 
        l_name_val(l_name), id_val(id), phone_number_val(phone),
        )
        for _ in val:
            if _ != True:
                return _
        else : return True
    else:
        val = (name_val(name), 
        l_name_val(l_name), id_val(id), phone_number_val(phone),
        email_val(email), account_existance_val(email, db)
        )
        for _ in val:
            if _ != True:
                return _
        else : return True

    

def password_validation(password, confirm_pass):
    # validation function for password
    chars = {'low' : 0, 'upper' : 0, 'number' : 0}
    for c in password:
        if 'a' <= c <= 'z':
            chars['low'] += 1
        elif 'A' <= c <= 'Z':
            chars['upper'] += 1
        elif '0' <= c <= '9' :
            chars['number'] += 1
    
    if chars['low'] == 0:
        return 'رمز عبور باید شامل یک حرف کوچک باشد'
    elif chars['upper'] == 0:
        return 'رمز عبور باید شامل یک حرف بزرگ باشد'
    elif chars['number'] == 0:
        return 'رمز عبور باید شامل یک رقم باشد'
    elif len(password) < 8:
        return 'رمز عبور باید حداقل 8 کارکتر باشد'
    elif chars['low'] + chars['number'] + chars['upper'] == len(password):
        return 'رمز عبور باید شامل یک غیر عدد و حروف الفبا باشد'
    elif password != confirm_pass:
        return 'رمز عبور مطابقت ندارد'
    else:
        return True
    