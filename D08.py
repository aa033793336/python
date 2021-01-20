import numpy as np

name_list = ['小明','小華','小菁','小美','小張','John','Mark','Tom']
sex_list = ['boy','boy','girl','girl','boy','boy','boy','boy']
weight_list = [67.5,75.3,50.1,45.5,80.8,90.4,78.4,70.7]
rank_list = [8,1,5,4,7,6,2,3]
myopia_list = [True,True,False,False,True,True,False,False]

#D08#1
dt = np.dtype({'names':('name', 'sex', 'weight', 'rank', 'myopia'), 'formats':('U8','U8',float,int,bool)})
a = np.zeros(8,dtype=dt)
a['name'] = name_list
a['sex'] = sex_list
a['weight'] = weight_list
a['rank'] = rank_list
a['myopia'] = myopia_list
print(a)

#D08#2
print(np.average(a['weight']))

#D08#3
boy=a[a['sex']=='boy']
girl=a[a['sex']=='girl']
print(np.average(boy['weight']))
print(np.average(girl['weight']))