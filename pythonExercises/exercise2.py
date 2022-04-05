# Ask the user for a number.
# Depending on whether the number is even or odd, print out an appropriate message to the user.
# Hint: how does an even / odd number react differently when divided by 2?
#
# Extras:
# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
# If check divides evenly into num, tell that to the user.If not, print a different appropriate message.

import sys

try:
    num1 = int(input("Hi man! Please enter a number:"))
    num2 = int(input("Please enter another number:"))
except ValueError:
    print("\nWhat kind of input is that? Stop messing with me!")
    sys.exit(1)

try:
    if num1 % num2 == 0:
        print(str(num1) + " divides perfectly by " + str(num2))
    elif num1 % num2 != 0:
        print("Residue is not 0.")
except ZeroDivisionError:
    print("Division by 0!")
    sys.exit(1)
