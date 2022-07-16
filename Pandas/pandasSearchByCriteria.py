import pandas as pd
from openpyxl.workbook import Workbook

df_csv = pd.read_csv('./data/Names.csv', header=None)

# Add headers
df_csv.columns = ['First', 'Last', 'Address', 'City', 'State', 'Code', 'Sth']

# Single search criteria
print(df_csv.loc[df_csv['City']=='Riverside'])

# More search criteria
print(df_csv.loc[
    (df_csv['City']=='Riverside') & (df_csv['First']=='John')
    ]
)