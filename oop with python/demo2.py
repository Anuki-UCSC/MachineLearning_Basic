class Computer:

    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram =ram

    def config(self):
        print("config is ",self.cpu, self.ram)


com1=Computer("15",16) #why only 2 parameters?  self=Computer(cpu,ram)  #com1 is also an argument
print(type(com1))

com2=Computer("Ryzen 3",0)  
print(type(com2))

Computer.config(com1) 
Computer.config(com2) 
com1.config() 
com2.config()

