
# Dunder or magic methods in Python are the methods having two prefix and suffix underscores in the method name. Dunder here means “Double Under (Underscores)”.
# These are commonly used for operator overloading. Few examples for magic methods are: __init__, __add__, __len__, __repr__ etc.
# The __init__ method for initialization is invoked without any call, when an instance of a class is created.
# Dunder methods are used for operator overloading


class Employee:
    no_of_leaves = 8  # class variable

    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The name is {self.name}, Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls,new_leaves):
        cls.no_of_leaves = new_leaves

    def __add__(self, other):
        #return self.name + other.name
        return self.salary + other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __repr__(self):
        return f"Employee('{self.name}',{self.salary},'{self.role}')"

    def __str__(self):
        return f"The name is {self.name}, Salary is {self.salary} and role is {self.role}"

    def __mul__(self, other):
        return self.salary * other.salary

emp1 = Employee("Harry",345,"Programmer")
emp2 = Employee("Rohan",45,"Cleaner")

print(emp1 + emp2)

print(emp1/emp2)

print(emp1*emp2)

print(emp1)               # e first t str method sabo, str method nathakile he repr loi jabo
print(repr(emp1))        # exclusively repr call korisu
