#higher order function = function mai function pass krte h 
                          # toh higher order function ban jata h
print("higher order function")
# filter() function
print("filter() function") 
# syntax:
# filter(function_name=filter,iterable=joki koi list ya tuple 
#         string ya dictionary jisko hum element by element 
#         dekh skte h=yh filter k liye function k hisab se 
#         filter hoga)

a=[89,33,56,80,99,60,72]

def medium_high_marks(n):
    for i in range(len(n)):
        if n[i]>=60:
            print(n[i],True)
        else:
            print(a[i],False)

m=medium_high_marks(a)
print(m)

def medium_high_marks(n):
    if n>=60:
        return True

b=filter(medium_high_marks, a)
print(b)
print(type(b))
for ie in b:
    print(ie)


result=list(filter(medium_high_marks, a))
#True wale element ko return krta h aur uss 
# elements ko show krta hai
print(result)
print(type(result))
for i in result:
    print(i)

result=list(filter(lambda n:(n>=60), a))
print(result)
print(type(result))
for i in result:
    print(i)

print("None filter")
result=list(filter(None, a)) #return full targeted list
print()
a=[True,False,True,True,True,False]
result=list(filter(None, a)) #return full targeted list
print(result)
print(type(result))
for i in result:
    print(i)

#map() function in high order function===
print("map() function in high order function===")
a=[10,20,325,357,68]

def inc(n):
    return n+2

n=map(inc, a)
print(n)
print(type(n))
for i in n:
    print(i)

n=list(map(inc, a))
print(n)
print(type(n))

# using lambda function
n=list(map(lambda m:m+2, a))
print(n)
#map m hum ek se jyada iterable object ka use kr skte hai
# but size same hone chahiye hain dono k
a=[100,200,300,400,500]
b=[1,2,3,4,5]

result= map(lambda n,m:n+m,a,b)
print(type(result))
for i in result:
    print(i)


result= list(map(lambda n,m:n+m,a,b))
print(result)
print(type(result))

#high order's reduce() function
print("reduce() Function")
# syntax==
from functools import reduce

# reduce(function_name, sequence)
a=[10,20,30,40]
 
result = reduce(lambda m,n:m+n,a)  #m and n are 0th positioned 
                                    #element and 1th positioned 
                                    # element
# print(sum(a))
print(result)
print(type(result))

#filter() function = is used to get the filtered data which we 
# need from the whole /giving the condition for filtering

#map() function = is used to change the function and we want
#  the changed function/ adding and subtracting in the function
#  or adding two functions 

#reduce() function = reduce kr dene h mile hue data ko



#Scenario=====!!!!!!************+++++++++++!!!!!!!!!
print("Scenario=====!!!!!!************+++++++++++!!!!!!!!!")
# pehle hume bhut sara data mila uss data me se humne pehle 
# filter kra data ko jo hume chahiye tha then humne map kra 
# data ko means modify jaisa hume chahiye tha aur wahi return 
# kra liya uske baad reduce kra data ko aur output le liya

# Generator function, Yield statement and Next function
print("Generator function, Yield statement and Next function")

def disp(a,b):
    yield a
    yield b

x,y=disp(200, 380)
print(x)
print(y)
 
result=disp(390,450)
print(result)
print(type(result))

print("Next() function only works on generator object")
print(next(result))
print(next(result))

lst = list(result)
print(lst)
print(type(lst))


#generator creates element sequence
# yield return an parameter/sequence of elements
# next() gives next object/helps to iterate generator object 

print("**********")
def show(a,b):
    while a<=b:
        yield a
        a+=1

result=show(1, 5)

print(type(result))
print(next(result))
print(next(result))
for i in result:
    print(i)

lst=list(result)
print(lst)


#Tuple in python = contains a group of elements which can be 
# same or different data types
print("####")
print("Caution:Tuples cannot be modified as they are immutable")
print("####")

print("Tuple in python")
a = (10,29,387,'aman',45.234327)
#with one element
a=(10)  #<----this will be treated as a integer
#so, give a comma "," to describe it as a tuple
a=(10,)
a= 10,20,30,'aman',65.6  #<---- by default this 
                                #will be treated as tuple

#accessing with for loop
#without index
for i in a:
    print(i)

#with index
n=len(a)
for i in range(n):
    print("Index",i,"=",a[i])

#accessing with for loop
print("while***************")
i=0
while i<n:
    print(a[i])
    i+=1

#slicing tuple
print("slicing tuple****")
a=(9,2093,343,74838,37)
print("1th position to 3rd position")

b=a[1:4]
print(b)

print("4 elements from behind")

c=a[-4:]
print(c)

print("elements with stride of 2")
 
d=a[-5: :2]
print(d)

#concatenation of tuple
print("concatenation of tuple")

a=(10,20,30,40)
b=(1,2,3,4)
c=(101,102,103)

print(a)
print(b)
print(c)

result=a+b+c

print(sum(result))

print(result)

#modifing tuple but as we know tuples are immutable so it 
# is not possible to modify,update or delete
print("modifing tuple")
a=(10,200,30000,4000000,50,'aman')
print(a)
print(id(a))

# adding data to the last of tuple
b=(20,40)
tup1=a+b
print(tup1)
print(id(tup1))

# slicing for needed data
tup2=a[0:4]
print(tup2)

# if we wantto add data in the middle then
# 1. slice the concatenated a saperate tuple with the 
# elements you want to add
a=(10,200,30000,4000000,50,'aman')

#i want to add the elements between 4000000 and 50 so,
b=(5000000,6000000)
print(a)
print(b)
sli1=a[0:4]
sli2=a[4:]
print(sli1)
print(sli2)
con1=sli1+b+sli2
print(con1)

#deleting tuple and its elements is immposible but we can 
# achieve it
print("deleting tuple and its elements")
a=(209,27673,253,45)
print(a)
del a  #deleted the full tuple
# del a[1]  #gives error as tuple doest support element deletion
#through slicing
a=(209,27673,253,45)

tup1=a[2:]
print(tup1)

#suppose we want to delete 27673 so,
s1=a[0:1]
s2=a[2:4]
a1=s1+s2
print(a1)

#Getting input from users in == Tuple
#easy way = pehle listm lelo input phir tuplem change krdo
a=[]
inp=int(input("Enter number of elements:"))
for i in range(inp):
    a.append(int(input("Enter Element:")))
    # a.insert(int(input("Enter Index number of the number")),(int(input("Enter element:"))))
    print("Index",i,"=",a[i])
print(a)
print(type(a))

a=tuple(a)
print(a)
print(type(a))
print("Tuple:")
for f in a:
    print(f)

#repetition of tuple == "*" operator for repition of tuple
print("repetition of tuple==")
a=(1,2,3)
result = a*8
print(result)

#aliasing Tuple==
print("aliasing Tuple==")
print("alisasing means giving another name it doesn't mean copying")
a=(10,20,30,40)
b=a

print("A:",a)
print("A:",id(a))
print("B:",b)
print("B:",id(b))
