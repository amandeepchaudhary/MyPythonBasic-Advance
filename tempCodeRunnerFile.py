
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
sleep(6)
print("End Session",current_thread().name) #this main thread is executing itself between the execution of t1 thread So,we will make it Daemon so when the non-daemon thread executes the execution of daemon thread stops
# or we can use join to execute the t1 thread first
