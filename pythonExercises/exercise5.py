# Take two lists, say for example these two:
#
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists
# (without duplicates). Make sure your program works on two lists of different sizes.
#
# Extras:
#
# Randomly generate two lists to test this
# Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)



import random

# Define variables
x = []
y = []
new_list = []
x_len = random.randrange(2, 11)
y_len = random.randrange(2, 11)

# Create random lists
for i in range(x_len):
    x.append(random.randrange(0, 101))
for i in range(y_len):
    y.append(random.randrange(0, 101))

print("First random list: " + str(x))
print("Second random list: " + str(y))

# Create a list of shared numbers
for element in x:
    if element in y:
        if element not in new_list:
            new_list.append(element)
print("\nList of numbers shared in BOTH lists: " + str(new_list))