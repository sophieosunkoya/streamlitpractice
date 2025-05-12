
product=1
while True:
    product=1
    factorial=int(input("Calculate the factorial of:"))
    for i in range(factorial,0,-1):
        print(i)
        product*=i

    print(1,"=",end=" ")
    print(product)
              
              
