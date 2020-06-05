# ketiaba amak enekua lage j jodi kunu eta class r pora beleg eta class a inherit kori ase, tente ami tak aitu order dibo paru j, kunuba eta particular method
# tat thakiboi lagibo.

#from abc import  ABCMeta, abstractmethod   # upto python 3.4 and above
from abc import  ABC, abstractmethod   # for above python 3.4


#class Shape(metaclass=ABCMeta):
class Shape(ABC):                     # for python 3.4 and above
# This is a Abstract Base Class, iyar ami object bonabo nuaru.
    @abstractmethod
    def printarea(self):  # aitu eta abstract method, ai Shape class tur pora kunu class a inherit korile tat ai printarea mrthod tu thakiboi lagibo
        return 0

class Recatangle(Shape):
    type = "Rectangle"
    sides = 4
    def __init__(self):
        self.length = 6
        self.breadth = 7

    def printarea(self):
        return self.length * self.breadth

#shape = Shape()   # Abstract base class r object bonabo nuari

rect1 = Recatangle()
print(rect1.printarea())