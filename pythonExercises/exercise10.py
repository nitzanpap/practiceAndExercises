# Take two lists, say for example these two:
#
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write, in one line of Python, a program that returns a list that contains only the elements
# that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.
#
# Extras:
# Randomly generate two lists to test this

import random

x = random.sample(range(10), 10)
y = random.sample(range(10), 10)

common_list = [element for element in y if element in x]

print(x)
print(y)

print("\n" + str(common_list))
