# DevOps Bootcamp Python Assignment

## EXERCISE 1: Working with Lists
Using the following list:

`my_list = [1, 2, 2, 4, 4, 5, 6, 8, 10, 13, 22, 35, 52, 83]`

* Write a program that prints out all the elements of the list that are higher than or equal 10.
* Instead of printing the elements one by one, make a new list that has all the elements higher than or equal 10 from this list in it and print out this new list.
* Ask the user for a number as input and print a list that contains only those elements from my_list that are higher than the number given by the user.

**Solution:**

`working_with_lists.py`

## EXERCISE 2: Working with Dictionaries
Using the following dictionary:

```
employee = {
  "name": "Tim",
  "age": 30,
  "birthday": "1990-03-10",
  "job": "DevOps Engineer"
}
```

Write a Python Script that:

* Updates the job to Software Engineer
* Removes the age key from the dictionary
* Loops through the dictionary and prints the key:value pairs one by one

Using the following 2 dictionaries:

```
dict_one = {'a': 100, 'b': 400} 
dict_two = {'x': 300, 'y': 200}
```

Write a Python Script that:

* Merges these two Python dictionaries into 1 new dictionary.
* Sums up all the values in the new dictionary and print it out
* Prints the max and minimum values of the dictionary

**Solution:**

`working_with_dictionaries.py`

## EXERCISE 3: Working with List of Dictionaries
Using a list of 2 dictionaries:

```
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
```

Write a Python Program that:

* Prints out - the name, job and city of each employee using a loop. The program must work for any number of employees in the list, not just 2.
* Prints the country of the second employee in the list by accessing it directly without the loop.

**Solution:**

`working_with_list_of_dictionaries.py`

## EXERCISE 4: Working with Functions
* Write a function that accepts a list of dictionaries with employee age (see example list from the Exercise 3) and prints out the name and age of the youngest employee.
* Write a function that accepts a string and calculates the number of upper case letters and lower case letters.
* Write a function that prints the even numbers from a provided list.
* For cleaner code, declare these functions in its own helper Module and use them in the main.py file

**Solution:**

`working_with_functions.py`

## EXERCISE 5: Python Program 'Calculator'
Write a simple calculator program that:

* Takes user input of 2 numbers and operation to execute
* Handles following operations: plus, minus, multiply, divide
* Does proper user validation and give feedback: only numbers allowed
* Keeps the Calculator program running until the user types “exit”
* Keeps track of how many calculations the user has taken, and when the user exits the calculator program, prints out the number of calculations the user did

**Concepts covered:** working with different data types, conditionals, type conversion, user input, user input validation

**Solution:**

`calculator.py`

## EXERCISE 6: Python Program 'Guessing Game'
Write a program that:

* runs until the user guesses a number (hint: while loop)
* generates a random number between 1 and 9 (including 1 and 9)
* asks the user to guess the number
* then prints a message to the user, whether they guessed too low, too high
* if the user guesses the number right, print out YOU WON! and exit the program

Hint: Use the built-in random module to generate random numbers https://docs.python.org/3.3/library/random.html

**Concepts covered:** Built-In Module, User Input, Comparison Operator, While loop

**Solution:**

`guessing_game.py`

## EXERCISE 7: Working with Classes and Objects
Imagine you are working in a university and need to write a program, which handles data of students, professors and lectures. To work with this data you create classes and objects:

**a) Create a Student class**

with properties:

* first name
* last name
* age
* lectures he/she attends
  
with methods:

* can print the full name
* can list the lectures, which the student attends
* can add new lectures to the lectures list (attend a new lecture)
* can remove lectures from the lectures list (leave a lecture)

**b) Create a Professor class**

with properties:

* first name
* last name
* age
* subjects he/she teaches


with methods:

* can print the full name
* can list the subjects they teach
* can add new subjects to the list
* can remove subjects from the list


**c) Create a Lecture class**

with properties:

* name
* max number of students
* duration
* list of professors giving this lecture


with methods:

* printing the name and duration of the lecture
* adding professors to the list of professors giving this lecture


**d) Bonus task**

As both students and professors have a first name, last name and age, you think of a cleaner solution:

**Inheritance** allows us to define a class that inherits all the methods and properties from another class.

* Create a Person class, which is the parent class of Student and Professor classes
* This Person class has the following properties: "first_name", "last_name" and "age"
* and following method: "print_name", which can print the full name
* So you don't need these properties and method in the other two classes. You can easily inherit these.
* Change Student and Professor classes to inherit "first_name", "last_name", "age" properties and "print_name" method from the Person class

**Solution:**

`working_with_classes_and_objects.py`