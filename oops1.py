class Student:
    pass

harry = Student()  # instance or object of the class Student
larry = Student()

print(harry,larry) # aitu saboloi j harry aru larry blg blg object hoi

harry.name = "Harry"   # instance variable
harry.std = 12         # instance variable
harry.section = 1      # instance variable
larry.std = 9
larry.subject = ["hindi","english"]

print(harry.name)
print(larry.subject)