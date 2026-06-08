"""
    @Created : on Thu Jan 19 06:56:25 2023
    @desc    : Number Guessing Game
    @author  : SWT
"""

# import package
import random

# generate random number
n = random.randrange(1, 10)

# user enter number
guess = int(input("Enter any number: "))

# loop
while n!= guess:
    if guess < n:
        print("Input less than guess number !!!")
        guess = int(input("Enter number again: "))
    elif guess > n:
        print("Input greater than guess number guessed !!!")
        guess = int(input("Enter number again: "))
    else:
      break
  
# if correct, Done
print("You guessed it right !!!")