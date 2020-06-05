# n this tutorial, you will learn about Python @property decorator; a pythonic way to use getters and setters in object-oriented programming.


# Class without Getters and Setters
class Celsius:
    def __init__(self,temperature):
        self.temperature = temperature
    def to_fahrenheit(self):
        return (self.temperature*1.8)+32

# human = Celsius(37)
# print(human.temperatute)
# print(human.to_fahrenheit())
# print(human.__dict__)

## Using Getters and Setters
# Etia ami janu j temperature -273.15 t koi tolot jabo nuare
## tar karone ami temperature attribute tuk hide koribo paru ie., private bonabo paru aru getter and setter method define koribo paru

# Making Getters and Setters methods
class Celsius:
    def __init__(self,temperature):
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.get_temperature()*1.8)+32

    # getter method
    def get_temperature(self):
        return self._temperature

    # setter method
    def set_temperature(self,value):
        if value<-273.15:
            raise  ValueError("temperature below -273.15 is not possible")
        self._temperature = value

human = Celsius(37)

# # get the temperature attribute via a getter
# # print(human.get_temperature())
# #
# # # get the tempeature in fahrenheit
# # print(human.to_fahrenheit())
# #
# # # Now set the values, ie., new constraint implementation
# # human.set_temperature(-300)
# #
# # # get the fahrenheit method
# # print(human.to_fahrenheit())

# USING the @property decorator
class Celsius:
    def __init__(self,temperature):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature*1.8)+32

    @property
    def temperature(self):
        print("Getting value...")
        return self._temperature

    @temperature.setter
    def temperature(self,value):
        print("Setting value...")
        if value<-273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        self._temperature = value

human = Celsius(37)

print(human.temperature)

print(human.to_fahrenheit())

coldest_thing = Celsius(-300)
