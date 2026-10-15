import numpy as np

# Filtering = Refers to the process of selecting the elements 
#               from an array that match a given condition. 

# 1. Boolean filtering — ages[ages < 18]

ages1 = np.array([21, 15, 18, 12])

print(ages1 < 18)   #[False  True False  True]

ages=np.array([[21,45,36,15,65,90,18],
               [39,22,15,99,87,45,12]])

teenagers=ages[ages < 18]  #[15 15 12]
print(teenagers)

adults=ages[(ages >=18) & (ages < 65)]
print(adults) #...[21 45 36 18 39 22 45]

seniors=ages[ages >= 65]
print(seniors)  #...[65 90 99 87]

evens=ages[ages % 2 ==0]
print(evens) #...[36 90 18 22 12]

odds=ages[ages % 2 !=0]
print(odds) #...[21 45 15 65 39 15 99 87 45]



'''
2. What is np.where()?
np.where() can choose one value when a condition is true and another value when it is false.
Your example:
adults2 = np.where(ages >= 18, ages, 0)



It has three parts:
np.where(condition, value_if_true, value_if_false)
- ages >= 18 → condition to check.
- ages → keep the original age if the condition is True.
- 0 → use zero if the condition is False.


'''

adults2=np.where(ages >= 18, ages, 0)
# adults2=np.where(ages >= 18, ages, -1)
# ...We can keep any value. 
print(adults2)

'''
OutPut:

[[21 45 36  0 65 90 18]
 [39 22  0 99 87 45  0]]

.....If any condition does not match, then it keeps the zero. 

'''

print(ages) # ...Original remain same 


'''
“NumPy filtering is used to select array elements that satisfy a condition. Boolean indexing selects only matching elements, while np.where() lets us choose what value to keep when the condition is true and what value to use when it is false.”

'''





