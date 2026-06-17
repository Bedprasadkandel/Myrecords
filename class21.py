import pandas as pd

df = pd.read_csv('E:\pythonbroadway\class21Data.csv')
# df.fillna(130, inplace = True)
# print(df)
# df.fillna({"Calories": 130}, inplace=True)
df['Date'] = pd.to_datetime(df['Date'], format='mixed')
df.dropna(subset=['Date'], inplace = True)
# df.loc[7, 'Duration'] = 45 #changed big value
#with using loop
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 45
# print(df)

# print(df.duplicated())
df.drop_duplicates(inplace = True)# removing all row of duplicated
print(df)
df.to_csv("bed.csv",index=False)



# new_df = df.dropna()
# print(new_df)
# print(new_df.to_string())