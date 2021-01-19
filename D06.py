import numpy as np

array1 = np.array(range(30))
array2 = np.array([2,3,5])

#D06#1
with open('array_1.npy', 'wb') as f:
    np.save(f, array1)
    np.save(f, array2)

#D06#2
newArray = np.array([1,2,3,4,5])
with open('array_1.npy', 'rb') as f:
    a=np.load(f)
    b=np.load(f)

with open('array_2.npy', 'wb') as f:
    np.save(f, a)
    np.save(f, b)
    np.save(f, newArray)