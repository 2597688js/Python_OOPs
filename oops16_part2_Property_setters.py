class Don:
    def __init__(self):
        self._age = 0

    # using property decorator
    # a getter function
    @property
    def age(self):
        print("getter method called")
        return self._age

    # a setter function
    @age.setter
    def age(self,a):
        if (a<8):
            raise ValueError("Sorry your age is below eligibilty criteria")
        print("setter method called")
        self._age = a

don = Don()
don.age = 19

print(don.age)