#----------------------------------------------------------------------------------------------------#
# ----------------------- <<< NUMPY ARRAY VS LIST >>> -----------------------------------------------
import numpy as np
import statistics as stats

# (1) list:  not the contiguous memory location
# (1) array: contiguous memory location

# (2) list: contain different data types
# (2) array: contain same data types

# (3) list: can't handle mathematical operations
# (3) array: handle mathematical operations

# (4) list: nested data with different size
# (4) array: nested data with same size
#----------------------------------------------------------------------------------------------------#



#----------------------------------------------------------------------------------------------------#
# ----------------------- <<< Slicing In numpy array >>> --------------------------------------------
# arr = np.array([2,4,5,7,9])
# print(arr[0:3])  #  [2 4 5]
# print(arr[:2])   #  [2 4]
# print(arr[::])   #  [2 4 5 7 9]
# print(arr[::-1]) # [9 7 5 4 2]

# arr = np.array([[2,4,5,7,9],[1,3,5,7,7]])
# print(arr[0:2 , 0:2]) #[[2 4]
#                       #[1 3]]
#
# print(arr[0:2 , 0:3]) #[[2 4 5]
#                       #[1 3 5]]
#
# print(arr[0,0:2]) #[2 4]

# arr = np.array([[2,4,5,7,9],[1,3,5,7,7],[32,4,1,6,5]])
# print(arr[0:3 , 0:2])  # 1st 3 rows and 1st 2 columns
#----------------------------------------------------------------------------------------------------#







# ----------------------- <<< ITERATION NUMPY ARRAY >>> -----------------------------------------------
# arr3 = np.array([[[1,2],[3,4],[5,6]]])

# for i in arr3:
#     for j in i:
#         for k in j:
#             print(k)

# FOR ITERATION:
# for i in np.nditer(arr3):
#     print(i) # iteration builtin fun

# FOR ITERATION AND INDEX
# for index , val in np.ndenumerate(arr3):
#     print(index , val)

#----------------------------------------------------------------------------------------------------#






#----------------------------------------------------------------------------------------------------#
# ----------------------- <<< COPY VS VIEW IN NUMPY ARRAY >>> ------
# (1) --> copy function returns the new array the mofifications in copy array does not changes the orignal array and orignal arrays changes does not reflect changes the copy array
# (2) --> view functions returns the orignal array
#
# arr = np.array([1,2,3])
# copyArray = arr.copy()
# print("before")
#
# print(arr)
# print(copyArray)
# arr[1] = 7
#
# print("after")
# print(arr)
# print(copyArray)

# arr = np.array([1,2,3])
# viewArray = arr.view()
# print("before")
#
# print(arr)
# print(viewArray)
# arr[1] = 7
#
# print("after")
# print(arr)
# print(viewArray)




#----------------------------------------------------------------------------------------------------#
# ----------------------- <<< Array Functions Converting Data types From One Form To Another >>> ------

# arr = np.array([2.4,4.3,5.6,7.7,9.5])
# print(arr.dtype) #float64
# # print(len(arr)) # 5
# print(arr.astype(int)) #convert float to int.
#----------------------------------------------------------------------------------------------------#

#-------------------------------------------------------------------------------------------#
# ---------------------- <<< 1. Array Creation and Initialization >>> ----------------------
# (1): np.array(): Converts lists or other sequences into NumPy arrays.




# concatenate of list:

# l1 = [1,2,3]
# l2 = [4,5,6]
#print(type(l1)
# print(l1+l2)

#Multiple Data Types In numpy array:

# l1 = np.array([1,2,3])
# l2 = np.array([4,5,"6"])
# print("ORIGNAL L1 ARRAY: " , l1)
# print("ORIGNAL L2 ARRAY: " , l2) # In l2 all elements makes string
# print("Addition of Numpy Array: " , l1+l2) # not add because data types changes error shows
#-------------------------------------------------------------------------------------------#





#-------------------------------------------------------------------------------------------#
# ---------------------- <<< 2. Special Type of Array Filled With Specific Values >>> -------
#(1): Array Filled With 0's
#(2): Array Filled With 1's
#(3): Create An Empty Array
#(4): An Array With a range of Element
#(5): Array diagonal elements filled with 1's
#(6): Create an array with values that are spaced linearly in a specified interval

