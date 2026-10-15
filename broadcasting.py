import numpy as np 

# Broadcasting along NumPy to perform operations on arrays 
# With different shapes by virtually expanding dimensions 
# So they match the larger array shape. 

# The dimensions have the same size. 
# OR
# One of the dimensions has a size of 1. 


a=np.array([10,20,30])
b=5

print(a+b)
# Output:
# [15 25 35]

# This is an example of NumPy broadcasting with 2D arrays.

array1=np.array([[1,2,3,4]])
array2=np.array([[1],
                 [2],
                 [3],
                 [4]])

print(array1.shape) #(1, 4)...1 row , 4 column
print(array2.shape)  #(4, 1) ...4 row , 1 column

print(array1 * array2)
# OutPut:
'''
[[ 1  2  3  4]
 [ 2  4  6  8]
 [ 3  6  9 12]
 [ 4  8 12 16]]

 NumPy virtually repeats the rows of array1 and the columns of array2 to make both shapes (4, 4).

'''


# ERROR
'''
1. Example: No error ✅
Shapes: (2, 1) and (4, 1)
Actually, these shapes cause an error because the first dimensions are 2 and 4, which are different, and neither is 1.

'''
a1=np.array([[1],
              [2]])   #(2,1)

b1=np.array([[1],
             [2],
             [3],
             [4]])    #(4,1)

# print(a1*b1)  #ValueError

# Output: ValueError: operands could not be broadcast together with shapes (2,1) (4,1)



a2=np.array([[1,2,3,4,5,6,7,8,9,10]])
b2=np.array([[1],
             [2],
             [3],
             [4],
             [5],
             [6],
             [7],
             [8],
             [9],
             [10]])

print(a2.shape)
print(b2.shape)

print(a2*b2)
# OutPut
'''
(1, 10)
(10, 1)

[[  1   2   3   4   5   6   7   8   9  10]
 [  2   4   6   8  10  12  14  16  18  20]
 [  3   6   9  12  15  18  21  24  27  30]
 [  4   8  12  16  20  24  28  32  36  40]
 [  5  10  15  20  25  30  35  40  45  50]
 [  6  12  18  24  30  36  42  48  54  60]
 [  7  14  21  28  35  42  49  56  63  70]
 [  8  16  24  32  40  48  56  64  72  80]
 [  9  18  27  36  45  54  63  72  81  90]
 [ 10  20  30  40  50  60  70  80  90 100]]

'''


arra=np.array([[
                ['A','B','C'],
                ['D','E','F'],
                ['G','H','I']],

                [['J','K','L'],
                 ['M','N','O'],
                 ['P','Q','R']],

                [['S','T','U'],
                 ['V','W','X'],
                 ['Y','Z',' ']]])


print(arra)