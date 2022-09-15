
from threading import *     #Lock,Thread,current_thread
class Flight:
    def __init__(self,avail_seats):
        self.avs=avail_seats
        self.l=RLock()
        print("Default:",self.l)   

    def num_of_seats(self,need_seats):
        self.l.acquire(blocking=True,timeout=4)    #can use multiple times but release it multiple times too and it locks multiple times 
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