# arrZero = np.zeros(5)         #[0. 0. 0. 0. 0.]
# arrZeroOne = np.zeros((2,3))  #[[0. 0. 0.]
#                               #[0. 0. 0.]]
#
# arrOne = np.ones(3)          # [1. 1. 1.]
# arrOne_1 = np.ones((2 , 3))  # [[1. 1. 1.]
#                              # [1. 1. 1.]]
#
# arrEmptyWithPrevMemoryValue = np.empty(2) #[8.90070286e-308 1.27945821e-307]
#
#
# arrArrange = np.arange(3)          # [0 1 2]
#
# arrDiagonal = np.eye(2)           # [[1. 0.]
#                                   #  [0. 1.]]
#
# arrDiagonal_1 = np.eye(3,2)   #[[1. 0.]
#                                      #[0. 1.]
#                                      #[0. 0.]]
#
# arrLinSpace = np.linspace(0,10 , num=5)
# print(arrLinSpace)  #[ 0.   2.5  5.   7.5 10. ]


#--------------------------------------------------------------------------------------------#








#-------------------------------------------------------------------------------------------#
# ---------------------- <<< 3. Array Shape and Reshape >>> ---------------------------------
# (1): np.reshape(): Reshapes an array without changing its data.
# (2): np.shape(): no of rows and no of columns
# (3): np.resize(): can change both the shape and size of an array by truncating or repeating elements as needed.
# (4): np.flatten()
# (5): np.ravel()

arr = np.array([[2,4,5,7,9]])
# arr1 = np.array([2,4,5,7,9,10,3,5])
# print(np.shape(arr)) #(1, 5) ; shows rows and col
# print(arr.ndim) #2 ; shows no of dimensions

# print(np.reshape(arr,(5,1)))           #[[2]
                                         # [4]
                                         # [5]
                                         # [7]
                                         # [9]]

# print(np.reshape(arr1,(2,2,2)))            #[[[ 2  4]
                                             # [ 5  7]]
                                             #
                                             # [[ 9 10]
                                             #  [ 3  5]]]

# print(np.reshape(arr1,(-1))) #[ 2  4  5  7  9 10  3  5]
# print(np.resize(arr , [2,6]))  # [[2 4 5 7 9 2]
                                 # [4 5 7 9 2 4]]



#--------------------------------------------------------------------------------------------#




#--------------------------------------------------------------------------------------------#
# ---------------------- <<< 4. Basic Statistical / Aggregating Functions >>> ------------------------------
# np.mean(): Calculates the mean of the elements.
# np.median(): Computes the median of the elements.
# np.std(): Computes the standard deviation.
# np.var(): Computes the variance.
# np.sum(): Sums the elements of an array.
# np.min(), np.max(): Finds the minimum and maximum values.
#np.argmax() , np.argmin() --> returns min index
# np.cumsum(): Returns the cumulative sum of elements.
# np.cumprod(): Returns the cumulative product of elements.
# np.corrcoef(): = +ve represents proportional relation ; -ve represents inversly relation ; 0 represents neutral relation

# arr1 = np.array([1, 2 , 3 , 4])
# price = np.array([300 , 100 , 350 , 150 , 200])
# sales = np.array([10, 20 , 7 , 17 , 3])

# print(np.sum(arr1))     #10
# print(np.min(arr1))     #1
# print(np.max(arr1))     #4
# print(np.size(arr1))    #4
# print(np.cumsum(arr1))  #[ 1  3  6 10]
# print(np.cumprod(arr1)) #[ 1  2  6 24]
# print(np.mean(arr1))    #2.5 ; sum of all val / total val
# print(np.median(arr1))  #2.5 ; after sorting middle val
# print(np.std(arr1))  #1.118033988749895 ; low standard deviation means values are close to mean val
# print(np.var(arr1))  #2.5 ; exponent of standard deviation
# print(stats.mode(arr1))  #2.5 ; most occurrence val
# print(np.corrcoef(price, sales))

# productPrice = np.array([1,2,3,4,5])
# quantity = np.array([2,1,3,2,2])
# totalProduct = np.cumprod([productPrice,quantity] , axis = 0)  #[[ 1  2  3  4  5]
#                                                                   #[ 2  2  9  8 10]]
# total = totalProduct[1].sum()
# print(total) #31

#--------------------------------------------------------------------------------------------#





#---------------------------------------------------------------------------------------------#
# ---------------------- <<< 5. Data Filtering and Conditional Selection >>> -----------------
# (1): np.where(): Returns the indices of elements that satisfy a given condition, or it can be used to apply conditional logic.

