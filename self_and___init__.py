## class varible and instance variable

class Employee:
    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    no_of_leaves = 8    # class variable

    def printdetails(self):
        return f"The name is {self.name}, Salary is {self.salary} and role is {self.role}"

#harry = Employee()    # instance variable
# rohan = Employee()   # instance variable
#
# harry.name = "Harry"
# harry.salary = 455
# harry.role = "Instructor"
#
# rohan.name = "Rohan"
# rohan.salary = 4553
# rohan.role = "Student"

# print(rohan.printdetails())
# print(harry.printdetails())

# ------------------------------------------------------------------------------------
harry = Employee("Harry",455,"Instructor")
print(harry.salary)
print(harry.printdetails())