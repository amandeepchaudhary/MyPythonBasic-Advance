#Multitasking
# Process Based Multitasking==executing different tasks at the same time where each task is a seperate independent program(process), this is used in operating systems level.
# Thread Based Multitasking==executing different tasks at the same time where each task is the part of one single program(process), this is used in Programming Level. 

#Thread is seperate flow of Execution,every thread has a task, and each task is independent from other task

import threading
th=threading.current_thread().getName()
print("Aman")
print(th)   #gives mainthread that is always running,       created by PVM
print()


#Creating Thread Without a Class = Our Own Thread
from threading import Thread

def disp(a):
    for i in range(5):
        print("Child Thread",a)

t=Thread(target=disp,args=(12,))  #arguments always in tuple, if single then a "," will add to show that this is the single tuple
t.start()  #used to start the thread 

for i in range(5):
    print("Main Thread")    #as this operation is done by the main thread and the child thread operation is done by thread_1

# and the positions of Execution are not discribable as both the Threads are working Seperately
#its like we have to upload 10 videos, we can use range and for loop to upload them one by one in numeric order, but in thread we assign two different threads to do a single work to do it quickly and efficiently and they do the work ina complete random way like any video downloader download a file in parts like it downloads the middle part then some part before the ending something similar like that 
#its like rendering 
#two threading doing there own work simultaneously in a single program
print()


#Setting and Getting Thread
from threading import Thread,current_thread

def disp():
    print("Child Default Object:",current_thread())
    print("Child Default Thread Name:",current_thread().getName())
    current_thread().setName("Laado")
    print("Child New Name:",current_thread().getName())

t=Thread(target=disp)
t.start()

print("Default Main object:",current_thread())
print("Default Main thread Name:",current_thread().getName())
current_thread().setName("Aman")
print("New Main Thread Name:",current_thread().getName())


#we use name instead for getname and setname for better things>>>>>>>>>>>

from threading import Thread,current_thread
def disp():
    print("Default Child Thread:",current_thread().name)
    current_thread().name='AMAN'
    print("New Child Thread Name:",current_thread().name)

t2=Thread(target=disp)
t2.start()

print("Default Main thread:",current_thread().name)
current_thread().name='DIKSHA'
print("New Main Thread Name:",current_thread().name)

def desp():
    pass

t=Thread(target=desp)
print(t.name)
t.name="Mummy"
print("New name",t.name)

def sen():
    pass

t34=Thread(target=sen, name="Loha")
print(t34.name)

#Creating a Threading by Creating a Child Class to Thread Class == Our Own Thread

from threading import Thread
class MyThread(Thread):
    def run(self):  #rum is a method from Thread class
        for i in range(5):
            print("Child class of Thread Class")

c1 = MyThread()
print(c1.name)
c1.start()  #start the Thread
c1.join()   #want to execute the Thread first out of others

for i in range(5):
    print("Main Thread")
print()


#Thread Child class with Constructor>>>>>>>>>>>>>>
from threading import *

class Mychild(Thread):
    def __init__(self,a):
        Thread.__init__(self) #always use Thrad class constructor if using the child class constructor
        self.a=a
        print("Child Thread Class parameter:",self.a)

    def run(self):
        pass

c2=Mychild(210)
c2.start()
print("Main Thread:",current_thread().name)

#Creating a thread without creating a child class to thread class>>>>>>>>>>>>>>>>>>>>
#we target the object of simple class>>>

class thrdwoC:
    def di(self,a,b):
        print("Thread without child class:",a,b)

dip=thrdwoC()
c3=Thread(target=dip.di(45,76))

#Single Tasking using a Thread >>>>>>>>
#in exam we solve Questions One by One SO,
from threading import Thread
from time import sleep
class MyExam:
    def solve_questions(self):
        self.q1()
        self.q2()
        self.q3()
    def q1(self):
        print("Solved Question 1")
        sleep(1)
    def q2(self):
        print("Solved Question 2")
        sleep(1)
    def q3(self):
        print("Solved Question 3")
        sleep(1)
mye = MyExam()
t56=Thread(target=mye.solve_questions())
t56.start()
print()

#Multitasking using Multiple Thread>>>>>>>>>>>>>
#when multiple tasks are executed at same time it is called multitasking. For this we need more than one thread and it is called multithreading>>>

from threading import Thread

class Hotel:
    def __init__(self,s):
        self.s=s
    def wait(self):
        for i in range(1,6):
            print(self.s, i)

h1=Hotel("Taking Order From Table:")
h2=Hotel("Serving Order to Table:")
t111=Thread(target=h1.wait)
t222=Thread(target=h2.wait)
t111.start()        #isme kabhi kabhi serving pehle aa rha h order dene se so its a "Race Condition". 
t222.start()
print("***************")

#Race Condition>>>>>>>>>>>>>>>

from threading import Thread,current_thread
class Flight:
    def __init__(self,avail_seats):
        self.avs=avail_seats
    def num_of_seats(self,need_seats):
        print('Available Seats:',self.avs)
        self.nos=need_seats
        if self.avs>=self.nos:
            name=current_thread().name
            # if self.nos==1:
            #     name=input("Enter the name of passenger:")
            # else:
            #     name=input("Enter the name of passengers:")
            print(f'{self.nos} Seats are Booked for {name}')
            self.avs-=self.nos
            # print('Now Remaining Number of Seats are:',self.avs)
        else:
            print('Sorry! There are no Available seats')

