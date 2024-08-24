# Driver Program Module #

# Description: This is the module of the three modules that runs the program. In this module, I brought all of the pieces together and created a while loop to ensure each player got their turns, 
    # then nested if-else loop for finishing touches.


from TriviaQuestions import TriviaQuestions

mainFunc = TriviaQuestions()

i = 0

player_list = ['Player 1', 'Player 2']

score_list = [0,0]

while i < len(mainFunc):
    turn = i%2

    if turn == 0:
        print(f'Question for {player_list[turn]}: ')
        print(mainFunc[i])
        guess = int(input('Enter your solution (a number between 1 and 4): '))
        if guess == mainFunc[i].correctAns:
            print('That is the correct answer.')
            score_list[0] += 1
        else:
            print(f'That is incorrect. The correct answer is {mainFunc[i].correctAns}.')
        print()

        
    elif turn == 1:
        print(f'Question for {player_list[turn]}: ')
        print(mainFunc[i])
        guess = int(input('Enter your solution (a number between 1 and 4): '))
        if guess == mainFunc[i].correctAns:
            print('That is the correct answer.')
            score_list[1] += 1
        else:
            print(f'That is incorrect. The correct answer is {mainFunc[i].correctAns}.')
        print()
            
    i += 1

print(f'{player_list[0]} earned {score_list[0]} points!')
print(f'{player_list[1]} earned {score_list[1]} points!')

if score_list[0] > score_list[1]:
    print(f'{player_list[0]} wins the game!')
elif score_list[0] < score_list[1]:
    print(f'{player_list[1]} wins the game!')
else:
    print("It's a tie everybody!")


