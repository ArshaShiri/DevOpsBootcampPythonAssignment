employee = {
  "name": "Tim",
  "age": 30,
  "birthday": "1990-03-10",
  "job": "DevOps Engineer"
}

# Updates the job to Software Engineer
employee["job"] = "Software Engineer"
print(employee)

# Removes the age key from the dictionary
employee.pop("age")
print(employee)

# Loops through the dictionary and prints the key:value pairs one by one
for key, value in employee.items():
  print(f"{key}:{value}")

dict_one = {'a': 100, 'b': 400} 
dict_two = {'x': 300, 'y': 200}

# Merges these two Python dictionaries into 1 new dictionary.
dict_merged = dict_one.copy()
dict_merged.update(dict_two)
print(dict_merged)

# Sums up all the values in the new dictionary and print it out
sum = 0
for value in dict_merged.values():
    sum = sum + value
print(sum)

max_value = dict_merged['a']
min_value = dict_merged['a']
for key, value in dict_merged.items():
   if value < min_value:
      min_value = value
   if value > max_value:
      max_value = value

print(f"Max value: {max_value}")
print(f"Min value: {min_value}")
