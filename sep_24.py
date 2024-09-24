dict1 = {
    1:'one',
    2:'two'
}

# print(dict1[3])
# print(dict1.get(3,'three'))

# print(dict1.keys())
# print(dict1.values())

# for i in dict1:
#     print(dict1[i])

# for k,v in dict1.items():
#     print(k,v)


dict1 = {
    1:'two',
    2:'two'
}

# dict1[3]='three'
# dict1[3]='four'
# print(dict1)

# dict1.update({3:'three',4:'four',4:'five'})
# print(dict1)


# x=dict1.pop(2)
# print(x)
# print(dict1)

# dict1.

# dict1.clear()
# print(dict1)

del dict1[1]
print(dict1)



# aasdfghjkllkjhgfdsa

# {'a':2,'s':5}

# s = 'aasdfghjkllkjhgfdsa'
# o={}

# for i in s:
#     o[i]=o.get(i,0)+1

# print(o)

# Write a Python program to drop empty items from a given dictionary.
# Original Dictionary:
# {'c1': 'Red', 'c2': 'Green', 'c3': None,'c4':''}
# New Dictionary after dropping empty items:
# {'c1': 'Red', 'c2': 'Green'}


# a = {'c1': 'Red', 'c2': 'Green', 'c3': None,'c4':''}
# b={}
# for k,v in a.items():
#     if v not in [None,'']:
#         b[k]=v
#         # a.pop(k)

# print(b)

#  Write a Python program to convert string values of 
# a given dictionary into integer/float datatypes.
# Original list:
# [{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
# String values of a given dictionary, into integer types:
# [{'x': 10, 'y': 20, 'z': 30}, {'p': 40, 'q': 50, 'r': 60}]
# Original list:
# [{'x': '10.12', 'y': '20.23', 'z': '30'}, {'p': '40.00', 'q': '50.19', 'r': '60.99'}]
# String values of a given dictionary, into float types:
# [{'x': 10.12, 'y': 20.23, 'z': 30.0}, {'p': 40.0, 'q': 50.19, 'r': 60.99}]

# a =[{'x': '10.12', 'y': '20.23', 'z': '30'}, {'p': '40.00', 'q': '50.19', 'r': '60.99'}]

# for i in a:
#     for k,v in i.items():
#         if '.' in v:

        # isinstance(v,str)