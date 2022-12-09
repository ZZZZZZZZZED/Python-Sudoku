import pandas as pd

df = pd.read_excel('resource/sudoku_base.xlsx')



def swap_rows(df, row1, row2):
    a, b = df.iloc[row1, :].copy(), df.iloc[row2, :].copy()
    df.iloc[row1, :], df.iloc[row2, :] = b, a


def swap_cols(df, col1, col2):
    df[[col1,col2]] = df[[col2,col1]]

def Randomization(df, line1, line2, row_or_col):

    # have two conditions
    if row_or_col == 'row':
        swap_rows(df, line1, line2)
    elif row_or_col == 'col':
        swap_cols(df, line1, line2)
    else:
        raise Exception('row_or_col should only be \'row\' or \'col\', not {}.'.format(row_or_col))
    return df

print(randomlization(df, 0, 1, 'row'))

print(randomlization(df, 4, 5, 'col'))
