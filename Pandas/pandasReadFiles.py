import pandas as pd
from openpyxl.workbook import Workbook

df_excel = pd.read_excel('./data/regions.xlsx')
df_csv = pd.read_csv('./data/Names.csv', header=None)
df_txt = pd.read_csv('./data/data.txt', delimiter='\t')

print('Excel:')
print(df_excel)

print('Csv:')
print(df_csv)

print('Txt:')
print(df_txt)