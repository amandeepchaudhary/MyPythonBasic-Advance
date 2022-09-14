#Array with logspace() function
from numpy import *
a= logspace(start=1,stop=3,num=3,base=10.0, dtype=None,endpoint=True)
print(a)
#accessing with for loop without index 
for el in a:
    print(el)
#accessing with for loop with index 
n=len(a)
for i in range(n):
    print('index',i,'=',a[i])

#accessing with while loop 
n=len(a)
i=0
while i<n:
    print('index',i,'=',a[i])
    i+=1

#creating array using arange() function
ar=arange(start=0,stop=5,step=1,dtype=None)
print(ar)
 
ar1=arange(5.0)
ar2=arange(1,6)
ar3=arange(1,10,2)
print(ar1)
print(ar2)
print(ar3)

#creating array through zeros() function 
#z=zeros(shape,dtype)
z=zeros(5)
print(z)

z1=zeros(5,dtype=int)
print(z1)

z2=zeros((5,3),dtype=int)
print(z2)
for el in z1:
    print(el)
n=len(z1)
for i in range(n):
    print(z1[i])

#creating array with ones() function
#o=ones(shape,dtype=float,order=C(row-major) or F(column-major))
o=ones(5)
print(o[1])

o1=ones(5,dtype=int)
print(o1)

o2=ones((3,2),dtype=int)
print(o2)

#Methematical funtion on arrays using numpy
a=array([101,102,103,104,105])
a=a+5
print(a)

for el in a:
    print(el)

n=len(a)
for i in range(n):
    print('index',i,'=',a[i])

i=0
while i<n:
    print('index while',i,'=',a[i])
    i+=1 
a1=array([101,102,103,104,105])
b1=array([202.201])
c=a1+b1
print(c)

#comparing arrays using numpy
a=array([100,200,300,400,500])
b=array([100,20,300,40,500])
result= a==b
print(result)

a=array([100,2,300,400,500])
b=array([100,20,300,40,500])
result= a<b
print(result)

#any and all functions
'''
if one is true then it gives true,if iterable is empty gives false==any
if all true then it gives true,if iterable is empty gives true==all
'''
a = array ([101,102,103,104])
b=array([101,102,103,40])
c= a==b
print(any(c))
print(all(c))

#where() function
a=array([100,10320,203,390])
b=array([20,210,45,4])
c2='a','hi','bda','hai'
c1=array(['jhai','ok','no'])
c=where(a>b,c2,b) #--if statement is true then 'a' if not the 'b'--
print(c)

#nonzero() function
a12= array([12,200,8239,234])
c= nonzero(a12)
print(c)

#Aliasing array
#to give another name to a existing array,it doesm't mean copying
a=array([10,20,30,40])
a=b
print(a)
print(b)
print("a",id(a))
print("b",id(b))

#view() method and copy() method
a=array ([100,102,1023])
b=a.view() 
a[1]=40
b[2]=23
print(a)
print(b) #id's are seperate but both are related to each other
print("a",id(a))
print("b",id(b))
#copy -- ids are seperate and both are not related to each other
a=array ([100,102,1023])
b= copy(a)
a[1]=2
b[2]=23
print(a)
print(b)
print("a",id(a))
print("b",id(b))

#Getting input from user in numpy one dimensional array using for loop
n=int(input("Enter Number of elements:"))
a=zeros(n, dtype=int)
a[0]=120
a[1]=34
print(a)

# from user
n=int(input("Enter Number of elements:"))
a=zeros(n, dtype=int)
for el in range(len(a)):
    x=int(input("Enter Element:"))
    a[el]=x
print(a)

for i in range(len(a)):
    print(a[i])

#Getting input from user in numpy one dimensional array using while loop
n=int(input("Enter number of Elements:"))
z=zeros(n, dtype=int)
i=0
j=0
while i<len(z):    #or n
    x=int(input("Enter Number:"))
    z[i]=x
    print(z)
    i+=1

print(type(z))
while j<n:
    print(z[j])
    j+=1