# date and time (latihan)

import datetime as dt

# user birth input
print("\nPlease enter your date, month and year of birth!!\n")
date = int(input("Date\t\t= "))
month = int(input("Month\t\t= "))
year = int(input("Year\t\t= "))

# birth user
user_birth = dt.date(year, month, date)
print(f"\nYour birth is {user_birth:%A}, {user_birth}")

# today
today = dt.date.today()
print(f"Today is {today:%A}, {today}")

# calculate user age
user_day_age = today - user_birth
user_age = user_day_age.days // 365
month_modulus = (user_day_age.days % 365) // 30

print(f"\nYour age is {user_day_age}, or {user_age} year {month_modulus} month\n")
