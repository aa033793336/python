import numpy as np
import pandas as pd

index = pd.date_range('1/1/2019', periods=20, freq='D')
series = pd.Series(range(20), index=index)

#D16#1
a = series.to_period(freq="W")
print(a)

#D16#2
b = a.resample('W').mean()
print(b)
