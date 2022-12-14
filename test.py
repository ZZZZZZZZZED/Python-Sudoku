import pandas as pd
import numpy as np
import random
import givens
import module

df = pd.read_excel('resource/sudoku_base.xlsx')



def make_empty(df, level:int):
    
    # 9 x 9 game board
    full_slots = 9 * 9

    if level == 1:
        random_list = [0, 1] # when random choose 0, make this locate a empty number for user to fill.
        mini_accept = 0.45 * full_slots
    elif level == 3:
        random_list = [0, 0, 0, 1]
        mini_accept = 0.25 * full_slots
    else:
        random_list = [0, 0, 1]
        mini_accept = 0.3 * full_slots
    
    # traverse dataframe
    for i in range(9):
        for j in range(9):
            if random.choice(random_list) == 0:
                df.at[j, i] = 0
                slots = full_slots - 1
                print(slots)
    if slots >= mini_accept:
        print(slots)
        print('accept')
        print(df)
    else:
        print('Not playable, {} only slots left, need {}.'.format(slots, mini_accept))
            
# def playable(df, pct):


make_empty(df, 1)
