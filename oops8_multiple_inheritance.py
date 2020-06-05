# Encapsulation means hiding the implementation details

## iyat ami Single inheritance(eta child a eta parents r pora he lobo) sam


class Employee:
    no_of_leaves = 8  # class variable
    var = 8
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

class Player:
    no_of_games = 4
    var = 9
    def __init__(self,name,game):
        self.name = name
        self.game = game

    def printplayerdetails(self):
        return f"The Player name is {self.name}, Game is {self.game}"


class CoolProgrammer(Employee,Player): # MULTIPLE INHERITANCE - iyat jitu first t likhisu tar __init__ function call hobo ie., Employee r mote hobo
    languages = ["C++","Python"]
    #var = 10
    def printlanguage(self):
        print(self.languages)


harry = Employee("Harry",455,"Instructor")
larry = Employee("Larry",4554,"Student")

shubham = Player("Shubham",["Cricket","Tennis"])
#print(shubham.printplayerdetails())

karan = CoolProgrammer("Karan",8999,"cool_programmer")
details = karan.printdetails()
print(details)

print(karan.var)   # first t iyar nijor class t jabo ie., CoolProgrammer t sabo var tu ase ne nai, jodi nai tente jitu class first loise ie., Employee r pora lobo
