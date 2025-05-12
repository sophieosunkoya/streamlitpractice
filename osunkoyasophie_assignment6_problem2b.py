# Even function
def is_even(a):
    if a % 2 == 0:
        return True
    else:
        return False

# Odd function
def is_odd(a):
    if a % 2 == 1:
        return True
    else:
        return False

# Prime function
def is_prime(a):
    if a > 1:
        for i in range(2, int(a/2)+1):
            if (a % i) == 0:
                return False
                break
        else:
            return True

    else:
        return False
    
# Perfect function 
def is_perfect(a):
    sum1 = 0
    for x in range(1,a):
        if a % x == 0:
            sum1 += x
    if sum1 == a:
        return True
    else:
        return False
        
# Abundant function
def is_abundant(a):
    sum1 = 0
    for x in range(1,a):
        if a % x == 0:
            sum1 += x
    if sum1 > a:
        return True
    else:
        return False

# Prime number function
def primeNumberFun(startingNumber, endingNumber): 
    # Process user input
    print('All prime number(s) between', str(startingNumber), "and", str(endingNumber))
    print("#################")
    for x in range(startingNumber, endingNumber):
        if (is_prime(x) == True):
            print(str(x))
    print("#################")
    
    
# Perfect number fuction 
def perfectNumberFun(startingNumber, endingNumber):
    # Process user input
    print('All perfect number(s) between', str(startingNumber), "and", str(endingNumber))
    print("#################")
    for x in range(startingNumber, endingNumber+1):
        if (is_perfect(x) == True):
            print(str(x))
    print("#################")
    
    
# Abundant number function
def abundantNumberFun(startingNumber, endingNumber):
    # Process user input
    print('All abundant number(s) between', str(startingNumber), "and", str(endingNumber))
    print("#################")
    for x in range(startingNumber, endingNumber+1):
        if (is_abundant(x) == True):
            print(str(x))
    print("#################")
    
    
# Chart function
def chartFunction(startingNumber, endingNumber):
    # Process user input
    print(format("Number","<8"),end="")
    print(format("Even","<8"),end="")
    print(format("Odd","<8"),end="")
    print(format("Prime","<8"),end="")
    print(format("Perfect","<10"),end="")
    print(format("Abundant","<8"),end="")
    print('')
    for x in range(startingNumber, endingNumber+1):
        print(format(x,"<8"),end="")
        if is_even(x):
            print(format("x","<8"),end="")
        else:
            print(format("","<8"),end="")
            
        if is_odd(x):
            print(format("x","<8"),end="")
        else:
            print(format("","<8"),end="")
            
        if is_prime(x):
            print(format("x","<8"),end="")
        else:
            print(format("","<8"),end="")
            
        if is_perfect(x):
            print(format("x","<10"),end="")
        else:
            print(format("","<10"),end="")
            
        if is_abundant(x):
            print(format("x","<8"))
        else:
            print(format("","<8"))


# Menu Function
while True:
    print('Main Menu')
    print('')
    print('1 - Find all prime numbers within a given range')
    print('2 - Find all perfect numbers within a given range')
    print('3 - Find all abundant numbers within a given range')
    print('4 - Chart all even, odd, prime, perfect and abundant numbers within a given range')
    print('5 - Quit')
    print('')
    choice = input("Your choice: ")
    print('')
    if (choice != '1' and choice != '2' and choice != '3' and choice != '4' and choice != '5'):
        print("I don't understand that...")
        print('')
    elif(choice == '5'):
        print("Good Bye!")
        break
    else:
        # Collect user range
        while True:
            startingNumber = int(input("Enter starting number: "))
            if (startingNumber < 0):
                print("Invalid, try again")
                print('')
            else:
                while True:
                    endingNumber = int(input("Enter ending number: "))
                    if (endingNumber < 0):
                        print("Invalid, try again")
                        print('')
                    else:
                        # Check user choice
                        if (choice == '1'):
                            primeNumberFun(startingNumber, endingNumber)
                            break
                        elif (choice == '2'):
                            perfectNumberFun(startingNumber, endingNumber)
                            break
                        elif (choice == '3'):
                            abundantNumberFun(startingNumber, endingNumber)
                            break
                        elif (choice == '4'):
                            chartFunction(startingNumber, endingNumber)
                            break
                print('')
                break



