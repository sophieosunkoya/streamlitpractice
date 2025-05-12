##Sophie Osunkoya 9/24/22 CSCI-UA.0002-011 Python
# Get date format
userDate = str(input("Enter a date in this format (YYYYMMDD): "));

# Extract the year month and day from the userDate;
year= userDate[:4]
month= userDate[4:6]
day= userDate[6:8]

isALeapYear = False
monthInWord = "None"
dayToWord = "None"

# Convert the month to word
if (int(month) == 1):
    monthInWord = "January"
elif (int(month) == 2):
    monthInWord = "Febuary"
elif (int(month) == 3):
    monthInWord = "March"
elif (int(month) == 4):
    monthInWord = "April"
elif (int(month) == 5):
    monthInWord = "May"
elif (int(month) == 6):
    monthInWord = "June"
elif (int(month) == 7):
    monthInWord = "July"
elif (int(month) == 8):
    monthInWord = "August"
elif (int(month) == 9):
    monthInWord = "September"
elif (int(month) == 10):
    monthInWord = "October"
elif (int(month) == 11):
    monthInWord = "November"
elif (int(month) == 12):
    monthInWord = "December"
    
# Convert the day to word
if int(day[:2]) == 1:
    dayToWord = str(int(day))+"st"
elif int(day[:2]) == 2:
    dayToWord = str(int(day))+"nd"
elif int(day[:2]) == 3:
    dayToWord = str(int(day))+"rd"
else:
    dayToWord = str(int(day))+"th"

# Check if the year is a leap year
canBeDividedby4= True if int(year) % 4 == 0 else False
canBeDividedBy100= True if int(year) % 100 == 0 else False
canBeDividedBy400= True if int(year) % 400 == 0 else False

if canBeDividedby4 == True:
    if canBeDividedBy100 == True:
        if canBeDividedBy400 == True:
            print(year, "is a leap year.")
            isALeapYear = True;
        else:
            print(year, "is NOT a leap year.")
    else:
        print(year, "is a leap year.")  
        isALeapYear = True;
else:
    print(year, "is NOT a leap year.")  

# Check if the month and date combination is valid
if int(month) == 9 or int(month) == 4 or int(month) == 6 or int(month) == 11:
    if int(day) <= 30:
        print(monthInWord, dayToWord, year,"is a valid date.")
    else:
        print("This is not a valid date in",year)

elif int(month) == 1 or int(month) == 3 or int(month) == 5 or int(month) == 7 or int(month) == 8 or int(month) == 10 or int(month) == 12:
    if int(day) <=31:
        print(monthInWord, dayToWord, year,"is a valid date.")
    else:
        print("This is not a valid date in",year)
        
elif int(month) == 2:
    if int(day) <= 28 or (int(day) == 29 and isALeapYear == True):
        print(monthInWord, dayToWord, year,"is a valid date.")
    else:
        print("This is not a valid date in",year)
else:
    print("This is not a valid date")
width=50
divider="_"*50
print(divider)
