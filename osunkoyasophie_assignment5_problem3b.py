#Sophie Osunkoya 10/13/22 CSCI-UA.0002-011 Python
#create a while true to test user input
while True:
    Lowestnumber=int(input("Lowest number: "))
    if Lowestnumber>=0:
        Highestnumber=int(input("Highest number: "))
        if Highestnumber<=Lowestnumber:
            print("Highest number must be larger than lowest number!")
            Highestnumber=int(input("Highest number: "))
        elif Highestnumber>Lowestnumber:
#create a while true to test user input
            while True:
                identifyPrimeNumbers=input("would you like to identify prime numbers in your table? (y/n): ")
                if (identifyPrimeNumbers != 'y' and identifyPrimeNumbers != 'n'):
                    print("Invalid command, try again")
                else:
                    break
            break
    else:
        print("Lowest number must be 0 or greater")
    
#set up variables 
x=len(str(Highestnumber*2))
range1=(Highestnumber+1)- Lowestnumber

z=range1 + 1
length=x+2
width=z*(length)
space1=round(length/2)
#print out formatting according to the length and spaces
print(format("+",">"+str(space1)), end="")

print(format("","<"+str(length-space1)),end="")
#print out for loops to print out the numbers to be added

for top in range(Lowestnumber, Highestnumber+1):
    print(format(top,">"+str(length)), end="")
print("")

print(str("-"*width))
#print out for loops to print out the numbers to be added
for y in range(Lowestnumber,Highestnumber+1):
    print(format(y,"<"+str(length-1)), end="|")
#print out for loops to check for prime number then print using new format
    for x in range(Lowestnumber,Highestnumber+1):
        isPrime = True
        sums=int(x+y)
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
