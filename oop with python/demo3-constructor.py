class Computer:

    def __init__(self):
        self.name="Anuki"

    def updateAge(self,age):
        self.age=age

    def compareAge(self,other):
        if self.age == other.age:
            return True
        else:
            return False

c1=Computer()
c2=Computer()
print(c1.name)
print(c2.name) #these gets "Anuki" because it calls __init__ constructor automtically


c3=Computer()
c3.name="Pawani" # we can change(replace) a value - of an object
print(c3.name) 

c3.updateAge(44)
print(c3.age)

c4=Computer()
c4.updateAge(33)

if c3.compareAge(c4):
    print("they are same")
else:
    print("they are different")

