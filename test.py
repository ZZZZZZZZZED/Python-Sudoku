import pandas as pd
import numpy as np
import random
import givens
import module

df = pd.read_excel('resource/sudoku_base.xlsx')


random_list = [0, 1, 3, 4, 6, 7]

pick = random.choice(random_list)
last_pick = -1

for i in range(30):
    pick = random.choice(random_list)
    if pick != last_pick:
        module.randomization(df, pick, pick+1, module.row_or_col())
        last_pick = pick
    else:
        print('pick repeated value, do again.')
        

print(df)

