import pandas as pd
from openpyxl.workbook import Workbook

df_csv = pd.read_csv('./data/Names.csv', header=None)

# Add headers
df_csv.columns = ['First', 'Last', 'Address', 'City', 'State', 'Code', 'Income']

# Save
df_csv.to_excel('./data/modified/modified.xlsx')

# print(df_csv)
