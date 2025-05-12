#Sophie Osunkoya 10/02/22 CSCI-UA.0002-011 Python
#create a while statement wih variables that evaluates the decimal to binary conversion
while True:
    remainder=int(input("Enter a number greater than or equal to 0:"))
    number=remainder
    bit=""
    if remainder<0:
        print("Invalid, try again")
    else:
        while True:
            moduloResult=remainder%2
            divisionResult=remainder//2
            bit=str(moduloResult)+bit
            print(remainder,"% 2 =", moduloResult,"---",bit)
            print(remainder,"/ 2 =",divisionResult)
            remainder=divisionResult
            if remainder==0:
                print(str(number)+" in binary is "+bit)
                break
        
            
