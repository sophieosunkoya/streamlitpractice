#Sophie Osunkoya 9/24/22 CSCI-UA.0002-011 Python
#collaborated with amina diouf
print("Valid Triangle Tester")
print()

#create input variables for all 6 points on the triangle
x1= float(input("Enter Point #1 -x position: "))
y1= float(input("Enter Point #1 -y position: "))
x2= float(input("Enter Point #2 -x position: "))
y2= float(input("Enter Point #2 -y position: "))
x3= float(input("Enter Point #3 -x position: "))
y3= float(input("Enter Point #3 -y position: "))
#print introduction to the length of each side
print()
print("The length of each side of your test shape is:")
print()
#create formula for each side using inputted points
side1= float(((x1-x2)**2 + (y1-y2)**2)**0.5)
side2= float(((x1-x3)**2 + (y1-y3)**2)**0.5)
side3= float(((x2-x3)**2 + (y2-y3)**2)**0.5)
#change the format for the sides to two decimal places
fside1 = "{:.2f}".format(side1)
fside2 = "{:.2f}".format(side2)
fside3 = "{:.2f}".format(side3)
print()
#print each side
print("Side 1: ", side1)
print("Side 2: ", side2)
print("Side 3: ", side3)
print()
#create easier variables for valid triangle sides
a=float(side1 + side2)
b=float(side2 + side3)
c=float(side3 + side1)

#if and elif statements to determine if triangle is valid and the type of triangle
if ((a > side3) and (b > side1) and (c > side2)) :
    print("This is a valid triangle!")
    if fside1==fside2==fside3:
        print("This is an Equilateral Triangle.")
        
    elif fside1==fside2 or fside2==fside3 or fside3==fside1:
        print("This is an isosceles triangle")
        
    elif fside1 !=fside2 and fside1 != fside3 and fside1 != fside3:
        print("This is a Scalene triangle")
#sides a^2 and b^2 must be equal to c^2
#set up variables a^2,b^2 and c^2
    aSqr=round(side1 ** 2)
    bSqr=round(side2 ** 2)
    cSqr=round(side3 ** 2)
#if statement for side3 being the bigger side
    if((fside1<fside3)and (fside2<fside3)):
        if((aSqr+bSqr)==cSqr):
            print("This is also a right triangle.")
#if statement for side2 being the bigger side
    if((fside1<fside2)and (fside3<fside2)):
        if((aSqr+cSqr)==bSqr):
            print("This is also a right triangle.")
#if statement for side1 being the bigger side
    if((fside2<fside1)and (fside3<fside1)):
        if((bSqr+cSqr)==aSqr):
            print("This is also a right triangle.")
else:
    print("This triangle is not valid.")
#Draw the triangle
#import turtle and set up dimensions
import turtle
turtle.setup(500,500,0,0)
turtle.goto(x1,y1)
turtle.left(120)
turtle.goto(x2,y2)
turtle.left(120)
turtle.goto(x3,y3)
turtle.left(120)
turtle.goto(x1,y1)
turtle.left(120)
