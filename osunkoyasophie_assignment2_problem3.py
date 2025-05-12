#Sophie Osunkoya 9/15/22 CSCI-UA.0002-011 Python
#create variables for the numbers as inputs
firstNumber = str(input('Enter a number between 0 - 999: '))
secondNumber = str(input('Enter a number between 0 - 999: '))
#create two lists with integers and an x value from each number input
list1 = [int(x) for x in firstNumber]
list2 = [int(x) for x in secondNumber]
#print the phrase alongside each number from each list
print("Sum of Ones", "\t\t=", list1[0], "+", list2[0],"=", (list1[0] + list2[0]))
print("Sum of tens", "\t\t=", list1[1], "+", list2[1],"=", (list1[1] + list2[1]))
print("Sum of hundreds", "\t=", list1[2], "+", list2[2],"=", (list1[2] + list2[2]))
