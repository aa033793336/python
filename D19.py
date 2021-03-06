import numpy as np
import matplotlib.pyplot as plt

#D19#1
n = 12 
X = np.arange(n)
Y1 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)
Y2 = (1-X/float(n)) * np.random.uniform(0.5,1.0,n)

plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
plt.bar(X, +-Y2, facecolor='#ff9999', edgecolor='white')

for x,y in zip(X,Y1):
    plt.text(x+0.4, y+0.05, '%.2f' % y, ha='center', va= 'bottom')
for x,y in zip(X,-Y2):
    plt.text(x+0.4, y+0.05, '%.2f' % y, ha='center', va= 'bottom')

fig = plt.figure()

plt.axes([0.1,0.1,.8,.8])

plt.axes([0.2,0.2,.3,.3])
plt.xticks([0,10]), plt.yticks([-1,1])
plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
plt.bar(X, +-Y2, facecolor='#ff9999', edgecolor='white')

plt.ylim(-1.25,+1.25)
plt.show()