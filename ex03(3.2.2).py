'''
def triple(x):
    print(x * 3)


triple(2)
triple('x')
'''

'''
from datetime import datetime

def korean_age(y):
    today = datetime.today().year
    return today - y + 1


print(f"한국 나이는 : {korean_age(1999)}살")
print(f"한국 나이는 : {korean_age(1992)}살")
print(f"한국 나이는 : {korean_age(1968)}살")
print(f"한국 나이는 : {korean_age(1970)}살")
'''


from datetime import datetime


def korean_age(birth_year):
    today = datetime.today()
    today_y = today.year
    today_m = today.month
    today_d = today.day
    is_korean = input('Are you Korean?(y/n): ')
    if is_korean.lower() == 'n':
        input_month = int(input('Input your birthday month(MM): '))
        input_day = int(input('Input your birthday day(DD): '))
        if today_m > input_month or ((today_m >= input_month) and (today_d >= input_day)):
            return today_y - birth_year
        else:
            return today_y - birth_year - 1
    elif is_korean.lower() == 'y':
        return today_y - birth_year + 1
    else:
        pass


print(korean_age(1992))
