# VsCode is a code editor , not a platform or tool
# code editor meaning we can write , show and edit the code
# platform and code editor are different 

# WHAT IS DATA SCIENCE  ---- RESEARCH ABOUT DATA
# TO run program  use python./filename.py

# python has no double and no char datatype
print("hello world")
print("123hello")

x=10
y="ritika"
print(x)
print(y)


#if we define variable again it will be treated as different variable i.e dynamic language
x=34
y="radha"
print(type(x))
print(type(y))

#Packing and Unpacking

x=y=z="orange"
print(x)
print(y)
print(z)

a="ABC" #here ABC are literals and a is variable
x="A"
y="B"
z="C"

print(x)
print(y)
print(z)




#VARIABLES---Variables are containers for storing data values.
# a variable name must start with a letter or an underscore character ,cannot start with a number
# A variable name can only contain alpha numeric characters and underscore(A-Z,a-z,0-9,_)
# Variable names are case sensitive(AGE,age and Age are different variables)
# This means uppercase and lowercase letters are treated as different variables 
# A variable name cannot be any of the python keyword

myvar="John"
my_var="John"
_my_var="John"
myVar="John"
MYVAR="John"
myvar2="John"

# print() pretty flexible you can enter multiple value output separated by space

print(34)
print("Sanjana")
# print(Sanjana)
print("divya",23,56.5,True)
print("divya",56,"radhika")

print("Hello kaha se ho aap", end=" ")    # use end when you want to print different print statements in a single line
print("main jaipur se hu")


print("hello", end="-")
print("world")


print("hello"); print("how are you"); print("I am ok")
print(x,y,z)


# DYNAMIC TYPING == C,C++ language you have to tell the datatype before giving values to variables

# int a = 20
x = 56
print(x)
print(type(x))

#Dynamic BINDING == In python there is nbo fix datatype 

a=45
print(a)

a="divya"
print(a)


#****CASTING******** 

a=('5')
print(a)
print(type(a))


a=int('5')  #str --> int 
print(a)
print(type(a))


##Many values to many variable --Python allows you to assign values to multiple variables --Python allows you to assign multiple values in one line 

x,y,z ="apple","orange","banana"
print(x)
print(y)
print(z)


x=y=z="orange"
print(x)
print(y)
print(z)


#Unpack a Collection --if you have a collection of values in a list,tuple etc.
# Python allows you to extract the values into variables.

#******List unpacking******

a=["divya","apple","juice"]
x,y,z = a
print(x)
print(y)
print(z)


#Tuple unpack
x=(3,4,5)
a,b,c = x
print(a,b,c)

# string unpack
name="ABC"
a,b,c = name
print(a,b,c)

x="python"
y="is"
z= "good"
print(x, y ,z)
print(x+y+z)
print(x+z+y)

#Casting--If you want to specify the data type of a variable,this can be done with casting.

x= int(3)
y=float(3)
z= str(3)

print(x)
print(y)
print(z)
print(type(z))


#Type Conversion--You can convert from one datatype to another with the int(),float()

#1. IMPLICIT type conversion--internally know the datatype
print(6+5.8)
print(type(5),type(5.8))

# print("6"+5.8)  #gives error because type incompatible
# print(type("6"),type(5.8))



#2.Explicit type conversion-- program required to change datatype
x=float(20)
print(x)

##USER INPUT--
#Static vs Dynamic software --static don't talk with users they only give information(eg calendar,blog,clock)

#Dynamic --User input deta h(e.g.-->youtube, ola, zomato)

# To take input from user use input()
a = input("What is your name: ")
b = input("What is your age: ")
print(a)
print(b)


a = input("Enter first number: ")
b = input("Enter second number: ")

c = a + b
print(c)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

c = a + b
print(c)


name = input("apna name batao: ")
print("hello", name)

a=int(input("Enter a number: "))
b= int(input("Enter a second number: "))

sum=a*b
print("Total= ", sum)

#Swap two numbers program 

a=20
b=12
a,b = b,a
print("A:",a)
print("B:",b)


#SWAP three numbers program
a=20
b=12
c=30

a,b,c = c,a,b
print("A:", a)
print("B",b)
print("C:",c)

print()