def print_numbers_higher_or_equal_to(list, value):
    for current_value in list:
        if current_value >= value:
            print(current_value)

def print_list_with_numbers_higher_or_equal_to(list, value):
    new_list = []
    for current_value in list:
        if current_value >= value:
            new_list.append(current_value)
    print(new_list)

my_list = [1, 2, 2, 4, 4, 5, 6, 8, 10, 13, 22, 35, 52, 83]


def print_numbers_higher_or_equal_to_from_input(list):
    value = input("Enter a number: ")
    new_list = []
    for current_value in list:
        if current_value >= int(value):
            new_list.append(current_value)
    print(new_list)

my_list = [1, 2, 2, 4, 4, 5, 6, 8, 10, 13, 22, 35, 52, 83]
value = 10
print_numbers_higher_or_equal_to(my_list, value)
print_list_with_numbers_higher_or_equal_to(my_list, value)
print_numbers_higher_or_equal_to_from_input(my_list)