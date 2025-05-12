
#Sophie Osunkoya 10/13/22 CSCI-UA.0002-011 Python
#set variable equal to false
NumberRange=False
#create a while loop to test if it is valid
while NumberRange==False:
    start=int(input("Start number: "))
    end=int(input("End number: "))
    if start > end:
        print("End number must be greater than start number")
    if (start<0)or(end<0):
        print("Start and end must be positive")
    else:
#then create a list of the prime numbers
        for x in range(start,end+1):
            if x >1:
                for y in range (2,x):
                    if (x%y)==0:
                        break
                else:
                    print(x)
                    
                    NumberRange==True
        
