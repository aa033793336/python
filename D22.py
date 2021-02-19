import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#D22#1
df_red = pd.read_csv('winequality_red.csv')
df_white = pd.read_csv('winequality_white.csv')

import keras
print("keras:",keras.__version__)
import tensorflow as tf
print("tf:",tf.__version__)

#D22#1
df_red["color"] = "R"
df_white["color"] = "W"
df_all=pd.concat([df_red,df_white],axis=0)
sns.catplot(x="quality", y="pH", kind="swarm", data=df_all);

df_all.rename(columns={'fixed acidity': 'fixed_acidity','citric acid':'citric_acid',
                       'volatile acidity':'volatile_acidity','residual sugar':'residual_sugar',
                       'free sulfur dioxide':'free_sulfur_dioxide',
                       'total sulfur dioxide':'total_sulfur_dioxide'}, inplace=True)

df_all = pd.get_dummies(df_all, columns=["color"])
df_all.isnull().sum()

sns.set(style="white")

penguins = sns.load_dataset("penguins")

g = sns.PairGrid(penguins, diag_sharey=False)
g.map_upper(sns.scatterplot)
g.map_lower(sns.kdeplot, colors="C0")
g.map_diag(sns.kdeplot, lw=2)

plt.show()