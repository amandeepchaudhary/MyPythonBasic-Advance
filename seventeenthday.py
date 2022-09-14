#Slicing on list
print("Slicing on list")

#syntax
# new_list_name= old_list_name[start,stop,stepsize]
x=[101,102,103,104,105,106,107]
for i in range(len(x)):
    print("Index",i,"=",x[i])
print()

print("from 1st position to 4th position:")
a=x[1:5]
for i in a:
    print(i)
print()

print("from 0th position to last position:")
b=x[0:]
for i in b:
    print(i)
print()

print("0th position to 4th position:")
c=x[:5]
for i in c:
    print(i)
print()

print("last 4 elements")
d=x[-4:]
for i in d:
    print(i)
print()

print("from 0th position to 6th position with stride 2:")
e=x[:7:2]
for i in e:
    print(i)
print()

print("last 5 elements with (-5-(-3))= 2 elements towards right:")
f=x[-5:-3]
g=x[-5:-7:-1]
for i in f:
    print(i)
print()

print("from full list having last two elements towards left:")
g=x[-5:-7:-1]
for i in g:
    print(i)
print()

print("from the last 5 elements 2 elements towards left:")
h=x[-3:-5:-1]
for i in h:
    print(i)
print()

#list concatenation
print("list concatenation")
a=[23232,32323,735634,343,34]
b=[523,23,223,54]
c=[55,26,231,78]

print(a)
print(b)
print(c)

result = a+b+c
print(result)
print()

#Repetition of list
print("Repetition of list")
a=[1,2,3]
result = a*4
print(result)

#aliasing a list
print("aliasing a list")
a=[187,12,1,2]
b=a
print("A:",a)  #same banda h abhisek
print("B:",b)  #abhi uska ghr ka naam h

print("Modifing a")
a[1]=359480
print("A:",a)  #same banda h abhisek
print("B:",b)  #abhi uska ghr ka naam h

print("Modifing b")
b[2]=359480
print("A:",a)  #same banda h abhisek
print("B:",b)  #abhi uska ghr ka naam h

#copy list and cloning list ='both lists are independent'
print("copy list and cloning list")
print("Copy")
a=[100,101,102,103]
b=a.copy()
print(a)
print(b)
a.append(104)
a.insert(0, 99)
b.pop()
b.pop(0)
a.remove(103)
a.extend(b)
print(a)
print(b)

print("Cloning")  #coping a list using slicing 
print("a:",a)
b=a[4:]
print("b:",b)


from numpy import *
print("slicing in 3d array")
a=array([[[1,2,3],[4,5,6],[7,8,9]],
        [[44,55,66],[88,99,33],[22,11,77]],
        [[200,300,400],[500,600,700],[100,800,900]]])

b=a[0:3,0:2,0:3] #0:3 is rows in 3d, 0:2 is rows in 2d, 0:4 is columns in 2d
print("b:",b)
print("c")
c=a[1:3,1:3,0:3]
print(c)
a[2][1][0]=9800  #2-row of 3d array,1-row of 2d array,1-column of 2d array
print("a:",a)

#nested list
print('nested list')
a=[89,0,78,[67,987]]  #one way
print(type(a[3]))

for i in range(len(a)):
    if type(a[i]) is list:
        if len(a[i])>=1:
            n=len(a[i])
            for j in range(n):
                print(i,j,a[i][j])
    else:
        print(i,a[i])

#while
print("while")
n=len(a)
i=0
while i<n:
    if type(a[i]) is list:
        if len(a[i])>=1:
            m=len(a[i])
            j=0
            while j<m:
                print(i,j,a[i][j])
                j+=1
            i+=1
    else:
        print(a[i])
        i+=1

print("a on index of a[3][1]",a[3][1])
print("a with nested array in itself:",a)
b=[78,89]
a=[45,9875,234,b]
print("a with nested list in itself by assigning to a variable",a)
a=[[1,234,43,4],[23,543,321,899]]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j])

#while
print("while")
n=len(a)
i=0
while i<n:
    j=0
    while j<len(a[i]):
        print(i,j,a[i][j])
        j+=1
    i+=1

# passing list to function
print("passing list to function")

def show(l):
    print(l)
    print(type(l))
    for i in l:
        print(i)

lst=[100,200,300,'aman','ishu',500]
show(lst)

#returning list from function
print("returning list from function")\

def show(l):
    print(l)
    print(type(l))
    for i in l:
        print(i)
    return l+lst2

lst2=[700,'dharmo','changdi','surender','sunita']
lst1=[100,200,3000,'aman','ishu',600]
l2=show(lst1)
print("ok")
print(l2)
print(type(l2))

#list() function
print("list() function")
a=list()      #created an empty list 
print(a)
print(type(a))

#getting elements 
print(list("aman"))
print(a)
print(type(a))

#using range function
a = list(range(0,5))
print(a)
print(type(a))

#slicing nested list
x=[[100,200,300],
   [400.399,388]]

b=x[1:2]       #we get a list in list
c=x[1:2][0]    #we get a list which was present on the upper 
                #list's 0th position
d=x[1:2][0][1] #we get the 1th positioned element in the list 
a=x[1:2][0][1] #1:2 is the row which i want, [0] is the 
                #[[400.399,388]] 0th list in the selected row, 
                # [1] is the element which i want

print(a)
# b=a[0]
# print(b)

x=[[100,200,300],
   [400,1.399,388]]

#we want 1.399 to 388
a=x[1:2]
b=a[0]
c=b[1:3]
print("x:",x)
print("a:",a)
print("b:",b)
for i in range(len(b)):
    print("b",i,"=",b[i])
print("c:",c)

