# *************<<< PART-01 >>>*************

# **WRITE A PROGRAM TO CHECK WEATHER A GIVEN NUMBER IS POSITIVE OR NOT.

# number = int(input("ENTER ANY NUMBER:"))
# print("NUMBER IS NEGATIVE: ") if number<0 else print("NUMBER IS POSITIVE: ")

# **WRITE A PROGRAM TO CHECK WEATHERA GIVEN NUMBER IS EVEN OR ODD.

# number = int(input("ENTER ANY NUMBER:"))
# if number % 2 == 0:
#     print("GIVEN NUMBER IS EVEN: ")
# else:
#     print("GIVEN NUMBER IS ODD: ")

# **WRITE A PROGRAM TO CREATE AN AREA OF CALCULATOR.
# print("<<< AREA CALCULATOR >>>")
# print("PRESS --> 1: TO CALCULATE THE AREA OF SQUARE: ")    # a2 = length of side.
# print("PRESS --> 2: TO CALCULATE THE AREA OF RECTENGLE: ") # l × h
# print("PRESS --> 3: TO CALCULATE THE AREA OF CIRCLE: ")    # π × r2 = radius.
# print("PRESS --> 4: TO CALCULATE THE AREA OF TRIANGLE: ")  # ½ × b × h

# choice = int(input("CHOOSE NUMBER: "))

# if choice == 1:
#     len = float(input("ENTER LENGTH OF SQUARE: "))
#     area = len**2
#     print("AREA OF SQUARE IS: " , area)

# elif choice == 2:
#     len = float(input("ENTER LENGTH OF RECTENGLE: "))
#     height = float(input("ENTER HEIGHT OF RECTENGLE: "))
#     area = len*height
#     print("AREA OF RECTENGLE IS: " , area)

# elif choice == 3:
#     radius = float(input("ENTER RADIUS OF CIRCLE: "))
#     pi = 3.14
#     area = pi * (radius**2)
#     print("AREA OF CIRCLE IS: " , area)

# elif choice == 4:
#     base = float(input("ENTER BASE OF TRIANGLE: "))
#     height = float(input("ENTER HEIGHT OF TRIANGLE: "))
#     area = (0.5*(base*height))
#     print("AREA OF TRIANGLE IS: " , area)
# else:
#     print("INCORRECT CHOICE!..")


# **WRITE A PROGRAM TO CHECK PASSED LETTER IS VOWEL OR NOT
# letter = input("ENTER ANY LETTER: ")
# if letter in "aeiou" or letter in "AEIOU":
#     print("LETTER IS VOWEL: ")
# else:
#     print("LETTER IS NOT VOWEL: ")

# WRITE A PROGRAM TO CHECK IF A NUMBER IS A SINGLE DIGIT NUMBER , 2 DIGIT NUMBER UPTO 5 DIGIT NUMBER:

# num = int(input("ENTER ANY NUMBER: "))

# if num >=0 and num <=9: print(num , " -->" , "single digit number")
# elif num >=10 and num <=99: print(num , " -->" , "double digit number")
# elif num >=100 and num <=999: print(num , " -->" , "triple digit number")
# elif num >=1000 and num <=9999: print(num , " -->" , "fourth digit number")
# elif num >=10000 and num <=99999: print(num , " -->" , "fifth digit number")
# else: print("RANGE IS EXCEED!..")


# *************<<< PART-02 >>>*************
# LOOPS , STRINGS AND LISTS

# LOOPS
# 2 types of loops : (for loop : while loop)
# (1) for loop , (2) while loop , (3) while true loop , (4) nested loop

# for i in range (1,6):
#     print(i)

# for i in range (1,6,2): # for odd number
#     print(i)

# for i in range (0,6,2): # for even number
#     print(i)

# num = 1
# while num < 6:
#     print(num)
#     num+=1

# ********* <<< PROBLEM SOLVING IN FOR LOOP ********* >>>

# *** (1) MULTIPLICATION TABLE:

# num = int(input("ENETR NUMBER HERE: "))

# for i in range(1,11):
#     print(num , "X" , i , "=" , (num*i))

