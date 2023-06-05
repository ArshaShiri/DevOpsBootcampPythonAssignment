from datetime import datetime
birthday = input("Enter your birthday (format: dd/mm/yyyy): ")

birthday_date = datetime.strptime(birthday, '%d/%m/%Y').date()
today = datetime.today()

birthday_current_year = datetime(today.year, birthday_date.month, birthday_date.day)

days_till_birthday = 0
if birthday_current_year > today:
    days_till_birthday = birthday_current_year - today
else:
    birthday_next_year = datetime(today.year + 1, birthday_date.month, birthday_date.day)
    days_till_birthday = birthday_next_year - today   

print(f"{days_till_birthday.days} days remaining till your birthday")
