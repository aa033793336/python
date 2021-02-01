import pandas as pd

#D09#1
data = pd.read_csv('boston.csv',usecols=['CHAS','NOX','RM'])
print(data)
data.to_excel('boston.xlsx',sheet_name='boston')