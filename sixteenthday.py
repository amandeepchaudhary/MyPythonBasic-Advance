#Recursion
print("^^^^^^^^^^^^^^Recursion^^^^^^^^^^^^^^")
#a function calling again and again to compute a value 
# is referred to recursive function or Recursion
import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(2000)
it=0
def recursion_fun():
    global it
    it=it+1
    print("Aman",it)
    
recursion_fun()

#--pass/call by object reference
str=("pass/call by object reference")
print(str.title())

def pc_by_or(x):
    print(x,id(x))
    x=15
    print(x,id(x))

x=10
pc_by_or(x)
print(x,id(x))

def call_by_obeject_ref(lst):
    print("IFBA:",lst,id(lst))
    lst.append(4)
    print("IFAA",lst,id(lst))

lst=[1,2,3]
print("BCF",lst,id(lst))
call_by_obeject_ref(lst)
print("ACF",lst,id(lst)) 

print("*************")
def call_by_obeject_ref1(lst):
    print("IFBA:",lst,id(lst))
    lst=[11,22,33]
    print("IFAA",lst,id(lst))

lst=[1,2,3]
print("BCF",lst,id(lst))
call_by_obeject_ref1(lst)
print("ACF",lst,id(lst)) 

#Function decorator in python ==== used to enhance a function 
# without changing the original function

def decorator(func):
    def inner():
        print("IF: Before enhancing Function")
        func()
        print("IF: After enhancing Function")
    return inner

@decorator   #--num=decorator(num),num() and decorator(num)upper 
                #jha parameter hai and func()==num()
def num():
    print("We will use this function")
    print("and will enhance this in decorator")

num()
# decorator_result_fun=decorator(num)
# decorator_result_fun()

print("***************")

def decor(fun):
    def inner():
        a=fun()
        add=a+5
        return add
    return inner

@decor
def enhance_fun():  #=par hum chahte h ki 10 na return kare
    return 10        #15 return kare and yh function is 
                      # out of our reach hai     

# enhance_fun=decor(enhance_fun)
print(enhance_fun())
# This is the @decore's Doing in background====
# enhance_fun = decor(enhance_fun)
# enhance_fun()

print("***ok*******")

def decor(num):
    def inner():
        a=num()
        multi =a*5
        return multi
    return inner

def decor1(num1):
    def inner():
        a=num1()
        add =a+5
        return add
    return inner
@decor1
@decor
def num():
    return 10

num()
num=decor1(decor(num))
print(num())


print("!!!!!!!!!!!!!!!!")
#passing variable
def num(y):
    x=10
    c=x+y
    print(c)

num(23)

#passing function in function
def num():
    def inner():
        print("Inner function")
    return inner

a=num()
a()

#passing array to function
from array import *

def passing_array_in_func(ar):
    print(ar)
    print(type(ar))
    for i in ar:
        print(i)
    
    #with index
    for i in range(len(ar)):
        print("Index",i,"=",ar[i])


a = array('i',[101,102,103,104,105])
passing_array_in_func(a)

#retrurning array from function

def returning_array_in_func(ar):
    print("Passed array ar:",ar)
    print(type(ar))
    for i in ar:
        print(i)
    return ar

a = array('i',[101,102,103,104,105])
ra=returning_array_in_func(a)
print("Returning array ra:",ra)
print(type(ra))\

for i in range(len(ra)):
    print("new array from a on index:",i,"=",ra[i])

print("***************")
from array import *

def creating_ar_and_returning_in_func():
    ar = array('i',[])
    ar1=int(input("Enter number of values you want in array:"))
    for i in range(ar1):
        ar.append(int(input(f"Enter {i} indexed number of array ar:")))
    print(ar)
    print(type(ar))
    for i in range(len(ar)):
        print("Index",i,"=",ar[i])

creating_ar_and_returning_in_func()
print("**********")

def passing_array_in_func_while_array_in_in_func():
    a=array('i',[101,102,103])
    print(a)
    print(type(a))
    for i in a:
        print(i)
    return a

y=passing_array_in_func_while_array_in_in_func()
print(y)

#passing and returning numpy array in python
st="******* passing and returning numpy array in python ********"
print(st.title())

from numpy import *

def passing_returning_numpy_array_in_func(ar):
    print("Passed array ar:",ar)
    print(type(ar))
    for i in ar:
        print(i)
    return ar

a = array([101,102,103,104,105])
ra=passing_returning_numpy_array_in_func(a)
print("Returning array ra:",ra)
print(type(ra))

for i in range(len(ra)):
    print("new array from a on index:",i,"=",ra[i])

print("***************")

#numpy build in math functions
npy_b_math="numpy build in math functions"
print(npy_b_math.title())

