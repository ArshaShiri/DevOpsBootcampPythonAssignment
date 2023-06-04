def calculator(number1, number2, operation):
    if operation == "plus":
        print(f"number1 + number2: {number1 + number2}")
    elif operation == "minus":
        print(f"number1 - number2: {number1 - number2}")
    elif operation == "multiply":
        print(f"number1 * number2: {number1 * number2}")
    elif operation == "divide":
        print(f"number1 / number2: {number1 / number2}")
    

number_of_calculations = 0 
while True:
    number1 = input("Enter the first number: ")

    if number1 == "exit":
        print(f"Number of calculations: {number_of_calculations}")
        break

    number2 = input("Enter the second number: ")
    operation = input("Enter operation (Supports plus, minus, multiply and divide): ")

    valid_numbers = number1.isnumeric() and number2.isnumeric()
    valid_operation = operation == "plus" or operation == "minus" or operation == "multiply" or operation == "divide"

    if not valid_numbers:
        print("Only numbers are allowed") 
    elif not valid_operation:
        print("Operation is not supported")
    else:
        calculator(int(number1), int(number2), operation)
        number_of_calculations += 1
