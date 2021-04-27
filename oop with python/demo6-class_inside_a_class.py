#inner class - class inside a class

class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

s1=Student("Anuki",2)
s2=Student("Sanduni",5)

print(s1.name, s1.rollno)
print(s2.name, s2.rollno)
