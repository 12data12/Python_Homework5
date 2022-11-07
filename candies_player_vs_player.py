from random import *
import os

print('Welcome to the game. Let me explain the rules to you.\n'
      'There are 2021 candies, players take turns tacking candies (no more than 28 candies in one turn.\n)'
      'The one who made the last move gets all the candies and becomes the winner.\n')

def player_vs_player():
    total_amount = 2021
    max_take = 28
    count = 0
    player_1 = input('\nEnter Player1 name: ')
    player_2 = input('\nEnter Player2 name: ')

    x = randint(1,2)
    if x == 1:
        lucky = player_1
        loser = player_2
    else:
        lucky = player_2
        loser = player_1
        print(f'The first move is determind randomly... Congrats, {lucky}, have some candy.')

    while total_amount > 0:
        if count == 0:
            step = int(input(f'Have some candy, {lucky} '))
            if step > total_amount or step > max_take:
                step = int(input(f'You can only take {max_take} candies at a time. Try again.'))
                total_amount = total_amount - step
        if total_amount > 0:
            print(f'There are {total_amount} candies avaliable.')
            count = 1
        else:
            print(f'No more candies.')
        if count == 1:
            step = int(input(f'Have some candy, {loser} '))
            if step > total_amount or step > max_take:
                step = int(input(f'You can only take {max_take} candies at a time. Try again, {loser}! '))
            total_amount = total_amount - step
        if total_amount > 0:
            print(f'There are {total_amount} candies avaliable.')
            count = 0
        else:
            print(f'No more sweets.')

    if count == 1:
        print(f'{loser} win!')
    if count == 0:
        print(f'{lucky} win!')

player_vs_player()