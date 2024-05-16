from datetime import date

day = date.today().weekday()

lst = ["mon", "tue", "wed", "thurs", "fri", "sat"]

print(lst[day])