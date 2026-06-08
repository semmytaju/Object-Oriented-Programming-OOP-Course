"""
    @Created : on Thu Jan 19 06:56:25 2023
    @desc    : Number Guessing Game
    @author  : SWT
"""

# import package
import random

def input_program():
    # generate random number
    n = random.randrange(1, 10)
    return n

def guess_game(input_pro):
    # user enter number
    guess = int(input("Enter any number: "))
        
    # loop
    while input_pro!= guess:
        if guess < input_pro:
            print("Input less than guess number !!!")
            guess = int(input("Enter number again: "))
        elif guess > input_pro:
            print("Input greater than guess number guessed !!!")
            guess = int(input("Enter number again: "))
        else:
          break
      
    # if correct, Done
    print("You guessed it right !!!")
    
# call functions
ipt = input_program();
guess_game(ipt);
