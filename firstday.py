import re


print("hello world")
#OPERATORS
#Arithematic operators
# print(4+2)
a,b=12,2
total= a+b
print(total)
#likewise subtraction and multiplication and division
value=a/b
print(value)
print(type(value))
#modulus
print(5%3)
value1= a%b
print(value1)
print(5**2)
print(5//2)
print(-5//3)
#Relational operators
print(5<2)
q=2
w=8
value3=q!=w
print(value3)
#Logical Operators
#Logical AND
a=5
b=2
c=3
print(a>b and c and 300 and c)    #if true Last exp will be shown
print(b>a and 200 and 34)   #if false then false will be shown 
#Logical OR
print(a>b or 300 or 456)    #if true then true will be shown
print(a<b or 76 or 67 or 6790)   # if false then exp1 will be shown
#Logical NOT
a=34
b=45
print(not(a>b))  #not(true) is false, not(false) is true.
#Assignment Operators
m=15
a=10
b=20
y=a+b #'=' 
print(y)
#m+=10 or
m = m+10   
print(m)
m-=10   #m=m-10
m*=10   #m=m*10   
m/=10   #m=m/10
m%=10   #m=m%10
m**=2   #m=m**2
m//=10  #m=m//10
#Bitwise Operators
a=10        #0000 1010
b=15        #0000 1111

print('~a=',~a)
print('a&b=',a&b)
print('a|b=',a|b)
print('a^b=',a^b)
print('a<<2=',a<<2)
print('a>>2=',a>>2)

#Membership Operator        #also works with String, tuple, lists and dictionaries.
#in
st1 = "Welcome to CodeWithAman"
print("to" in st1)
st2 = "Welcome top CodeWithAman"   #detect the sequence that 't' with 'o' is there or not
print("to" in st2)
st3= "Welcome to CodeWithAman"
print("subs" in st3)

#not in
st1= 'welsome to CodeWithAman'
print('subs' not in st1)
tt= 'monday - work'
print('tell me are you free on monday')
an= 'free' not in tt
if(an==True):print('i am not free on monday')

#Identity Operators
#is
a=10
b=10
print(a is b)
a=10
b='10'
print(a is b)
#is not
a=10
b=10
print(a is not b)
a=10
b='10'
print(a is not b)
#OPERATORS FINISHED

#Operator precedence and associativity

#Implicit and Explicit Conversion
#implicit
a='me'
b='aman'
c= a+b
print(c)

# a=10
# b='10'  or b="Aman"
# c=a+b     ---> this is not possible in implicit as python 
                # is not able to conacatinate int and string 

a=4
b=3
value=a/b   #pyhton gives value of this in float automatically i.e., Implicit conversion
print(value)

#Explicit
a=45
b=34
value=a/b
print(type(value))
int_value = int(value)
print(type(int_value))
print(int_value)

#forcing a data type by explicit
q=10
u='10'          #this is possible as we forced the string to int and the thing in string 
                #co9nvert to int 10 that is possible
print(type(u))
r=q+int(u)
print(r)

# q=10
# u='aman'-------#this is not possible even though we forced it to int that gives error
# print(type(u))
# r=q+int(u)
# print(r)

#string to tuple
zn="aman"
nv= tuple(zn)
print(nv)
print(type(nv))

#string to list
zn="aman"
nv= list(zn)
print(nv)
print(type(nv))

#string to list
n=('aman','sihu','raj')
vn=list(n)
print(vn)
print(type(vn))
print(type(n))

#conveert into binary
n=10
result=bin(n)
print(result)
print(type(result))
print(type(n))

#direct show
n=10
print(bin(n))





