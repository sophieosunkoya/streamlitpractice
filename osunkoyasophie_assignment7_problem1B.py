def isUpperCase(string):
    if (string.isupper() == True):
        return True
    else:
        return False

def isLowerCase(string):
    if (string.islower() == True):
        return True
    else:
        return False
    

def isNumber(string):
    if (string.isnumeric() == True):
        return True
    else:
        return False

def isAlphaNum(string):
    if (string.isalnum() == True):
        return True
    else:
        return False
        


while True:
    userString = input('Enter a user name: ')
    if (userString == ""):
        print("invalid username")
    else:
        userStringLength = 0
        isAlphaNumeric = False
        firstLetterIsNumber = False
        lastLetterIsNumber = False
        numberOfUpperCase = 0
        numberOflowerCase = 0
        numberOfDigits = 0

        # Get the sting length
        userStringLength = len(userString)

        # Check if isAlphaNumeric
        isAlphaNumeric = isAlphaNum(userString)

        # check if the first and the lastnumber is not digit
        firstLetterIsNumber = isNumber(userString[0])
        lastLetterIsNumber = isNumber(userString[len(userString) - 1])

        for i in userString:
            if(isUpperCase(i) == True):
                numberOfUpperCase += 1

            elif(isLowerCase(i) == True):
                numberOflowerCase +=1
                
            if(isNumber(i) == True):
                numberOfDigits += 1
                
        print("")
        print("Length of the username: " + str(userStringLength))
        print("All character alphanumeric: "+ str(isAlphaNumeric))

        if ((firstLetterIsNumber == False) and (lastLetterIsNumber == False)):
            print("First and last characters are not digit: ", str(True))
        else:
            print("First and last characters are not digit: ", str(False))
            
        print("Number of upper case character is: "+ str(numberOfUpperCase))
        print("Number of Lower case character is: "+ str(numberOflowerCase))

        print("Number of digits in the username: "+ str(numberOfDigits))


        # Check the length of the string
        if userStringLength < 8 or userStringLength > 15:
            print("Username is invalid, please try again")
            
        elif isAlphaNumeric == False:
            print("Username is invalid, please try again")

        elif (firstLetterIsNumber == True) or (lastLetterIsNumber == True):
            print("Username is invalid, please try again")

        elif numberOfUpperCase == 0:
            print("Username is invalid, please try again")

        elif numberOflowerCase == 0:
            print("Username is invalid, please try again")

        elif numberOfDigits == 0:
            print("Username is invalid, please try again")

        else:
            print("Username is valid!")
            break


#COLLECT AND VALIDATE PASSWORD
while True:
    userPassword = input('Enter your password: ')
    if userPassword == "":
        print("invalid username")
    else:
        userPasswordLength = 0
        usernameInPassword = False
        passwordNumberOfUpperCase = 0
        passwordNumberOflowerCase = 0
        passwordNumberOfDigits = 0
        passwordNumberOfSpecialCharacter = 0
        passwordIsAlphaNumeric = False

        for i in userPassword:
            if(isUpperCase(i) == True):
                passwordNumberOfUpperCase += 1

            elif(isLowerCase(i) == True):
                passwordNumberOflowerCase +=1 
                
            if(isNumber(i) == True):
                passwordNumberOfDigits += 1

            if (not i.isalnum()):
                passwordNumberOfSpecialCharacter += 1

        #Get the length
        userPasswordLength = len(userPassword)
        print("Length of password: ", str(userPasswordLength))

        #Check if the username is in the password
        if (userPassword.find(userString) > -1) :
            usernameInPassword = True
            print("Username is part of password", str(usernameInPassword))
        else:
            usernameInPassword = False
            print("Username is part of password", str(usernameInPassword))

        print("Number of upper case character is: "+ str(passwordNumberOfUpperCase))
        print("Number of Lower case character is: "+ str(passwordNumberOflowerCase))
        print("Number of digits in the password: "+ str(passwordNumberOfDigits))
        print("Number of special character in the password: "+ str(passwordNumberOfSpecialCharacter))


        # Check the length of the string
        if userPasswordLength < 8 :
           
            print("Password is invalid, please try again")
            
        elif usernameInPassword == True:
            
            print("Password is invalid, please try again")


        elif passwordNumberOfUpperCase == 0:
            
            print("Password is invalid, please try again")

        elif passwordNumberOflowerCase == 0:
            
            print("Passord is invalid, please try again")

        elif passwordNumberOfDigits == 0:
            
            print("Password is invalid, please try again")

        elif passwordNumberOfSpecialCharacter == 0:
           
            print("Password is invalid, please try again")

        else:
            print("Password is valid!")
            break


        
