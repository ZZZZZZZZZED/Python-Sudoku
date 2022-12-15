import pandas as pd
import numpy as np
import random
import givens
import module

df = pd.read_excel('resource/sudoku_base.xlsx')



def make_empty(df, level:int):
    
    copy_df = df.copy()

    # 9 x 9 game board
    full_slots = 9 * 9
    slots = full_slots

    if level == 1:
        random_list = [0, 1] # when random choose 0, make this locate a empty number for user to fill.
        mini_accept = 0.5 * full_slots
    elif level == 3:
        random_list = [0, 0, 0, 1]
        mini_accept = 0.25 * full_slots
    else:
        random_list = [0, 0, 1]
        mini_accept = 0.35 * full_slots
    
    # traverse dataframe
    for i in range(9):
        for j in range(9):
            if random.choice(random_list) == 0:
                copy_df.at[j, i] = 0
                slots = slots - 1
    if slots >= mini_accept:
        print('Accepted, {} slots available.'.format(slots)) 
        return copy_df
    else:
        print('Not playable, only {} slots left, need {}.'.format(slots, mini_accept))


# while make_empty(df, 2):
while True:
    df_temp = make_empty(df, 2)
    if isinstance(df_temp, pd.core.frame.DataFrame):
        df = df_temp
        break
print(df)