# *** (2)WRITE A PROGRAM TO FIND THE SUM OF ALL THE EVEN NUMBERS UPTO 50
# sum = 0
# for i in range(1,51):
#     if i % 2 == 0:
#         sum+=i
# print("SUM OF ALL EVEN NUMBERS UPTO 50: ",sum)

# ***(3)WRITE A PROGRAM TO WRITE FIRST 20 NUMBERS AND THEIR SQUARED NUMBERS

# for i in range(1,21):
#     print(i , "-->" , (i**2))

# ***(4) WRITE A PROGRAM TO CHECK IF A NUMBER IS DIVISIBLE BY 8 AND 12, UPTO 100 NUMBERS

# for i in range(1,101):
#     if i%8 == 0 and i%12 == 0:
#         print("COMMAN MULTIPLES OF 8 AND 12 ARE: " , i)


# ***(5)  1
#        1 2
#        1 2 3
#        1 2 3 4
#        1 2 3 4 5

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j , end = " ")
#     print()


# ***(6) 1
#        2 2
#        3 3 3
#        4 4 4 4
#        5 5 5 5 5

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i , end = " ")
#     print()

# ***(7) 1 1 1 1 1
#        2 2 2 2
#        3 3 3
#        4 4
#        5

# for i in range(1,6):
#     for j in range(6,i ,-1):  # 5 > 1
#         print(i , end = " ")
#     print()

# ***(7)   *
#        * *
#      * * *
#    * * * *
#  * * * * *

# for i in range(1,6):
#     for j in range(5,i ,-1):  # 5 > 1
#         print(" " , end = " ")

#     for k in range(i):
#         print("*" , end = " ")
#     print()


# ***(7)   1
#          2 1
#          3 2 1
#          4 3 2 1
#          5 4 3 2 1

# for i in range(1,6):
#     for j in range(i , 0 , -1):
#         print(j , end = " ")
#     print()

# ***(8)   *
#          * *
#          * * *
#          * * * *
#          * * * * *
#          * * * *
#          * * *
#          * *
#          *

# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*" , end = " ")
#     print()

# for k in range(1,5):
#     for l in range(5,k,-1):
#         print("*" , end = " ")
#     print()

# 1
# 2 4
# 3 6 9
# 4 8 12 16
# 5 10 15 20 25
# 6 12 18 24 30 36
# 7 14 21 28 35 42 49
# 8 16 24 32 40 48 56 64

# for i in range(1,9):
#     for j in range(1,i+1):
#         print(i*j , end = " ")
#     print()

# *** (9) WRITE A PROGRAM TO GET FABONACCI SERIES UPTO 10 NUMBERS:
# FABONACCI SERIES: # 0 , 1 , 1 , 2 , 3 , 5 , 8 , 13 , 21 , 34
# a , b
# 1 , 1
# a = 0
# b = 1
# for i in range(2,11):
#     print("Value of a & b: " , a , b)
#     result = a+b
#     a = b
#     b = result
#     print("Result: " , result)

# prime number program upto 100:
# num = int(input("ENTER NUMBER HERE: "))
# if num > 1:
#     for i in range(2,num+1):
#         if num%i == 0:
#             print(num , ": not prime number")
#             break
#         else:
#             print(num , ": prime number ")
#             break

# PALINDROME WITH NUMBERS

# number = int(input("ENTER NUMBER HERE: "))
# temp = number
# rev = 0

# while number > 0:
#     lastDigit = number%10
#     rev = rev*10+lastDigit
#     number = number//10


# if temp == rev:
#     print("YES! IT'S AN PALINDROME")
# else:
#     print("PONKA!..")


# ********* <<< PROBLEM SOLVING IN WHILE LOOP ********* >>>
# *** (1) MULTIPLICATION TABLE:

# num = int(input("ENTER NUMBER HERE:"))
# range = 1
# while range < 11 :
#     print(num , "X" , range , "=" , (num*range))
#     range+=1


# ***(2) WRITE A PROGRAM TO FIND SUM OF FIRST 10 ODD NUMBERS USING WHILE LOOP

# sum = 0
# range = 0
# while range < 20:
#     if range % 2 != 0:
#         sum+=range
#     range+=1
# print("SUM OF ALL ODD NUMBERS UPTO 10: " , sum)

