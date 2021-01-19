import numpy as np

english_score = np.array([55,89,76,65,48,70])
math_score = np.array([60,85,60,68,np.nan,60])
chinese_score = np.array([65,90,82,72,66,77])

#D05#1
def calculate(array):
    array=array[~np.isnan(array)]
    a=np.average(array, axis=None, weights=None)
    b=np.max(array)
    c=np.min(array)
    d=np.std(array)
    return a,b,c,d

print(calculate(english_score))
print(calculate(math_score))
print(calculate(chinese_score))

#D05#2
math_score[4]=55
print(calculate(math_score))

#D05#3
a={
    "math":np.corrcoef(chinese_score,math_score)[0][1],
    "english":np.corrcoef(chinese_score,english_score)[0][1]
    }
print(max(a,key=a.get))