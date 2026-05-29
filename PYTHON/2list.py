lst= [ 1,2,3,4,5,5,6,6,"hello",3.2]   #heterogeneous, allow duplicate , changable , mutable(changable) 
# array is faster than list ,size of array is fixed while list is flexible
print("This is my first list:",lst)
print("Length of my list ",len(lst))
print("Type of my list ",type(lst))

# print = 10
# print(print) ---->give error int is not callable because it don't know what is print() as we have redefine print
#list = 10
# print("aaaaaaa",list)-----> give ouput aaaaaaa 10 i.e we can keep keyword as variable name it will not give error
# but it is not a good practice

lst=[1,2,3,5,2,5,"hello",3.2]
print(lst[0])
print(lst[3])
print(lst[4])
print(lst[2])
print(lst[5])
print(lst[7])

print(lst[-1])
print(lst[-2])

print(lst[0:5])
print(lst[2:5])
print(lst[2:7])


# Mutable
fruits = ["apple","banana","mango"]


# Add item
# .append(item) add elements at end of list
fruits.append("orange")   # these function does not return anything,they make change in original

print("Fruits list : ",fruits)

# insert(index , item ) inserts value at a particular position in list
fruits.insert(0, "grapes")
print("Fruits list : ",fruits)

# remove(item) remove the item from list
fruits.remove("apple")
print("Fruits list : ",fruits)

# fruits.remove("watermelon")
# print("Fruits list : ",fruits) ----->gives error ValueError: list.remove(x): x not in list
 

# pop() removes last element
# pop(index) removes particular index item

fruits.pop(1)
print("Fruits list : ",fruits)

# fruits.clear()  -----> clears the list
# fruits.copy() -----> creates copy of list
print(fruits.count("grapes"))
print(fruits.index("grapes"))

fruits[0]="kiwi"
print("Fruits list : ",fruits)

fruits.reverse()
print("Fruits list : ",fruits)


# LOOPING IN LIST
lst1 = [1,82,32]
lst2 = [2,3,5]
print(lst1 + lst2)
# print(lst1 * lst2) ----> gives error
print(lst1 * 2)   #OUTPUT = [1, 2, 32, 1, 2, 32]
print(">>>>>>>>>>", 2 in lst2) #gives boolean output
 

# TASK 1 len() , max() , min() , sum() , sort() , sorted()
sorted ()
# sorted(list) (Returns a New Sorted Copy) 
print(len(lst1))
print(max(lst1))
print(min(lst1))
print(sum(lst1))
lst1.sort()
print(lst1)