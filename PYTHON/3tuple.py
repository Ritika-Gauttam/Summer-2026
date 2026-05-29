tpl = (1,2,3,45,"hello", 3.2 , 1, 2 )  #heterogeneous,immutable ,unchangable,ordered,allow duplicates , 

print("This is my first tuple : ",tpl)
print("Length of my tuple: ",len(tpl))

print(tpl[0])
print(tpl[1])
print(tpl[2])
print(tpl[0 : 2])
print(tpl[0 : 5 : 2])


a = 1,23,5,4,5   #By default these are stored in tuple
print(a)  
print(type(a))
print(len(a))


# TUPLE UNPACKING

a , b, c = (1,2,3)
print(a)
print(b)
print(c)


# a , b =(1,2,3)
# print(a)
# print(b) 
# ------> ValueError: too many values to unpack (expected 2)

tpl = (1,2,3,"hello",5.5,5,1,2,3,3,4,5)
print(tpl)

# TUPLE ONLY HAVE THESE TWO OPERATIONS
print(tpl.count(2))   #give count of a particular element means how many times it in present in tuple
print(tpl.index(2))   #index give first index value of encountered value


# To add , remove or to perform other operations we need to typecast tuple into list 
# Then perform operation and then typecast into list again

tpl = (1,2,3,"hi" , 5 ,4)

print("ye mera tpl:",tpl )
print("Type of my tuple:",type(tpl))
print("tpl convert into list")
lst = list(tpl)
print(">>>>>>>>>",lst)
print("Type of lst:",type(lst))
lst.append(100)
print(lst)
tpl = tuple(lst)
print(tpl)
