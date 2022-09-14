#Abstract class
#in abstract class we cannot define the method in parent class itself balki hum son class m define krte h isse nhi toh hume son class ko bhi abstract class banana padta h aur hum parent abstract class ka object nhi bana skte

from abc import ABC, abstractmethod

class Father(ABC):
    @abstractmethod
    def disp(self):
        pass
    
    def show(self):
        print("Concrete Method in father class")

# my = Father()   #This is not possible

class Child(Father):
    def disp(self):
        print("Child Class")
        print("Defining Abstract Method")

c=Child()
c.disp()
c.show()
print()

#Defence Example>>>>>>>>>>>>>>>>>>>>>>>>

class Defence(ABC):
    def __init__(self,country): #Constructor in Abstract Class
        self.ce=country
    @abstractmethod
    def defence(self,DefenceName):
        pass
    @abstractmethod
    def weapon(self,weapon):
        pass
    @abstractmethod
    def area(self,area):
        pass

    def UnderWhoseCOmm(self):
        print("Under The Command Of Government of",self.ce)

class Army(Defence):
    def defence(self,DefenceName):
        self.d=DefenceName
        print("Defence Name:",self.d)
    def weapon(self,weapon):
        self.w=weapon
        print("Weapon used:",self.w)
    def area(self,area):
        self.a=area
        print("Area On which the defence Control:",self.a)

class AirForce(Defence):
    def defence(self, DefenceName):
        self.d=DefenceName
        print("Defence Name:",self.d)
    def weapon(self, weapon):
        self.w=weapon
        print("Weapon used:",self.w)
    def area(self, area):
        self.a=area
        print("Area under the defence:",self.a)

class Navy(Defence):
    def defence(self, DefenceName):
        self.d=DefenceName
        print("Defence Name:",self.d)
    def weapon(self, weapon):
        self.w=weapon
        print("Weapon used:",self.w)
    def area(self, area):
        self.a=area
        print("Area under the defence:",self.a)

a=Army("India")
a.defence("Army")
a.weapon("Ak47")
a.area("Land")
a.UnderWhoseCOmm()
print()

af=AirForce("Sri Lanka")
af.defence("Air Force")
af.weapon("Fighter Jet")
af.area("Sky")
af.UnderWhoseCOmm()
print()

n=Navy("Nagaland")
n.defence("Navy")
n.weapon("Missiles")
n.area("Water")
n.UnderWhoseCOmm()
print()



#Interface
# in python interface class is called an abstract class which has no concrete method in it 

#an abstract class without Concrete method

#we use interface when all the features need to be implemented differently for different objects

#yaad rakhne k liye>>>>>>>>>>>>>>>>>>
#interface ek structure h jiske base p child class banegi<<<<<<<<<<<<<<<<<<<<<<<<<<<

from abc import ABC,abstractmethod
class Father(ABC):
    @abstractmethod
    def disp1(self):
        pass
    @abstractmethod
    def disp2(self):
        pass

class Child(Father):
    def disp1(self):
        print("Child Class Disp1")
        print("Father Class Inherited Child Class")
#we only define one abstract method so we cannot create object for Child Class>>>>>>>>>>

class GrandChild(Child):
    def disp2(self):
        print("Father class Disp2")
        print("Child class Inherited class")
#now both the methods are are defined in GrandChild Class so we can make the object of GrandChild Class

gc=GrandChild()
gc.disp1()
gc.disp2()

#abstract class have both concrete and abstract methods, whereas in interface only abstract methods are there
#we use abstract class when some common features are used by all classes, whereas we use interface when all features need to be implemented differently for different objects
#its a programers job to make a child class for an abstract class, but in interface any third party vendor will take resposibility to make child class

# Interface are slow Compared to Abstract Class