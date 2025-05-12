class Smartphone:
    global phones
    phones={}
    def __init__(self,capacity,name):
        self.ca=capacity
        self.capacity=capacity
        self.name=name
    def add_app(self,appname,appsize):
        if (appsize<self.capacity):
            if appname in phones:
                print("\nApp Already Installed")
            else:
                phones[appname]=appsize
                self.capacity=self.capacity-appsize
        else:
            print("Cannot install app, no available space")
    def remove_app(self,appname):
        if appname in phones:
            si=phones[appname]
            phones.pop(appname)
            self.capacity=self.capacity+si
            print("App removed:",appname)
        else:
            print("There is no app with name",appname)
    def has_app(self,appname):
        if appname in phones:
            return True
        else:
            return False
    def get_available_space(self):
        return self.capacity
    def report(self):
        print("Name:",self.name)
        print("Capacity:",self.ca-self.capacity,"out of",self.ca,"GB")
        print("Available space:", self.capacity)
        print("Apps installed:",len(phones))
        for i in phones:
            print("*",i,"is using",phones[i],"GB")

def main():
    size=int(input("Size of your new smartphone (32, 64 or 128 GB): "))
    smartname=input("Smartphone name: ")
    print("Smartphone created!")
    smt=Smartphone(size,smartname)
    smt.report()
    while(True):
        option=input("(r)eport, (a)dd app, r(e)move app or (q)uit: ")
        if(option =='a'):
            addname=input("App name to add: ")
            addsize=int(input("App size in GB: "))
            smt.add_app(addname,addsize)
        if(option=='r'):
            smt.report()
        if(option=='e'):
            addname=input("App name to remove: ")
            smt.remove_app(addname)
        if(option=='q'):
            print("Good Bye!")
            break

if __name__ == "__main__":
    main()
