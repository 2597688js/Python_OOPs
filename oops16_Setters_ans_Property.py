# https://www.python-course.eu/python3_properties.php          See this link for better understanding


class Employee:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        #self.email = f"{fname}.{lname}@gmail.com"
    def explain(self):
        return f"This employee is {self.fname} {self.lname}"
    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return  "Email is not found. Please set it using setter"
        return f"{self.fname}.{self.lname}@gmail.com"

    @email.setter
    def email(self,string):
        print("Setting now ...")
        names = string.split("@")[0]
        fname = names.split(".")[0]
        lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

hindustani_supporter = Employee("hindustani","supporter")
#nikhil_raj_pandey = Employee("Nikhil","Raj")

print(hindustani_supporter.explain())
print(hindustani_supporter.email)

hindustani_supporter.fname = "US"

print(hindustani_supporter.email)

hindustani_supporter.email = "this.that@gmail.com"

print(hindustani_supporter.fname)
print(hindustani_supporter.lname)

print(hindustani_supporter.fname)

del hindustani_supporter.email

print(hindustani_supporter.email)

