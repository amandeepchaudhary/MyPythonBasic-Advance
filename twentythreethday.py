#Constructor
class Myname:
    def __init__(self):   #init is the constructor 
        #and the variables inside init is instance variables
        print("I am the constructor")
        self.model="Chaudhary"
    
    def saymyname(self):
        self.model      #accessing instance variables
        print("My name is:",self.model)

aman=Myname()
aman.saymyname()
aman.model    #accessing instance variable outside class 
print()

####changes are seen differently in every object

#class variable/Static Variable:::::
class Myname:
    fp="yes"    #class variable::::This will be same for all objects
    def __init__(self):   #init is the constructor 
        #and the variables inside init is instance variables
        self.model="Chaudhary"
    
    def show_model(self):
        self.model      #accessing instance variables

    @classmethod    #Class Method::::
    def is_fp(cls):  #accessing class variable inside class method
        #as self, cls is mandatory for class method
        print("Finger Print:",cls.fp)       

aman=Myname()
ishu=Myname()
sunita=Myname()

print("aman:",Myname.fp)
print("ishu:",Myname.fp)
print("sunita:",Myname.fp)
print()
Myname.fp="no"
Myname.is_fp()  #class_name.class_variable ::#accessing class varibale outside the class

print("aman:",Myname.fp)
print("ishu:",Myname.fp)
print("sunita:",Myname.fp)
print()
print()

#namespace

class Mobile:
    fp="Yes"
    
    @classmethod
    def is_fp(cls):
        print("Finger Print:",cls.fp)

realme=Mobile()
samsung=Mobile()
apple=Mobile()

print("Class FP:",Mobile.fp)
print("Realme FP:",realme.fp)
print("Samsung FP:",samsung.fp)
print("Apple FP:",apple.fp)
print()

Mobile.fp="No"

print("Class FP:",Mobile.fp)
print("Realme FP:",realme.fp)
print("Samsung FP:",samsung.fp)
print("Apple FP:",apple.fp)
print()

samsung.fp="Not Available"

print("Class FP:",Mobile.fp)
print("Realme FP:",realme.fp)
print("Samsung FP:",samsung.fp)
print("Apple FP:",apple.fp)
print()

#Instance Methods
class Mobile1:
    def __init__(self):
        self.model="Iphone 14"
    def show_model(self,p):
        self.price=p
        print(self.model,self.price)

aman=Mobile1()
aman.show_model(70000)

#Accessor Method////Getter Method
print(f"to read or access the data")
#Mutator Method////Setter Method
print("to modify the data")

class Mobile:
    def __init__(self):
        self.model="Samsung fold"
    def get_model(self):
        return self.model
    def set_model(self):
        self.model="Samsung flip"

samsung=Mobile()
s=samsung.get_model()
print(s)
print()
print(samsung.model)
samsung.set_model()
print(samsung.model)
print()

class Mobile:
    @classmethod                #Decorator
    def show_model(cls):        #Class Method
        print("Aman_Is_Brand")  

no=Mobile()
Mobile.show_model()             #Calling Class Method

#for handling class variable we need class method:::: 
class Mobile:
    fp="Yes"                    #Class Variable/Static var
    @classmethod                #Decorator
    def show_model(cls,r):        #Class Method
        cls.ram =r
        print("Finger Print Scanner:",cls.fp)  
        print("RAM:",cls.ram)

no=Mobile()
Mobile.show_model("4 GB")             #Calling Class Method

#static methods:::::::
#  class se related kuch kaam krna ho pr class ke object ki jarurat nhi padegi isse:::::::::::::::::::::::::
#when we want to pass some values from outside and perform some action on the method
#we use @staticmethod above the static method
# simple like function in core python with @staticmethod without any default parameter i.e..,cls or self

'''
@staticmethod
def method_name():      def method_name(p1,p2)
    method body
'''
print()
class Mobile:
    fp="Yes"
    @staticmethod
    def show_model(m,p):
        model=m
        price=p
        print("Model:",m,"& Price:",p)
        print("FingerPrint:",Mobile.fp)

# aman=Mobile()
Mobile.show_model("X", 50000)

#Passing members of one class to another class:::::::::::
class Student:
    #Constructor
    def __init__(self,n,r):    #parameters /Formal Arguments
        self.name=n            #Instance Variables
        self.roll_no=r
    #Instance Method
    def disp(self):
        print("Student Name:",self.name)
        print("Student Roll Number:",self.roll_no)

class User:
    # Static Method
    @staticmethod
    def copy(c):
        print("User Name:",c.name)
        print("User Roll Number:",c.roll_no)
        c.disp()

stu=Student("Aman", 21)
User.copy(stu)
print()

#Nested Class::::::!!!!!!!!!!!!!
class Army:                     #Outer Class
    def __init__(self):
        self.name="Aman"
        self.gn=self.Gun()      #Creating Inner Class Object
    def disp(self):
        print("Name:",self.name)

    class Gun:
        def __init__(self):
            self.name = "AK47"
            self.capacity = 75
            self.length = 34.3
        def disp(self):
            print("Gun name:",self.name,",Gun length:",self.length,"& Gun Capacity:",self.capacity)

ar = Army()
print(ar.name)
ar.disp()
# print(gn.name)     #this will show error we have to go step by step like>>>>>>>>>>>>
print(ar.gn.name)
print(ar.gn.capacity)
print(ar.gn.length)
ar.gn.disp()
print()

g=ar.gn
g.disp()
