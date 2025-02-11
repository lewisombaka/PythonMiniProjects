import random
num = random.randint(1,6)
lower = ["a","b","c","d","e","f"]
upper = ["G","H","I","J","K","L"]
chars = ["!","@","#","$","%","^"]
user_name = input("Enter Name: ")

new_array = []

for i in user_name:
    new_array.append(i)

firstLetter = new_array[0]
secondLetter = new_array[1]
randomLower = lower[num]
randomUpper = upper[num]
randomChars = chars[num]

print(f"{randomUpper}{randomChars}{firstLetter}{secondLetter}{randomUpper}{randomLower}{num}{randomChars}")