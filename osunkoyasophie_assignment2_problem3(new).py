#Sophie Osunkoya 9/15/22 CSCI-UA.0002-011 Python
#create variables for the numbers as inputs
firstNumber = int(input('Enter a number between 0 - 999: '))
secondNumber = int(input('Enter a number between 0 - 999: '))
#create formulas for every number from the ones,tens and hundreds
lastNumber1=(firstNumber%10)
middleNumber1=int(((firstNumber%100)-(lastNumber1))/10)
firstNumber1=int((firstNumber- firstNumber%100)/100)
lastNumber2=(secondNumber%10)
middleNumber2=int(((secondNumber%100)-(lastNumber2))/10)
firstNumber2=int((secondNumber- secondNumber%100)/100)
#print the phrase alongside each variable that was stored as a formula
print("Sum of Ones", "\t\t=", lastNumber1, "+", lastNumber2,"=", lastNumber1+lastNumber2)
print("Sum of tens", "\t\t=", middleNumber1, "+", middleNumber2,"=", middleNumber1+middleNumber2)
print("Sum of hundreds", "\t=", firstNumber1, "+", firstNumber2,"=", firstNumber1+firstNumber2)
print("_"*45)
