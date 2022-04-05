# Make a two-player Rock-Paper-Scissors game.
# (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner,
# and ask if the players want to start a new game)

repeat = True
while repeat:
    print("This is Rock, Paper, Scissors game.\n")
    player1 = input("Player 1, please enter r/p/s: ")
    player2 = input("Player 2, please enter r/p/s: ")
    if (player1 or player2) != ('r' or 'p' or 's'):
        print("Invalid input.")
        break

    if player1 == player2: print("It's a TIE!")
    elif player1 == 'r' and player2 == 's' or player1 == 'p' and player2 == 'r' or player1 == 's' and player2 == 'p':
        print("Player 1 won!")
    else: print("Player 2 won!")

    repeat = input("Would you like to start again (y/n)?")
    if repeat == 'n':
        exit()
    elif repeat != 'y':
        print("Invalid input.")
        exit()