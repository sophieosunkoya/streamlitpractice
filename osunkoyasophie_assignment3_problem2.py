##Sophie Osunkoya 9/24/22 CSCI-UA.0002-011 Python
#import random and print out the beginning of the program
import random
print("Im thinking of a number of a number between 1 and 10!")
#set variable for number and guess
number= random.randint(1,10)
guess= int(input("Whats your guess? "))
#set if statements and prompt user if the number is too high or low
if guess==number:
    print("You got it!")
    print("The secret number was", number)
    print("It took you 1 try to guess the number.")
elif guess!=number:
    if guess< number:
        print("Too low, try again.")
    elif guess> number:
        print("Too high try again.")
#set if statements and prompt user if the number is too high or low with additional indents
    guess= int(input("Whats your guess? "))
    if guess==number:
        print("You got it!")
        print("The secret number was", number)
        print("It took you 2 tries to guess the number.")
    elif guess!=number:
        if guess< number:
            print("Too low, try again.")
        elif guess> number:
            print("Too high try again.")
#set if statements and prompt user if they got it right or end program 
        guess= int(input("Whats your guess? "))
        if guess==number:
            print("You got it!")
            print("The secret number was", number)
            print("It took you 3 tries to guess the number.")
        elif guess!=number:
            print("The secret number was", number)
            print("You didn't guess the number.")

