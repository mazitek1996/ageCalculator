from datetime import date
current_year = date.today().year
today_date = date.today().day
month = date.today().month

name = input("What is your name?")
birth_year = input("What is your birth year?")
age = current_year - int(birth_year)

print("Hello", name , "Today's date is ",month, today_date, "and you're", age ,"years old" )