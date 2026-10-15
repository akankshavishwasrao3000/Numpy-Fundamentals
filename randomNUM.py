from django.conf.locale import fr
import numpy as np

rng= np.random.default_rng()
# This line creates a random number generator object using NumPy's default random number generator. The rng object can be used to generate random numbers.
# defult_rng() is a function that returns a new instance of the default random number generator. This generator is based on the PCG64 algorithm, which is a modern and efficient pseudorandom number generator.


print(rng.integers(1,7)) #...every time generate a new number between 1 to 7.
'''
OutPut Randomly:
6
'''

print(rng.integers(low=1,high=101)) 
#THis means generate a random number between 1 to 100.
'''
OutPut Randomly:
35
'''
print(rng.integers(low=1,high=105,size=3))
#Size refer to how many random numbers you want to generate.
#low refers to the starting number, and high refers to the ending number.

'''
OutPut Randomly:
[46 23  4]

'''

print(rng.integers(low=1,high=105,size=(3,2)))
#Size =(3,2) means generate a 2D array with 3 rows and 2 columns, where each element is a random integer between 1 and 104 (inclusive of 1 and exclusive of 105).

'''
OutPut Randomly:
[[20 13]
 [95 41]
 [71 39]]
'''


# rng= np.random.default_rng(seed=1)
'''
If you want to generate the same random numbers every time you run the code, you can set a seed value when creating the random number generator object.
rng= np.random.default_rng(seed=1)

'''


# -------------------------------------------

#uniform distribution: A type of probability distribution in which all outcomes are equally likely. In the context of random number generation, it means that each number within a specified range has an equal chance of being selected.
print(np.random.uniform(low=-1,high=1,size=3))
'''
OutPut Randomly:
[-0.32412556  0.0144465   0.47736571]

'''

print(np.random.uniform(low=-1,high=1,size=(3,2)))
'''
OutPut Randomly:
[[ 0.77168875 -0.36353288]
 [-0.30297231  0.73519478]
 [-0.4974264   0.17543284]]

'''

# --------------------------------------------------

array=np.array([1,2,3,4,5])

rng.shuffle(array)
print(array)

'''
[4 3 1 2 5]
'''
#The shuffle() method randomly reorders the elements in the array in place, meaning that 

# it modifies the original array rather than creating a new one. After calling rng.shuffle(array), the order of the elements in array will be changed randomly.

# ---------------------------------------------------

fruits=np.array(['apple','banana','cherry','date','fig','grape'])
fruits=rng.choice(fruits, size=3)
print(fruits)

'''
['date' 'cherry' 'cherry']
'''

fr=rng.choice(fruits)
print(fr) 

'''
OutPut Randomly:
banana

'''

# ---------------------------------------
#Fun Game....

animals=np.array(['🦓','🐴','🐯','🐺','🐸','🐲','🦄'])
animals=rng.choice(animals, size=(3,3))
print(animals)
'''
[['🐺' '🦓' '🐸']
 ['🐯' '🐴' '🐲']
 ['🦓' '🦓' '🐲']]

'''


