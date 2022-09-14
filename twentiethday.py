print("revise slicing on list")
a=[[100,200,300],
[1000,489,67],
[908,786,789],
[890.5467,378]]

x=a[1:2][0][1:]
print(x)
y=a[2:3][0][1:]
print(y)
z=x+y
print(z)

#some important set methods
print("some important set methods")
#inersection method() = The values exist on both the sets will show having a as the main set
a={100,20,'rahul','devi','singh','aman','ishu'}
b={20,'aman',100,'devi','sunita','deep'}

print("A:",a)
print("B:",b)

ism = a.intersection(b)
print(ism)
#union
unim = a.union(b)
print(unim)
#difference
difm = a.difference(b)
print(difm)
#issubset
isssm = a.issubset(b)
print(isssm)
#issuperset
issusm = a.issuperset(b)
print(issusm)

#passing set to function
print("passing set to function")

def show(st):
    print(st)
    print(type(st))
    for i in st:
        print(i)

set1 = {100,200,700,'aman'}
show(set1)

#returning set to function
print("returning set to function")
def show(st):
    print(st)
    print(type(st))
    for i in st:
        print(i)
    return st

set1 = {100,200,700,'aman'}
s=show(set1)
print(s)
print(type(s))


#DICTIONARY
print("************DICTIONARY************")
# a dictionary represents a group of elements in the form of key value pairs
# empty dictionary
t={}
print(t)
stu={101:'aman',102:'ishu',103:"sunita",104:"surender"} 
print(stu)

print(stu[101])
print(stu[102])
print(stu[103])
print(stu[104])

fees={'rahul':20000,'aman':49500,'ishu':35000}
print(fees)

print(fees['rahul'])
print(fees['ishu'])
print(fees['aman'])


#modifing dictionary
stu={101:'aman',102:"ishu",103:"ram"}

print("Before modification:")
print(stu)
print(id(stu))
print()

stu[103]='sunita'
print("After modification:")
print(stu)
print(id(stu))
print()


#adding item in dictionary
stu={101:'aman',102:"ishu",103:"ram"}

print("Before adding:")
print(stu)
print(id(stu))
print()

stu[105]='surender'
stu[104]='dharmo'
stu['Name']='chandgi'

print("after adding:")
print(stu)
print(id(stu))
print()

#deletion in dictionary
# using del statement
stu={101: 'aman', 102: 'ishu', 103: 'ram', 105: 'surender', 104: 'dharmo', 'Name': 'chandgi'}
#delete an item toh del stu[102]
del stu[102]
#delete whole dictionary del stu
print(stu)

del stu

#testing key in dictionary
# whether the ket is present or not 
# we use membership operator
stu={101: 'aman', 102: 'ishu', 103: 'ram', 105: 'surender', 104: 'dharmo', 'Name': 'chandgi'}

print(102 in stu) #return True as 102 is in the dictionary stu
print(108 in stu)

print(108  not in stu) #as 108 is not in the dictionary stu so return True

#clear method = used to remove all elements in dictionary
#---> stu.clear()

#copying a dictionary
#stu.copy()
stu={10:'40',101: 'aman', 102: 'ishu', 103: 'ram', 105: 'surender', 104: 'dharmo', 'Name': 'chandgi'}

print("Original Dictionary:")
print(stu)
print(id(stu))
print()

stu1=stu.copy()

print("Copied Dictionary:")
print(stu1)
print(id(stu1))
print()

stu[10]=90
print(stu)
print(stu1)

#creating new dictionary by using fromkeys() method==like insert
#dic.fromkeys(keys, value)

key=(101,102,103)
values="Aman"
stu2=dict.fromkeys(key , values)
print(stu2)

#if values not given
key=(101,102,103)
stu2=dict.fromkeys(key)
print(stu2)

key=(101,102,103)
values=("aman","sawan","thand") #sabme pura ka pura tuple ayega
stu2=dict.fromkeys(key , values)
print(stu2)

#get() method
# this method returns the value of specified key
#dict.get(key, defaultvalue)
stu={10:'40',101: 'aman', 102: 'ishu', 103: 'ram', 105: 'surender', 104: 'dharmo', 'Name': 'chandgi'}

print(stu.get(104))
print(stu.get(108,"NotHere"))

#items() method=returns an object that contains key-value pairs of dictionary, stored as a tuple in the object
# dict_name.items()
stu={10: '40', 101: 'aman', 102: 'ishu', 103: 'ram', 105: 'surender', 104: 'dharmo', 'Name': 'chandgi'}

