# mutable, fastest , unordered , unique collections of items
# We can't do indexing and slicing in set


# Task 2 -----> set operations
sat = {1,2,3,5}
print("This is my first set:- ",sat)
print("Type of my set:- ",type(sat))
print("Length of my set:- ",len(sat))

# Difference between discard and remove is 
# remove ----> remove the item if it is present otherwise give error
# discard ----->remove item if it is present otherwise keep set as it is

sat.discard(1) 
print(sat)

sat.discard("1")
print(sat)

sat.remove(5)
print(sat)

# sat.remove("hello")   ----->KeyError: 'hello'
# print(sat)
