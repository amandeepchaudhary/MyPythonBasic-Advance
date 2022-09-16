#Thread Communication Event
#when two or More thread Communicated with each other

from threading import Thread,Event
from time import sleep  #kitni der tak red or green light hogi
#we are making two threads, one will do red light green light and the other will say walk ,both threads are communicating with each other so we need Events for that
def switch_light():
    sleep(3)
    e.set() #Event set method ,when this calls then it sets True
    print('Green Light On') 
    sleep(5)
    print('Red Light On')
    e.clear()   #it gives False 

def traffic():
    e.wait()
    i=0
    while e.is_set():
        print('You can Go.....',i)
        i+=1
        sleep(0.5)
    print('Program Done')
        
e=Event()   #Event class ka object banana padta h pehle
t1=Thread(target=switch_light)
t2=Thread(target=traffic)
t1.start()
t2.start()


#Advance Version of Communication object=<<<<<Condition>>>>>
#in object of event some times its overlapping with the other thread but in the CONDITION this will not happen
#isme lock k sath event mtlb Condition is Lock+Event, lock mai acquire and release krte hai,and event mai set() se true krte h clear() se false and wait se wait krwate h jab tak set() call na ho dusre wale ka ,Vaise hi Condition mai pehle lock lga dete h taki koi dusra thread na aaye phir usko commands dete h tab tak dusra thread dusre function m chala jata h vha p bhi acquire hota h aur hum wha wait call kr dete hain jisse ki jab tak notify ya release na ho tab tak wait kre dusre function ka thread jaise hi pehle function ka thread Conditionobj(cv).notify notify krta hai vaise hi ek object notify ho jata h ki time aa gya h dusre function ko chalane ka aur phir pehle wale se release() milta hai toh dusre wala call ho jata h and stateements run krta hai  
# iske object ko Condition Variable Khte hai 

#syntax== 
# from threading import Condition
# cv=Condition()

from threading import Thread,Condition
from time import sleep

lst=[]
def produce():
    cv.acquire()    #used to lock 
    for i in range(1,6):
        lst.append(input("Enter item:"))
        sleep(3)
    cv.notify()
    cv.release()

def consume():
    cv.acquire()
    cv.wait(timeout=0)
    cv.release()
    print('Produced Item List is:',lst)

cv=Condition()
t3=Thread(target=produce)
t4=Thread(target=consume)
t3.start()
t4.start()
print()

#Thread Communication=<<<<<<<Queue>>>>>>>>>
# q=Queue,q.full,q.empty,q.put(i),p.q.get(i)

from queue import Queue
from threading import Thread
from time import sleep

class Producer():
    def __init__(self):
        self.q=Queue()
    def produce(self):
        for i in range(1,6):
            print('Item produced:',i)
            self.q.put(i)
            sleep(1)    
class Consumer():
    def __init__(self,producer):
        self.prod=producer
    def consume(self):
        for i in range(1,6):
            print('all the items of the queue:',self.prod.q.get(i))

p=Producer()
c=Consumer(p)
t5=Thread(target=p.produce)
t6=Thread(target=c.consume)
t5.start()
t6.start()
print()

# <<<<<<<<<<<<<<<<<<<<AISE HI>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# from threading import Thread
# def lo():
#     for i in range(5):
#         print("produce m")

# def lol():
#     for i in range(5):
#         print("produce ok")

# t1=Thread(target=lo)
# t2=Thread(target=lol)
# t1.start()
# t2.start()
# <<<<<<<<<<<<<<<<<<AISE HI KA END>>>>>>>>>>>>>>>>>>>>>>>>>>

#Daemon Thread == is a Supportive thread for another thread

from threading import Thread
def disp():
    print('daemon Thread')

t7=Thread(target=disp)
print("Before:",t7.daemon)
# t7.setDaemon(True) #deprecated ho chukka h mtlb purana 
#OR
t7.daemon=True
print("After:",t7.daemon)
t7.start()

# Three Points for Interview>>>>>>>>>>>>>>>>>>>>
#1. Main Thread is Daemon or non-daemon
from threading import current_thread,Thread
mt=current_thread()
print(mt.name)
print(mt.daemon)
# ans. main thread is always non-daemon

#2.daemon or non-daemon nature ayyega apne parents se
from threading import Thread,current_thread

def disp():
    print("Non-daemon after conversion")
    t2=Thread(target=show)
    print("T2 Child of T1:",t2.daemon)
    t2.start()

def show():
    print("Show Function")

mt=current_thread()
print(mt.name)
print(mt.daemon)
t1=Thread(target=disp)
print("Before:",t1.daemon)  #non-daemon nature from MainThread
t1.daemon = True
print("After:",t1.daemon)   #converted t1 to Daemon
t1.start()
t1.join()       #as we want ki t1 thread pehle pura execute ho
print("Main Thread is here Boss!!!!!")

#3. When last non-daemon thread is terminated then all Daemon threads are also terminated automatically
#exam khtam hote i padai khtam, padhai k liye moral support khatam, teacher ka padhana khatam

from threading import Thread,current_thread
from time import sleep
def Teacher():
    for i in range(1,11):
        print("Teachers Session:",i)
        sleep(1)

t1=Thread(target = Teacher)
t1.daemon = True
t1.start()
# t1.join()
sleep(6)    #execute t1 for 6sec then execute the MainThread  
print("End Session",current_thread().name) #this main thread is executing itself between the execution of t1 thread So,we will make it Daemon so when the non-daemon thread executes the execution of daemon thread stops
# or we can use join to execute the t1 thread first