# ********* <<< PROBLEM SOLVING IN WHILE TRUE ********* >>> # while true is infinite loop
# result = 0
# while True:
#     num1 = int(input("ENTER NUMBER 1: "))
#     num2 = int(input("ENTER NUMBER 2: "))
#     result = result + (num1 + num2)
#     print("RESULT OF PREVIOUS ADDED NUMBER: " , result)

#     choice = input("DO YOU WANT TO ADD MORE NUMBERS? YES ? NO ____")
#     if choice == "NO":
#         print("FINAL RESULT: " , result)
#         break

# ***(2) WRITE A PROGRAM TO CREATE A BILLING SYSTEM AT SUPER MARKET:
# finalTotal = 0
# while True:
#     customerName = input("ENTER CUSTOMER NAME: ")
#     total = 0

#     while True:
#         productQuantity = int(input("Enter Product Quantity: "))
#         productPrice = int(input("Enter Product Price: "))
#         result = productQuantity*productPrice
#         total = total+result
#         finalTotal = finalTotal+total
#         choice = input("DOU YOU WANT TO CONTINUE SHOPPING? YES/NO: ---> ")
#         if choice.upper() == "NO":
#             break

#     print("YOUR NAME: " , customerName)
#     print("TOTAL: " , total)
#     choice = input("DOU YOU WANT BACK AT MENU? YES/NO: ---> ")
#     if choice.upper() == "NO":
#         break

# print("FINAL TOTAL: " , finalTotal)


# ***************** <<< STRING >>> *****************
# FUNCTIONS
# length , count , upper , lower , index , capitalize , casefold , find , format , center ,
# isalnum , isalpha , isdecimal , isdigit , isnumeric , islower , issupper , isspace , istitle,
# endswith() , startswith() , swapcase() , strip() -> remove space , split() , ljust() , rjust() , replace() ,
# rindex() , rfind() ,
# *** WRITE A PROGRAM TO FIND THE LENGTH OF THE FOLLOWING STRING

# myString = "HELLO, I'm Muhammad Sufyan. from SSUET."
# print(len(myString))

# *** WRITE A PROGRAM TO CHECK HOW MANY TIMES  ALPHABET 'O' IS OCCURING

# myString = "HELLO, I'm Muhammad Sufyan. from SSUET."
# print(myString.lower().count("o"))

# *** WRITE A PROGRAM TO CONVERT THE FOLLOWING STRING INTO TITLE:

# myString = "HELLO, I'm Muhammad Sufyan. from SSUET."
# print(myString.title())

# *** WRITE A PROGRAM TO CONVERT THE FOLLOWING STRING INTO CAPITALIZED:
# myString = "HELLO, I'm Muhammad Sufyan. from SSUET."
# print(myString.capitalize())

# *** WRITE A PROGAM TO FIND THE INDEX NUMBER OF Muhammad Sufyan
# myString = "HELLO, I'm Muhammad Sufyan. from SSUET."
# print(myString.index("Muhammad Sufyan"))

# *** WRITE A PROGAM TO FIND THE INDEX NUMBER OF Muhammad Sufyan
# myString = "HELLO, I'm Muhammad Sufyan. from SSUET."
# print(myString.find("Muhammad Sufyan"))

# *** WRITE A PROGAM TO INJECT VARIABLES IN STRING
# age = 19
# institute = "saylani"
# myString = f"HELLO, I'm Muhammad Sufyan. from SSUET. I'm {age} Years Old.Currently studies in {institute}"
# print(myString)

# *** WRITE A PROGAM TO CENTER STRING

# myString = "Harry"
# print(myString.center(20 , "*"))

# *** WRITE A PROGRAM TO SEPARATE THE FOLLOWING STRING INTO COMMA SEPARATED VALUES
# a = "OOTD.YOLO.ASAP.BRB.GTG.OTW"
# print(a.split("."))

# *** WRITE A PROGRAM TO SORT STRINGS ALPHABETICALLY IN PYTHON
# a = "HELLO"
# print(sorted(a))

# *** WRITE A PROGRAM TO remove a given character from a string
# myString = "hello"
# removeCharacter = input("ENTER THE CHARACTER YOU WANT TO REMOVE? ---")
# print(myString.replace(removeCharacter , ""))

