
while True:
    die_sides=int(input("How many sides on your dice(4,6,8,10,12 or 20)? "))
    if die_sides != 4 and die_sides != 6 and die_sides != 8 and die_sides != 10 and die_sides != 12 and die_sides != 20:
        print("Invalid size, try again.")
    else:
        print("Thanks, here we go!")
        break
import random 
total=0
double=0
high=0
highLow=0
even=0
odd=0
sumValue=0
count=0
totalrolls=0
sum1=0
sum2=0
while True:
    count+=1
    die1=random.randint(1,die_sides)
    die2=random.randint(1,die_sides)
    sum1+=die1
    sum2+=die2
    print(count,"die #1 is","*",die1,"*","and die #2 is","*",die2,"*",end=" ")
    totalrolls+=1
    if die1==1 and die2== 1:
        print("Snake Eyes!")
        break
    if die1==die2:
        print("Double Roll!"," ", end="")
        double+=1
    if die1%die_sides==0 and die2%die_sides==0:
        print("High Roll!"," ", end="")
        high+=1
    if (die1==1 and die2==die_sides) or (die1==die_sides and die2==1):
        print("High/Low roll!"," ", end="")
        highLow+=1
    if die1%2==0 and die2%2==0:
        print("Evens!"," ", end="")
        even+=1
    if  die1%2==1 and die2%2==1:
        print("Odds!"," ", end="")
        odd+=1
    if  die1+die2==die_sides:
        print("Sum value is size value! "," ", end="")
        sumValue+=1
    print()

doublePercent=(format(float((double/totalrolls)*100),'.2f'))
highPercent=(format(float((high/totalrolls)*100),'.2f'))
highLowPercent=(format(float((highLow/totalrolls)*100),'.2f'))
evenPercent=(format(float((even/totalrolls)*100),'.2f'))
oddPercent=(format(float((odd/totalrolls)*100),'.2f'))
sumValuePercent=(format(float((sumValue/totalrolls)*100),'.2f'))

print("You finally got snake eyes on roll #", totalrolls)
print("Along the way you rolled DOUBLES",double,"times",(doublePercent+"% of all rolls were doubles",))
print("Along the way you rolled TWO HIGH VALUES",high,"times",(highPercent+"% of all rolls were twp high values",))
print("Along the way you rolled HIGH/LOW ",highLow,"times",(highLowPercent+"% of all rolls were high/low",))
print("Along the way you rolled TWO EVENS",even,"times",(evenPercent+"% of all rolls were two evens",))
print("Along the way you rolled TWO ODDS",odd,"times",(oddPercent+"% of all rolls were two odds",))
print("Along the way you rolled A SUM VALUE ",sumValue,"times",(sumValuePercent+"% of all rolls were a sum value",))
print("Average roll for die #1:", sum1/totalrolls)
print("Average roll for die #2:", sum2/totalrolls)


