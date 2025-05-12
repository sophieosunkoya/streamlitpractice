def is_even(a):
    if a % 2 == 0:
        return True
    else:
        return False

def is_odd(a):
    if a % 2 == 1:
        return True
    else:
        return False


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
    
    
def is_perfect(a):
    sum1 = 0
    for x in range(1,a):
        if a % x == 0:
            sum1 += x
    if sum1 == a:
        return True
    else:
        return False
        

def is_abundant(a):
    sum1 = 0
    for x in range(1,a):
        if a % x == 0:
            sum1 += x
    if sum1 > a:
        return True
    else:
        return False
    



#collect user numbers
while True:
    start = int(input("Enter starting Number: "))
    if (start < 0):
        print("Invalid, try again")
    else:
        while True: 
            end = int(input("Enter ending Number: "))
            if end<0 or end<start:
                print("Invalid, try again")
            else:
                break
        break

for x in range(start,end+1):
    print()
    print(x,"is ... ",end=" ")
    if is_even(x):
        print("even"," ",end="")
    if is_odd(x):
        print("odd"," ", end="")
    if is_prime(x):
        print("prime"," ", end="")
    if is_perfect(x):
        print("perfect"," ", end="")
    if is_abundant(x):
        print("abundant"," ", end="")
            
                
