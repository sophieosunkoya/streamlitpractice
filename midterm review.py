


def gcf (num1,num2):
    if num1 == num2:
        return num1
    elif num2 == num1:
        return num2
    
    for i in range(2,num1+1):
        if num1 % i==0 and num2 % i ==0:
            return (max(i))


print(gcf(30,36))
