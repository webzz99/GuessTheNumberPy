# Import Random Library
import random

# Guessing Range and Max number of attemps 
lower_bound = 1
upper_bound = 1000
max_attempts = 10

# Generate random number within Lower and upp range 
secret_num = random.randint(lower_bound, upper_bound)

# Players guess 
def player_guess():
    while True:
        try:
            guess = int(input(f"Guess a number between {lower_bound} and {upper_bound}: "))
            if lower_bound <= guess <= upper_bound:
                return guess
            else:
                print("Oh No!! This number is out of range !!. Please enter a number within the range.")
        except ValueError:
            print("Oh !! That's Not a Number !! . Please enter a number in range.")