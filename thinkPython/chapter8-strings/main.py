# fruit = 'Lewis'
# letter = fruit[1:5]
# print(letter)
# length = len(fruit)
# print(fruit[length])

# Transversal with a for loop

# index = 0
# while index < len(fruit):
#     letter = fruit[index]
#     print(letter)
#     index+=1

# write a function that takes a string as an arguement and displays the letters backward, one per line, use a transversal loop

# def stringer(fruit_name):
#     length = len(fruit_name)
#     accurate_length = length - 1
#     banana_three = fruit_name[-3:]
#     print(fruit_name[::2])


# stringer('Banana')
# three = fruit[-3:]
# print(three)
# reverse = three[::-1]
# print(reverse)

# for letter in fruit:
#     print(letter)

# prefixes = 'JKLMNOPQ'
# suffix = 'ack'
# special_suffix = 'uack'

# for letter in prefixes:
#     if letter == 'O' or letter == 'Q':
#         print(f'{letter}{special_suffix}')
#     else:
#         print(f'{letter}{suffix}')


# thre = fruit[-3:]
# print(fruit[:3])
# print(thre[::-1])

# strings are immutable
# greetting = 'Hello, world!'
# greeting[0] = 'J' #This will cast an error
# You can rather create a new string
# new_greeting = 'J' + greetting[1:]
# print(new_greeting)

# Searching

def find(word,letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index+=1
    return -1


print(find('Lewis','s'))