# *** WRITE A PROGRAM TO remove a > sign from a following string
# myString = "F>R>I>E>N>D"
# print(myString.replace(">" , ""))

# *** TAKE AN INPUT FROM USER AS A STRING THEN , REVERSE IT
# userInput = input("ENTER ANYTHIN: ")
# print(userInput[::-1])

# *** WRITE A PROGRAM TO CHECK IF A STRING CONTAINS ONLY DIGITS
# myString = "HARRY"
# print(myString.isdigit())

# *** WRITE A PROGRAM TO CHECK IF A STRING IS PALINDROME OR NOT
# myString = "WOW"
# reverse = myString[::-1]

# if myString == reverse:
#     print(myString , "is palindrome")
# else:
#     print(myString , "it's not an palindrome")


# *** WRITE A PROGRAM TO FIND THE VOWELS ARE EXIST IN STRING

# myString = "HRRY"
# vowels = "AEIOU"

# if any(char in vowels for char in myString):
#     print("VOWELS EXIST: ")
# else:
#     print("VOWELS DOES'T EXIST: ")

# *** WRITE A PROGRAM TO FIND THE NUMBER OF VOWELS IN STRING
# myString = input("ENTER ANYTHING HERE: ")
# vowels = 0

# for i in myString.lower():
#     if i == "a" or i == "e"or i == "i" or i == "o" or i == "u":
#         vowels+=1
# print("NUMBER OF VOWELS ARE PRESENT HERE: " , vowels)

# *** WRITE A PROGRAM TO CHECK IF EVERY WORD IN A STRING BEGINS WITH A CAPITAL LETTER

# mySting = "Hello , My Name is muhammad sufyan."
# print(mySting.istitle())


# ********************* <<< SLICING IN STRING >>> *********************

# myString = "Harry Potter"
# print(myString[0:5]) # output Harry

# myString = "Harry Potter" # output Harry
# print(myString[:5])

# myString = "Harry Potter" # output Harry Potter
# print(myString[::])

# myString = "Harry Potter" # reverse of string
# print(myString[::-1])

# myString = "0123456789" # output: 987
# print(myString[-1:-4:-1])


# ************** <<< LIST >>> **************
# COLLECTION OF OREDERD AND MUTABLE DATA

# list = ["apple" , "mango" , "banana" , 100 , 12.092 , 'T']
# print(list)


# ****************** <<< LIST ITERATION >>> ******************

# (1) using for loop
# (2) using for loop with range and length function
# (3) using while loop
# (4) using short hand for loop

# (1)using for loop
# myList = ["apple" , "mango" , "banana"]
# for i in myList:
#     print(i)

# (2) using for loop with range and length function
# myList = ["apple" , "mango" , "banana"]
# for i in range(len(myList)):
#     print(myList[i])

# (3) using while loop
# myList = ["apple" , "mango" , "banana"]
# i = 0
# while i<len(myList):
#     print(myList[i])
#     i+=1

# (4) using short hand for loop
# myList = ["apple" , "mango" , "banana"]
# [print(i) for i in myList]

# ****************** <<< LIST FUNCTIONS >>> ******************
# length , count , append --> add last index , insert , remove --> if val is duplicated in list so remove first val of duplication , pop --> only index val provide
# copy ,  index --> found an index val , extend --> extend list or you can say merge more thann one list , reverse ,
# sort , clear

# ****************** <<< LIST COMPREHENSIONS >>> ******************

# l1 = [1,2,3,4,5]
# l2 = []
# for i in l1:
#     if i>3:
#         l2.append(i)
# print(l2)

# INTEAD OF ABOVE WE USED LIST COMPREHENSION

# l1 = [1,2,3,4,5]
# l2 = [i for i in l1 if i>3]
# print(l2)

# WRITE A PROGRAM TO SWAP FISRT AND FOURTH VALUE
# l1 = ["karachi" , "lahore" , "islamabad" , "queeta" , "peshawar"]
# for i in l1:
#     print(i)
# print("\n\nAFTER SWAPING: ")

# l1[1] , l1[4] = l1[4] , l1[1]
# for i in l1:
#     print(i)

