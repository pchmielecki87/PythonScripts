import pandas as pd

df_csv = pd.read_csv('./data/Names.csv', header=None)

# Add headers
df_csv.columns = ['First', 'Last', 'Address', 'City', 'State', 'Code', 'Income']

# Add column with tax % (15% <10k,40k>, 20% <40k,80k>, 25% >80k)
df_csv['Tax %'] = df_csv['Income'].apply(lambda x: .15 if 10000 < x < 40000 else .2 if 40000 < x < 80000 else .25)

# Add column with tax value
df_csv['Tax value'] = df_csv['Income'] * df_csv['Tax %']

# Drop some not needed columns
to_drop = ['First', 'Address', 'State', 'Code']
df_csv.drop(columns=to_drop, inplace=True)

print(df_csv)