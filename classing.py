#create a class
#have a unique function and pass in args as parameters
#create object of the array.
from array import array
from mimetypes import init


class People:
    def __init__(self,*pizo):
        self.pizo=pizo
        # return f"the block box has{self}"
    def greet_me(self):
        return  f"The dice has {self.pizo} blocks"
for name in init.__dict__:
    print(name)
# def somebody(*green):n
#create a function and pass in args as argumnts.
#use return type and End function.
def Somezy(*met):   
    return f"{met} are the number of students present"

    
    
    