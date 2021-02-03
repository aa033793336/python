import pandas as pd

score_df = pd.DataFrame([[1,56,66,70], 
              [2,90,45,34],
              [3,45,32,55],
              [4,70,77,89],
              [5,56,80,70],
              [6,60,54,55],
              [7,45,70,79],
              [8,34,77,76],
              [9,25,87,60],
              [10,88,40,43]],columns=['student_id','math_score','english_score','chinese_score'])

#D13#1
a = score_df[score_df.student_id==6]
b = (a.math_score + a.english_score + a.chinese_score)/3
print(b.iloc[0])

#D13#2
c = score_df[score_df.student_id!=6]
d = (c.math_score + c.english_score + c.chinese_score)/3
e = d[d>b.iloc[0]].count()>5
print(e)

score_df = score_df.set_index('student_id')
f = score_df.apply(lambda x : x**(0.5)*10)
print(f.loc[6])

print(f.sum(axis=0)/f.count())