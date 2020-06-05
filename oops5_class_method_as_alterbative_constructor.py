## class varible and instance variable

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

karan = Employee.from_dash("karan-800-Student")
print(karan.no_of_leaves)
print(karan.printdetails())

# harry = Employee("Harry",455,"Instructor")
# larry = Employee("Larry",4554,"Student")
#
# print(larry.no_of_leaves)
#
# larry.change_leaves(89)
#
# print(larry.no_of_leaves)