## class varible and instance variable

class Employee:
    no_of_leaves = 8    # class variable
    # ami class variable k class r porau acess koribo paru ba object r pora u paru. But, class variable k change koribo hole only class r pora he paru
    pass

harry = Employee()    # instance variable
rohan = Employee()   # instance variable

harry.name = "Harry"
harry.salary = 455
harry.role = "Instructor"
rohan.name = "Rohan"
rohan.salary = 4553
rohan.role = "Student"

print(harry.salary)

print(rohan.no_of_leaves)
print(rohan.__dict__)    # rohan r ki ki instance variable ase dibo
rohan.no_of_leaves = 9   # etia rohan r aru eta instance variable hol no_of_leaves
print(rohan.__dict__)
print(Employee.no_of_leaves)