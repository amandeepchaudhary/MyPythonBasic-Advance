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
print()

#abstract class have both concrete and abstract methods, whereas in interface only abstract methods are there
#we use abstract class when some common features are used by all classes, whereas we use interface when all features need to be implemented differently for different objects
#its a programers job to make a child class for an abstract class, but in interface any third party vendor will take resposibility to make child class

# Interface are slow Compared to Abstract Class



#Time Module
from time import time, ctime, localtime

epoch = time()
print(epoch)

ct=ctime(epoch)
print(ct)

stobj=localtime()
print(stobj)
#we can access seperate data form localtime>>>>>>>

print(f"Year:{stobj.tm_year}",end="/ ")
print(f"Year Day:{stobj.tm_yday}",end="/ ")
print(f"Month Number:{stobj.tm_mon}",end="/ ")
print(f"Week day:{stobj.tm_wday}",end="/ ")
print(f"Month day:{stobj.tm_mday}",end="/ ")
print(f"Hours now:{stobj.tm_hour}",end="/ ")
print(f"Minutes now:{stobj.tm_min}",end="/ ")
print(f"Seconds now:{stobj.tm_sec}")

#datetime
from datetime import datetime
dt1 = datetime(year=2022,month=9,day=14)
dt2 = datetime(year=2022,month=9,day=14,hour=23,minute=59)
dt3 = datetime(2022,9,24)
dt4 = datetime(2022,9,14,00,1)

print(dt1)
print(dt2)
print(dt3)
print(dt4)

dtn=datetime.now()
print(dtn)

from datetime import date
d1 = date(year=2022, month=9, day=30)
d2 = date(2022,9,3)
print(d1)
print(d2)
print(d1.year)

cd1=date.today()
print(cd1)

from datetime import time
t43=time(hour=23,minute=34,second=45)
t43=time(23,34,59)
print(t43.hour)
print(t43)

#timedelta class>>>>>>>>>>>
#used to get a previous and Future dates
#we can use this in Subscriptions as user can see how many days are there for him to enjoy his/her subscription
from datetime import timedelta,date
td=timedelta(days=30)
d=date.today()  #can get todays date from date.today &
print(f"Date of Subscription:{d}")
print(f"Subscription End date:{d+td}")     #can get date after 30 days from timedelta
print(d-td)

i=31
print(type(i))
while i>0:
    print("Days Remaining for the subscription:",i)
    i-=1
print("Subscription is Over! Recharge to Enjoy services")

#Comparing two dates>>>>>>
from datetime import date 
d123=date(2022,3,22)
d234=date(2019,9,8)
print(d123==d234)
print(d123<d234)
print(d123>d234)
print(d123!=d234)

#Formatting date and time>>>>>>>>>>>>>>>
from datetime import datetime
d=datetime.today()
print(d)
print(type(d))
print()

a11=d.strftime("%m/%d/%y")
print(a11)
print(type(a11))
print()

a12=d.strftime("%B %d, %Y")
print(a12)
print()

a13=d.strftime("%d-%b-%y")
print(a13)
print()

a14=d.strftime("%H:%M:%S")  #gives hour in 24 hour Format
print(a14)
print()

a15=d.strftime("%I:%M:%S")  #Gives hour in 12 Hour Format
print(a15)
print()

#sleep() method = is used to stop execution of a program temporarily for a given amount of time. When this function  is called, PVM stops program execution for given amount of time
#It belongs to time module>>>>>>>>>>>>>>>

import time

for i in range(20): #in 0 sleep for 0 seconds and in 20 sleep for 20 Seconds
    print(i)
    if(i<20):
        time.sleep(i)

#calculating age 
from datetime import date
dob=date(2000,8,22)

t=date.today()
print(t)
age=t.year - dob.year-((t.month, t.day)<(dob.month,dob.day))
print(age)

print(2-False) #False is Zero(0)
print(2-True)  #True is One(1)