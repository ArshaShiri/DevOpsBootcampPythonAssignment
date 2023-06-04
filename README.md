# DevOps Bootcamp Python Assignment

## EXERCISE 1: Working with Lists
Using the following list:

`my_list = [1, 2, 2, 4, 4, 5, 6, 8, 10, 13, 22, 35, 52, 83]`

* Write a program that prints out all the elements of the list that are higher than or equal 10.
* Instead of printing the elements one by one, make a new list that has all the elements higher than or equal 10 from this list in it and print out this new list.
* Ask the user for a number as input and print a list that contains only those elements from my_list that are higher than the number given by the user.

**Solution:**

`working-with-lists.py`

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

`working-with-dictionaries.py`

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