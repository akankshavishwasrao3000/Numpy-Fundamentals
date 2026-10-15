import numpy as np


# Aggregation function  : summarizes the data and  
#                       typically returns a single value.

'''
-An aggregation function in NumPy is a function that summarizes data by calculating a result, such as the total, average, minimum, or maximum.
-Why do we use it?
We use aggregation functions to understand data quickly without calculating each value manually.

''' 

array=np.array([[1,2,3,4,5],
                [6,7,8,9,10]])

print(np.sum(array))   #55
print(np.mean(array))  #5.5
print(np.std(array))   #2.8722813232690143
print(np.var(array))   #8.25
print(np.min(array))   # 1 ...min value in array
print(np.max(array))   # 10 ...Max value in array
print(np.argmin(array))    # 0  ...index of min value in array
print(np.argmax(array))   # 9   ...Index of max value in array

print(np.sum(array, axis=0))
# axis=0 means column wise operation
# OutPut
# [ 7  9 11 13 15]

print(np.sum(array,axis=1))
# axis=1 means row wise operation
# OutPut
# [15 40]


'''
-What does axis mean?
Using your array:
array = np.array([[1, 2, 3],      
                 [4, 5, 6]])
---------------------------------
axis=0

Column-wise operation
Adds vertically: 1+4, 2+5, 3+6
Result: [5, 7, 9]
---------------------------------
axis=1

Row-wise operation
Adds horizontally: 1+2+3 and 4+5+6
Result: [6, 15]
-----------------------------

Simple answer: 
“Aggregation functions in NumPy are used to summarize array data. For example, sum() calculates the total, mean() calculates the average, and min() and max() find the smallest and largest values. We can also use the axis parameter to perform calculations row-wise or column-wise.”
'''

