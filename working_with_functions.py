def print_youngest_employee_info(employees):
    youngest_employee_age = employees[0]["age"]
    youngest_employee_name = employees[0]["name"]
    for employee in employees:
        if employee["age"] < youngest_employee_age:
            youngest_employee_age = employee["age"]
            youngest_employee_name = employee["name"]

    print(f"Name of the youngest employee: {youngest_employee_name}")
    print(f"Age of the youngest employee: {youngest_employee_age}")

def count_upper_and_lower_letters(string):
    lower_letters = 0
    upper_letters = 0
    for char in list(string):
        if char.islower():
            lower_letters += 1
        elif char.isupper():
            upper_letters += 1
    print(f"Number of lower case letters: ", lower_letters)
    print(f"Number of upper case letters: ", upper_letters)

def print_even_numbers(list):
    for number in list:
        if number % 2 == 0:
            print(number)

employees = [{
  "name": "Tina",
  "age": 30,
  "birthday": "1990-03-10",
  "job": "DevOps Engineer",
  "address": {
    "city": "New York",
    "country": "USA"
  }
},
{
  "name": "Tim",
  "age": 35,
  "birthday": "1985-02-21",
  "job": "Developer",
  "address": {
    "city": "Sydney",
    "country": "Australia"
  }
}]

print_youngest_employee_info(employees)
count_upper_and_lower_letters("fajgKAGmbLDHVIalbmnal")
print_even_numbers([0, 3, 9, 10, 2, 13, 120])
