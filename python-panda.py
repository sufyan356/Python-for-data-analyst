import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)  # Disable line wrapping


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
# subs = pd.read_csv(r'C:\Users\Windows10\Desktop\my-data\datasets-session-16\subs.csv').squeeze()
# print(subs) #squeezed Fun return data in series

# vk = pd.read_csv(r'C:\Users\Windows10\Desktop\my-data\datasets-session-16\kohli_ipl.csv' ,  index_col = 'match_no').squeeze()
# print(vk)

# bw = pd.read_csv(r'C:\Users\Windows10\Desktop\my-data\datasets-session-16\bollywood.csv' , index_col = 'movie').squeeze()
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


### SOME IMP FUNCTIONS
#astype , between , clip , drop_duplicates , duplicated ,  isnull , dropna , fillna , isin ,
# apply --> used to custom logic in series , copy , view

# changeTypeOfVk = vk.astype('int16')
# print(changeTypeOfVk.dtype)

#find how many matches that kohli runs between 50 to 100 50 and 100 included
# print(vk[vk.between(50 , 100)].size)

# print(vk.clip(100 , 200))  # return less than 100 to 100 greater than 200 to 200 and 100 and 200 in between val makes not change

# duplicatedValues = pd.Series([1,1,2,3,4,4,5,5,6,6,6,7])
# print(duplicatedValues.drop_duplicates())  # remove duplicate by first val

# duplicatedValues = pd.Series([1,1,2,3,4,4,5,5,6,6,6,7])
# print(duplicatedValues.drop_duplicates(keep = "last"))  # remove duplicate by last val

# duplicatedValues = pd.Series([1,1,2,3,4,4,5,5,6,6,6,7])
# print(duplicatedValues.duplicated().sum())

# valWithNull = pd.Series([1,2,3,np.nan , 5 , 6 , np.nan])
# print(valWithNull.size)  #return all series size with null val
# print(valWithNull.count())  #return all series size with out null val
# print(valWithNull.isnull().sum())
# print(valWithNull.dropna())
# print(valWithNull.fillna(valWithNull.mean()))

# print(vk[(vk == 49) | (vk == 99)])
# print(vk[vk.isin([49,99])])


# print(bw.apply(lambda x : x.split()[0].upper()))
# print(subs.apply(lambda x: 'good-day' if x>=subs.mean() else 'bad-day'))

# view = vk.head()
# print(view)
# view[1] = 100
# print(view , "\n")
# print(vk)

# copy = vk.head().copy()
# print(copy)
# copy[1] = 100
# print(copy)
# print(vk)

### PANDA DATA FRAMES
# More than 1 col and more than 1 row called an data frames
# single col and single row called an series

### DATAFRAMES WITH LISTS
stdData = [
    [100 , 90 , 10000],
    [90 , 80 , 30000],
    [80 , 70 , 20000],
]
stdDataWithDataFrames = pd.DataFrame(stdData , columns = ['iq' , 'marks' , 'package'])
# print(stdDataWithDataFrames)

stdDict = {
    'iq' : [100 , 90 , 80],
    'marks' : [100 , 90 , 80],
    'package' : [100 , 90 , 80],
}
stdDictDataframes = pd.DataFrame(stdDict)
# print(stdDictDataframes)

### READING CSV FILES
iplData = pd.read_csv(r'C:\Users\Windows10\Desktop\my-data\datasets-session-17\ipl-matches.csv')
# print(iplData.head())
moviesData = pd.read_csv(r'C:\Users\Windows10\Desktop\my-data\datasets-session-17\movies.csv')
# print(moviesData.head())

### DATAFRAMES ATTRIBUTES AND METHODS:
# shape , dtypes , index , columns , values , head , tail , sample , info  --> returns name of col and dtypes and how many null val ,
# describe ---> only work in numerical col ; provide the summary of mathematical fun like mean and median
# isnull , duplicated , rename
print(iplData.shape)
# print(iplData.dtypes)
# print(iplData.index)
# print(iplData.columns)
# print(iplData.values)  # return val in 2d numpy array
# print(iplData.sample(3))
# print(iplData.info())
# print(iplData.describe())
# print(iplData.isnull().sum()) #return every col null val
# print(moviesData.duplicated().sum())
# stdDictDataframes.rename(columns = {'iq' : 'Iq' , 'marks' : 'Marks' , 'package' : 'LPA'} , inplace = True)
# print(stdDictDataframes)







