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

def block_valid(boardpos):
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
    

    for i, lst in enumerate(large_grid):
        if x in lst:
            x_list = large_grid[i]
        if y in lst:
            y_list = large_grid[i]

    permutations = list(itertools.product(x_list, y_list))
    
    # 3 * 3
    dct = {}
    for i, pos in enumerate(permutations):
        overwrite_color_by_pos(dct, pos)
                                    
def overwrite_color_by_pos(dct, pos):
    name = 'given_' + str(pos[0]) + '_' + str(pos[1])
    for g in module.given_list:
        if g.name == name and g.num > 0:
            dct[(g.x, g.y)] = g.num
            dup = module.duplicate_values(dct)
            if dup:
                for poslist in dup:
                    for pos in poslist:
                        name = 'given_' + str(pos[0]) + '_' + str(pos[1])
                        for g in module.given_list:
                            if g.name == name and not g.fixed:
                                g.color = "RED"
                                g.last = g.num
            else:
                if not g.fixed:
                    g.color = "BLUE"


def line_valid(boardpos):
    
    x = boardpos[0]
    y = boardpos[1]

    # 1 * 9 and 9 * 1
    x_list = []
    y_list = []

    dct_x = {}
    dct_y = {}

    for i in range(9):
        x_list.append((x, i))
        y_list.append((i, y))
    
    for x, y in zip(x_list, y_list):
        overwrite_color_by_pos(dct_x, x)
        overwrite_color_by_pos(dct_y, y)

