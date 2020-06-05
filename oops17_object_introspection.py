# Object Introspection mane hoise object tur bikhoye enquery kora, j e kuntu class r pora ahise, e keneke store hoise etc.

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

skillf = Employee("Skill","F")
print(skillf.email)

print(type(skillf))     # skillf object tu kuntu class r pora ahise dibo

print(type("I am human"))

print(id("I am human"))      # e given string tur id dibo, jitu di string tu store hoise python r backend t

print(dir(skillf))       # ki ki methods aru attributes ase xeibur dibo

import inspect
print(inspect.getmembers(skillf))   # skillf r details pai jam