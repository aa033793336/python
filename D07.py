import numpy as np

array1 = np.array([[10, 8], [3, 5]])

#D07#1
inv = np.linalg.inv(array1)
print(np.dot(array1, inv))

#D07#2
a=np.linalg.eig(array1)
print(a)

#D07#3
b=np.linalg.svd(array1)
print(b)