# arr = np.array([[2,4,5,7,9],[1,3,5,7,7],[32,4,1,6,5]])
# arr1 = np.array([[1, 2], [3, 4]])
# arr3 = np.array([10,20])
# filteredArray = [True , False]

# print(np.where(arr1%2==0)) #(array([0, 1]), array([1, 1]))

# print(arr3[filteredArray]) #[10]
# greaterThan10 = arr3 > 10
# print(arr3[greaterThan10]) #[20]
#--------------------------------------------------------------------------------------------------#






#--------------------------------------------------------------------------------------------------#
# ---------------------- <<< 6. Array Manipulation >>> ----------------------
# np.concatenate(): Joins arrays along an existing axis. axis = 0 (horizontally concatenate in the direction of vertical)
# np.vstack(), np.hstack(): Stack arrays vertically or horizontally.
# np.split(): Splits an array into multiple sub-arrays.
# np.delete(arr,[1]): Removes elements from an array.
# np.insert(arr,index,val): Inserts values into an array. if array in 2D its convert into 1D
# np.append(arr,val): append values into an array. if array in 2D its convert into 1D
# np.size(): no of elements in an array
# np.ndim(): dimension of an array
# np.array_split(nameOfArray , value)

# arr = np.array([[2,4,5,7,9],[1,3,5,7,7],[32,4,1,6,5]])
# arr1 = np.array([[1, 2], [3, 4]])
# arr2 = np.array([[5, 6], [7, 8]])
# arr3 = np.array([10,20])
# arr4 = np.array([1,2,3,4] , ndmin = 4) #[[[[1 2 3 4]]]]
# print(arr4)

# print(np.size(arr)) #15
# print(np.ndim(arr)) #2D
# print(np.concatenate((arr)))

# print(np.concatenate([arr1,arr2] , axis = 0)) # concatenate horizontal in the direction of vertical
# print(np.concatenate([arr1,arr2] , axis = 1)) # concatenate vertical in the direction of horizontal

# print(np.hstack([arr1,arr2])) # concatenate vertical in the direction of horizontal
# print(np.vstack([arr1,arr2])) # concatenate horizontal in the direction of vertical

# splitArr = np.array_split(arr1, 5)
# print(splitArr)

# print(np.append(arr1,[804,805])) # [  1   2   3   4 804 805]
# print(np.insert(arr1,1 , [804 , 805])) # [  1 804 805   2   3   4]
# print(np.insert(arr1,1 , 804 , axis = 0))          # [[  1   2]
                                                     #   [804 804]
                                                     #   [  3   4]]

# print(np.insert(arr1,1 , 804 , axis = 1)) # [[  1   804  2]
                                            # [  3   804 4]]

# print(np.delete(arr1,1)) # [[  1   804  2]
#--------------------------------------------------------------------------------------------------#






#--------------------------------------------------------------------------------------------------#
# ------------------------------ <<< 7. Sorting and Searching >>> ---------------------------------
# np.sort(): Sorts an array.
# np.searchsorted(): Finds indices where elements should be inserted to maintain order.

# arr1 = np.array([[1, 2], [3, 4]])
# arr3 = np.array([10,20])
# print(np.sort(arr1))
# x = np.searchsorted(arr3, [12 , 13]) #array must be in sorted, it returns index , array must be in 1D
# print(x)

#--------------------------------------------------------------------------------------------------#





#---------------------------------------------------------------------------------------------------#
# ---------------------- <<< 8.Mathematical/Arithmetic Operations >>> -----------------------------------------
# np.add(), np.subtract(), np.multiply(), np.divide(): Basic arithmetic operations.
# np.argmax() , np.argmin() , np.sin() , np.cos()
# np.dot(): Computes the dot product of two arrays (used in linear algebra).


# addition of numpy array:

# l1 = np.array([1,2,3])
# l2 = np.array([4,5,6])

# print("ORIGNAL L1 ARRAY: " , l1)
# print("ORIGNAL L2 ARRAY: " , l2)
# print("Addition of Numpy Array: " , l1+l2)
# print(np.add(l1,l2))




# addition of numpy Multidimensional array:
# l11 = np.array([[1,2,3],[4,5,6]])
# l22 = np.array([[4,5,6],[1,2,3]])

