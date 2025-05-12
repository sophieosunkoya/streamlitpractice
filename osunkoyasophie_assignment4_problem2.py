#Sophie Osunkoya 10/02/22 CSCI-UA.0002-011 Python


#create while statement for the validity of amount of sticks
while True:
    numsticks=int(input("How many sticks(10-100)?"))
    if numsticks>100:
        print("Sorry, that's too many sticks. Try again")
    if numsticks<10:
        print("Sorry, that's too few sticks. Try again.")
    if (numsticks<=100) and (numsticks>=10):
        print("Great Let's play...")
        print()
        break
       
#create variables for the turns      
count=1
isValidNumber=True
#create while True statement to run the pick up sticks game and alternate players
while True:
    if(count%2==1):
        print("Turn: Player 1")
    elif(count%2==0):
        print("Turn: Player 2")
    print("There are", numsticks, " sticks on the table.")
    takeAway=int(input("How many sticks do you want to take(1,2 or 3)?"))
    numleft=numsticks-takeAway
    if takeAway==1 or takeAway==2 or takeAway==3:
        isValidNumber=True
        
        if numleft>=0:
            numsticks=numleft
        if numleft==0:
            print("There are no sticks left on the table!  Game over.")
            if(count%2==1):
                print("Player 2 wins!")
                break
            elif(count%2==0):
                print("Player 1 wins!")
                break
        elif numleft<0:
            print("Sorry, that would bring the total # of sticks below 0. Try again.")
            count+=1

            
    else:
        print("Sorry, that's not a valid number")
        isValidNumber=False

    if isValidNumber==True:
        count+=1
    
