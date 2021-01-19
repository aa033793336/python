import numpy as np

#D04#1
english_score = np.array([55,89,76,65,48,70])
math_score = np.array([60,85,60,68,55,60])
chinese_score = np.array([65,90,82,72,66,77])
a=np.greater(english_score,math_score)
a=np.where(a==True)
a=np.size(a)
print(a)

#D04#2
b=np.logical_and(np.greater(chinese_score,math_score), np.greater(chinese_score,english_score))
b=np.array_equal(b,np.ones(np.size(b)))
print(b)