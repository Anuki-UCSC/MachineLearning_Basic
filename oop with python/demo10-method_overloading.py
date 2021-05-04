class Student:

    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def sum(self,x1,x2):
        return x1+x2

s1=Student(56,78)
s2=Student(34,98)

print(s1.sum(56,78))


