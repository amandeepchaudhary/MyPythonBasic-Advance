#Multi dimensional array 2D 3D and many more dimensional arrays
#Two dimensional numpy array using array() function 
'''
numpy.array(object, dtype=None, copy=True, order='K', subok=False, ndmin=0)
2d array ===== 
a=array([[101,202],[109,12],[98,78],[9,33]])  ---two square brackets
a=array([['ok','sbi'],['aman','ishu'],['rahul','raj']], dtype=str)

3d array =====
a=array([[[200,34],[200.98]],
         [[298,67],[34,560]])
'''

from numpy import *
#of different lengths shows as tuple or list not as int
a = array ([[10,20,30,40],[50,60,70,80,90]])
print(a)
print(id(a[1][3]))

#same lengths arrays
a = array ([[10,20,30,40],[50,60,70,80]],dtype=float)
print(a)
print(a.dtype)

a = array ([["aman","ishu"],["no","name"]])
print(a)
print(a.dtype)
print(a[0][1])
print(a[1][1])

#Accessing numpy 2D array using for loop in pyhton
a4 = array ([[10,20,30,40],[50,60,70,80]])
print(a4[0][2])
# print(a)  
# without index
for el in a4:  #--outer for loop represents rows
    for i in el:  #--inner for loop represents column
        print(i)

# with index 
for el in a4:
    # print("index",el,"=",a[el])
    for i in range(len(a4)):
        for j in range(len(el)):
            print("Index [",i,"]","[",j,"]","=",a4[i][j])

            #OR

a4 = array ([[10,20,30,40],[50,60,70,80]])
a4[1][2]=100
n=len(a4)
for i in range(n):    #--outer represents the rows
    for j in range(len(a4[i])):  #--inner for loop represents column
        print(a4[i][j])
    print()

#Accessing the 2d numpy array with while loop
a=array([[2002,393,6348],[7832,2355,2]])
# b=array([[232,2,213],[23,34,2]])
# c= a==b
# print(c)
n=len(a)
i=0
while i<n:
    j=0
    while j<len(a[i]):
        print(a[i][j])
        j+=1
    print()
    i+=1

#Numpy 2d array using Zeros() function
# a=zeros((shape=rows,column), dtype=float, order=C or F)
a=zeros((3,2),dtype=int)
print(a)
#for loop
for el in a:
    for el1 in el:
        print(el1)

c=len(a)
print()
print(c)
for el in range(len(a)):
    for el1 in range(len(a[el])):
        print(a[el][el1])

for el in a:
    for el2 in range(len(a)):
        for el1 in range(len(el)):
            print(a[el2][el1])

#while loop
i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        print(a[i][j])
        j+=1
    i+=1

#ones() function
#same syntax as zeros
a=ones((3,2))
#for loop
for el in a:
    for el1 in el:
        print(el1)

#with index for loop
for el in range(len(a)):
    for el1 in range(len(a[el])):
        print("index",el,el1,"=",a[el][el1])

#while loop
n=len(a)
i=0
while i<n:
    print(a[i])
    i+=1

i=0
while i<n:
    j=0
    while j<len(a[i]):
        print(a[i][j])
        j+=1
    i+=1

#Reshape() function
a=array([1,2,3,4,5,6,7,8,9,10,11,12])
b=reshape(a,(3,4))
print(b)

a=array([1,2,3,4,5,6,7,8,9,10,11,12])
b=reshape(a,(2,3,2))
print(b)

a=array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
b=reshape(a,(12))
print(b)

#flatten() method
# to convert 2d array or 3d array inro 1d array
a=array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
b=a.flatten()
print(b)

#Input from user in numpy two dimensional array using for loop
n1=int(input("Enter Number of Elements for rows:"))
n2=int(input("Enter Number of Elements for column:"))
a=zeros((n1,n2),dtype=int)
a[0]=20
for el in range(len(a)):
    for el1 in range(len(a[el])):
        x=int(input("Enter next element:"))
        a[el][el1]=x
    print(a)

#while loop
l=len(a)
i=0
while (i<l):
    j=0
    while j<len(a[i]):
        y=int (input("Enter the Elements:"))
        a[i][j]=y
        j+=1
    print(a)
    i+=1

#slicing on two Dimensional array
n=array([ [10,20,30],
          [40,50,60],
          [70,80,90] ])
print("Original Array")
print(n)
print(type(n))

print("0th Row all columns")
a=n[0, :]
print(a)

print("1st Row all columns")
a=n[1, :]
print(a)

print("2nd Row all columns")
a=n[2, :]
print(a)

print("0th columns all rows")
a=n[:,0]
print(a)
for i in a:
    print(i)

#accessing n[0][0]=10
a=n[0:1,0:1]
print(a)

print("2nd Row till 1st column")
a=n[2:3,1:2]
print(a)

a=n[0:2,1:3]
print(a)