# WRITE A PROGRAM TO ADD A NEW VALUE AT SECOND POSITION
# l1 = ["karachi","lahore","islamabad","queeta","peshawar"]
# l1.insert(1,"liyari")
# print(l1)

# WRITE A PROGRAM TO DELETE VALUE AT SECOND POSITION
# l1 = ["karachi","lahore","islamabad","queeta","peshawar"]
# l1.pop(1)
# print(l1)

# WRITE A PROGRAM TO MULTIPLY ALL NUMBERS IN THE LIST
# l1 = [2,4,6,8]
# result = 1
# for i in l1:
#     result*=i
# print(result)

# WRITE A PROGRAM TO GET THE LARGEST NUMBER IN THE LIST
# l1 = [20,400,6,8]
# l1.sort()
# print("LARGEST NUMBER IN THE LIST: " , l1[-1])


# WRITE A PROGRAM TO GET THE SMALLEST NUMBER IN THE LIST
# l1 = [20,400,6,8]
# l1.sort()
# print("SMALLEST NUMBER IN THE LIST: " , l1[0])

# ************************* <<< TUPLES >>> *************************
# (1) ordered and unmutable data
# (2) once created tuples can't be changed
# (3) no need brackets if want simple brackets used

# myTuples = "mango","banana" , 123
# print(type(myTuples))
# print(myTuples[0])

# ************************* <<< ITERATION >>> *************************

# myTuples = "mango","banana" , 123

# (1)
# for i in myTuples:
#     print(i)

# (2)
# for i in range(len(myTuples)):
#     print(myTuples[i])

# (3)
# i=0
# while i < len(myTuples):
#     print(myTuples[i])
#     i+=1

# ************************* <<< SLICING >>> *************************


# myTuples = "mango","banana" , "grapes" , "apple" , "pinapple"
# print(myTuples[0:3])   #('mango', 'banana', 'grapes')
# print(myTuples[1:4])   #('banana', 'grapes', 'apple')
# print(myTuples[::])    #print(myTuples[1:4])   #('banana', 'grapes', 'apple')
# print(myTuples[::-1])  #('pinapple', 'apple', 'grapes', 'banana', 'mango')

# print(myTuples.count("banana"))
# myTuples = "mango","banana" , "grapes" , "apple" , "pinapple" , "banana"

# CONVERSION OF TUPLES INTO LIST
# convertedTuple = list(myTuples)
# print(type(convertedTuple))
# print(type(myTuples))

# FUNCTIONS IN TUPLES
# print(myTuples.index("banana"))
# print(myTuples.count("banana"))

# ************************* <<< DICTIONARY >>> *************************
# (1) : DICTINARY ALLOW USERS TO WRITE DATA IN THE FORM OF KEYS AND VALUES KEYS MUST BE IN STRING FORMAT

# studentData = {"name" : "M.Sufyan" , "class" : "9th" , "fees" : "Clear"}
# print(studentData["name"])
# print(studentData["class"])
# print(studentData["fees"])

# ************************* <<< ITERATION IN DICTIONARY >>> *************************

# studentData = {"name" : "M.Sufyan" , "class" : "9th" , "fees" : "Clear"}
# for i in studentData:
#     print(studentData[i])

# studentData = {"name" : "M.Sufyan" , "class" : "9th" , "fees" : "Clear"}
# for i in studentData.values():
#     print(i)

# studentData = {"name" : "M.Sufyan" , "class" : "9th" , "fees" : "Clear"}
# for i , j in studentData.items():
#     print(i ,":", j)

# ************************* <<< DICTIONARY'S FUNCTION >>> *************************
# get , items , keys , values , copy
# setdefault , update , pop , popitem , clear

# studentData = {"name" : "M.Sufyan" , "class" : "9th" , "fees" : "Clear"}

# getName = studentData.get("name")
# print(getName)

# allDataInFormOfTuples = studentData.items()
# print(allDataInFormOfTuples)

# getKeys = studentData.keys()
# print(getKeys)

# getValues = studentData.values()
# print(getValues)

# dictionaryCopy = studentData.copy()
# print(dictionaryCopy)


# ************************* <<< NESTED DICTIONARY >>> *************************

