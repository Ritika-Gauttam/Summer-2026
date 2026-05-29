#String rules:

#1. Sequence of characters written inside quotes(single,double or triple)(To write multiple statements use triple quotes).
#2. Includes letters,numbers and spaces.
#3. Strings are immutable/unchanged 
#4. But we can manipulate strings -- use methods like concatenation,slicing,formatting to create new string based on original
#5. Delete an entire string variable(python not possible to delete individual characters from a string)

# string functions return  new string so we should store them in new variable , it keeps original string unchanged

a='hello world'
print(a)

b="python is good"
print(b)

c='''Hey how are you
sb bdhiya
main thik hu'''

print(c)


name="sapna"
print("My name is",name)
print("Type of my variable:",type(name))  #type() used to check datatype

print("Length of my string:",len(name))

upper_case=name.upper()    #upper() function converts in uppercase or capital letters
print("Upper case:",upper_case)

lower_case = upper_case.lower()    #lower() function converts in lowercase or small letters
print("Lower case:",lower_case)

lw=upper_case.casefold()
print(lw)

name="dev"
print(name.title())

print(name.capitalize())


company_name="upflairs   "
print(len(company_name)) #count spaces also
print(company_name.count)

print(company_name.strip())  #strip remove spaces at the end

intro = "hi kese ho"
print(intro.strip())

#indexing and slicing

company_name="upflairs"
print(company_name[0])
print(company_name[7])
print(company_name[-1])

print(name[0:4])

# task 4 reverse the string company_name

name = "ritika"
lst_name ="gauttam"
lt_name = " gauttam"
print(name+lst_name)   # to join 
print(name,lst_name)
print(name+" "+lst_name)


name="Dev"
# print(name*name)  throws error
print(name+name)
# print(name+2) throws error
print(name*2)


# intro="hello my name is  \n ritika"
# intro.split("\n", " ")   # split at \n and replace it by 1

name="aman"
address = "jaipur"
print(f"My name is {name} and i am from {address}")  # f can be used when we want variable value in between string
# or r can be used : r means row string used for path --> when we want to access value from a path
# path="C:\Users\user\OneDrive\Desktop"
# print(r"[path]")


# input function
name=input("enter your name: ")
print(name)
print(type(name))


num1=int(input("Enter your first number: "))
num2=int(input("Enter your second number: "))
print(num1+num2)
print(type(num1))
print(type(num2))


# intro="hello my name is  \n ritika"
# val,tab=intro.split("\n", " ") 
# print(val)
# print(tab)
# # split at \n and replace it by 1

# Different ways to reverse a string

text = " Python"

# METHOD 1
result = text[::-1]
print(result)

# METHOD 2   USING reversed() with join ----->reversed returns a backward iterator over the string characters
reversed_text = "".join(reversed(text))
print(reversed_text)
pa_ss =reversed(text)
print(pa_ss)

# METHOD 3--> using manualiteration by for loop

reversed_text = ""
for char in text:
    reversed_text =  char + reversed_text 

print(reversed_text)




