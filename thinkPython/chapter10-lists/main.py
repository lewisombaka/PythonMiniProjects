# age = [10, 20, 30, 40]

# for i in age:
#     print(i)

# nested list
# empty list

# cheeses = ['Chedda','Edam','Gouda']
# numbers = [42,123]
# empty = []
# numbers[0]=44
# print(cheeses,numbers,empty)
# print('Edam' in cheeses)

# for i in range(len(numbers)):
#     print(numbers[i])

# for x in []:
#     print('This never happens')

# print(len(['spam', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]
# )) #4

# List Operations
# a = [1,2,3] # the + operator
# b = [4,5,6]
# c = a+b
# d = [0]*4 # the * operator
# e = [1,2,3]*4 # the * operator
# print(e)

# List slices
# List are mutable
# t = ['a','b','c','d','e','f']
# print(t[1:3])
# print(t[3:])
# print(t[:4])
# print(t[:])
# t[1:3] = ['x','y']
# print(t[1:3])

# List Methods
# t = ['a','b','c']
# t.append('d') # append
# print(t)
# t1 = ['a','b','c']
# t2 = ['d','e']
# t1.extend(t2) #extend
# print(t1)
# print(t2)
# t3 = ['d','c','e','b','a']
# t3.sort() # sort arranges elements from low to high
# print(t3)

# Map, filter and reduce

# t = [1,2,3]
# def add_all(arra):
#     total = 0
#     for x in arra:
#         total = total + x
#     return total

# print(add_all(t))


def add (tas):
    tot_sum = 0
    for i in tas:
        tot_sum += i
    return tot_sum
mada = add([1,2,3])

print(mada)

