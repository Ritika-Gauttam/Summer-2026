#Q1. Explain Python Data Types in detail.Discuss the following data types with syntax and examples: Integer,Float,String,Boolean,List,Tuple,Set,Dictionary

# Integer ----> used to store whole numerical value (positive or negative) without decimal points
# Syntax ---> variable_name = integer_value
# Example
a = 10 
# Float -----> used to store decimal numbers or fractional numbers
# Syntax -----> variable_name = float_value
# Example 
x = 10.5

# String -----> sequence of characters enclosed within single quotes, double quotes or triple quotes.Supports indexing and slicing.Immutable data type
# Syntax -----> variable_name = "text"
# Example
name = "Ritika"
print(name)
print(name[0])

# Output
# Ritika
# 8

# Boolean ----->Stores only two values True or False values
variable_name = True

# EXAMPLE 
is_passed = True
is_failed = False

print(is_passed)
print(is_failed)

# OUTPUT
True
False

# List -------> ordered, mutable collection of elements, store heterogenous datatype   
# SYNTAX:list_name = [val1 , val2 ,......]
# EXAMPLE :
my_list = [10, 20, "Python", 5.5]

print(my_list)
print(my_list[2])

# OUTPUT
# [10, 20, 'Python', 5.5]
# Python


#Tuple : Ordered but immutable collection of data , allow duplicate values
#SYNTAX : tuple_name = (val1 , val2 ,.....)
#Example:
tup = (10, 20, 30)

print(tup)
print(tup[1])
print(type(tup))

# OUTPUT
# (10, 20, 30)
# 20
# <class tuple>

#Set : Unordered Collection of unique elements,mutable ,does not allow duplicates,No indexing
#SYNTAX : set_name = {item_1,item_2}
#Example:
s = {1,2,3,2}
print(s)
print(type(s))

# OUTPUT
# {1, 2, 3}

#Dictionary : Collection of item in pair of key and value.
#SYNTAX : dict_name = {key_1:val_1,key_2:val_2}
#Example:
student = {
    "name": "Ritika",
    "age": 20,
    "branch": "AIML"
}

print(student)
print(student["name"])

# OUTPUT
# {'name': 'Ritika', 'age': 20, 'course': 'AI/ML'}
# Ritika


#Q2. Write a Python program to demonstrate dynamic typing and type checking using the type() function.
# The program should Declare variables of multiple data types,Print their values, Print their corresponding data types	

integer = 5
print(integer)
print(type(integer))
price = 99.98
print(price)
print(type(price))
name = "RIITKA"
print(name)
print(type(name))
lst = [1,52,5.98]
print(lst)
print(type(lst))
tup = (12,"hi",32)
print(tup)
print(type(tup))
dictionary = {"fruits" : ["apple","mango"],"count":5}
print(dictionary)
print(type(dictionary))
sat = {1,2,2,3,3,1,5}
print(sat)
print(type(sat))

#Q3. Differentiate between	Mutable	and	Immutable Data Types in Python	with suitable examples.
# Also explain: Why strings are immutable, Why	lists are mutable, Real-time use cases of both

# Mutable Data Types – Object Values can be changed after creation. E.g: List,Dictionary,Set etc.
# Immutable Data Types – Object Values cannot be changed after creation. E.g: Integer,float,Tuple,String etc.

# Why strings are immutable : Strings are immutable because once created, their contents cannot be changed.
name = "RITIKA"
# name[0] = "N"         #returns TypeError

# Why lists are mutable: Lists are mutable because it allows changing,adding or removing elements after creation.They are designed for dynamic data storage.
lst = [1,2,"hello"]
lst[1] = 23
print(lst)          #returns 23 at index 1 instead of 2

# Real-time use cases of both 
# Immutable DataType : String: Used for Username,Passwords, Tuple : Used for Database records,etc.
# Mutable DataType : List : Used for Student records,To-do lists, Dictionary : Used for User profile,JSON data etc.


#Q4.Write a Python program to perform various operations on Python collections:


# List operations (append(),remove(),slicing,pop , insert ,count)
lst = [1,2,3,"Hello",5.2,2,3]
lst.append("apple")
print(lst)
lst.remove(2)
print(lst)
print(lst[1:5])
lst.pop()
print(lst)
lst.insert(1,"Apple")
print(lst)
cnt=lst.count(2)
print(cnt)


#Tuple --> index and count: 
tup = (1,3 ,"banana",5.2,1,1)
print(tup[2])
print(tup[::2])
print(tup.count(1))

# Setoperations(union,intersection,difference,add,update):
set1 = {1,2,3}
set2 = {3,4,5}
uni = set1.union(set2)
print(uni)
intersect = set1.intersection(set2)
print(intersect)
diff = set1.difference(set2)
print(diff) 
set1.add(23)
print(set1)
set1.update([4,5,6])
print(set1)

# # Dictionary operations(keys(),values(),item(),popitem,fromkeys)
Student = {"name":"RITIKA","age":19,"height":5}
print(Student.keys())
print(Student.values())
print(Student.items())
Student.popitem()
print(Student)
branch = ["CSE","AIML","IT"]
COURSE = dict.fromkeys(branch,1)
print(COURSE)


#Q5. Develop a mini	Student	Management	System	using Python datatypes.	
# The program	should:	
# ● Store student details using	Dictionary	
# ● Store subject marks	using List	
# ● Calculate total	and	average	marks	
# ● Display	the	output in proper format	

#Sol:
student = {"name": ["DEEPIKA","RITIKA"],
           "Roll_no.":[5,6],
           "Branch": ["AIDS","AIML"]}
marks = [99 , 100 ,98]
total_marks = sum(marks)
average_marks = total_marks / len(marks)

print("Roll Number:", student["Roll_no."])
print("Name:", student["name"])
print("Course:", student["Branch"])

print("Subject Marks :", marks)

print("Total Marks   :", total_marks)
print("Average Marks :", average_marks)