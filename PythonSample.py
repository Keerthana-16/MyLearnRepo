class Animal:
    def __init__(self, Name="", Age=0, Type="Chicken"):
        self.Name = Name
        self.Age = Age
        self.Type = Type
    def __str__(self):
        return "{0} is a {1} aged {2}".format(self.Name,self.Type,self.Age)

class Chicken(Animal):
    def SetType(self, Type):
        print("Sorry, {0} will always be a {1}".format(self.Name, Type))
    def MakeSound(self):
        print("{0} says Cluck, Cluck,Cluck!".format(self.Name))


MyChicken = Chicken("sally",2)
c = Chicken("Sally", 3 , "Gorilla")
print(MyChicken)
print(c)
MyChicken.SetType("Chicken")
MyChicken.MakeSound()

