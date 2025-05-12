#Sophie Osunkoya 10/13/22 CSCI-UA.0002-011 Python

#set start and end number
start=1
end=1000
if start==1:
    print(start,"is technically not a prime number")
#use the for loop to create a list
    for x in range(start,end+1):
        if x > 1 :
            for y in range (2,x):
                if (x%y)==0:
                    break
            else:
                print(x,"is a prime number")
