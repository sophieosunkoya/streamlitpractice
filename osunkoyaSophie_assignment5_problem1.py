#Sophie Osunkoya 10/13/22 CSCI-UA.0002-011 Python
#create variables for budget using user input
Budget=int(input("Enter budget for your party: "))
#create variables for pizza slices and total
sliceCost=2.50
pizzaCost=12.50
total=0
#print the cost
print("Cost per slice of pizza:","{:.2f}".format(sliceCost))
print("Cost pery whole pizza pie (8 slices):","{:.2f}".format(pizzaCost))
#create user input for people
People=int(input("How many people will be attending your party? "))
#create for loop for validity of number of pizza slices
for i in range(1,People+1):
    valid=False
    while valid==False:
        slices=int(input("Enter number of slices for person #"+str(i)+":"))
        if slices>0:
            valid=True
            total+=slices
        else:
            print("Not a valid entry, try again!")

#calculate pies and slices and print out the outcome        
pies=total//8
slices2=total%8
print("You should purchase",pies,"and",slices2,"slices")
totalCost=(slices2*sliceCost+pies*pizzaCost)
remaining=(Budget-totalCost)
if remaining<0:
    print("Your order cannot be completed.")
    print("This would put you over budget by", abs(remaining))
elif remaining==0:
    print("Your total cost will be:","{:.2f}".format(totalCost))
    print("You will have no money left after your order.")
else:
    print("Your total cost will be:","{:.2f}".format(totalCost))
    print("You will still have","{:.2f}".format(remaining),"left after your order")

