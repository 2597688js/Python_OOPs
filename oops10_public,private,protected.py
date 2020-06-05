# Public - Anywhere it can be accessed
# Protected -  Jitu class t define kora hoise aru tar pora derive kora classbur (ie., tar child class bur) t access koribo pari.
# Private - Jitu class t define kora hoise, only xeitu class t he access koribo parim.

class Employee:
    no_of_leaves = 8                        # class variable / and it is public
    var = 8                                 # class variable /  public variable
    _protec = 9                             # protected variable - it starts with a underscore(_)
    __private = 10                          # private variable - it starts with double underscore (__)
    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The name is {self.name}, Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls,new_leaves):
        cls.no_of_leaves = new_leaves

    @classmethod
    def from_dash(cls,string):
        params = string.split("-")
        return cls(params[0],params[1],params[2])

    @staticmethod
    def printgood(string):
        print("This is good " + string)



emp = Employee("Harry",455,"Instructor")
print("Public : ",emp.var)                      # accessing public variable
print("Protected : ",emp._protec)                  # accessing protected variable
print("Private :",emp._Employee__private)        # accessing private variable -- Syntax : object._className__privateVariableName
