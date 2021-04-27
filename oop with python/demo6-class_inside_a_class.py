#inner class - class inside a class

class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.Laptop() # call an inner class inside the constructor of outer class



    class Laptop:
        def __init__(self):
            self.brand="HP"
            self.processer="i7"
            self.ram=8


s1=Student("Anuki",2)
s2=Student("Sanduni",5)

print(s1.name, s1.rollno)
print(s2.name, s2.rollno)