# studentData = {"1":{"name" : "M.Sufyan" , "class" : "9th" , "fees" : "Clear"},
#                "2":{"name" : "M.Riyan" , "class" : "10th" , "fees" : "Clear"},
#                "3":{"name" : "M.Kamran" , "class" : "8th" , "fees" : "Not Clear"},
#                "4":{"name" : "M.Arham" , "class" : "7th" , "fees" : "Clear"},
#                "5":{"name" : "M.Furqan" , "class" : "6th" , "fees" : "Clear"}
#                }

# print(studentData[3]["name"])

# for stdId , stdInfo in studentData.items():
#     print(f"STUDENT ID: {stdId}")

#     for key , val in stdInfo.items():
#         print(key.capitalize() , ":" , val.capitalize())

#     print()

# ************************* <<< PROBLEM SOLVING >>> *************************

# ***(1) WRITE A PROGRAM TO SORT A DICTIONARY BY VALUE

# stdMarks = {"std1":100 , "std2":40 , "std3":80 , "std4":90 , "std5":60}
# sortedMarks = sorted(stdMarks.values())
# print(sortedMarks)


# ***(2) WRITE A PYTHON SCRIPT TO PRINT A DICTIONARY WHERE THE KEYS ARE
# NUMBERS BETWEEN 1 AND 15 AND THE VALUES ARE SQUARED OF KEYS

# dic = {}
# for i in range(1,16):
#     dic[i] = i**2
# print(dic)

# ***(3) WRITE A PYTHON PROGRAM TO MULTIPLY ALL THE ITEMS IN DICTIONARY
# total = 1
# stdMarks = {"std1":100 , "std2":40 , "std3":80 , "std4":90 , "std5":60}
# for i in stdMarks.values():
#     total*=i
# print(total)

# ***(4) WRITE A PYTHON PROGRAM TO SORT A DICTIONARY BY KEY

# stdMarks = {1:100 , 3:40 , 2:80 , 5:90 , 4:60}
# a = sorted(stdMarks.keys())
# print(a)

# ************************* <<< SETS >>> *************************

# (1) unique , mutable and unordered data

# mySet = {1,2,3,5.6,5}
# print(mySet)

# ************************* <<< ITERATION >>> *************************
# mySet = {1,2,3,5.6,5}
# for i in mySet:
#     print(i)

# ************************* <<< FUNCTION IN SETS >>> *************************
# add , max , min , pop --> remove random value , remove --> remove value you want , discard --> remove value you want , copy
# isdisjoint , issubset , issuperset , update --> union and its changed values in orignal set , clear --> clear orignal values in set
# union --> do not modify the orignal set , difference , difference update , intersection , intersection update , symmetric difference , symmetric difference update
# a = {"karachi" , "lahore" , "islamabad" , "multan" , "peshawar"}
# b = {"murre" , "lyari" , "newkarachi"}
# c = {"karachi","lahore"}

# print(a.isdisjoint(b)) # a ke saare elements b me mojood nahi hain
# print(c.issubset(a)) # c ke saare elements a me mojood hain
# print(a.issuperset(c)) # a ke kuxh elements c me mojood hain
# a.update(c)  # a union c
# a.clear() # clear orignal values in set


# union = a.union(c)
# print(union)

# diff = a.difference(c)  # do not modify the orignal set
# print(diff)


# a.difference_update(c)   # modify the orignal set
# print(a)

# intersect = a.intersection(c)   # do not modify the orignal set
# print(intersect)

# a.intersection_update(c)   # modify the orignal set
# print(a)

# symmetricDifference = a.symmetric_difference(c)   # do not modify the orignal set. eliminate the common element
# print(symmetricDifference)

# symmetricDifference = a.symmetric_difference_update(c)   # modify the orignal set. eliminate the common element
# print(symmetricDifference)


# ************************* <<< PROBLEM SOLVING >>> *************************
# (1) WRITE A PROGRAM TO FIND MAX AND MIN IN A SET
# mySet = {1,4,2,54,3,54}
# print(max(mySet))
# print(min(mySet))

# (2) WRITE A PROGRAM TO FIND A COMMON ELEMENTS IN THREE LIST USING SETS

