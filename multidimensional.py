import numpy as np

# 1. One-dimensional array (1D)
# A 1D array contains a single row of elements.

arr=np.array([10,20,30,40])

print(arr)
print(arr.ndim)  #number of dimensions (1).
print(arr.shape)  #number of elements (4).

'''
Output:
[10 20 30 40]
1
(4,)
'''

# 2. Two-dimensional array (2D)
# A 2D array contains rows and columns, like a table.

array1=np.array([['D','E','F'],
                ['G','H','I']])

print(array1.ndim)
print(array1.shape)


# 3. Three-dimensional array (3D)
# A 3D array contains multiple 2D arrays, like layers of tables.
array=np.array([[
                ['A','B','C'],
                ['D','E','F'],
                ['G','H','I']],

                [['J','K','L'],
                 ['M','N','O'],
                 ['P','Q','R']],

                [['S','T','U'],
                 ['V','W','X'],
                 ['Y','Z',' ']]])

# print(array) ....print 3D Array
# print(array.ndim)
# print(array.shape)

# print(array[0][0][0])   ...//A    ....chain indexing
              
# print(array[0,0,2])   # zero layar  , zero row , zero  column   ..//C
# Multi-dimensional indexing is faster than chain indexing. 
 


'''
-array.ndim → tells you the number of dimensions. Here, it is 3.

-array.shape → tells you the size along each dimension: 3 layers, 3 rows, and 3 columns.


'''


word=array[1,1,0]+array[0,0,0]+array[1,2,2]+array[2,1,0]+array[0,1,1]+array[1,0,2]

# MARVEL
 
print(word)

# 4. Four-dimensional array (4D)
# A 4D array adds another level of nesting.
arr = np.array([[    
    [[1, 2], [3, 4]],  
    [[5, 6], [7, 8]]
    ]])
print(arr.ndim)
print(arr.shape)
print(arr[0, 0, 1, 0])

'''
Output:
4
(1, 2, 2, 2)
3
'''


