import pandas as pd

df = pd.read_excel('resource/sudoku_base.xlsx')

print(df)

def randomlization(df, col1, col2, row_or_col):
    df_temp = df[col1]
    if row_or_col == 'row':
        row_or_col = 0
    elif row_or_col == 'col':
        row_or_col = 1
    else:
        raise Exception('row_or_col should only be \'row\' or \'col\', not {}.'.format(row_or_col))

    df.drop(col1, axis=row_or_col, inplace = True)
    df.insert(col2, col1, df_temp)
    return df

print(randomlization(df, 1, 2, 'col'))
print(df)


# print(randomlization(df, 0, 2))
# print(randomlization(df, 3, 4))
# print(randomlization(df, 6, 8))


