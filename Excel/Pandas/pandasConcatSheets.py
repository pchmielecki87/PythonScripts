import pandas as pd

# Read data from files
df_1 = pd.read_excel('./data/shifts.xlsx', sheet_name='Sheet')
df_2 = pd.read_excel('./data/shifts.xlsx', sheet_name='Sheet1')
df_3 = pd.read_excel('./data/shift_3.xlsx')

# Concat without sorting
df_all = pd.concat([df_1, df_2, df_3],sort=False)

# Print
print(df_all)