# print(np.add(l11,l22))    #[[5 7 9]
                            # [5 7 9]]



# Subtraction of numpy array:

# l1 = np.array([1,2,3])
# l2 = np.array([4,5,6])
# print("Subtraction of Numpy Array: " , l1-l2)
# print(np.subtract(l1,l2))

#Multiply of numpy array:

# l1 = np.array([1,2,3])
# l2 = np.array([4,5,6])
# print("Multiply of Numpy Array: " , l1*l2)
# print(np.multiply(l1,l2))

#Division of numpy array:

# l1 = np.array([1,2,3])
# l2 = np.array([4,5,6])
# print("Division of Numpy Array: " , l1//l2)
# print(np.divide(l1,l2))

#Exponent of numpy array:

# l1 = np.array([1,2,3])
# l2 = np.array([4,5,6])
# print("Exponent of Numpy Array: " , l1**l2)
# print(np.pow(l1,l2))

#Square Root of numpy array:

# l1 = np.array([1,2,3])
# l2 = np.array([4,5,6])
# print(np.sqrt(l1))


#----------------------------------------------------------------------------------------------------#




#----------------------------------------------------------------------------------------------------#
# ---------------------- <<< 9.Random Number Generation >>> -----------------------------------------
# (1): np.random.rand(): Generates random numbers between 0 & 1.
# (2): np.random.randn(): Generates random numbers very close to 0. return +ve or -ve no as well
# (3): np.random.randint(): return a random no between a given range
# (4): np.random.choice(): Randomly selects elements from an array.
# (5): np.random.ranf(): returns  random floats in the half-open intervals[0.0 , 1.0) ; 0 --> include
# (6): np.shuffle()
#(7): np.unique()
# arr = np.array([1,2,3,3,4,5,5])
# arrRand = np.random.rand(3)  #[0.43904435 0.95497486 0.17403811]
# arrRandn = np.random.randn(3)  #[-0.15503015 -2.14469184  0.48795248]
# arrRanf = np.random.ranf(3)  #[0.70230923 0.19820595 0.74421457]
# arrRandInt = np.random.randint(3 , 6 , 10)  #[3 3 5 5 4 3 3 4 3 4]
# print(arrRandInt)
# np.random.shuffle(arr)
# print(arr)
# print(np.unique(arr , return_index=True , return_counts=True)) #array([1, 2, 3, 4, 5]), array([0, 1, 2, 4, 5]), array([1, 1, 2, 1, 2])

#----------------------------------------------------------------------------------------------------#







#----------------------------------------------------------------------------------------------------#
# ---------------------- <<< 10.Broadcasting Numpy Array >>> -----------------------------------------
# 5 RULES:
# (1,3) , (4,3)
# (3,1) , (3,4)
# (1,3) , (3,1)
# (1,1) , (10,2)
# (5) , (2,5) ; same row and col


# arr1 = np.array([1,2,3,4])
# arr2 = np.array([5,6,7])
# print(np.add(arr1,arr2))  # BROADCASTING ERROR

# arr1 = np.arange(3).reshape(1,3)
# arr2 = np.arange(12).reshape(4,3)
# print(arr1+arr2)

# arr1 = np.arange(3).reshape(3,1)
# arr2 = np.arange(12).reshape(3,4)
# print(arr1+arr2)

# arr1 = np.arange(3).reshape(3,1)
# arr2 = np.arange(3).reshape(1,3)
# print(arr1+arr2)

# arr1 = np.arange(10).reshape(5,2)
# arr2 = np.arange(1).reshape(1,1)
# print(arr1+arr2)

# arr1 = np.arange(5)
# arr2 = np.arange(10).reshape(2,5)
# print(arr1+arr2)


# -------------------------------------------------------------------------------------------





# ---------------- <<< Common Use Cases for Data Analysis & Data Science >>> ----------------

# Data Wrangling:
# Use np.where(), np.concatenate(), np.unique(), and np.split() to clean and preprocess data.

# Statistical Analysis:
# Leverage np.mean(), np.median(), np.std(), np.percentile() for exploratory data analysis (EDA).

# Matrix Operations:
# Apply np.dot() for matrix multiplications, essential in machine learning models.

# Random Sampling:
# Utilize np.random.choice() and np.random.randn() to generate random samples for simulation and bootstrapping.

# Data Import/Export: Use np.loadtxt() and np.savetxt() to efficiently handle large datasets.





