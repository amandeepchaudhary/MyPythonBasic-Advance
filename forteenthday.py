from numpy import *

#Attributs of numpy array
a=array([101,102,103,104,105])
b=array([[10,20,30,40],[50,60,70,80]])
print()
#ndim attribute
print("1D array ndim:",a.ndim)
print("2D array ndim:",b.ndim)
print()
#shape attribute
#for 1D array shape elements in the row
#for 2d array shape specifies number of row and column in each row
print("1D array shape:",a.shape)
print("2D array shape:",b.shape)
print()
#size Attribute
print("1D array size:",a.size)
print("2D array size:",b.size)
print()
#itemsize attribute
print("1D array itemsize:",a.itemsize)
print("2D array itemsize:",b.itemsize)
print()
#dtype attribute
print("1D array dtype:",a.dtype)
print("2D array dtype:",b.dtype)
print()
#nbytes attribute
print("1D array nbytes:",a.nbytes)
print("2D array nbytes:",b.nbytes)
print()

#String in python
aman='''hello guys
            my name is aman'''

amand="""yo 
        boy"""

str3='Hello "me aman" kaise ho'
str4="Hello 'me aman' kaise ho"
str5="Hello \nme aman kaise ho"
#--raw string is ussed to nullify the effect of escape characters
str6=r"Hello \nme aman kaise ho"
print(str5)
print(str6)
for el in str3:
    for ch in el:
        print(ch)

print("negative")
str3="hello boi"
x=len(str3)
print(x)
for el1 in range(0-1,-(len(str3)+1),-1):
    print(str3[el1])
    # l=len(el1)
    # # x=range((l-(l+1)),l-(2*l),-1)
    # # print(x)
    # for ch1 in range(l,0-1,-1):
    #     print(ch1)
    #     print("Index",ch1,"=",el1[ch1])

#Mutable and Immutable objects 
# Mutable can be changes==list,set,dictionaries
# Immutable objects can not be changed==numbers,String,tuples

# Immutable String
str1="aman"
# str1[2]="an" not possible but you can resassign like srt1="ishu"
print(str1)

for c in str1:
    print(c)

#repetition operator
# used to repeat a string several times by multiply sign(*)
print("$"*7)     
str1="amanbhai"
#slicing in string repetition
print(str1[0:4]*5)

#concatenation operator--used to join two strings. It is denoted by(+)
print("Aman"+" Bhai")
str1="Aman"
str2=" Bhai"
str3=str1+str2
print(str1+str2)
print(str3)

print("hello"+str1) #--isme space apne app nhi milta
print("hello",str1,"kya hal hai") #--isme space apne aap mil jta h
#comparing strings
str1="aman"
str2="aman"
result= str1 == str2
print(result)

str1="aman"
str2="python"
result= str1 == str2
print(result)

str1="A"
str2="B"
print(str1<str2)

str1="acquaint"
str2="acne"
print(str2<str1)

#Formatting string
# C-styling formatting XXXXNOXXXX
#format() method XXXXNOXXXX
#fstring/Formatted string literal====
#integers==
print("*****Interger******")
a=10
b=20
print(f"{a}")
# print(f"{}") --not allowed
print(f"{a}      {b}")
print(f"{b}{a}")
print(f"my age is {a}")
value=f"{a}"
print(value)
#float==
print("*****Float******")
c=10.47
d=20.647
print(f"{a}")
# print(f"{}") --not allowed
print(f"{c}      {d}")
print(f"{d} {c}")
print(f"my age is {c}")
value=f"{c}"
print(value)
#String==
print("*****String******")
f_name="Aman"
l_name="Singh"
print(f"{f_name}")
# print(f"{}") --not allowed
print(f"{f_name}      {l_name}")
print(f"{l_name} {f_name}")
print(f"my name is {f_name}")
value=f"{f_name}"
print(value)
#integer and string
print("*****Interger and String******")
name="aman"
age=22
print(f"my name is {name} and i am {age} years old")
print(f"{name} {age}")
print(f"{age} {name}")

#integer with format specifiers
print("****integer*****")
num= 15
print(f"{num}")
print(type(f"{num}"))
print(f"{num:d}")
print(type(f"{num:d}"))
print(f"{num:5d}")
print(type(f"{num:5d}"))
print(f"{num:05d}")
print(f"{num:+5d}")
print(f"{num:<5d}")
print(f"{num:*<5d}")
print(f"{num:*>5d}")
print(f"{num:^5d}")
print(f"{num:*^5d}")

#Floating point number
print("***Floating point numbers***")
num=15.678
print(f"{num:8f}")
print(f"{num:8.2f}")
print(f"{num:+8.2f}")
print(f"{num:08.2f}")
print(f"{num:+08.2f}")
print(f"{num:<8.2f}")
print(f"{num:$<8.2f}")
print(f"{num:>8.2f}")
print(f"{num:*>8.2f}")
print(f"{num:^8.2f}")
print(f"{num:@^8.2f}")

