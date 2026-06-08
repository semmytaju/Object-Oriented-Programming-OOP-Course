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
    return n;

def guess_game(parm_input):
    # user enter number
    guess = int(input("Enter any number: "))

    # loop
    while parm_input!= guess:
        if guess < parm_input:
            print("Input less than guess number !!!")
            guess = int(input("Enter number again: "))
        elif guess > parm_input:
            print("Input greater than guess number guessed !!!")
            guess = int(input("Enter number again: "))
        else:
          break
      
    # if correct, Done
    print("You guessed it right !!!")
    
# call functions
inp_prog = input_program();
guess_game(inp_prog);