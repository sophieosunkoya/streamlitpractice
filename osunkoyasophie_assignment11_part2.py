import random
mylist = ["red", "green", "blue"]
class Gumball_Machine:
    def __init__(self,capacity):
        self.capacity=capacity
        self.money=0.00
        self.gumballs=random.choices(mylist,  k = 5)
        print("Gumball Machine created with",self.capacity,"random gumballs")
    
    def report(self):
        print("\nGunball Machine Report:")
        print("* Gunballs in machine:",len(self.gumballs))
        print("* Money in machine: $",round(self.money,2),sep="")
    
    def dispense(self,coin_value):
        if(coin_value==0.25):
            if(len(self.gumballs)!=0):
                a=self.gumballs.pop()
                self.money=self.money+0.25
                print("\nAccepting 0.25; Dispensing a",a,"gumball")
            else:
                print("\nMachine is empty, no gumball will be dispensed")
        else:
            print("\nInvalid coin, no gumball will be dispensed")
    
    def count_gumballs_by_type(self,typ):
        co=self.gumballs.count(typ)
        print("\nThere are",co,"gumballs of type",typ,"in the machine")

machine = Gumball_Machine(5)
machine.report()

machine.count_gumballs_by_type("red")
machine.count_gumballs_by_type("green")
machine.count_gumballs_by_type("blue")

machine.dispense(0.10)
machine.dispense(0.50)
machine.dispense(0.01)

machine.report()

machine.count_gumballs_by_type("red")
machine.count_gumballs_by_type("green")
machine.count_gumballs_by_type("blue")

machine.dispense(0.25)
machine.dispense(0.25)
machine.dispense(0.25)

machine.report()

machine.count_gumballs_by_type("red")
machine.count_gumballs_by_type("green")
machine.count_gumballs_by_type("blue")

machine.dispense(0.25)
machine.dispense(0.25)
machine.dispense(0.25)

machine.report()

machine.count_gumballs_by_type("red")
machine.count_gumballs_by_type("green")
machine.count_gumballs_by_type("blue")
