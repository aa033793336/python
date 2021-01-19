import numpy as np

#D02#1
array1 = np.array(range(30))
a=np.reshape(array1, (5, 6),order='F')
print(a)

#D02#2
b=np.where(a%6==1)
print(b)