#String formatting
print("***String***")
name="Aman"
print(f"{name:8s}")
print(f"{name:<8s}")
print(f"{name:>8s}")
print(f"{name:^8s}")
print(f"{name:!<8s}")
print(f"{name:%>8s}")
print(f"{name:!^8s}")
print("***more string format specifiers***")
name="Amandeep"
print(f"{name:.4s}")
print(f"{name:16.4s}")
print(f"{name:!>16.4s}")
print(f"{name:!^16s}")
print(f"{name:!<16.4s}")

#More fstring operators
print("***Thousand operator***") #--',' and '_'
price=1805.009765
print(f"{price:,.6f}")
print(f"{price:_.6f}")
print("**Expessions**")
print("10*8")
print(type("10*8"))
print(f"{10*8}")
print(type(f"{10*8}"))
print(10*8)
print(type(10*8))

a=50
b=3
print(f"{a/b:.290000000}")
print(f"{a/b:.290000000f}")
print(f"{a/b:.29%}")

print("**how to get value**")
#tuple
value=(10,20)
print(f"{value[0]} {value[1]}")
#dictionary
data={'aman':25000,'sonam':34000}
print(f"{data['aman']:$>6d} {data['sonam']:$>6d}")

print("**Applying functions**")
name="Amandeep Singh"
print(f"{name.upper()}")

print(f"{10}")
print(f"{{10}}")

#date and time
print("***date and time***")
from datetime import datetime
today= datetime(2022,8,31,2,40,50)
print(f"{today}")
print(f"{today:%d-%b-%Y}")
print(f"{today:%d %b,%Y}")
print(f"{today:%d/%b/%Y}")

#String functions
print("***String Functions***")
name="hello aman"
print(name.upper())
print(name.lower())
print(name.swapcase())
print(name)
print(name.title())
E=input("Enter Your full name:")
U_name=E.title()
print(U_name)
print(E.title())

#string functions to find the case is true or not
print("**String functions to find the case is true or not**")
name="Amandeep Singh"
str1=name.isupper()
print(str1)
str1=name.islower()
print(str1)
str1=name.istitle()
print(str1)

#isdigit() used to know that a string has numeric value only then returns True
name="47398475"
print(name.isdigit()) #--True
name="4739AMAN475"
print(name.isdigit()) #--False
print("!")
#isalpha() used to know that a string has only character values without space and no other datatype values (str,int,float,etc)then returns True
name="AMANdeep Singh"
print(name.isalpha()) #--False
name="173"
print(name.isalpha()) #--False
name="Amandeep"
print(name.isalpha()) #--True
name="A"
print(name.isalpha()) #--True
print("!!")
#isalnum() is alpha numeric means both numeric and character type values with no space between them are there and it will check that and returns True if both are present without space
name="amandeep Singh 1"
print(name.isalnum()) #--False

name="a 1"
print(name.isalnum()) #--False
name="aman1"
print(name.isalnum()) #--True
name="a1"
print(name.isalnum()) #--True
print("!!!")

#isspace() if only space is there in my string then it will return True if we add anything in the str then it will retuwn false
name="             amna"
print(name.isspace()) #--False
name=" "
print(name.isspace()) #--True
print("!!!!")

#lstrip() is used to remove space which are at left side of the string
lstrip_name="    Amandeep Singh   o"
print(lstrip_name)
print(lstrip_name.lstrip())
print("!!!!!")
#rstrip() is used to remove space which are at right side of the string
rstrip_name="Amandeep Singh   o k     o            "
print(rstrip_name)
print(rstrip_name.rstrip())
print("!!!!!!")
#strip() is used to remove space from the both side of the string
strip_name="    Amandeep Singh   o       "
print(strip_name)
print(strip_name.strip())
print("!!!!!!!")

#Replace() *****************************************
print("<<Replace Is IMPORTANT>>")
print("as string is immutable which means a='aman' {a[2]=an}--this is not possible but we can do this action by replace() Function but the orignal string will remain same and we have to assign a new variable to the modified string")
print("^^Replace Is IMPORTANT^^")
replace_name="Amandeep"
old ="deep"
new =" Singh"
r_name=replace_name.replace(old,new)
r1_name=replace_name.replace("Aman","Ran")
print(r_name)
print(r1_name)
print(replace_name)
#split('separator') 
print("**Split**")
split_name="how-are-you-aman"
s_name=split_name.split('-')
split_name="Aman Singh"
s_name=split_name.split(' ')
s0_name=s_name[0]
s1_name=s_name[1]
print(s_name)
print(s0_name)
print(s1_name)
#join()=='separator'.join(str_name) 
print("**Join**")
join_name=('Aman', "Hello",'ok')
j_name='_'.join(join_name)
j_name=' '.join(join_name)
print(join_name)
print(j_name)
 
#startswith('specified_string')==this method is used to chexk whether a string  is starting with a substring or not. It returns True if the string is starting with a substring
print("**Startswith**")
startswith_name="Hi how are you"
print(startswith_name.startswith('Hi'))   #--True
print(startswith_name.startswith('aman')) #--False
#endswith('specified_string')
print("**Endswith**")
endswith_name="Hi how are you?"
print(endswith_name.endswith("?")) #--True
