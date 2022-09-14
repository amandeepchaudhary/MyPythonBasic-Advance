#linspace() function
from numpy import *
aman = linspace(23,34,num=50,endpoint=True)
print(aman)
ab = linspace(1,8,num=5,endpoint=False)
print(ab)
a = linspace(1,8,num=5,endpoint=True)
print(a)
print(a[1])

#Accessing by for loops Without index
for el in a:
    print(el)

#Accessing by for loop With index
n=len(a)
for i in range(n):
    print(a[i],'=',i,'=','Index')

#Accessing by while loop Without index
n=len(a)
i=0
while i<n:
    print(a[i])
    i+=1

#Accessing by while loop With index
n=len(a)
i=0
while i<n:
    print('Index',i,'=',a[i])
    i+=1

#Creating array with logspace() function
