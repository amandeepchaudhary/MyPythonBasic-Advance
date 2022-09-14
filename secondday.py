#Output statement and Print Function
a=10
b='34'
print(list(b))
print("","like", "share", "subscribe", sep='Please')
print('anab', end=' ')
print('fvyy', end=' ')
print("ryt")
a=10
b=30
print('This is the time right now:' ,a,b,sep=':')
name= 'rahul'
age=45
print('my name is',name,"and my age is",age)
#the   45.67
#    9489.678 the point must be at the same positions ,we will learn this in formatting


#Taking Input from the User like Scanner in JAVA
# name24 = input()
# print(name24,',you have a nice name')
print("i love python")
mobile= input('your mobile number is:')
print(mobile)
mb= int(mobile)
print(type(mb))

#Escaoe sequences
print("Welcome to CodeWithAman")
print("Welcome to\nCodeWithAman")
print("Welcome to\tCodeWithAman")
print("Welcome to\'CodeWithAman")
print("Welcome to \"CodeWithAman\"")

#if Statement
if 5>2:
    print('5 is greater than 2')
    print('this is a experiment')
a= int(input("Enter number greater than 2:"))
if(a>2):
    print('You have entered the right number that is:',a)

#Nested if
if(5>2):
    print("Greater")
    print("5 is greater than 2")
    if(6>2):
        print("greater")
        print("6 is greater than 2")
    if(7>2):
        print("greater")
        print("7 is greater than 2")
print('rest of the code')

#if Statement with Logical Operators
if(7>2):
    print("if sattement with logical operators")
print("Rest of the Code")

aui=int(input('enter a number for if statement:'))
auo=int(input('enter second number for if statement:'))
if(aui>2 and auo>2):
    print('the input numbers are greater than 2')
    print('the numbers are:',aui,"and",auo)
print("if statement with logical operators is done!")

#if else Ststements
asd= 5
asf=2
if(asd>asf):
    print("if is printing as condition is True")
else:
    print("the else statement is executing as the condition is False")
#we can print all this in one line
#print this if (condition) else print this
print("if is printing in one line Scenario") if (asd>asf) else ("else is printing as in one line scenario")


#Nested if else 
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c=int(input("Enter the value of c:"))
d=int(input('Enter the value of d:'))
if(a>b):
    print('a is greater than b')
    if(c>d):
        print("c is greater than d")
    else:
        print("d is greater than c")    
else:
    print("b is greater than a")
print('Rest of the Code')


#if elif Statement
a=10
b=20                 #only one statement will execute after that it will break the loop
if(a>b):
    print("a is greater than b")
elif(a==b):
    print("a is equal to b")
elif(a<b):
    print("a is smaller than b")

#if elif else Statement
day=input("Enter the day\n")
if(day=="Monday" or day=="monday"):
    print("Today is Monday")
elif(day=="Tuesday" or day=="tuesday"):
    print("Today is Tuesday")
elif(day=="Wednesday" or day=="wednesday"):
    print("Today is Wednesday")
else:
    print("Today is Holiday")


#While loop 
a=2
while(a<=20):
    print(a)
    a+=2
print("Rest of the Code") 
print("\n\n\n\n\n")
#While else statements 
a=1
while(a<=5):
    print(a)
    a+=1
else:
    print("The loop has ended and the else statement of the of the while loop is executed")
print("Rest of the code")

#when the condition got false on first try 
a=6
while(a<=5):
    print(a)
    a+=1
else:
    print("The loop has ended and the else statement of the of the while loop is executed")
print("Rest of the code")


