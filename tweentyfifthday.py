#Polymorphism
# 1. Duck Typing
# 2. Operator Overloading 
# 3. Method Overloading
# 4. Method Overriding

#Duck typing

class Duck:
    def walk(self):
        print("tapak tapak tapak tapak")

class Horse:
    def walk(self):
        print("Tagdak Tagdak Tagdak Tagdak")

class Cat:
    def talk(self):
        print("Meaw Meaw Meaw Meaw")

def myfunction(obj):
    obj.walk()  #this function didn't have any relation whether the obj is duck or horse it simply show the method if it is present in the obj object  

d=Duck()
myfunction(d)
h=Horse()
c=Cat()
print()

#Cheaking if the method is present in the obj or not
#is Called Strong Typing

class Duck:
    def walk(self):
        print("tapak tapak tapak tapak")

class Horse:
    def walk(self):
        print("Tagdak Tagdak Tagdak Tagdak")

class Cat:
    def talk(self):
        print("Meaw Meaw Meaw Meaw")

def myfunction(obj):
    if hasattr(obj, "walk"):
        obj.walk() 
    if hasattr(obj, "talk"):
        obj.talk()
#Hence, this will not give an error if the method is not present , this is called strong typing

h=Horse()
myfunction(h)
c=Cat()
myfunction(c)
print()

#Method Overloading = methods in a class having same names
# in java we have method overloading but in python we try to achieve it with different methods
# in java we do it like this>>>>>>>>>>>>>
# if we call a method having parameters then the parameterized method will be called as java identifies this automatically

class sum1:
    def sum(self,a):
        print("1st Sum Method:",a)
    
    def sum(self):
        print("2nd Sum Method:")

# obj=sum1()
# obj.sum(2)      #by this in java we can call the parameterized method
# obj.sum()       #and by this we can call the unparameterized method

#######But in python this will not work and always call the last method of the same name that will be the "2nd Method"

# in python

class Myclass():
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:
            s="Atleast Give Two Parameters"
        return s    

obj=Myclass()
o=obj.sum(200, 300) #if we give 2 parameters then it will give error, this can solve by if else in method and giving default values to the parameters
#after giving default values none to the parametres the sum will not happen as the none and int cannot add 
# so we do use the if else statements  
print(o)
print(obj.sum(100))
print(obj.sum(100,1000,2900))

#Method Overriding::::when the son class has the same named method as the father class then the father class method is overrided by the son class method like the constructors
#so we use super here tooo

class Father:
    def salary(self):
        print("Father class Instance Method")

class Son(Father):
    def salary(self):
        print("Son class Instance Metthod Having same name")

s=Son()
s.salary()
print()

#now we want the father class instance method which is overrided by the son class instance method having same name 
#we will use super()

class Father:
    def salary(self,office,passive,savings):
        self.resulted=office+passive+savings
        print(f"Father class Instance Method:Total Income:{self.resulted}, Office:{office}, Passive:{passive}, Savings:{savings}")

class Son(Father):
    def salary(self,office,passive):
        super().salary(40000,20000,3000000)    #we have to assign values for parent class in super() method
        self.result=office+passive
        print(f"Son class Instance Metthod Having same name:Total Income: {self.result}, Office:{office}, Passive:{passive}")

s=Son()
s.salary(10000, 4000)
#used when want both the father and child class methods of same name
print()

#Operator Overloading:::::::::

print(10+20)
print('aman'+"chaudhary")
print(str.__add__('aman','chaudhary'))  #in background
# int.__add__(self,other)
print(int.__add__(10,200))
print()

class A:
    def __init__(self,x):
        self.x=x
    def __add__(self,other):        #runs automatically
        return self.x + other.x

class B:
    def __init__(self,x):
        self.x=x

a = A(204)
b = B(303)
print(a+b)   #A.__add__(self,other)     Magic Functions
# a.__add__(other)

#Module::::::::::
#on module folder twentysixthday