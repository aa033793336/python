import itertools
import matplotlib.pyplot as plt
import numpy as np

#D18#1
x = np.arange(0, 3 * np.pi, 0.1)
y_cos = np.cos(x)
plt.plot(x, y_cos)

#D18#2
n = 1024
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)
T = np.arctan2(Y, X)
fig = plt.figure()
ax = fig.add_axes([0.025, 0.025, 0.95, 0.95])
ax.scatter(X, Y, s=75, c=T, alpha=.5)

ax.set_xlim(-1.5, 1.5), ax.get_xticks([])
ax.set_ylim(-1.5, 1.5), ax.get_yticks([])

# savefig('../figures/scatter_ex.png',dpi=48)
plt.show()