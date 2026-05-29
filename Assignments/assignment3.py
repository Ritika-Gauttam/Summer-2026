# 1. Write a program to declare variables of different data types and print them.
age = 10
bmi = 11.9
str = "Hello"
lst = ["a",1,5,2,4,4,68,16,2,"z",93,100]
tup = ("d",4,4,2,3,5,7,5,16,93,112,"x","y")
st =("d",1,2,4,5,3,19,"r")
is_Safe = True

print(age ,"\n","Datatype is :",type(age))
print(bmi ,"\n","Datatype is :",type(bmi))
print(str ,"\n","Datatype is :",type(str))
print(lst ,"\n","Datatype is :",type(lst))
print(tup,"\n","Datatype is :",type(tup))
print(st,"\n","Datatype is :",type(st))
print(is_Safe,"\n","Datatype is :",type(is_Safe))


# 2. Write a program to create a string and perform operations like uppercase,lowercase, and length check.

NAME = "Ritika Gauttam"

print(NAME.upper())
print(NAME.lower())
print(len(NAME))

# 3. Write a program to create a list of numbers and print its elements using indexing.

numbers = [1,3,5,6,3,15,10]
print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])
print(numbers[4])
print(numbers[5])
print(numbers[6])


# 4. Write a program to concatenate two strings and store the result in a variable.
str1 = "Ritika"
str2 = "Gauttam"

comb_str = str1 + str2
print("String 1 :",str1)
print("String 2 :",str2)
print("Concatenated string ----> ",comb_str)

# 5. Write a program to create a list of student names and add a new name into the list

lst = ["ritika","rakhi","aman","rohit"]
lst.append("aaradhna")
lst.insert(1,"bhavya")

