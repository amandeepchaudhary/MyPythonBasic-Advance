#ok here i am tested whether the cursor go to next line or after the ending of the line .... and succeed

#nested dictionary
#a dictionary within aniother dictionary 

# nested_dict={'dict a':{key_a1:value_a1},
#              'dict b':{key_b1:valueb1}}

a={"dict1":{101:'aman',102:'ishu'},
"dict2":{101:"rowdy",102:'tela'}}
print(a)             

aa={'course':"python",'fees':18000,'next_course':{"course":"java","fees":2000}}
print(aa)
print(aa['course'])
print(aa['next_course']['course'])

for i in aa:
    if type(aa[i]) is dict:
        for j in aa[i]:
            print(i,j,aa[i][j])
    else:
        print(i,"=",aa[i])

aa['course']='Machine Learning'
print(aa['course'])
del aa['next_course']['fees']
print(aa)

aa['duration']='6 months'
print(aa)
aa['next_course']['Teacher']='souma'
print(aa)

aa['course2']={'course':'django','fees':12000}
print(aa)

{'course': 'Machine Learning', 'fees': 18000,'duration': '6 months', 
'next_course': {
                'course': 'java', 'Teacher': 'souma'
                },  
'course2': 
                {
                'course': 'django', 'fees': 12000
                }
}

aa={'course':"python",'fees':18000,'next_course':{"course":"java","fees":2000}}

aa['next_course']['course3']={'course':"MySql","fees":"3000"}
print(aa)

{   'course': 'python', 'fees': 18000, 
    'next_course': {
                    'course': 'java', 'fees': 2000, 'course3': 
                        {'course': 'MySql', 'fees': '3000'
                        }
                    }
}

# forloop
print("forloop")
for i in aa:
    if type(aa[i]) is dict:
        for j in aa[i]:
            if type(aa[i][j]) is dict:
                for k in aa[i][j]:
                    print(i,j,k,aa[i][j][k])
            else:
                print(i,j,"=",aa[i][j])
    else:
        print(i,"=",aa[i])

a12=aa.keys()
a13=aa.values()
print(a12)
print(a13)

#passing dicionary to function

def show(d):
    print(d)
    print(type(d))
    for i in d:
        print(i,"=",d[i])
    return d

dic={1:'aman',2:'ishu'}
d1=show(dic)
print(d1)
print(type(d1))


#Comprehension
#contains very compact code usually a single statement that performs a task
#list comprehension
#set comprehension
#dictionary comprehension
# syntax====
# name=[expression for i in object if statements]

#without list comprehension
lst=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
lst1=[]
for i in lst:
    lst1.append(i+1)

for i in range(20):
    lst1.append(i+1)

print(lst1)

#with list comprehension
lst=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
lst2=[i+1 for i in lst]
print(lst2)
lst2=[i+1 for i in range(20)]
print(lst2)

#with condition 
lst1=[]
for i in range(20):
    if(i%2==0):
        if(i%3==0):
            lst1.append(i)

print(lst1)

#with list comprehension
lstt1=[i for i in range(20) if (i%2==0) if (i%3==0)]
print("New list:",lstt1)

#if else syntax==
# new_list=[expression if_statement else expression for item in iterable_object]
lst1=[]
for i in range(20):
    if(i%2==0):
        lst1.append(i)
    else:
        lst1.append("Invalid")

print(lst1)

lst22=[i if(i%2==0) else "Invalid" for i in range(20)]
print(lst22)

lstt22=[[i*j for j in range(4,7)] for i in range(6,8)]
print(lstt22)


#set comprehension
#same as list but chane of brackets '{}' set.add(i)
#nested nhi banta

#dict comprehension
dict1={}
for n in range(10):
    if (n%2==0):
        dict1[n]=n*2
    
print(dict1)

#comprehension
dict2={n:n*2 for n in range(10) if(n%2==0)}
print(dict2)


dict1={}
for n in range(10):
    if (n%2==0):
        if(n%3==0):
            dict1[n]=n*2
        else:
            dict1[n]="Invalid after 3"
    else:
        dict1[n]="Invalid after 2"
print(dict1)

#comprehension
dict2={n:n*2 if(n%3==0) else "Invalid afteR 3" if(n%2==0) else "Invalid After 2" for n in range(10) }
print(dict2)

#tuple to list using comprehension
lst234=[(101,'aman'),(102,'ram')]

lst34={k:v for k,v in lst234}
print(lst34)

#membership operator
# in and not in

#core python end********************************************

# Advance  python Starts************************************

str="Object oriented programming"
s1=str.title()
print(s1)
# is a programming model in which see problems and connect them to real world which helps us to solve them efficiently
o="1. Encapsulation"
print(o)