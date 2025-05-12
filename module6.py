
#dimensionsare10x10

#rows=10
#cols=10
#for x in range(0,cols):
      #for c in range (0,rows):
        #if(rows+cols)%2==0:
            #print("@")
        #else:
            #print("#")
      #print()

userinput=int(input("Enter Number"))
for x in range(0,1):
    if userinput%2==1 and userinput%3==1 and userinput%4==1:
        print("Your number is not a prime number")
        break
    else:
        print("Your number is a prime number")
        
  
    
    

