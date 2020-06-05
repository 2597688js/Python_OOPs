
class Employee:
    no_of_leaves = 8  # class variable

    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The name is {self.name}, Salary is {self.salary} and role is {self.role}"

    @classmethod  # e eta decorator hoi, iyat self dibo nalage, instead it takes a 'cls' ji class bujai, amar iyat 'cls' a Employee class bujaise
    def change_leaves(cls,new_leaves):
        cls.no_of_leaves = new_leaves

    @classmethod # e enekua eta classmethod jak ami as a constructor use koribo paru. E etai string lobo aru amak eta object bonai dibo
    def from_dash(cls,string):
        params = string.split("-")
        return cls(params[0],params[1],params[2])

    @staticmethod
    def printgood(string):
        print("This is good " + string)
    # Static methods in Python are similar to python class level methods, the difference being that a static method is bound to a class rather than the objects for that class.
    #  This means that a static method can be called without an object for that class. This also means that static methods cannot modify the state of an object as they are not bound to it.
    # When we need some functionality not w.r.t an Object but w.r.t the complete class, we make a method static.
karan = Employee.from_dash("karan-800-Student")

karan.printgood("Karan")

Employee.printgood("Janarddan")
