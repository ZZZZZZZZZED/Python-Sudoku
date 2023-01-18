import module
import pygame
import itertools

window_pos_grid = []
board_pos_grid = []
dct_x_line = {}
dct_y_line = {}


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
    
def check_block():
    large_grid = [[0,1,2], [3,4,5], [6,7,8]]

    for i, x in enumerate(large_grid):
        for j, y in enumerate(large_grid):
            permutations = list(itertools.product(x, y))
            dct = {}
            for i, pos in enumerate(permutations):
                given = module.find_by_pos(pos)
                if given.num > 0:
                    dct[(given.x, given.y)] = given.num
            dup_value = module.duplicate_values(dct)
            if dup_value:
                for poslist in dup_value:
                    for pos in poslist:
                        given = module.find_by_pos(pos)
                        given.color = "RED"
        dct = {}

def check_lines():
    x_list = []
    y_list = []
    

    pos_list = module.board_pos_list()
    for pos in pos_list:
        given = module.find_by_pos(pos)
        if not given.fixed:
            for i in range(9):
                x_list.append((given.x, i))
                y_list.append((i, given.y))

            find_duplicate_from_list(x_list) 
            find_duplicate_from_list(y_list)          
            x_list = []
            y_list = []

def find_duplicate_from_list(lst):
    dct = {}
    for pos in lst:
        given = module.find_by_pos(pos)
        if given.num > 0:
            module.form_dic(dct, given)

    dup_value = module.duplicate_values(dct)

    if dup_value:
        for poslist in dup_value:
            for pos in poslist:
                given = module.find_by_pos(pos)
                given.color = "RED"
    dct = {}