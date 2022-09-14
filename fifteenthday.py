#Functions
# 1. build in like print(),upper(),lower() and etc
# 2. user defined==important
# syntax==
# def funtion_name():               -|
#     local variable                -|=Function
#     block of statements           -|=Body
#     return(variable or expression)-|

#syntax==
# def funtion_name(parameter1,parameter2,...):  -|
#     local variable                            -|=Function
#     block of statements                       -|=Body
#     return(variable or expression)            -|
#Note= need to maintain proper indentation
#Reusablility=======================*************
#Defining a function
#function with argument
def add(a,b):  #==parameter
    c=a+b
    print(c)

a=int(input("Enter first number for addition= "))
b=int(input("Enter second number for addition= "))
#calling a function
add(a,b)  #==argument
add(a,b)  #==argument   ===Reusability
add(a,b)  #==argument

def disp():
    func_name="Aman"
    print(f"Welcome {func_name:!>8s}")
    print(f"Welcome",func_name)
disp()
disp()
disp()

#Divide large task into small tasks====******************
#defining function
#funtion Without argument
def add():
    x=10
    y=20
    c=x+y
    print(c)

add()

def sub():
    x=10
    y=20
    c=x-y
    print(c)

sub()

#return statement
#isme hume call krte hue calling function ko 
# kisi variable m store krwana padta h jabki 
# without return wale m hum print likhte te function k andar hi
# and function jab call hota tha toh voh value dikha deta tha

def add(y):
    x=100
    c=x+y
    return(c)


func_return=add(2009)
print(func_return)
print("***********")

def add(y):
    x=100
    return(x+y)


func_return=add(2009)
print(func_return)
print("**********")

def add_sub(y):
    x=2900
    c=x+y
    d=x-y
    return(c,d)


func_return=add_sub(int(input("Enter the number for add_sub:")))
print(func_return)

print("**********")

def add_sub(y):
    x=2900
    c=x+y
    d=x-y
    return(c,d)


func_return1,func_return2=add_sub(int(input("Enter the number for add_sub:")))
print(func_return1)
print(func_return2)

print("**********")

#Return Statement with multiple values
print("*******Return Statement with multiple values**********")
def add_sub(y):
    x=2900
    c=x+y
    d=x-y
    return(c,d,500)


func_return1,func_return2,func_return3=add_sub(int(input("Enter the number for add_sub:")))
print(func_return1)
print(func_return2)
print(func_return3)

#Nested Function
def disp():
    def show():
        print("Show Function")
    print("Display Function")
    show()

disp()

print("***With return statement***")
def disp(st):
    def show():
        return "Show Function"
    nestfunc_return=show() + " Display Function"+ st
    return nestfunc_return

nested_func_return=disp("Aman")
print(nested_func_return)
print(disp("Aman"))

#pass a function as a parameter
def disp(sh):
    print("Display Function" + sh())
    
def show():
    return ("Show Function")

disp(show)

print("****")
def disp(sh):
    return "Display Function" + sh()
    
def show():
    return ("Show Function")

func_as_a_para=disp(show)
print(func_as_a_para)

#Funstion returning another function
def disp():
    def show():
        return "Show function"
    print("Display Function")
    return show()

Function_return_ano_func=disp()
print(Function_return_ano_func)

print("********")
def disp(sh):
    print("Display function")
    return sh()

def show():
    return "Show function"

function_return_ano_func_as_para=disp(show)    
print(function_return_ano_func_as_para)

#Actual and Formal Argument
print("*****Actual and Formal Argument****")
def disp(name):
    print("hi ",name)

disp("aman") 
# aman is actual argument where as the parameter(name) name is formal argument


#Types of actual arguments 
print("*****Types of actual arguments *****")
#1..Positional Argument
#2..Keyword Argument
#3..Default Argument
#4..Variable Length Argument
#5..Keyword Variable Length Argument
print("****1..Positional Argument****")
def pa(x,y):
    z=x**y
    print(z)
pa(5,3)
#humme 125 hi chahiye h pr agr hum inhe flip kr denge toh ans bhi change hoga
pa(3,5)
# pw(5,3,2) -- this will not execute
print("****2..Keyword Argument****")
def ka(name,age):
    print("my name is",name,"and my age is",age)
    print(f"Name:{name} and Age:{age}")

ka(name="Aman",age=22)
#keyword argument is good kyuki bina key k dete h argument ko toh ==
ka(22,"aman")  #===toh ulta seedha aata h upper ki accordance/position k hisab se
ka(age=22,name="Aman")

#default keyword
print("****3..Default Argument****")
def dv(name,age=22):
    print(f"Name:{name} Age:{age}")

dv("Aman")
dv(name="Aman")
dv("Aman",27)
dv(name="Aman",age=27)

print("****4..Variable Length Argument****")
#the variable length argument is written with ''''*''''
#it stores all value in tuple
#so i can provide n number of arguments and it will take it without no error
#--!!use when do not know hoe many argyuments will be there!!--
def VLA(*num):
    z=num[0]+num[1]
    print(z)
