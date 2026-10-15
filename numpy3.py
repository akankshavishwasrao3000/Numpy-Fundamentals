import numpy as np

x=[1,2,3,4]
y=np.array(x)
# y=np.array([1,2,3,4,5,6])

print(y)

l=[]

for i in range(1,9):
    int_l=input("Enter :")
    l.append(int_l)

print(np.array(l))

'''
Output:

[1 2 3 4]
Enter :2
Enter :6
Enter :4
Enter :6
Enter :7
Enter :56
Enter :12
Enter :89
['2' '6' '4' '6' '7' '56' '12' '89']
'''