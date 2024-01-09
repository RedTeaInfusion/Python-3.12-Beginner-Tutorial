'''
Lesson 20 - Snake
'''
import os
import time
import random
import msvcrt


BOARD_SIZE = [20, 5]
SNAKE = 'O'
TAIL = 'o'
FRUIT = 'F'
DIFFICULTY = 8
playing = True
directions = {'RIGHT': True, 'LEFT': False, 'UP': False, 'DOWN': False}
score = 0

def game_over(head_position, tail_positions):
    if head_position in tail_positions:
        global playing
        playing = False
        
def change_side(head_position):
    if head_position[0] == 0:
        head_position[0] = BOARD_SIZE[0]
    elif head_position[0] == BOARD_SIZE[0] + 1:
        head_position[0] = 1
    if head_position[1] == 0:
        head_position[1] = BOARD_SIZE[1]
    elif head_position[1] == BOARD_SIZE[1] + 1:
        head_position[1] = 1
    return head_position

def button():
    key = msvcrt.kbhit()
    if key:
        return msvcrt.getch().decode()
    else:
        return ''

def move(head_position):
    key = button()

    if key == 'q':
        global playing
        playing = False
    elif key == 'd' and directions['LEFT'] == False:
        head_position[0] += 1
        directions[list(directions.keys())[list(directions.values()).index(True)]] = False
        directions['RIGHT'] = True
    elif key == 'a' and directions['RIGHT'] == False:
        head_position[0] -= 1
        directions[list(directions.keys())[list(directions.values()).index(True)]] = False
        directions['LEFT'] = True
    elif key == 's' and directions['UP'] == False:
        head_position[1] += 1
        directions[list(directions.keys())[list(directions.values()).index(True)]] = False
        directions['DOWN'] = True        
    elif key == 'w' and directions['DOWN'] == False:
        head_position[1] -= 1
        directions[list(directions.keys())[list(directions.values()).index(True)]] = False
        directions['UP'] = True        
    else:
        if directions['RIGHT'] == True:
            head_position[0] += 1
        elif directions['LEFT'] == True:
            head_position[0] -= 1
        elif directions['DOWN'] == True:
            head_position[1] += 1
        elif directions['UP'] == True:
            head_position[1] -= 1

    head_position = change_side(head_position)

    return head_position

def create_fruit(tail_positions):
    fruit_position = [random.randint(1, BOARD_SIZE[0]), random.randint(1, BOARD_SIZE[1])]
    while fruit_position in tail_positions:
        fruit_position = [random.randint(1, BOARD_SIZE[0]), random.randint(1, BOARD_SIZE[1])]

    return fruit_position

def create_board(fruit_position, head_position, tail_positions):
    board = ''
    for i in range(BOARD_SIZE[1] + 2):
        for j in range(BOARD_SIZE[0] + 2):
            if i == 0 or j == 0 or i == BOARD_SIZE[1] + 1 or j == BOARD_SIZE[0] + 1:
                board += '#'
            elif fruit_position == [j, i]:
                board += FRUIT
            elif head_position == [j, i]:
                board += SNAKE
            elif [j, i] in tail_positions:
                board += TAIL
            else:
                board += ' '
        board += '\n'

    return board

def draw(fruit_position, head_position, tail_positions):
    tail_positions.pop(0)
    tail_positions.append(head_position.copy())

    board = create_board(fruit_position, head_position, tail_positions)
    
    os.system('cls')
    print(board)
    print('Score: ' + str(score))

def main():
    head_position = [BOARD_SIZE[0] // 2, BOARD_SIZE[1] // 2]
    tail_positions = [head_position.copy()]
    fruit_position = create_fruit(tail_positions)

    while playing:
        global score

        draw(fruit_position, head_position, tail_positions)

        head_position = move(head_position)

        game_over(head_position, tail_positions)

        if head_position == fruit_position:
            tail_positions.append(head_position.copy())
            fruit_position = create_fruit(tail_positions)
            score += 9      

        time.sleep(1/DIFFICULTY)


main()