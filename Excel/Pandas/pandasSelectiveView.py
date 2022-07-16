import pandas as pd

df_csv = pd.read_csv('./data/Names.csv', header=None)

# Add headers
df_csv.columns = ['First', 'Last', 'Address', 'City', 'State', 'Code', 'Income']

# Selective viewing
## one column
print(df_csv['Last'])
## two columns
print(df_csv[['State', 'Code']])
## rows 0-2 (first three)
print(df_csv['Last'][0:3])

#i-location function
## print first entry (1 row, all columns)
print(df_csv.iloc[1])
## print 2nd row and 1st column (both starts from 0!!!)
print(df_csv.iloc[2,1])
