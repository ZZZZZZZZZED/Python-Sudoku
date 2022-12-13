import pandas as pd
import givens

df = pd.read_excel('resource/sudoku_base.xlsx')

g = givens.Given(0, 5, 5, "name")
print(g)

def num_updates(given:givens, dataframe):
    x = given.x
    y = given.y
    given.num = dataframe.at[y, x]
    print(given)



get_value_form_coords(g,df)