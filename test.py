import pandas as pd

df = pd.read_excel('resource/sudoku_base.xlsx')

print(df)

def randomlization(df, col1, col2):
    df_temp = df[col1]
    df = df.drop(col1,axis=1)
    df.insert(col2,col1,df_temp)
    return df


print(randomlization(df, 1, 2))


