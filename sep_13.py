# # data type 

# # integer - non iterable , 
# # float - non iterable , 
# # string - immutable , iterable ,ordered 
# # complex - non ietreable 
# # list - mutable  , iterable ,ordered 
# # tuple  - immutable , iterable ,ordered 
# # dictionary - key - immuatble (unchangeable) ,value mutable
# # set - unique elements, unachangeable , unindex ,unordered 
# # frozen set- unique elements, immuatble , unindex ,unordered 


# # list - append, extend (iterable data), insert(particular index data adding)


# # list1 = [1,2,3,4]
# # list2 = [5,6,7]

# # print(list1+list2)
# # list1.extend(list2)
# # print(list1)

# # set1 = {1:4,23}
# # dict = {}
# # set1 = {}
# # set1 = set()
# # # liust1=[]
# # # print(type(set1))

# # set1.add(1)
# # set2={2,3,4,'apple',5,6,'chiku',('chiku',2,3)}
# # set2.update(set1)
# # print(set2)

# set1 ={1,2,3,4}
# set2={4,5,6}
# # print(set1.union(set2))
# # print(set1.intersection(set2))
# # print(set1.intersection_update(set2))
# # print(set2.difference(set1))
# # set1.difference_update(set2)
# print(set1.symmetric_difference(set2))
# set1.symmetric_difference_update(set2)
# print(set1)
# # print(set2)
# # tuple =()
# # list =[]
# # str ='', ""
# # add()

# set1 = {1,2,3,4,5}
# # set1.pop()
# # set1.remove(4)
# # del set1 
# print(set1)

# Write a Python program to remove all duplicates from a given 
# list of strings and return a list of unique strings. Use the Python set data type.






# Write a Python program to find the third
# largest number from a given list of numbers.Use the Python set data type.

# li = [3,2,5,6,1,2,3]
# set1 = set(li)
# print(set1)
# li2= list(li)

# li2.sort(reverse=True)
# print(li2[2])

# for i in set1:
#     print(i)
# print(sorted(set1,reverse=True)[2])

# Write a Python program to find all the unique combinations 
# of 3 numbers from a given list of numbers, adding up to a target number.

traget = 12

list1 = [1,2,3,4,5,6,7,8,9] 

# out = [(1,3,8),(1,2,9)]

set1 = set()

for i in list1:
    for j in list1:
        k = traget - i - j
        if k in list1:
            set1.add(tuple(sorted((i,j,k))))

print(set1)


tuple1 = (1,2,3,4,4,4,4)

li = list(tuple1)

li.append(5)
print(tuple(li))


# sorted(tuple)

min(tuple1)

print(tuple1.count(4))

print(tuple1.index(4))
print(tuple1[3])