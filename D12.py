import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#D12#1
data = pd.read_csv('boston.csv')
print(data)
data.boxplot()

a = np.median(data, axis=0)
b = data.columns[np.logical_and(a>300,a<400)]
print(b)

#D12#2
data.plot.scatter(x='NOX', y='DIS')
plt.show()