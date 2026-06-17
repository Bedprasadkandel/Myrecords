# import pandas as pd

# df = pd.read_csv('E:\pythonbroadway\class21A.csv')
# x = df["Calories"].median()
# df.fillna({"Calories": x}, inplace=True)####
# df['Date'] = pd.to_datetime(df['Date'], format='mixed') #### time ko farmet ma convert garxa
# df.dropna(subset=['Date'], inplace = True) ###Data  vitra ko coluoumn ko data  ko na remove garxa
# df.drop_duplicates(inplace = True)    ###Removing duplicated rows data
# print(df)

import pandas as pd
df = pd.read_csv("E:\pythonbroadway\class21A.csv ")
# df.dropna(inplace=True)### NA vako jati row remove garxa
# df.fillna({"Calories": 130}, inplace=True) ### colories ko row ma NA xaa vani 130 rakxa 
x = df["Calories"].mean()
df.fillna({"Calories": x}, inplace=True)
print(df)