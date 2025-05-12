# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
while True:
    Lowestnumber=int(input("Lowest number: "))
    if Lowestnumber>=1:
        Highestnumber=int(input("Highest number: "))
        if Highestnumber<=Lowestnumber:
            print("Highest number must be larger than lowest number!")
            Highestnumber=int(input("Highest number: "))
        elif Highestnumber>Lowestnumber:
            while True:
                identifyPrimeNumbers=input("would you like to identify prime numbers in your table? (y/n): ")
                if (identifyPrimeNumbers != 'y' and identifyPrimeNumbers != 'n'):
                    print("Invalid command, try again")
                else:
                    while True:
                        mathsSymbol='+'
                        mathsSymbol=input("select an arithmetic symbol [+,-,/,*,%,//]: ")
                        if(mathsSymbol != '+' and mathsSymbol != '-' and mathsSymbol != '/' and mathsSymbol != '*' and mathsSymbol != '%' and mathsSymbol != '//'):
                            print("Invalid arithmentic symbol, try again")
                        else:
                            break
                    break
            break
    else:
        print("Lowest number must be greater than 0")
    
#set up variables 
x=len(str(Highestnumber*2))
range1=(Highestnumber+1)- Lowestnumber

z=range1 + 1
length=x+2
width=z*(length)
space1=round(length/2)

print(mathsSymbol);

print(format(mathsSymbol,">"+str(space1)), end="")

print(format("","<"+str(length-space1)),end="")

for top in range(Lowestnumber, Highestnumber+1):
    print(format(top,">"+str(length)), end="")
print("")

print(str("-"*width))

for y in range(Lowestnumber,Highestnumber+1):
    print(format(y,"<"+str(length-1)), end="|")
    for x in range(Lowestnumber,Highestnumber+1):
        isPrime = True
        if mathsSymbol == '+':
            sums=int(x+y)
        elif mathsSymbol == '-':
            sums=int(x-y)
        elif mathsSymbol == '/':
            sums=int(x/y)
        elif mathsSymbol == '*': 
            sums=int(x*y)
        elif mathsSymbol == '%':
            sums=int(x%y)
        elif mathsSymbol == '//':
            sums=(x//y)
            
        if (sums > 1):
            for i in range(2, sums):
                if ((sums % i) == 0):
                    isPrime = False
                    break
        
        if (isPrime == True and sums > 1 and identifyPrimeNumbers == 'y'):     
            print(format(str(sums)+"p",">"+str(length)),end="")
        else:
            print(format(sums,">"+str(length)),end="")
    print()
