# two types of variables
#       1) Instance variables
#       2) class variables

class Car:

    wheels=4 #class variable

    def __init__(self):
        self.mil=10  #instance variables
        self.brand="BMW"

c1=Car()
c2=Car()
print(c1.mil, c1.brand, c1.wheels)
print(c2.mil, c2.brand, c2. wheels)

Car.wheels =5  #

print(c1.mil, c1.brand, c1.wheels)
print(c2.mil, c2.brand, c2. wheels)

