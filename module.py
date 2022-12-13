import givens
import pygame
import pandas as pd

given_list = []


df = pd.read_excel('resource/sudoku_base.xlsx')



def get_base_num(x, y, df):
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
    elif row_or_col == 'col':
        swap_cols(df, line1, line2)
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

def init_givens():

    # in 9 x 9 game board
    for i in range(9):
        for j in range(9):

            # make givens instance by their location
            # instance name should be 'given_0_0'
            name = 'given_' + str(i) + '_' + str(j)
            globals()[name] = givens.Given(i, j, get_base_num(i, j, df), name) # (x, y, num, name)

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
    