# set1 = [1,3,5,7,9]
# set2 = [7,9]
# set3 = [1,2,3,4,5,6,7,8,9]
# print(set(set1) & set(set2) & set(set3))

# convertedset1 = set(set1)
# convertedset2 = set(set2)
# convertedset3 = set(set3)
# print(convertedset1.intersection(convertedset2).intersection(convertedset3))

# (3) WRITE A PROGRAM TO FIND A DIFFERENCE BETWEEN TWO SETS

# set1 = {1,3,5,7,9}
# set2 = {7,9}
# print(set1.difference(set2))


# (4) WRITE A PROGRAM TO CHECK IF A SET IS A SUBSET OF ANOTHER SET

# set1 = {1,3,5,7,9}
# set2 = {7,9}
# print(set1.issubset(set2))

# ************************* <<< FUNCTIONS >>> *************************
# def myFun():
#     print("HELLO WORLD!..")
# myFun()

# ************************* <<< PARAMETERS AND ARGUMENTS >>> *************************
# def myFun(x,y): # parameters
#     print(f"ADDING TWO NUMBERS: {x+y}")
# myFun(2,3) # arguments

# ************************* <<< DEFAULT PARAMETER >>> *************************
# def myFun(x = 2 , y = 3): # default parameters
#     print(f"ADDING TWO NUMBERS: {x+y}")
# myFun(17)

# ************************* <<<RETURN FUNCTION >>> *************************
# def add(x,y):
#         return x+y
# def subtract(x,y):
#         return x-y
# def multiply(x,y):
#         return x*y
# def divide(x,y):
#         return x//y

# def menu():
#     print("PRESS 1 TO ADD")
#     print("PRESS 2 TO SUBTRACT")
#     print("PRESS 3 TO MULTIPLY")
#     print("PRESS 4 TO DIVIDE")

#     choice = int(input("SELECT CHOICE: "))

#     if choice == 1:
#         num1 = int(input("NUMBER 1: "))
#         num2 = int(input("NUMBER 2: "))
#         result = add(num1 , num2)
#     elif choice == 2:

#         num1 = int(input("NUMBER 1: "))
#         num2 = int(input("NUMBER 2: "))
#         result = subtract(num1 , num2)
#     elif choice == 3:

#         num1 = int(input("NUMBER 1: "))
#         num2 = int(input("NUMBER 2: "))
#         result = multiply(num1 , num2)
#     elif choice == 4:

#         num1 = int(input("NUMBER 1: "))
#         num2 = int(input("NUMBER 2: "))
#         result = divide(num1 , num2)

#     print(f"RESULT: {result}\n\n")
#     isContinue = input("DOU YOU WANT TO CONTINUE? Y/N:  \n\n")
#     if isContinue.capitalize() == 'Y':
#         while True:
#             menu()

# menu()


# ************************* <<<RECURSION >>> *************************

# def hello():
#     print("world!..")
#     return hello()
# print(hello())

# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return (n*fact(n-1)) # 5! = 5 * 4 * 3 * 2 * 1 OR 5 * 4! (BOTH HAVE SAME MEANING)
# print(fact(5))

# ************************* <<<LAMBDA >>> *************************
# memory me function nhi hota temporarily function hota hai
# (1) ANONYMOUS FUNCTION
# (2) USED FOR SHORT PERIOD OF TIME
# (3) IT TAKES NUMERIC ARGUMENT
# (4) IT CAN HAVE ONE EXPRESSION

# a = lambda b:b*5
# print(a(5))

# a = lambda b,c,d : b+c+d
# print(a(5,5,5))

# ************************* <<<LOCAL AND GLOBAL VARIABLES >>> *************************
# x = 24
# print(x)
# def hello():
#     x = 25
#     return x
# print(hello())
# print(x)

# x = 24
# print(x)
# def hello():
#     global x
#     x = 25
#     print(x)
# hello()
# print(x)

# ************************* <<<PROBLEM SOLVING >>> *************************

# (1) WRITE A FUNCTION TO FIND MAX OF THREE NO IN PYTHON
# def findMax(x,y,z):
#     if x > y and x > z:
#         print(x , "is maximum")

#     elif y > x and y > z:
#         print(y , "is maximum")

#     else:
#         print(z , "is maximum")

# findMax(1,3,5)