ft=Flight(1)
t333=Thread(target=ft.num_of_seats, args=(1,), name='Aman and Diksha')
t444=Thread(target=ft.num_of_seats, args=(20,), name='Aman and Diksha and Gang')
t333.start()
t444.start()    #race condition hai jisme dono thread khte h ki pehle main krunga execute code ko
#Race condition is a situation that occurs when threads are acting in an unexpected sequence, thus leading to unreliable output

#Thread Synchronization
#when many threads are trying to acces the same object, can lead to problems, when a thread accessing a object remaining threads are prevented from accessing the same object
#the object on which many threads are synchronized is called Synchronized Object or Mutually Exclusive Lock(mutex)
# Thread Synchronization is recommended when many threads are acting on the same object simultaneously

# 1.Using Locks
# 2.Using RLock(Re-Entrant Lock)
# 3.Using Semaphores

######LOCK#############################################
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
from threading import *     #Lock,Thread,current_thread
class Flight:
    def __init__(self,avail_seats):
        self.avs=avail_seats
        self.l=Lock()

    def num_of_seats(self,need_seats):
        self.l.acquire()
        print('Available Seats:',self.avs)
        self.nos=need_seats
        if self.avs>=self.nos:
            name=current_thread().name
            # if self.nos==1:
            #     name=input("Enter the name of passenger:")
            # else:
            #     name=input("Enter the name of passengers:")
            print(f'{self.nos} Seats are Booked for {name}')
            self.avs-=self.nos
            # print('Now Remaining Number of Seats are:',self.avs)
        else:
            print('Sorry! There are no Available seats')
        self.l.release()

f=Flight(20)
t555=Thread(target=f.num_of_seats, args=(12,),name='Aman')
t666=Thread(target=f.num_of_seats,args=(3,), name='vidya')
t777=Thread(target=f.num_of_seats,args=(3,), name='bhanu')
t888=Thread(target=f.num_of_seats,args=(3,), name='hitesh')
t999=Thread(target=f.num_of_seats,args=(3,), name='jayant')
t555.start()
t666.start()
t777.start()
t888.start()
t999.start()
t555.join()
t666.join()
t777.join()
t888.join()
t999.join()     #used join to execute these threads first then the main thread
print("Main Thread")
print()

#R(reentrant) Lock = object acquired multiple times by a same thread

from threading import *     #Lock,Thread,current_thread
class Flight:
    def __init__(self,avail_seats):
        self.avs=avail_seats
        self.l=RLock()
        print("Default:",self.l)   

    def num_of_seats(self,need_seats):
        self.l.acquire(blocking=True,timeout=-1)    #can use multiple times but release it multiple times too and it locks multiple times 
        self.l.acquire()
        print("Locked And Count 2 as written two times:",self.l)
        print('Available Seats:',self.avs)
        self.nos=need_seats
        if self.avs>=self.nos:
            name=current_thread().name
            # if self.nos==1:
            #     name=input("Enter the name of passenger:")
            # else:
            #     name=input("Enter the name of passengers:")
            print(f'{self.nos} Seats are Booked for {name}')
            self.avs-=self.nos
            # print('Now Remaining Number of Seats are:',self.avs)
        else:
            print('Sorry! There are no Available seats')
        self.l.release()
        self.l.release()
        print("Unlocked at Released two times:",self.l)

f=Flight(20)
t55=Thread(target=f.num_of_seats, args=(12,),name='Aman')
t66=Thread(target=f.num_of_seats,args=(3,), name='vidya')
t77=Thread(target=f.num_of_seats,args=(3,), name='bhanu')
t88=Thread(target=f.num_of_seats,args=(3,), name='hitesh')
t99=Thread(target=f.num_of_seats,args=(3,), name='jayant')
t55.start()
t66.start()
t77.start()
t88.start()
t99.start()
t55.join()
t66.join()
t77.join()
t88.join()
t99.join()     #used join to execute these threads first then the main thread
print("Main Thread")
print()

#Semaphore = in this e can assign number of threads we want to use to process the one object
# and boundsemaphore for release error as we can give infinite number of release in Semaphone but not in BoundedSemaphore


from threading import *     #Lock,Thread,current_thread
class Flight:
    def __init__(self,avail_seats):
        self.avs=avail_seats
        self.l=BoundedSemaphore(2)     #2 is number of threads we want to enter the object at same time
        print("Default:",self.l)   

    def num_of_seats(self,need_seats):
        self.l.acquire()    #can use multiple times but release it multiple times too and it locks multiple times 
        print("Locked two Threads as written two times:",self.l._value)
        print('Available Seats:',self.avs)
        self.nos=need_seats
        if self.avs>=self.nos:
            name=current_thread().name
            # if self.nos==1:
            #     name=input("Enter the name of passenger:")
            # else:
            #     name=input("Enter the name of passengers:")
            print(f'{self.nos} Seats are Booked for {name}')
            self.avs-=self.nos
            # print('Now Remaining Number of Seats are:',self.avs)
        else:
            print('Sorry! There are no Available seats')
        self.l.release()
        print("Unlocked at Released two times:",self.l)

f=Flight(20)
t5555=Thread(target=f.num_of_seats, args=(12,),name='Aman')
t6666=Thread(target=f.num_of_seats,args=(3,), name='vidya')
t7777=Thread(target=f.num_of_seats,args=(3,), name='bhanu')
t8888=Thread(target=f.num_of_seats,args=(3,), name='hitesh')
t9999=Thread(target=f.num_of_seats,args=(3,), name='jayant')
t5555.start()
t6666.start()
t7777.start()
t8888.start()
t9999.start()
t5555.join()
t6666.join()
t7777.join()
t8888.join()
t9999.join()     #used join to execute these threads first then the main thread
print("Main Thread")
print()
