"""
Design an algorithm that determines the
day you were born, based on the date
"""

import datetime

def birthday(birthday_date):
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    index_day = birthday_date.weekday()
    return days[index_day]

if __name__ == '__main__':
    date_string = input("Enter your dirthday (YYY-MM-DD) : ")
    date_object = datetime.datetime.strptime(date_string, "%Y-%m-%d")
    day = birthday(date_object)
    print(f"You was born a {day}")
