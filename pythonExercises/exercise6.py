# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

num = input("Please enter a natural number: ")
rev_num = num[::-1]

if num == rev_num:
    print("Congrats! " + num + " is a palindrome.")
else:
    print("Sorry. " + num + " is NOT a palindrome.")