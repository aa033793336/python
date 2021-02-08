import numpy as np 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 

#D20#1
x = np.random.normal(2, 1, 75)
y = 2 + 1.5 * x + np.random.normal(0, 2, 75)
sns.set(color_codes=True)
sns.displot(x);
sns.displot(x, bins=20, kde=True, rug=True);
plt.show()