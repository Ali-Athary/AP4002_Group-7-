import jdatetime

def turn_int_to_price(n):
    n = str(n)
    result = ""
    for i in range((len(n) -1) // 3):
        result += n[::-1][3*i:3*(i+1)]
        result += ','
    result = result[::-1]
    result = n[:len(n)-((len(n) -1) // 3) * 3] + result
    return result

def get_date():
    d = jdatetime.datetime.now().date()
    return f"{d.year}/{d.month}/{d.day}"


