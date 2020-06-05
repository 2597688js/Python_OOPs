# Encapsulation means hiding the implementation details

## iyat ami Single inheritance(eta child a eta parents r pora he lobo) sam


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

class Programmer(Employee): # single inheritance -- iyat Programmer class a Employee class r guteibur methods lobo
    no_of_holidays = 56

    def __init__(self,aname,asalary,arole,languages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages = languages

    def printprogdetails(self):
        return f"The Programmer's name is {self.name}, Salary is {self.salary} and role is {self.role} and he knows {self.languages}"

harry = Employee("Harry",455,"Instructor")
larry = Employee("Larry",4554,"Student")

shubham = Programmer("Shubham",555,"Programmer",["python"])
karan = Programmer("Karan",777,"Programmer",["python","java"])

print(karan.printprogdetails())  # aitu Programmer class r pora ahise
print(karan.printdetails())     # aitu Employee class r pora ahise

print(karan.no_of_holidays)

