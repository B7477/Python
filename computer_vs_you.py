## Python Game: Rock Paper Scissors Lizard Spock ##

# In this python programmed game, a player and the computer will be playing a variation of the game called Rock Paper Scissors Lizard Spock. 
  # This is programmed using multiple conditional expressions.

import random

yourScore = 0
compScore = 0
playAgain = 1

while playAgain:

    print("\nLet's play Rock, Paper, Scissors, Lizard, Spock!")
    print()

    player = input('Please choose one of the following: Rock, Paper, Scissors, Lizard, Spock: ').lower()
    print()

    game_list = ['rock', 'paper', 'scissors', 'lizard', 'spock']
    computer = random.choice(game_list)
    print(f'The computer chose {computer}.')
    print()

    if player == 'rock':
        if computer == 'lizard':
            print('Rock crushes Lizard! You Win!')
            yourScore+=1
        elif computer == 'scissors':
            print('Rock crushes Scissors! You Win!')
            yourScore+=1
        elif computer == 'paper':
            print('Paper covers Rock! Computer Wins!')
            compScore+=1
        elif computer == 'spock':
            print('Spock vaporizes Rock! Computer Wins!')
            compScore+=1
        else:
            print("It's a tie!")
            
    elif player == 'paper':
        if computer == 'scissors':
            print('Scissors cuts Paper! Computer Wins!')
        elif computer == 'rock':
            print('Paper covers Rock! You Win!')
        elif computer == 'lizard':
            print('Lizard eats Paper! Computer Wins!')
        elif computer == 'spock':
            print('Paper disproves Spock! You Win!')
        else:
            print("It's a tie!")

    elif player == 'scissors':
        if computer == 'paper':
            print('Scissors cuts Paper! You Win!')
        elif computer == 'rock':
            print('Rock crushes Scissors! Computer Wins!')
        elif computer == 'lizard':
            print('Scissors decapitates Lizard! You Win!')
        elif computer == 'spock':
            print('Spock smashes Scissors! Computer Wins!')
        else:
            print("It's a tie!")

    elif player == 'lizard':
        if computer == 'paper':
            print('Lizard eats Paper! You Win!')
        elif computer == 'rock':
            print('Rock crushes Lizard! Computer Wins!')
        elif computer == 'scissors':
            print('Scissors decapitates Lizard! Computer Wins!')
        elif computer == 'spock':
            print('Lizard poisons Spock! You Win!')
        else:
            print("It's a tie!")

    elif player == 'spock':
        if computer == 'paper':
            print('Paper disproves Spock! Computer Wins!')
        elif computer == 'rock':
            print('Spock vaporizes Rock! You Win!')
        elif computer == 'scissors':
            print('Spock smashes Scissors! You Win!')
        elif computer == 'lizard':
            print('Lizard poisons Spock! Computer Wins!')
        else:
            print("It's a tie!")

    else:
        print('Invalid Input.')

    ques = input('\nDo you want to play again? (yes or no): ')
    if ques == 'yes': continue
    else: playAgain = 0

    print()

print(f'The computers final score is {compScore} and your final score is {yourScore}.')

if compScore > yourScore:
    print('\nIn the end, the computer wins :(')
elif yourScore > compScore:
    print('\nYou defeated the machine, nice!')
else:
    print('\nThe final tally was a tie!')


print('\nThanks for playing!')
