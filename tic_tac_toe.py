board = list(range(1,10))

def draw_board(board):
    print ('-' * 13)
    for i in range(3):
        print ('|', board[0+i*3], '|', board[1+i*3], '|', board[2+i*3], '|')
        print ('-' * 13)

def player_turn(turn):
    valid = False
    while not valid:
        answer = input(f'Select a cell for {turn}: ')
        try:
            answer = int(answer)
        except:
            print (f'It does not look like a number.')
            continue
        if answer >= 1 and answer <= 9:
            if (str(board[answer-1]) not in "XO"):
                board[answer-1] = turn
                valid = True
            else:
                print (f'Ooops, occupied.')
        else:
            print (f'The cell number cannot be less than 1 and more than 9.')

def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            player_turn("X")
        else:
            player_turn("O")
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print (f'Congrats! {tmp}, you win!')
                win = True
                break
        if counter == 9:
            print (f'It is a draw.')
            break
    draw_board(board)
main(board)