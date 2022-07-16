from re import RegexFlag
import pandas as pd
import numpy as np
from openpyxl.workbook import Workbook

df_csv = pd.read_csv('./data/Names.csv', header=None)

# Add headers
df_csv.columns = ['First', 'Last', 'Address', 'City', 'State', 'Code', 'Income']

# Drop some not needed columns
to_drop = ['Address']
df_csv.drop(columns=to_drop, inplace=True)

# Set index
df_csv = df_csv.set_index('Code')

# Split each word in separate column
print(df_csv.First.str.split(expand=True))

# Replace value
df_csv = df_csv.replace(np.nan, 'N/A', regex=True)

print(df_csv)