import pandas as pd
from openpyxl.workbook import Workbook

df_csv = pd.read_csv('./data/Names.csv', header=None)

# Add headers
df_csv.columns = ['First', 'Last', 'Address', 'City', 'State', 'Code', 'Income']

# Save extracted data to file

extracted_data = df_csv[['First', 'Last']]
stored = extracted_data.to_excel('./data/modified/extracted_data.xlsx', header=None)
