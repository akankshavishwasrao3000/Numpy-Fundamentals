import numpy as np

# Scalar arithmetic 

'''
1. What is a scalar?
- A scalar is a single value, such as 1, 2, 10, or 4.5.

EX: 
-array is [1, 2, 3].
-1 is the scalar (a single number).
-NumPy adds 1 to every element in the array.
'''

array= np.array([1,2,3])

print(array + 1)
print(array - 2)
print(array * 2)
print(array / 4)
print(array ** 4)
print(array // 2)
print(array % 4)

'''
[2 3 4]
[-1  0  1]
[2 4 6]
[0.25 0.5  0.75]
[ 1 16 81]
[0 1 1]
[1 2 3]

'''


# Vectorize math function 

'''
2. What is a vectorized operation?
-Vectorization means applying an operation to all elements of an array without writing an explicit Python loop.

For example:
array = np.array([1, 2, 3])

print(array * 2)
Output:
[2 4 6]


NumPy multiplies each element by 2 automatically. You don't need to write a for loop.

Compare the two approaches:
1.Without vectorization (using a loop)
result = []
for n in array:
    result.append(n * 2)

print(result)
# ....You write the loop yourself.

2. With vectorization (using NumPy)
result = array * 2
print(result)
# ....NumPy applies the multiplication to every element.

'''

array1=np.array([1.20, 2.30, 3.40])

print(np.sqrt(array1))  # square root

print(np.round(array1))  #round to nearest integer

print(np.floor(array1))  #round down to nearest integer

print(np.pi)  #3.141592653589793 it is pi value

print(np.exp(array1))  #exponential of all elements in the input array means e raised to the power of array1



# Exercise: #area of circle = pi * r^2

radii=np.array([1, 2, 3, 4, 5])

print(np.pi * radii **  2) 



# 3. Element-wise arithmetic 

'''
-Two arrays, with an operation performed on corresponding elements.

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)
Output: [5 7 9]
'''

array3=np.array([1,2,3])
array4=np.array([4,5,6])

print(array3 + array4)
print(array3 - array4)
print(array3 * array4)
print(array3 // array4)
print(array3 ** array4)
print(array3 % array4)

'''
[5 7 9]
[-3 -3 -3]
[ 4 10 18]
[0 0 0]
[  1  32 729]
[1 2 3]
'''

# 4.Comparison operators

'''
comparison operators compare array elements with a value or with another array and return True or False.

ex:
scores = np.array([91, 45, 50, 84, 100])
print(scores > 50)
'''

scores=np.array([91,40,50,84,100,35,100,75,100])

print(scores == 100)
# OutPut
# [False False False False  True False  True False  True]

print(scores >=60)
# [ True False False  True  True False  True  True  True]

scores[scores < 50]=0
print(scores)
# OUTPUT
# [ 91   0  50  84 100   0 100  75 100]
'''
“Boolean indexing in NumPy lets us select array elements using a condition. We can use it to filter values or modify specific elements without writing a loop.”

-How does this connect to Boolean indexing?
-You can use the comparison result to select or modify values.
-scores[scores < 50] = print(scores)

Output:
[91  0 50]

'''

'''
What does scores[scores < 50] mean?
Look at the two parts:
- scores < 50 → finds which scores are below 50.
- scores[...] → selects the scores at the positions where the condition is True.

'''

