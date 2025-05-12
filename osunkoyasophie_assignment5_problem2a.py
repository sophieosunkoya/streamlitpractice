##Sophie Osunkoya 10/13/22 CSCI-UA.0002-011 Python
#set a variable equal to false in order to control the for loop
posNumber=False
#create a for loop to test the user input
while posNumber==False:
#use user input to create a test to determine if they are prime and positive
 number=int(input("Enter a positive number to test: "))

 if number<0:
    print("This is not a positive number")
 elif number==1:
    print(number,"is technically not a prime number. ")
 else:
    for i in range (2,number):
        divisor=(number % i)
        count=0
        if divisor==0:
            print(i,"is a divisor of", number,"...stopping.")
            print(number,"is not a prime number.")
            break
        else:
            count+=1
            print(i,"is NOT a divisor of",number,"... continuing")
 if count==1:
        print(number,"is a prime number!")

