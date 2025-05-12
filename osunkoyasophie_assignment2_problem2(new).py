#Sophie Osunkoya 9/15/22 CSCI-UA.0002-011 Python
#Collect our inputs (savingsAmount, expectedAnnualInterest)
savingsAmount = float(input('Enter the amount you wish to save? '))
expectedAnnualInterest = int(input('Enter your expected annual rate? '))

# Calculate the monthly interest
monthlyInterest =  (expectedAnnualInterest / 12)/100

#Set width for divider
width=26
divider="_"*26

# Calculate and display compounded interest over a 3 month period
balance = float(savingsAmount)
count = int(0)
interestValue = float(0)

print()
print(divider,"Calculating",divider,sep="")
print()
print('Month', '\t Starting Balance', '\t Interest', '\t Ending Balance')
while count < 3:
    monthlyInterestmoney=(monthlyInterest)*(balance)
    interestValue = monthlyInterestmoney
    newBalance = balance + monthlyInterestmoney
    count += 1

    print(count,"\t\t{:.2f}".format(balance),"\t\t{:.2f}".format(interestValue),"\t\t\t{:.2f}".format(newBalance))
    balance = newBalance;
