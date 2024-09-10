

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
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

# temp = pd.Series([1,2,3,np.nan,5,6,np.nan,8,np.nan,10])
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

### VIDEO 01
### DATA FRAMES IN PANDAS
### using lists
student_data = [
    [100,80,10],
    [90,70,7],
    [120,100,14],
    [80,50,2]
]

dataFrameList = pd.DataFrame(student_data,columns=['iq','marks','package'])
# print(dataFrameList)
### using dicts

student_dict = {
    'name':['nitish','ankit','rupesh','rishabh','amit','ankita'],
    'iq':[100,90,120,80,0,0],
    'marks':[80,70,100,50,0,0],
    'package':[10,7,14,2,0,0]
}

students = pd.DataFrame(student_dict)
students.set_index('name',inplace=True)
# print(students)

### using read_csv
movies = pd.read_csv(r'C:\Users\Windows10\Desktop\my-data\datasets-session-17\movies.csv')
# print(movies.sample(3))

iplData = pd.read_csv(r'C:\Users\Windows10\Desktop\my-data\datasets-session-17\ipl-matches.csv')
# print(iplData.sample(3))

### DataFrame Attributes and Methods
# shape , dtypes , index , columns , values , head and tails , sample , info , describe , isnull,
#duplicated , rename

# print(movies.shape)
# print(iplData.dtypes)
# print(iplData.columns)
# print(iplData.values) # return values in 2d numpy array
# print(iplData.head())
# print(iplData.tail())
# print(iplData.sample())
# print(iplData.info())
# print(iplData.describe()) # work only numerical col to perform mathematical operations like mean , median etc
# print(iplData.isnull().sum())
# print(students.duplicated().sum())
# dataFrameList.rename(columns={'iq': 'IQ' , 'marks' : 'MARKS' , 'package' : 'LPA'} , inplace=True)
# print(dataFrameList)


### Math Methods

# print(dataFrameList)
# print(dataFrameList.sum(axis=1))
# print(dataFrameList.mean(axis=1))
# print(dataFrameList.var())

### Selecting cols from a DataFrame
# single cols
# print(movies['title_x'])

# multiple cols
# print(movies[['title_x' , 'imdb_id' , 'summary']])

### Selecting rows from a DataFrame
# iloc - searches using index positions
# loc - searches using index labels

# print(iplData.iloc[0]) #retuen 1st row data
# print(iplData.iloc[0 , 1]) #return 0th row of 1th col
# print(iplData.iloc[0:3 , 0:3]) #return 3 rows and 3 col data
# print(iplData.iloc[: , 5:7]) #return all rows but 5th and 6th col data

# print(students.loc[['nitish','ankita','rupesh']])
# print(movies.loc[0:2]) # starting ending values works with len not index
# print(movies.loc[0:2,'title_x':'poster_path'])

### Filtering a DataFrame

## find all the final winners
# print(iplData[iplData['MatchNumber'] == 'Final'][['WinningTeam' , 'Season']])

## how many matches has csk won in kolkata
# print(iplData[(iplData['WinningTeam'] == 'Chennai Super Kings') & (iplData['City'] == 'Kolkata')].shape[0])

## toss winner is match winner in percentage
# print(iplData[iplData['WinningTeam'] == iplData['TossWinner']].shape[0] / iplData.shape[0] * 100)

## movies with rating higher than 8 and votes>10000
# print(movies[(movies['imdb_rating'] > 8) & (movies['imdb_votes'] > 10000)].shape[0])

## Action movies with rating higher than 7

# print(movies[(movies['genres'] == 'Action') & (movies['imdb_rating'] > 7)])


## adding lead actors columns
# movies.dropna(inplace=True)
# first_names = movies['actors'].str.split('|').apply(lambda x: x[0])
# movies['lead actors'] = first_names
# print(movies['lead actors'])

## Important DataFrame Functions
# astype
# iplData['ID'] = iplData['ID'].astype('int16')
# iplData['Team1'] = iplData['Team1'].astype('category')
# iplData['Team2'] = iplData['Team2'].astype('category')
# print(iplData.info())


###VIDEO 02
# value_counts(series & Dataframes) , sort_values() , rank , set index , rename , reset index , unique , nunique ,
# isnull , notnull , hasnans , dropna , fillna , drop_duplicates , drop , apply , isin , corr
# nlargest , nsmallest , insert , copy

## value_counts(series & Dataframes)
## FIND WHICH PLAYER HAS WON MOST POTM -> IN FINALS AND QUALIFIERS
# print(iplData[~iplData['MatchNumber'].str.isdigit()]['Player_of_Match'].value_counts())

## Toss decision plot
# iplData['TossDecision'].value_counts().plot(kind = 'pie')
# plt.show()

## how many matches each team has played
# print((iplData['Team1'].value_counts() + iplData['Team2'].value_counts()).sort_values(ascending = False))

## sort_values(series and dataframe) -> ascending -> na_position -> inplace -> multiple cols

students = pd.DataFrame(
    {
        'name':['nitish','ankit','rupesh',np.nan,'mrityunjay',np.nan,'rishabh',np.nan,'aditya',np.nan],
        'college':['bit','iit','vit',np.nan,np.nan,'vlsi','ssit',np.nan,np.nan,'git'],
        'branch':['eee','it','cse',np.nan,'me','ce','civ','cse','bio',np.nan],
        'cgpa':[6.66,8.25,6.41,np.nan,5.6,9.0,7.4,10,7.4,np.nan],
        'package':[4,5,6,np.nan,6,7,8,9,np.nan,np.nan]

    }
)

