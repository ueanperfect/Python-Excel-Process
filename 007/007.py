import pandas as pd

products = pd.read_excel('/Users/faguangnanhai/Documents/GitHub/Python-Excel-process/007/List.xlsx', index_col='ID')
products.sort_values(by=['Worthy', 'Price'], ascending=[True, False], inplace=True)
print(products)
