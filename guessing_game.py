# Guessing Game - Automate The Boring Stuff with Python Programming Course

import random

print("Hi there, what\'s your name?")
name = input("Your name: ")

print ("Hi " + name + ", I\'m thinking of a number between 1 - 10, what is it? (You have six guesses)")

x = random.randint(1,10) # Set random number to guess
limit = 6 # Set guess limit to six

# Detect if higher or lower
for limit in range(1,7):
    guess = int(input())
    if guess < x:
        print("That's lower.")
    elif guess > x:
        print("That's higher.")
    else: break # Stop once correct guess

if guess == x: # Display win/loss message
    print("Correct! You got it! Nice work " + name + ", the number is " + str(x))
else:
    print("Better luck next time, " + name + ", the random number is " + str(x))