import pandas as pd

#D10#1
data1 = pd.read_csv('STOCK_DAY_0050_202009.csv')
data2 = pd.read_csv('STOCK_DAY_0050_202010.csv')

data = pd.concat([data1,data2],axis=0,join='inner')
print(data)

index = data.loc[data.open<data.close]
print(index)