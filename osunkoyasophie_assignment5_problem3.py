#Sophie Osunkoya 10/13/22 CSCI-UA.0002-011 Python
#while true statement to test the lowest and highest number variable

while True:
    Lowestnumber=int(input("Lowest number: "))
    if Lowestnumber>=0:
        Highestnumber=int(input("Highest number: "))
        if Highestnumber<=Lowestnumber:
            print("Highest number must be larger than lowest number!")
            Highestnumber=int(input("Highest number: "))
        elif Highestnumber>Lowestnumber:
            break
        break
    else:
        print("Lowest number must be 0 or greater")
    
#set up variables for the length and use it for spacing
x=len(str(Highestnumber*2))
#set up variables for range, length and width
range1=(Highestnumber+1)- Lowestnumber
z=range1 + 1
length=x+2
width=z*(length)
#set up a variable to figure out spacing
space1=round(length/2)
#use variables to set up formatting
print(format("+",">"+str(space1)), end="")

print(format("","<"+str(length-space1)),end="")
#use  for loops to print the table using exact formatting using previous variables
for top in range(Lowestnumber, Highestnumber+1):
    print(format(top,">"+str(length)), end="")
print("")

print(str("-"*width))
#use for loops to print the table using exact formatting using previous variables

for y in range(Lowestnumber,Highestnumber+1):
    print(format(y,"<"+str(length-1)), end="|")
    for x in range(Lowestnumber,Highestnumber+1):
        sum=int(x+y)
        
        print(format(sum,">"+str(length)),end="")
    print()    
    
