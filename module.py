import givens
import pygame

given_list = []

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
            globals()[name] = givens.Given(i, j, 0, name)

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
        return window.blit(text_surface, (given.get_x(), given.get_y()))

    # else show the input box
    else:
        return
    
