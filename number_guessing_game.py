### Guessing Game :) ###

## Description: In this program, a user will be propmted to guess a number between 1 and 100 (inclusive).  the user will be trying to guess what number the computer has choosen. Th limit of attempts is 10 tries.
    # If the user inputs a correct guess, the program will say so and also display the amount of guesses the user used.  If the user does not input the correct answer within the given attempts, 
    # the program will state the correct answer.

import random

comp_num = random.randrange(101)

guess = int(input('Enter a number between 1 and 100 (inclusive): '))

i = 1
while i < 10:

    while guess < 1 or guess > 100:
        guess = int(input('Um no. Enter a number between 1 and 100 (inclusive): '))

    if guess < comp_num:
        guess = int(input('Too low. Enter another guess: '))
        i += 1
    
    elif guess > comp_num:
        guess = int(input('Too high. Enter another guess: '))
        i += 1
        
    else:
        print(f'You guessed it correctly! You got it in {i} guess(es)!')
        break

else: print(f'Really sorry, but the correct answer is {comp_num}.')
