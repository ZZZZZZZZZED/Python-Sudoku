import module
import pygame
import itertools

window_pos_grid = []
board_pos_grid = []

def init_highlight_pos():
    # Make highlight pos when the game starts

    # Presetting the highlight pos.
    # These value will be fixed by px when rendering a highlight box.
    for i in range(9):
        for j in range(9):
            x = i * 42.5
            y = j * 42.5
            pos = (x, y)

            # If not fix slot, add its window pos and board pos into list for matching use.
            if module.check_available(pos):
                window_pos_grid.append(pos)
                board_pos_grid.append((i,j))

def find_gridpos_by_click(pos:tuple):

    # If match, return the preseted window pos for rendering.
    if module.mousepos_to_boardpos(pos) in board_pos_grid:
        i = board_pos_grid.index(module.mousepos_to_boardpos(pos))
        return window_pos_grid[i]
    else:
        return 'fail find, or fixed slot.'

def check_valid(boardpos, num):
    # check related 3 x 3, 1 x 9, 9 x 1 after each edit.
    # if valid return BLUE color, if not return RED color.
    # Returned value should be use in text_surface color parameter.

    x = boardpos[0]
    y = boardpos[1]
    x_list = []
    y_list = []
    block1 = [0,1,2]
    block2 = [3,4,5]
    block3 = [6,7,8]
    large_grid = [block1, block2, block3]
    block_locate = [9,9]
    
    for i, lst in enumerate(large_grid):
        if x in lst:
            block_locate[0] = i
            x_list = large_grid[i]
        if y in lst:
            block_locate[1] = i
            y_list = large_grid[i]

    permutations = list(itertools.product(x_list, y_list))
    permutations.remove((x, y))

    # 3 * 3
    for i, pos in enumerate(permutations):
        name = 'given_' + str(pos[0]) + '_' + str(pos[1])
        for g in module.given_list:
            if g.name == name and g.num > 0:
                if g.num == num:
                    print("block fail")
                    return False

    # 1 * 9 and 9 * 1
    x_list = []
    y_list = []
    for i in range(9):
        x_list.append((x, i))
        y_list.append((i, y))
    
    for x, y in zip(x_list, y_list):
        name = 'given_' + str(x[0]) + '_' + str(x[1])
        for g in module.given_list:
            if g.name == name and g.num > 0:
                if g.num == num:
                    print("x fail")
                    return False
        name = 'given_' + str(y[0]) + '_' + str(y[1])
        for g in module.given_list:
            if g.name == name and g.num > 0:
                if g.num == num:
                    print("y fail")
                    return False
    # for i, pos in enumerate(y_list):

    return True
    

    
    # print(x_list,y_list)
