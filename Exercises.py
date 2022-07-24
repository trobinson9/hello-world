import numpy as np
import pandas as pd


#  Make pd series from np
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))


#  Ex 1
ser1 = pd.Series(mylist)
ser2 = pd.Series(myarr)
ser3 = pd.Series(mydict)

# print(ser3.head())

#  Ex 2
df = ser3.to_frame().reset_index()
# print(df.head())

#  Ex 8 - get percentiles
ser = pd.Series(np.random.normal(10, 5, 25))
print(ser.quantile([0, 0.25, 0.5, 0.75, 1]))
