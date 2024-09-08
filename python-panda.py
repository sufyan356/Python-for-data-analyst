from unittest.mock import inplace

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# from numpy.ma.core import squeeze

### SERIES FROM LIST:
# country = ['India' , 'Pakistan' , 'Nepal' , 'Afghanistan']
# print(pd.Series(country))    # return --> index and value

# marks = [100 , 90 , 80 , 70 , 60]
# subjects = ['maths' , 'english' , 'chemistry' , 'physics' , 'urdu']
# print(pd.Series(marks , index=subjects))   # custom indexing

marks = [100 , 90 , 80 , 70 , 60]
subjects = ['maths' , 'english' , 'chemistry' , 'physics' , 'urdu']

# print(pd.Series(marks , index=subjects , name = "Sufyan's Marks"))   # naming

### SERIES FROM DICTIONARY:
# marks = {
#     "maths" : 100,
#     "english" : 90,
#     "chemistry" : 80,
#     "physics" : 70,
#     "urdu" : 60,
# }
# marksSeriesDict = pd.Series (marks , name = "Sufyan's Marks")
# print(marksSeriesDict)

### SERIES ATTRIBUTES
# size , dtype , name --> return col name , is_unique , index , values

# marks = {
#     "maths" : 100,
#     "english" : 90,
#     "chemistry" : 80,
#     "physics" : 70,
#     "urdu" : 60,
# }
# marksSeriesDict = pd.Series (marks , name = "Sufyan's Marks")
# print("Size: " , marksSeriesDict.size)
# print("Data Type: " , marksSeriesDict.dtype)
# print("Name Att: " , marksSeriesDict.name)
# print("Is Unique: " , marksSeriesDict.is_unique)
# print("index: " , marksSeriesDict.index)
# print("Size: " , marksSeriesDict.values)  #returns the numpy array

### SERIES USING REAL WORLD DATA SET
subs = pd.read_csv(r'C:\Users\Windows10\Desktop\my-data\datasets-session-16\subs.csv').squeeze()
# print(subs) #squeezed Fun return data in series

vk = pd.read_csv(r'C:\Users\Windows10\Desktop\my-data\datasets-session-16\kohli_ipl.csv' ,  index_col = 'match_no').squeeze()
# print(vk)

bw = pd.read_csv(r'C:\Users\Windows10\Desktop\my-data\datasets-session-16\bollywood.csv' , index_col = 'movie').squeeze()
# print(bw)


### SERIES METHODS
# head , tails , sample , value_counts , sort_values , sort_index
# print(subs.head()) ###returns by default 5 top values
# print(subs.head(10))

# print(subs.tail())
# print(subs.tail(10))

# print(bw.sample())  ###returns by default 1 random value
# print(bw.sample(3))

# print(bw.value_counts())  ###returns no of movies by doing individual actors in descending order

# print("Highest Runs By Virak Kohli: " , vk.sort_values(ascending = False).head(1).values[0]) ## does not sort the orignal data
# print("Lowest Runs By Virak Kohli: " , vk.sort_values().head(1).values[0])

# print(bw.sort_index())


### SERIES MATHS METHODS
# count --> null val does not count , sum , product , mean , median , mode , std , var , min , max , describe
# print(subs.count())
# print(subs.sum())
# print(subs.product())
# print(vk.mean())
# print(subs.median())
# print(bw.mode())
# print(vk.std())
# print(vk.var())
# print(subs.min())
# print(subs.max())
# print(subs.describe())


### SERIES INDEXING
# directely negative indexing in panda not work.

# x = pd.Series([1,3,2,5,4,7,6,9])
# print(x.iloc[-1]) # return 9

# y = pd.Series(["karachi","bulbulay","chocolate","donkey","elephant","flag"])
# print(y[0]) # return karachi

# print(bw.iloc[0]) # iloc used when index value is not set integer numbers in bw case index value is movie name that why we used iloc


### SERIES SLICING
# print(subs[0:101])
# print(bw[-5:])

### INDEXING WITH LABELS
# print(bw['Hum Tumhare Hain Sanam'])

### FANCY INDEXING
# print(subs[[0,100,364]])


### SERIES WITH PYTHON FUNCTIONALITIES
# len , type , dir , sorted , max , min
# type conversion
# membership operator
# looping
# Arithmetic operator

### len , type , dir , sorted , max , min
# print(len(subs))
# print(type(subs))
# print(dir(subs))
# print(sorted(subs)) #return in list form
# print(max(subs))
# print(min(subs))

### membership operator (works in indexing val)
# print(bw.head())

# print('Battalion 609' in bw) #True
# print('Vicky Ahuja' in bw)    #False
# print('Vicky Ahuja' in bw.values)    #True


###LOOPING
# for i in bw.index:
#   print(i)

### Boolean Indexing on Series

# Find no of 50's and 100's scored by kohli
# print(vk[vk >= 50].size)

# find number of ducks
# print(vk[vk == 0].size)

# Count number of day when I had more than 200 subs a day
# print(subs[subs > 200].size)

# find actors who have done more than 20 movies
# num_movies = bw.value_counts()
# print(num_movies[num_movies > 20])

# PLOTTING GRAPH ON SERIES
# subs.plot()
# plt.show()

# bw.value_counts().head(20).plot(kind='pie')
# plt.show()

### Some Important Series Methods
# astype
# between
# clip  --> return less than 100 to 100 more than 200 to 200
# drop_duplicates
# isnull
# dropna
# fillna
# isin
# apply
# copy
# size return size with null val
# count return count without null val
#isin
# apply
#copy and view

# changingDtype = vk.astype('int16')
# print(changingDtype)

# print(vk[vk.between(51,99)].size)
# print(subs.clip(100,200))

# temp = pd.Series([1,1,2,2,3,3,4,4])
# print(temp.drop_duplicates(keep='last'))
# print(temp.duplicated().sum())

# print(vk.duplicated().sum())

temp = pd.Series([1,2,3,np.nan,5,6,np.nan,8,np.nan,10])
# print(temp.size)
# print(temp.count())

# print(temp.isnull().sum())
# print(temp.dropna())
# print(temp.fillna(temp.mean()))

# print(vk[(vk == 49) | (vk == 99)])
# print(vk[vk.isin([49,99])])

# print(bw.apply(lambda x:x.split()[0].upper()))
# print(subs.apply(lambda x:'good day' if x > subs.mean() else 'bad day'))

# view = vk.head()
# print(view)
# view[1] = 100
# print(view)
# print(vk.head())

# copy = vk.head().copy()
# print(copy)
# copy[1] = 100
# print(copy)
# print(vk.head())