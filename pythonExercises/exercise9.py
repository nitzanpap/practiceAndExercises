# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
# (Hint: remember to use the user input lessons from the very first exercise)
#
# Extras:
#
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random

num = random.randrange(1, 100)
success = False
count = 0
print("This a Guessing Game. I choose a number between 1 and 100, and you guess it! ")

while(not success):
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Invalid input.")
        break
    if guess == num:
        print("Job well done!")
        success = True
    elif guess > num:
        print("Your guess is too high!")
    elif guess < num:
        print("Your guess is too low!")
    count += 1

print("Took you " + str(count) + " guesses.")