print("Original Dictionary:")
print(stu)
print(id(stu))
print()

it = stu.items()  #it will be tuple 
print(it)
print(type(it))
print()

lst = list(it)
print(lst)
print(type(lst))
print()

#accessing the elements
print(lst[0])  #we want the value or key give address accordingly
print(lst[0][1])  #we want the value or key give address accordingly

#accessing all
for i in lst:
    for j in i:
        print(j)

for i in range(len(lst)):
    for j in range(len(lst[i])):
        print(i,j,lst[i][j])

#keys() method = returns a sequence of keys 
# dist_name.keys()
'''
        stu[102]
        get()
        items()
        keys()
'''
stu={10: '40', 101: 'aman', 102: 'ishu', 103: 'ram', 105: 'surender', 104: 'dharmo', 'Name': 'chandgi'}
print("Original Dict:")
print(stu)
print()

all_keys=stu.keys()
print(all_keys)
print(type(all_keys))

keys_lst= list(all_keys)
print(keys_lst)
print(type(keys_lst))

print(keys_lst[0])
print(keys_lst[1])
print(keys_lst[2])
print(keys_lst[3])
print(keys_lst[4])
print(keys_lst[5])
print(keys_lst[6])
for k in keys_lst:
    print(k)

#values() method = returns a sequence of values from the dictionary
# dict_name.values()

stu={10: '40', 101: 'aman', 102: 'ishu', 103: 'ram', 105: 'surender', 104: 'dharmo', 'Name': 'chandgi'}
print("Original Dict:")
print(stu)
print()

all_value = stu.values()
print(all_value)
print(type(all_value))

lst= list(all_value)
print(lst)

for i in lst:
    print(i)

#update() Method = used to update the dictionary with the specified key value pair 
# dict_name.update(iterable)
#single^^^^
stu={10: '40', 101: 'aman', 102: 'ishu', 103: 'ram', 105: 'surender', 104: 'dharmo', 'Name': 'chandgi'}
print("Original Dict:")
print(stu)
print(id(stu))
print()

stu.update({106:'Gupchup'})
print("Updated Dict:")
print(stu)
print(id(stu))
print()

#multiple^^^^^^^^^^^^^

stu={10: '40', 101: 'aman', 102: 'ishu', 103: 'ram', 105: 'surender', 104: 'dharmo', 'Name': 'chandgi'}
print("Original Dict:")
print(stu)
print(id(stu))
print()

valu = {'age':45,'gender':"male",'fav_colour':"purple"}
stu.update(valu)
print("Updated Dict:")
print(stu)
print(id(stu))
print()

# pop() method= used to remove the item with specified key
# dict_name.pop(key, defaultvalue)
print("pop() method")
stu={10: '40', 101: 'aman', 102: 'ishu', 103: 'ram', 105: 'surender', 104: 'dharmo', 'Name': 'chandgi'}
removed_value1=stu.pop(10,"ValueNotPresent")
print(stu)
removed_value2=stu.pop(110,"ValueNotPresent")
print(stu)
print("Removed Value:",removed_value1)
print("Removed Value:",removed_value2)

#popitem() method==this is used to remove the item which was last inserted into the dcitionary
#return removed items in the form of tuple
# pairs are returned in LIFO (Last In First Out) order
# dict_name.popitem()
stu={10: '40', 101: 'aman', 102: 'ishu', 103: 'ram', 105: 'surender', 104: 'dharmo', 'Name': 'chandgi'}

p1=stu.popitem() #removed last  inserted
print(p1)

#setdefault() method = returns value of specified key, if key is not present then the key will be inserted 
# dict_name.setdefault(key,value)
stu={10: '40', 101: 'aman', 102: 'ishu', 103: 'ram', 105: 'surender', 104: 'dharmo', 'Name': 'chandgi'}

returned_value0=stu.setdefault(109,"gulab") #agar 109 hota toh return ho jata agr nhi h toh insert ho jayega
print(stu)
print("Returned Value:",returned_value0)

#accessing dictionary using for loop
stu={10: '40', 101: 'aman', 102: 'ishu', 103: 'ram', 105: 'surender', 104: 'dharmo', 'Name': 'chandgi'}
for k in stu:
    print(k)     #this will give keys soooo

for k in stu:
    print(k,"=",stu[k]) 

print(stu[102])

#user input in dictionary
a={}
n=int(input("Enter the number of elements you want in your dictionary:"))
for i in range(n):
    k=input("Enter Key:")
    v=input("Enter Value:")
    a.update({k:v})

print(a)
    