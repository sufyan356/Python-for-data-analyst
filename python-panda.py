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

marks_Series = pd.Series(marks , index=subjects , name = "Sufyan's Marks")  # naming
# print(marks_Series)

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
subs = pd.read_csv(r'C:\Users\Windows10\Desktop\datasets-session-16-20240904T114815Z-001\datasets-session-16\subs.csv').squeeze()
# print(subs) #squeezed Fun return data in series

vk = pd.read_csv(r'C:\Users\Windows10\Desktop\datasets-session-16-20240904T114815Z-001\datasets-session-16\kohli_ipl.csv' ,  index_col = 'match_no').squeeze()
# print(vk)

bw = pd.read_csv(r'C:\Users\Windows10\Desktop\datasets-session-16-20240904T114815Z-001\datasets-session-16\bollywood.csv' , index_col = 'movie').squeeze()
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
# for i in bw:
#     print(i)  #returns value

# for i in bw.index:
#     print(i)  #returns index

### ARITHMETIC OPERATORS
# difference_100 = 100 - marks_Series
# print(difference_100)

### RELATIONAL OPERATORS
# find no of 50's and more than 50's by kohli
# print(vk[vk>=50].size)

# find no of duck's by kohli
# print(vk[vk==0].size)

# count the no of days when campusx owner had more than 200 subs a day
# print(subs[subs>200].size)

#find actors who have done more than 20 movies
# noOfMoviesByActors = bw.value_counts()
# print(noOfMoviesByActors[noOfMoviesByActors > 20])

### PLOTING GRAPH ON SERIES
# subs.plot()
# plt.show()

# bw.value_counts().head(20).plot(kind='bar')
# plt.show()

# bw.value_counts().head(20).plot(kind='pie')
# plt.show()






















