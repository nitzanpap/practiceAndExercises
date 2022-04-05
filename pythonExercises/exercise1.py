# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
#
# Extras:
# Add on to the previous program by asking the user for another number and printing out that many copies of the previous message.
# (Hint: order of operations exists in Python)
# Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

name = input("Hello there user! Please enter your name: ")
age = int(input("Now please enter your current age: "))
num_of_copies = int(input("How many copies of the answer would you like?"))
current_year = 2019
year_when_100_years_old = current_year + (100 - age)

while num_of_copies > 0:
    print("Hi " + name + "! When you'll be a 100 years old, it will be " + str(year_when_100_years_old) + "! Wow..\n")
    num_of_copies -= 1
