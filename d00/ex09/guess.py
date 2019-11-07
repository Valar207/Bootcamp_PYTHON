import random

rnb = random.randint(1, 99)
print("This is an interactive guessing game!\
\nYou have to enter a number between 1 and 99 to find out the secret number.\
\nType 'exit' to end the game.\nGood luck!")
guess = input("What's your guess between 1 and 99?\n >>")
t = 1
while (guess != "exit"):
    if (guess.isnumeric() is True):
        guess = int(guess)
        if (guess < 1 or guess > 99):
            print("BETWEEN 1 AND 99!!!")
        elif (guess == 42):
            print("The answer to the ultimate question of life,\
 the universe and everything is 42.\nCongratulations! You got it on your first\
 try!")
            exit(0)
        elif (guess > rnb):
            print("Too high!")
        elif (guess < rnb):
            print("Too low!")
        elif (guess == rnb):
            print(f"Congratulations, you've got it!\nYou won in {t} attempts!")
            exit(0)
    elif (guess == "exit"):
        print("Goodbye!")
        exit(0)
    else:
        print("That's not a number.")
    t += 1
    guess = input("What's your guess between 1 and 99?\n >>")

if (guess == "exit"):
    print("Goodbye!")
    exit(0)
