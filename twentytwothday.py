#Encapsulation
print("1. Encapsulation")
#== is used to encapsulate the names for preventing the (*********naming conflict********)    overright na ho isliye

#Abstraction
print("2. Abstraction")
#jo cheze jaruri hain voh dikhana bakki cheze side kar dena 
#user ko vahi dikhana jo uske mtlb ka hai baki jo uske mtlb ka nhi h vohnhi dikhana
#source and destination k bech mai jo kaam ho rha h voh chupana abstraction khlata hai

#Inheritance
print("3. Inheritance")
#father ki property bete ko inherit ho gyi 
# ek code kai class's mai use hoga toh inherit kr denge

#Polymorphism
print("4. Polymorphism")
#input alag alag pr function ka naam same ho pr outputs alag alag ho

#class and object
# attributes = same as variables like a=10
# methods = is same as functions

#variable k liye __init__
#method k liye like function

#Example 1
class Myclass(object):
    def show(self):
        print("I am a Method")
    
x=Myclass()
x.show()

#Example 2
class Myclass:
    def show(self):
        print("I am a Method 2")
    
x=Myclass()
x.show()

#Example 3
class Mobile:
    def __init__(self,m):
        self.model = m

    def show_model(self,p):
        price = p
        print("The model is:",self.model,"Price:",price)

realme=Mobile("Realme X7 Max")
print(realme.model)  #gives the variable of the object class
realme.show_model(29500)
print(id(realme))
print()

realme.model="Realme 9 pro"  #changing the variable
print(realme.model)  #changing the variable
realme.show_model(19550)  #gives value of this function
print(id(realme))
print()

redmi = Mobile("Redmi Note 10 pro")
print(redmi.model)
redmi.show_model(20000)
print(id(redmi))
print()

aman = Mobile("Amandeep")
print(aman.model)
aman.show_model(99999)
print(id(aman))
print()