a = array([25,737,345,43,5])
b = array([[23,233,2321,11,3],[232,21,212,34,3]])
print()
#Sum() Function
print("a:",sum(a))
print("b:",sum(b))
print()
#prod() Function
print("a:",prod(a))
print("b:",prod(b))
print()
#sqrt() function
print("a:",sqrt(a))
print("b:",sqrt(b))
print("*******")

#math module
print("*****math module******")
from math import *

print(floor(4.5))
print(ceil(4.5))
print(sqrt(49))
print(factorial(5))
print(pow(5,2))
print("***********")

#list
print("!!!!!!!!!!!!!!!!List!!!!!!!!!!!!!!!!!!!!!")
#lists are very similar to array but there is major 
# difference, an array can store only one type of elements 
# whereas a list cn store different type of elements.
#mutable = mai address same rehta h even after the changes 
# where as in unmutable = mai address change hota h after 
# changing the values

a=[10,29,394,83.46,'aman']
print(a[0])
print(a,id(a))
a[1]=40
print(a,id(a))
print()
n=len(a)
for i in range(0-1,-(n+1),-1):
    print(a[i])
a=[]

#accessing list using for loop
a=[10,29,394,83.46,'aman']

#without index
for i in a:
    print(i)

# with index
for i in range(0-1,-(n+1),-1):
    print(a[i])

#accessing list using while loop
print("accessing list using while loop")
# without index
a=[10,29,394,83.46,'aman']
n=len(a)
i=0
while i<n:
    print(a[i])
    i+=1

# with index
i=0
while i<n:
    print("index",i,"=",a[i])
    i+=1

#append() method = is used to add an element at the end of 
# the existing list
# Opposite===
#pop() is used to remove elements from the last of existing list
print("append() method")

a=[10,29,394,83.46,'aman']
a.append(500)
print(a)

#Getting list input from the user in python
print("Getting list input from the user in python")

a=[]
print(a)
n=int(input("Enter number of Elements:"))
for i in range(n):
    a.append(int(input("Enter Element:")))

print("List:")
for element in a:
    print(element)

print(a)

#insert() method= this element is used to insert an element 
# in a particular position of the existing list
# Opposite===
#pop(n) is used to remove a element with a given position and 
# it also returns the removed element
print("insert() method")
#syntax======
# list_name.insert(position_number,new_element)
a=[10,20,30,40,50,'aman','chaudhary']
print("Before: insert()",a)
a.insert(6, 'deep')
print("After: insert()",a)

for element in a:
    print(element)

#pop() method= is used to remove the last element from 
# the existing list
print("pop() method")
a=[10,20,30,40,50,'aman','chaudhary']
print("Before pop():",a)
a.pop()
print("After: pop()",a)

#pop(n) method= is used to remove an element specified 
# by position number,from the existing list and also **return 
# removed elements**. 
print("pop(n) method") 

a=[10,20,30,40,50,'aman','chaudhary']
print("Before pop(n):",a)
n=a.pop(2)
print("After: pop(n)",a)
#it also returns he removed element so
print("Removed Element:",n)

#remove() method = is used to remove the first occurence of 
# the given element from the existing list.if it doesn't 
# found the element, shows valueError.

# if an element is ocucuring many times then the first 
# occurence of the particular element will be removed 

print("Remove(element) method")

a=[10,20,30,10,40,50,'aman','chaudhary']
print("Before remove():",a)
a.remove(10)
print("After: remove()",a)

#index(element) method=returs position number of first
# occurence of given element in the list
print("Index() method")
a=[8,48,493,48]
list_index=a.index(48)
print(list_index)

#reverse() method=this method is used to reverse the order 
# of the elements in the list
print("Reverse() method")

a=[10,20,30,10,40,50,'aman','chaudhary']
print("Before reverse():",a)
a.reverse()
print("After: reverse():",a)

#extend() method = is used to append another list or 
# iterable object at the end of the list
print("Extend() method")

a=[10,20,30,10,40,50,'aman','chaudhary']
b=[900,4536,276.367,42]
print("Before Extend():",a)
a.extend(b)
print("After: Extend():",a)

#count() method = return number of occurence of a specified 
# element in te list
print("count() method")
a=[900,4536,42,276.367,42,'aman',42]

c_method=a.count(42)
print(c_method)

#sort() method = used to sort te elements in the ascending order
print("sort() method")
a=[900,4536,42,276.367,42,'aman',42]
a=[900,4536,42,276.367,42,42]

print("Before sort():",a)
a.sort()
print("After: sort():",a)

#clear() method=is used to delete all the elements from the list
print("clear() method")
a=[900,4536,42,276.367,42,'aman',42]
a=[900,4536,42,276.367,42,42]

print("Before sort():",a)
a.clear()
print("After: sort():",a)
