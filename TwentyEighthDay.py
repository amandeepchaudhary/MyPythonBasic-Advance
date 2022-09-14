#Multitasking
# Process Based Multitasking==executing different tasks at the same time where each task is a seperate independent program(process), this is used in operating systems level.
# Thread Based Multitasking==executing different tasks at the same time where each task is the part of one single program(process), this is used in Programming Level. 

#Thread is seperate flow of Execution,every thread has a task, and each task is independent from other task

import threading
th=threading.current_thread().getName()
print("Aman")
print(th)   #gives mainthread that is always running,       created by PVM


#Creating Thread Without a Class = Our Own Thread
