
class Students:
    def __init__(self,name,roll_no,classs,address):
        self.n=name
        self.rn=roll_no
        self.c=classs
        self.a=address
    
    def show_details(self):
        print(f'Name:{self.n} ,Roll_no:{self.rn} ,Class:{self.c} ,Address:{self.a}')