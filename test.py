import pandas as pd

df = pd.read_excel('resource/sudoku_base.xlsx')

# print(df)
# col = 1

# # df_temp = df.iloc[[col]]#提取一行
# df_temp = df[[col]]
# print(df_temp)
# # loc = df.columns.get_loc()
# lable = df.columns[col]
# print(lable+1)
# df.drop(lable, axis = 1, inplace = True)

# df.insert(col+1, col, df_temp)
# print(df)

def t(df, col1, col2):
    df_temp = df[col1:col1+1]
    df.drop(col1, axis = 0, inplace = True)
    df1 = df.iloc[:col2, :]
    df2 = df.iloc[col2:, :]
    print(df_temp)
    print()
    print(df1)
    print(df2)

# t(df,3,5)

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
        # replacing column method
        # save col by col name
        exchange_col(df, col1, col2)

    else:
        raise Exception('row_or_col should only be \'row\' or \'col\', not {}.'.format(row_or_col))

    
    return df

def exchange_col(df, col1, col2):
    df_temp = df.iloc[:, col1] # get column from index: col1
    lable = df.columns[col1]
    df.drop(lable, axis = 1, inplace = True)
    print('after drop:')
    print(df)
    df.insert(col2, lable, df_temp) #(iloc, name, data)


exchange_col(df, 0, 1)
print("df1:")
print(df)
print("2:")
exchange_col(df, 0, 1)
print(df)
exchange_col(df, 1, 2)
print(df)
# print(randomlization(df,0,2,'col'))
# print(randomlization(df,0,2,'col'))

