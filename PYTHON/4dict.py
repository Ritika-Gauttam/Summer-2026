# ALLOW duplicate value but not duplicate key 
# Mutable , changeable 
# Denoted by dict

# Task 1 update function , fromkeys , difference between copy and deep copy
student = {"name" : "Ritika",
           "class" : "Third year", "Roll_number" : 18 , "branch" : "CSE" ,"Address" : "Jaipur" 
} 

# Here name , class , Roll_number , branch , Address >>>>> keys
# Ritika ,  Third year , 21, AIML , Jaipur >>>>>>> values

print("My Dictionary is : ", student)
print("Keys in dictionary :",student.keys())    #To see keys in dictionary use .keys()
print("Values in dictionary :",student.values())    #To see values in dictionary use .values()
print("ITEMS in dictionary :",student.items())  #To see keys value pair in dictionary use .items()


# To see value at a particular key -----> either give key value directly or use .get(key)
print(student['name'])
print(student['class'])
# print(student['Branch']) -----> KeyError: 'Branch'
print(student['branch'])\

print(student.get('name'))  # give value at a particular key


# To add new key
student['subject'] = 'python'
print(student)


# student.clear() 
# print(student)------> {}

College = student.copy()
print("NEW COLLEGE DICTIONARY IS :" , College)


# To remove element give pop(key)
College.pop("name")
print(College)


# TO pop last item popitem() is used
College.popitem()
print(College)



car = {
    "brand" : "ford",
    "model" : "Mustang",
    "year" : 1964, 
}

x = car.setdefault("color" , "white")
print(x)
print(car)


# To give multiple values to a key
CAR = {
    "brand" : ["ford","Honda" , "hero" ],
    "model" : "Mustang",
    "year" : 1964, 
}

print(CAR)

# TO UPDATE ANY KEY VALUE WITHOUT ANY PREDEFINED FUNCTION

CAR['year'] = 2000
print(CAR)

# TO UPDATE ANY KEY VALUE USE UPDATE() FUNCTION

# There are only 2 types of loop in python -----> for and while


for x in car:    #BY DEFAULT IT TAKES KEYS
    print(x)   

for x in car.keys():
    print(x)
for x in car.values():
    print(x)
for x in car.items():
    print(x)