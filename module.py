import givens
import pygame
import random
import pandas as pd


given_list = []


df = pd.read_excel('resource/sudoku_base.xlsx')

def check_available(pos):
    pos = mousepos_to_boardpos(pos)
    name = 'given_' + str(pos[0]) + '_' + str(pos[1])
    for g in given_list:
        if g.name == name:
            return g.fixed

def overwrite(pos, input):
    # overwrite a value into a boardpos

    name = 'given_' + str(pos[0]) + '_' + str(pos[1])

    # find given by given's name, if not create at init then overwrite
    for g in given_list:
        if g.name == name and not g.fixed:
            g.num = input

def mousepos_to_boardpos(pos):
    # covert mouse click pos to boardpos
    # by finding nearest y first, then finding nearest x

    min_x = []
    min_y = []
    for i in range(9):
        name = 'given_' + str(i) + '_' + str(0)
        for g in given_list:
            if g.name == name:

                # append distance to list, min is the nearest
                temp = abs(g.window_x - pos[0])
                min_x.append(temp)
    for j in range(9):
        name = 'given_' + str(0) + '_' + str(j)
        for g in given_list:
            if g.name == name:

                # append distance to list, min is the nearest
                temp = abs(g.window_y - pos[1])
                min_y.append(temp)

    # return nearest pos(x,y) for upcoming operation
    return (min_x.index(min(min_x)), min_y.index(min(min_y)))

def make_empty(df, level:int):
    
    copy_df = df.copy()

    # 9 x 9 game board
    full_slots = 9 * 9
    slots = full_slots

    # add difficulty scale by level
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



def row_or_col():
    row_col_list = [0, 1]
    if random.choice(row_col_list) == 0:
        return 'row'
    else:
        return 'col'

def get_base_num(x, y, df):
    
    # use pandas '.at' method, at[ilocRow, ilocCol]
    return df.at[y, x]

def swap_rows(df, row1, row2):

    # custom function from stack overflow: https://stackoverflow.com/questions/63423089/how-to-swap-two-rows-of-a-pandas-dataframe
    # copy row a, b then 
    a, b = df.iloc[row1, :].copy(), df.iloc[row2, :].copy()

    # switch to b, a according to index
    df.iloc[row1, :], df.iloc[row2, :] = b, a

def swap_cols(df, col1, col2):
    df[[col1,col2]] = df[[col2,col1]]

def randomization(df, line1, line2, row_or_col):

    # have two conditions
    if row_or_col == 'row':
        swap_rows(df, line1, line2)
        print('swaping row {} and {}.'.format(line1, line2))
    elif row_or_col == 'col':
        swap_cols(df, line1, line2)
        print('swaping col {} and {}.'.format(line1, line2))
    else:
        raise Exception('row_or_col should only be \'row\' or \'col\', not {}.'.format(row_or_col))
    return df

def exchange_col(df, col1, col2):

    # df[[col1,col2]] = df[[col2,col1]] can also make this but index not change
    # only need to consider two adjacent columns to cover all possibilities
    # two adjacent columns should in same 3x3 block xy[0,2][3,5][6,8]
    df_temp = df.iloc[:, col1] # get column from index: col1
    lable = df.columns[col1] # get column name from index for drop and insert operations
    
    # drop and insert column to make exchange
    df.drop(lable, axis = 1, inplace = True)  # drop col1
    df.insert(col2, lable, df_temp) #(iloc, name, data); insert col1 at the index of loc2

def random_base(times):
    random_list = [0, 1, 3, 4, 6, 7]
    pick = random.choice(random_list)
    last_pick = -1

    for i in range(times):
        pick = random.choice(random_list)
        if pick != last_pick:
            randomization(df, pick, pick+1, row_or_col())
            last_pick = pick
        else:
            print('pick repeated value, do again.')

def init_givens():
    global df
    random_base(30)

    # do make_empty while random game df_temp is success generated.
    while True:
        df_temp = make_empty(df, 2)
        if isinstance(df_temp, pd.core.frame.DataFrame):
            df = df_temp
            break

    # in 9 x 9 game board
    for i in range(9):
        for j in range(9):

            # make givens instance by their location
            # instance name should be 'given_0_0'
            name = 'given_' + str(i) + '_' + str(j)
            globals()[name] = givens.Given(i, j, get_base_num(i, j, df), name) # (x, y, num, name)

            # fixed slots cannot be changed in the game
            if globals()[name].num != 0:
                globals()[name].fixed = True
                
            # convert the original coord to px coord in the window
            globals()[name].coord_convert(i, j, 42.5)
            given_list.append(globals()[name])
            print(globals()[name])

            # if need to visit instance use "globals()['name'].attributes/methods" 
            # only "globals()[name]" makes Error
    
    # ✔ : print(globals()['given_0_6'].name)
    # × ： print(globals()[given_0_6].name)

    
    

def text_render(window, given):

    # set font
    font = pygame.font.Font(None,50)

    # if each number > 0 then show the number according to coords
    if given.get_num() > 0:
        text_surface = font.render(format(given.get_num()), True, "BLACK")
        return window.blit(text_surface, (given.window_x, given.window_y))

    # else show the input box
    else:
        return
    
