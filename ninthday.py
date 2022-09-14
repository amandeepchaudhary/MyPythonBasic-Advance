print('#numpy ')
import numpy  #OR
from numpy import *
stu_roll= array([101,102,103,104,105])
print(stu_roll)
print(stu_roll.dtype)
print(type(stu_roll))
print()

print('#convert into float data type')
stu_roll= array([101,102,103,104,105], dtype=float)
print(stu_roll)
print(stu_roll.dtype)
print(type(stu_roll))
print()

print('#character data type')
stu_roll= array(['a','b','c','d'])
print(stu_roll)
print(stu_roll.dtype)
print(type(stu_roll))
print()

print('#String data type')
stu_roll= array(['aman','babita','chawla','diksha'])
print(stu_roll)
print(stu_roll.dtype)
print(type(stu_roll))
print()

print('#Modify data')
stu_roll= array(['aman','babita','chawla','diksha'])
print(stu_roll)
print(stu_roll.dtype)
print(type(stu_roll))
print('Modifing stu_roll[1]')
stu_roll[1]='brar'
print(stu_roll)
print()
print("****************")

print('#accessing 1-D array of numpy using loops')
print('#accessing 1-D array of numpy using for loop -- Without index')
for element in stu_roll:
    print(element)

print('#accessing 1-D array of numpy using for loop -- With index')
n= len(stu_roll)
for j in range(n):
    print("Index",j,"=",stu_roll[j])
print('***********')

print("#accessing 1-d array of numpy using while loop")
stu_roll= array([101,102,103])
n1=len(stu_roll)
print(n1)
i=0
while i<n1:
    print("Index",i,'=',stu_roll[i])
    i+=1