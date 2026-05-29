# 1. Write a Python program to print your name, course, and city using proper formatting.

name = "RITIKA GAUTTTAM"
course = "Data Science with ML and AI"
city = "Ajmer"
print(f"My name is {name}. My course is {course}. My city is {city}.")


# 2. Take user input for name and age, then print:
# "Hello <name>, you are <age> years old"

name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello {name}, you are {age} years old")

# 3. Write a program to:
# ● Take a string input 
# ● Print its reverse 
# ● Count total number of character

string=input("Enter a string: ")
print(string[::-1])
print("Total number of characters in string are :",len(string))