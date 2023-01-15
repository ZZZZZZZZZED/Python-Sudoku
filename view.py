import module
import pygame

window_pos_grid = []
board_pos_grid = []

def init_highlight_pos():
    for i in range(9):
        for j in range(9):
            x = i * 42.5
            y = j * 42.5
            posi = (x, y)
            if module.check_available(posi):
                window_pos_grid.append(posi)
                board_pos_grid.append((i,j))

def find_gridpos_by_click(pos:tuple):
    a = module.mousepos_to_boardpos(pos)
    print(a)
    if module.mousepos_to_boardpos(pos) in board_pos_grid:
        i = board_pos_grid.index(module.mousepos_to_boardpos(pos))
        return window_pos_grid[i]
    else:
        return 'fail find, or fixed slot.'