VLA(12,3,2,12,3,23,637,"aman")

def VLA(*num):
    for i in range(len(num)):
        print(num[i])

VLA(3,23,637,"aman")
print("****!!!!!!!!!*****")


def VLA(x,*num):
    z=x+num[0],num[1],num[2],num[3]
    print(z)
VLA(3,23,34,637,"aman")

print("****5..Keyword Variable Length Argument****")
#the keyword variable length argument is written with ''''**''''
# it stores all the values in Dictionary in the form of key-value format
def KVLA(x,**num):
    z=x + num['a'] + num['b'] + num['c']
    print("Addition",z)

KVLA(2,a=347,b=277,c=5879,d=7938)

print("_______________________")

#Anonymous Function or Lambda 
print("--------Lambda--------")
#a function without a name is called a lambda function
#anonymous function is not defined by def keyword rather they are defined using lambda keyword 
#doesn't have any name
#returns function
#lambda function contains can take zero or any number of arguments but only one expresion
#no need to write return statement
#only expressions no statements like:- if,else,for loop etc.
#can use all type of actual arguments-positional,keyword,default,variable length(*),keyword variable length(**)
sum_lambda=lambda x,y:print(x+y)  #here sum_lambda is the function name that is assigned to this lambda 
sum_lambda(5,3)
sum_lambda1=lambda x:x+1
print(sum_lambda1(44))
print("***")

def show(x):
    print(x) #==function ek expression bhi h statement bhi h but expression alag hota h

show(3764628)
print("***")

store=lambda x:print(x)
store(12321)
print("***")

sum_sub_lambda=lambda x,y:(x+y,x-y,x*y,x**y,x/y)  #here sum_sub_lambda is the function name that is assigned to this lambda 
a=sum_sub_lambda(45,15)
for i in range(len(a)):
    print(a[i])

a,b,c,d,e=sum_sub_lambda(45,15)
print(a)
print(b)
print(c)
print(d)
print(e)

#using type of actual arguments in lambda
Aa=lambda x,y=4:x + y
print(Aa(x=356))

#nested lambda function
nested_lambda= lambda x=100:(lambda y:x+y)
print(nested_lambda())
nl=nested_lambda()  #--lambda x return krta h lambda y ko nested_lambda m as a expression
print(nl(1000))
print()

#passing lambda function to another function
def disp(sh):
    print(sh(98))

disp(lambda x:x)
disp(lambda x:x+x)
print()

#returning lambda function from function
def return_lambda_from_func():
    y=128
    return (lambda x: x+y)

rlff=return_lambda_from_func()
print(rlff(22))

#Immediately Invoked Function Expression--IIFE--Jaise hi likhte h vaise hi call ho jata hai
#no need for calling this function
IIFE=lambda x:x+5
IIFE(3)

(lambda x:x+5)(65)

#more than one argument
IIFE=lambda x,y:x+y
IIFE(3,67)

(lambda x,y:x+y)(65,5)  #==not recommended cause smjh nhi aayega kuch din mai code ko dekhenge toh

#Local variables
# local variable is accessed inside the function only
def disp(y):
    v=109
    print(v)
    print(v+y)

disp(10)
#print(v) #==this is not possible as the variable 'x' is only availbale 
            #inside the function in which it is created i.e.., local variable

#Global Variables
a=51
def gv():
    x=100
    print(a)
    print(x)
gv()
#print("x:",x)  #--not possible as it is local variable
print("a:",a)

# drawback if same name
i=0
def myglobalfun():
    i=0    #<<<<this needs to be done if wants python to understand what we want to doo
    i=i+1   #this won't work as python needs local variable to assign the value if the variable_name matched from a global variable (then we use global keyword for this scenario)
    print("My Function:",i)

myglobalfun()

#Global Keyword =if local and global has same name then the function by default use
#  local variable not the global variable so we use this keyword to use global keyword
i=50
def globalkey():
    global i   #the changes in global varible will be reflected in global too means now i=i+10 ==60 so the global i's value is now 60
    i=i+10
    print("I:",i)

globalkey()   #showing local variables values
print(i)

i=0
def myfun():
    global i
    while i<5:
        print(i)
        i+=1

myfun()
print("Global:",i)
print(f"Global: {i}")
#if i want ki function k andar global ki value change
#  ho aur mujhe changed value use krni ho toh global lga
#  k function k andar global value use kro nahi toh local
#  variable banao aur usse use kro agr global wali value 
# m change nhi chahiye h toh

print("______________*")
#globals() function - returns a table of current global 
# variables in the form of dictionary 
print("********Globals() function**********")
#if we want both variable local bhi and global bhi with 
# the same name but they both are having different value toh
i=50

def globals_fun():
    i=10
    print("local variable i:",i)
    x=globals()['i']  #--by this the values we change will be changed of the x variable not the global variable's 
    print("""Global Variable with golbals() function within the 
    function having same variable_name X:""",x)
    x=40
    print(x)

globals_fun()
print()
