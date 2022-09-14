#copying in Tuple
#we can copy elements of tuple into another tuple using slice
#independent
a=(100,200,321)
b=a
print(id(a))
print(id(b))
b=a[0:3]
print(b)
print(id(b))
#^^^^^^^^^^all the data is same so the 'b' assigned to the 
# same data at the same id^^^^^^^^^^^^^^^^^
b=a[1:3]
#when we slice different from the original data that is 
# called copying

#nested tuple
print("nested tuple")
a=(10,203,40,(20,4594,784))
n=len(a)
for i in range(n):
    if type(a[i]) is tuple:        
        m=len(a[i])
        for j in range(m):
            print("Index",i,j,"=",a[i][j])
    else:
        print("Index",i,"=",a[i])

#while loop
a=(10,203,40,(20,4594,784))
n=len(a)
i=0
while i<n:
    if type(a[i]) is tuple:
        if len(a[i])>1:
            m=len(a[i])
            j=0
            while j<m:
                print(a[i][j])
                j+=1
            i+=1
    else:
        print(a[i])
        i+=1    


print("next")
a=((12,222,3423,234),(443,3465,56))

for i in a:
    for r in i:
        print(r)

print("While")
n=len(a)
i=0
while i<n:
    j=0
    m=len(a[i])
    while j<m:
        print(a[i][j])
        j+=1
    i+=1

#slicing nested tuple 
print("slicing nested tuple")
x = ((10,20,30),
     (40,50,60),
     (70,80,90),
     (11,12,13),
     (14,15,16),
     (17,18,19))

print("Original tuple:")
print(a)
print()

print("From 1st position to 4th position;")
a=x[1:5]
print(a)

print("Slice nested 2nd position,0th position")
b=x[4:5][0]
c=b[1:3]
print(b)
print(c)

print("Last nested 4 tuples then 1st position")
d=x[-4:]
e=x[-4:][1]
print(d)
print(e)

print("Last nested 4 tuples then 1st position then extract elements")
f=x[-4:][1][0]
print(f)
for i in e:
    print(i) 

print("From 1st position to 4th position;")
a=x[1:5]            #slice 1st tuple to 4th tuple and making a new tuple
print(a)        
a=x[1:5][0][1:3]    #0=selected the 0th positioned tuple, 1:3 is cutted from 1st positioned element to 2nd positioned element
print(a)

a1=x[1:5][0][1:3]
print(a1)
a2=x[1:5][1][1:3]
print(a2)
print(a1+a2)

#passing tuple in function==
print("passing tuple in function==")

def show(t):
    print(t)
    print(type(t))
    for i in t:
        print(i)

tup=(22,77,55,44,'aman',33)
show(tup)

# returning tuple from function
print("returning tuple from function")

def tuple_1(t):
    print(t)
    print(type(t))
    for i in t:
        print(i)
    return t

tup=(10,20,30,'shy',60)
t12=tuple_1(tup)
print(t12)
print(type(t12))

#list of tuples
print("list of tuples")
a=[10,20,30,(40,50)]
print("Original List A:",a)
print(id(a))
print(type(a))
print()

#appending a new tuple
a.append((210,32))
print("After appending a tuple:",a)
print(id(a))
print(type(a))

#asseccing list of tuples using for loop
for i in range(len(a)):
    if type(a[i]) is tuple:
        n=len(a[i])
        for j in range(n):
            print(i,j,a[i][j])
    else:
        print(i,a[i])

#tuple of lists
print("tuple of lists")
a=(98,88,909,[20,78])
print("Original tuple:",a)
print(id(a))
print(type(a))
print()

#modifing list 
a[3][0]=46
print("modified list of tuple:",a)

# set type == et in mathematics
print("set type")
#a set does not accpet duplicate values
#represented by {}
#sets are mutables
#elements can be of different types except like lists,sets and dictionaries are a big nooooo.
#we cannot access ssets using indexs
#empty set =set() cause {}<-- this is taken by dic so set is made by set()
a=set()
print(a)
a={44,56,10,67,'aman',10,56,98} #eliminate duplicate values
print(a)
# print(a[0])  <== not possible
print(type(a))
print(id(a))

#adding one element in set==
# syntax==
# set_name.add(new_element)
a=set()
a.add('Aman')
print(a)
a={30,20,'Python',90,89}
a.add("Aman")
print(a)
#adding multiple elements==
#syntax==
# the update() method can take tuples,lists,strings and other sets as its arguments
# set_name.update(elements)
a={"aman",687,76,222,3}
print("Before adding A:",a)
print(id(a))
a.update([101,102,103])
print("After aadding A:",a)
print(id(a))
print(a)

#deleting a element in set
# we use
# remove() and discard() method
# Remove() method raise error while the element doesn't exist whereas discard() method remains unchanged
a={12,23,25,4,3,'aman',3,23,43432,'yo'}
print(a)
print(id(a))
a.discard("aman")
a.remove(23)
print(a)
print(id(a))

#accessing set with for loop
print("accessing set with for loop") 
#without index=only this is posible
a={12,23,25,4,3,'aman',3,23,43432,'yo'}

for i in a:
    print(i)

#getting input from user
print("getting input from user")
a=set()
print(id(a))

n=int(input("Enter number of elements:"))

for i in range(n):
    el=input("Enter elements:")
    a.add(el)

print(a)
print(id(a))
for i in a:
    print(i)

#copying set elements = copy() Method is used to copy existing set's elements into another set
print("copying set elements")
# new_set_name=set_name.copy()
new_a=a.copy()
print("Before copying:",a)
print("After copying:",new_a)
print(id(a))
print(id(new_a))

#clearing set all elements = Clear() method is used to remove all elements
print("clearing set all elements")
# set_name.clear()
a.clear()
print(a)  #gives empty set 
