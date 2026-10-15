import numpy as np

array=np.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12],
                [15,16,17,18]])

# array[start:end:step]
# print(array[1:4:2])  
# print(array[::-1])   ...reverse step one by one

print(array[:,1]) 
# output...
# [ 2  6 10 16]

print(array[:, 0:3])
# OutPut

'''
[[ 1  2  3]
 [ 5  6  7]
 [ 9 10 11]
 [15 16 17]]
 ...first three column

'''

print(array[:, ::-1])
# OutPut

'''
[[ 4  3  2  1]
 [ 8  7  6  5]
 [12 11 10  9]
 [18 17 16 15]]

...reverse column


'''

print(array[0:2 , 0:2])
# OutPut
'''
[[1 2]
[5 6]]

 ...IMP...  
....Two columns of the first two rows 
'''

print(array[0:2,2:4])  
# OutPut
'''
[[3 4]
 [7 8]]
 First two rows  0:2  ...column 2:4

'''

print(array[2:4, 0:2])
# OutPut

'''
[[ 9 10]
 [15 16]]

 second rows 2:4 /2: and column in that row 0:2
'''

print(array[2:, 2:])
# OutPut

'''
[[11 12]
 [17 18]]
 second rows 2:4 /2: and column in that row 2: / 2:4
'''


