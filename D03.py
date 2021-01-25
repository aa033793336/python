import numpy as np

#D03#1
V1 = 20000
V0 = 20
a=20*np.log10(V1/V0)
print(a)

#D03#2
def Pascal(db):
    return 20*np.power(10, db/20)
b=Pascal(30)/Pascal(50)
print(b)