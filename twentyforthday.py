#Inheritance::::::::::::
#Sabse Badi Object Class Hai
# parent and child class
#types of inheritance
# 1.single inheritance
# 2.multi level inheritance
# 3.hierarchical inheritance
# 4.Multiple inheritance

#Single Inheritance:::::::::::::
'''
 syntax::::

class ChildClassName(ParentClassName):
    Members of Child class

'''

class Father(object):
    money=1000      #class Variable
    
    def show(self):
        print("Parent class Instance method")

    @classmethod
    def showmoney(cls):
        print("Parent class Class Method:",cls.money)
    @staticmethod
    def static():
        a=10
        print("Parent Class Static Method:",a)

class Son(Father):
    def disp(self):
        print("Child Class Instance Method")

s=Son()
s.disp()
s.show()
s.showmoney()
s.static()
print()

f=Father()
f.show()
f.showmoney()
f.static()
print()

#Constructor in Inheritance
class Father:
    def __init__(self,m):
        self.money = m
        print("Parent class Constructor")
    def disp(self):
        print("Father class instance method")
class Son(Father):
    def show(self):
        print("Child class Instance method:",self.money*9000)

s=Son(23000)
s.show()
print(s.money)
s.disp()
print()

#Constructor OverRiding::::::::::::::@@@@@@@
# if we write constructor in both parent class and child class then the parent class's constructor is not available for child class
class Father:
    def __init__(self,m):
        self.money = m
        print("Father class Constructor")

    def show(self):
        print("Father Class Instance Method")

class Son(Father):
    def __init__(self,r):
        self.money = r
        self.car = 'Royal Royce'
        print("Son class Constructor")

    def dis(self):
        print("Son Class Instance Method")

s=Son(39920)    #39920 will go in r as child class constructor parameter
print(s.money)
print(s.car)
s.dis()
s.show()
f=Father(300)
# if child class constructor is there then parent class constructor will not show
print()

print()
#how can we call parent class Constructor if we have child class Constructor
#IMPORTANT>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# super() method is used to call parent constructor if the child constructor is overriding it
class Father:
    def __init__(self):
        print("Parent class Constructor")
    
    def show(self):
        print("Parent class Instance Variable")

class Son(Father):
    def __init__(self):
        super().__init__()
        print("Child class Constructor")

    def shown(self):
        print("Child Class Instance Method")

s=Son()
print()

#MUlti level inheritance
class Father:
    def __init__(self):
        print("Father Class Constructor")
    def showF(self):
        print("Father Class Instance Method")

class Son(Father):
    def __init__(self):
        super().__init__()
        print("Son Class Constructor")
    def showS(self):
        print("Son Class Instance Method")

class GrandSon(Son):
    def __init__(self):
        super().__init__()
        print("GrandSon Class Constructor")
    def showGS(self):
        print("GrandSon Class Instance Method")

gs=GrandSon()
#if we want constructor of father and son in grand son then call super in grand son for son's constructor and super in son for father's constructor by that grandson will have all the three constructors
#and all the variables and methods are already here in the grandson class for accessing
print()


#Hierarchical Inheritance
#one super class having two or more sub classes 
#father class having son and daughter class
#there is no relation between son and daughter class

class Father:
    def __init__(self):
        print("Father class Constructor")
    def showF(self):
        print("Father class Instance Method")

class Son(Father):
    def __init__(self):
        super().__init__()
        print("Son class Constructor")
    def showS(self):
        print("Son class Instance method")

class Daughter(Father):
    def __init__(self):
        super().__init__()
        print("Daughter class Constructor")
    def showD(self):
        print("Daughter class Instance Variable")

s=Son()
print()
d=Daughter()
print()
s.showF()
s.showS()
d.showF()
d.showD()
print()
#but
# d.showS()   #not possible as daughter and son class are not related
# s.showD()   #not possible as daughter and son class are not related
print()


#Multiple Inheritance::::::::::

# two or more super classes inherited by a single sub class
#father and mother class inherited y son class

class Father:
    def __init__(self):
        super().__init__()
        print("Father Class Constructor")
    def showF(self):
        print("Father Class Instance Method")

class Mother:
    def __init__(self):
        super().__init__()
        print("Mother Class Constructor")
    def showM(self):
        print("Mother class Instance method")

class Son(Father,Mother):
    def __init__(self):
        super().__init__()
        super().__init__()
        print("Son Class Constructor")
    def showS(self):
        print("Son class Instance Method")

#the serach will start from calling the son class, then it will go parent father class constructor, then parent of father class that is object will be called, objject doesn't have any constructor so it will go to right that is mother class, then mother parent class has the parent constructor so the cursor goes to object class again But the object class is already visited so the search will stop here, then it will start to give the output while returning from mother parent class to son class
so=Son()

so.showF()
so.showM()
so.showS()

