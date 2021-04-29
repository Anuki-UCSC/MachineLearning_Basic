# Polymorphism
#       1) Duck Typing
#       2) Operator Ovrloading
#       3) Method overloading 
#       4) Method Overriding

#Duck Typing

class Pycharm:

    def execute(self):
        print("executing !")
        print("running !")

class MyEditor:
    
    def execute(self):
        print("spell check")
        print("execute ")
        print("running")

class Laptop:
    def code(self,ide):
        ide.execute() 

ide=Pycharm()
lap1=Laptop()
lap1.code(ide)    
