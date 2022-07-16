import pandas as pd

df_csv = pd.read_csv('./data/Names.csv', header=None)

# Add headers
df_csv.columns = ['First', 'Last', 'Address', 'City', 'State', 'Code', 'Income']

# Add new fake column with the default 'false' value
df_csv['True or False'] = False

# Change 'false' to 'true' if income > 60k
df_csv.loc[df_csv['Income'] < 60000 , 'True or False'] = True

# Group by in average
print(df_csv.groupby(['True or False']).mean().sort_values('Income'))