class Computer:

    def config(self):
        print("15' , 16gb, 1TB")


com1=Computer()
print(type(com1))

com2=Computer()
print(type(com2))

Computer.config(com1) # call a function of an object
Computer.config(com2) # call config function of com2(belongs to computer class) 

com1.config() # this is the normal syntax uses 
com2.config()

a=5
a.bit_length() # bit_length function calls and it uses "a" as the parameter