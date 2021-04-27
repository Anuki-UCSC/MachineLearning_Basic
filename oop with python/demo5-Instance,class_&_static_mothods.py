#methods
#       1)instance methods -self
#       2)class methods -cls
#       3)static methods

# two types of instance
#           -Accessor method - getters
#           -Mutator method - setters

class Student:

    university="UCSC"

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):  #instance method - self means it belongs to a perticular method
        return (self.m1 +self.m2 +self.m3)/3

    def get_m1(self): # Accessor
        return self.m1

    def set_m1(self,vlaue): #Mutator
        self.m1=vlaue

    @classmethod  #class method 
    def return_uni(cls):
        return cls.university
    
    @staticmethod
    def static_uni():
        print("**static methods do not have any thing to do with instance variables or class variables\n")
s1=Student(23,56,78)
s2=Student(65,87,43)

print(s1.avg())
print(s2.avg())

print(Student.return_uni()) #call class method 

Student.static_uni() #call static class