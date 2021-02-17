import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

#D21#1
df = sns.load_dataset('titanic')
#df.info()

sns.barplot(data = df, x = "sex", y = "survived",hue = 'class', orient = "v")

#D21#2
g = sns.FacetGrid(data = df, col="sex")
g.map(plt.hist, "survived");

plt.figure()

df.groupby('pclass').survived.sum()
survived=df.groupby(['pclass','sex']).survived.sum()
survived.plot(kind='bar')

survived_counts = pd.crosstab([df.pclass, df.sex],df.survived)
survived_counts.plot(kind='bar',stacked=True)

plt.figure()

sns.violinplot(data=survived_counts)

plt.show()

