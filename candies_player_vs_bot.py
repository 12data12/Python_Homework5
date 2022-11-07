from random import *
import os

print('Welcome to the game. Let me explain the rules to you.\n'
      'There are 2021 candies, players take turns tacking candies (no more than 28 candies in one turn.\n)'
      'The one who made the last move gets all the candies and becomes the winner.\n')

def player_vs_bot():
    total_amount = 2021
    max_take = 28
    player_1 = input('\nEnter Player name: ')
    player_2 = 'Bot'
    players = [player_1, player_2]

    print(f'{player_1} and {player_2}, ready to start?')
    lucky = randint(-1, 0)
    print(f'The first move is determind randomly... Congrats, {players[lucky+1]}, have some candy.')

    while total_amount > 0:
        lucky += 1

        if players[lucky % 2] == 'Bot':
            print(f'{players[lucky%2]} takes candies. There are {total_amount} candies avaliable.')

            if total_amount < 29:
                step = total_amount
            else:
                division = total_amount//28
                step = total_amount - ((division * max_take)+1)
                if step == -1:
                    step = max_take -1
                if step == 0:
                    step = max_take
            while step > 28 or step < 1:
                step = randint(1,28)
            print(step)
        else:
            step = int(input(f'{players[lucky%2]}, have some candy! There are {total_amount} candies avaliable.'))
            while step > max_take or step > total_amount:
                step = int(input(f'You can only take {max_take} candies at a time.'))
        total_amount = total_amount - step

    print(f'There are no more candies. {players[lucky%2]} is win!')

player_vs_bot()