# students.sort_values('name' , na_position = 'first' , ascending = False , inplace = True)
# print(students)

# print(movies.sort_values(['title_x' , 'title_y'] , ascending=[False , True]))

## rank(series)
batsmanRuns = pd.read_csv(r'C:\Users\Windows10\Desktop\my-data\datasets-session-17\batsman_runs_ipl.csv')

## ADDING BATTING RANK COL
batsmanRuns['rank'] = batsmanRuns['batsman_run'].rank(ascending=False)
# print(batsmanRuns.sort_values('batsman_run' , ascending=False))

## sort_index(series and dataframe)
# print(iplData.sort_index(ascending=False))

## set_index(dataframe) -> inplace
batsmanRuns.set_index('batter' , inplace = True)
# print(batsmanRuns.sort_values('batsman_run' , ascending = False))

## reset_index(series + dataframe) -> drop parameter
# batsmanRuns.reset_index(inplace = True)
# print(batsmanRuns)

### how to replace existing index without loosing
# print(batsmanRuns.reset_index().set_index('rank'))

## rename(dataframe) -> index

# movies.set_index('title_x',inplace=True)
# movies.rename(columns = {'poster_path' : 'poster_link'} , inplace = True)
# movies.rename(index = {'Uri: The Surgical Strike' : 'The Surgical Strike'} , inplace = True)
# print(movies.head())

##unique(series)
temp = pd.Series([1,1,2,2,3,3,4,4,5,5,np.nan,np.nan])
# print(len(temp.unique()))

## nunique(series + dataframe) -> does not count nan -> dropna parameter
# print(temp.nunique())

## isnull(series + dataframe)

# print(iplData['ID'].isnull().sum())
# print(iplData.isnull().sum())
# print(iplData['City'][iplData['City'].isnull()])

## notnull(series + dataframe)
# print(iplData['City'][iplData['City'].notnull()])

## hasnans(series)
# print(iplData['City'].hasnans)

## dropna(series + dataframe) -> how parameter -> works like or

# print(students.dropna(how = 'any'))
# print(students.dropna(how = 'all'))
# print(students.dropna(subset = ['name' , 'college']))

## fillna(series + dataframe)

# print(students['name'].fillna('unknown'))
# print(students['package'].fillna(students['package'].mean()))
# print(students['name'].bfill())
# print(students['name'].ffill())

## drop_duplicates(series + dataframe) -> works like and -> duplicated()
# print(students.drop_duplicates())
# print(students['name'].drop_duplicates(keep = 'last'))

## find the last match played by virat kohli in Delhi

# print(iplData[((iplData['Team1Players'].str.contains('V Kohli')) +
#               (iplData['Team2Players'].str.contains('Kohli'))) &
#               (iplData['City'] == 'Delhi')].head(1))

## drop(series + dataframe)

# print(students.drop(index = [0,2]))
# print(students.set_index('name').drop(columns = ['branch']))

## apply(series + dataframe)
# def mul(num):
#     return num**2
# print(temp.apply(mul))

#POINTS DATA FRAME
# pointsDF = pd.DataFrame({
#     'point1' : [(1,3) , (-2,5) , (6,5) , (8,0)],
#     'point2' : [(-5,-9) , (9,1) , (3,4) , (6,7)]
# })

# def euclidean(row):
#     pointA = row['point1']
#     pointB = row['point2']
#     return ((pointA[0] - pointB[0])**2 + (pointA[1] - pointB[1])**2)**0.5

# pointsDF['distance'] = pointsDF.apply(euclidean, axis = 1)
# print(pointsDF)

################################### <<< GROUP BY PANDA >>> #################################################
matchDeleviries = pd.read_csv(r'C:\Users\Windows10\Desktop\my-data\datasets-session-19\deliveries.csv')
# print(matchDeleviries.head())

topMovies = pd.read_csv(r'C:\Users\Windows10\Desktop\my-data\datasets-session-19\imdb-top-1000.csv')
# grpByGenre = topMovies.groupby('Genre')

## Applying builtin aggregation fuctions on groupby objects
# print(topMovies.select_dtypes(include='number').std())

## find the top 3 genres by total earning
# grpByGenre = topMovies.groupby('Genre')
# print(grpByGenre['Gross'].sum().sort_values(ascending=False).head(3))

## find the genre with highest avg IMDB rating
# grpByGenre = topMovies.groupby('Genre')
# print(grpByGenre['IMDB_Rating'].mean().sort_values(ascending=False).head(1))

## find director with most popularity
# print(topMovies.head())
# grpByDirector = topMovies.groupby('Director')
# print(grpByDirector['No_of_Votes'].max().sort_values(ascending=False).head())

## find the highest rated movie of each genre
# print(topMovies.head())
# grpByGenre = topMovies.groupby('Genre')
# print(grpByGenre['IMDB_Rating'].max().sort_values(ascending=False).head(1))

## GroupBy Attributes and Methods

# find total number of groups -> len
# find items in each group -> size
# first()/last() -> nth item
# get_group -> vs filtering
# groups
# describe
# sample
# nunique


















