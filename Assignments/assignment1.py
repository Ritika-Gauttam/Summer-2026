# # import sys
# # n=int(sys.argv[1])
# # if n>1:
# # 	for i in range(2,n):
# # 		if n % i==0:
# # 			print("Number is not prime")
# # 			break
# # 	else:
# # 		print("Number is prime")
# # else:
# # 	print("Number is not prime")


# #2. FOR INTEGER DATATYPE
# a=10
# b=10
# print(a==b)
# print(a is b)

# # FOR LIST DATATYPE
# x = [1,2,3]
# y=[1,2,3]
# print(x==y)
# print(x is y)

# #FOR STRING DATATYPE
# s1="HELLO"
# s2="HELLO"
# print(s1==s2)
# print(s1 is s2)

# """3.Write a program that iterates through a list, skips negative numbers, 
# stops execution at zero, and handles non-integer values using exception 
# handling."""
# lst=[1,2,3,4,5,"p",-1,-2,4,5,"a",0,8,7,56,1]

# for x in lst:

#     try:
#         if not isinstance(x,int):
#             raise ValueError
        
#         elif x < 0:
#             continue

#         elif x==0:
#             break

#         print(x, end=" ")
        
#     except ValueError:
#         print("\nNon-integer value found")
    

# """4.Using a single list comprehension, generate a list of squares of numbers 
# from 1 to 20 that are divisible by both 2 and 5."""

# lst= [x*x for x in range(1,21) if x%2==0 and x%5==0]
# print(lst)


# """5. Write a user-defined function that returns the largest and smallest 
# values from a list without using built-in functions."""


# def find_values(num):
#     small=num[0]
#     large =num[0]

#     for x in num:

#         if x < small:
#             small =x

#         if x > large:
#             large=x

#     return small,large

# lst=[1,5,4,56,4,4,3,5,6,643,22,3,45,6,6,878,9,6,7,8,8,0]

# s,l=find_values(lst)

# print("Smallest number is ",s)
# print("Largest number is ",l)



# # 1.
# # import sys

# # if len(sys.argv) < 2:
# #     print("Please enter a number")
# #     n = int(input("Enter number: "))
# # else:
# #     n = int(sys.argv[1])

# # if n > 1:
# #     for i in range(2, n):
# #         if n % i == 0:
# #             print("Number is not prime")
# #             break
# #     else:
# #         print("Number is prime")
# # else:
# #     print("Number is not prime")


# 1.
import sys

if len(sys.argv)<2:
    print("Enter a number: ")
    n=int(input())

else:
    n=int(sys.argv[1])

if n>1:
    for i in range(2,n):
        if n%i==0:
            print("NOT A PRIME NUMBER")
            break

    else:
        print("PRIME NUMBER")

else:
    print("NOT A PRIME NUMBER")

