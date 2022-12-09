import pandas as pd

df = pd.read_excel('resource/sudoku_base.xlsx')

print(df)


row0 = 0
row1 = 1
df_temp = df.iloc[row0]
lable = df.index[row0]
print(df_temp)
print(lable)
df.drop(lable, axis = 0, inplace = True)
df.loc[lable] = df_temp
print(df)

def randomlization(df, col1, col2, row_or_col):
    # have two conditions
    if row_or_col == 'row':
        row_or_col = 0

        # replacing row method
        # get row by index[col1]
        df_temp = df[col1:col1+1]
        # df.drop(col1, axis = row_or_col, inplace = True)
        # df.loc[col2] = df_temp
        df1 = df.iloc[:i, :]
        df2 = df.iloc[i:, :]
        df_new = pd.concat([df1, df_temp, df2], ignore_index=True)


        #TODO

    elif row_or_col == 'col':

        # exchanging columns for randomlizing
        exchange_col(df, col1, col2)
    else:
        raise Exception('row_or_col should only be \'row\' or \'col\', not {}.'.format(row_or_col))

    
    return df

def exchange_col(df, col1, col2):
    # only need to consider two adjacent columns to cover all possibilities
    # two adjacent columns should in same 3x3 block xy[0,2][3,5][6,8]
    df_temp = df.iloc[:, col1] # get column from index: col1
    lable = df.columns[col1] # get column name from index for upcoming operations
    
    # drop and insert column to make exchange
    df.drop(lable, axis = 1, inplace = True)  # drop col1
    df.insert(col2, lable, df_temp) #(iloc, name, data); insert col1 at the index of loc2


