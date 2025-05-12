 #Sophie Osunkoya
#Section 011
#collaboration with amina diouf
import digitalclock
import random
'''
#PART B

#printing zero
temp = digitalclock.number_0(5, '*')
print(temp)
print()

#print 1
temp = digitalclock.number_1(5, '*')
print(temp)
print()

#print 2
temp = digitalclock.number_2(5, '*')
print(temp)
print()

#print 3
temp = digitalclock.number_3(5, '*')
print(temp)
print()

#print 4
temp = digitalclock.number_4(5, '*')
print(temp)
print()

#print 5
temp = digitalclock.number_5(5, '*')
print(temp)
print()

#print 6
temp = digitalclock.number_6(5, '*')
print(temp)
print()

#print 7
temp = digitalclock.number_7(5, '*')
print(temp)
print()

#print 8
temp = digitalclock.number_8(5, '*')
print(temp)
print()

#print 9
temp = digitalclock.number_9(5, '*')
print(temp)
print()
import digitalclock
#printing zero
temp = digitalclock.number_0(5, '*')
print(temp)
print()

#print 1
temp = digitalclock.number_1(5, '*')
print(temp)
print()

#print 2
temp = digitalclock.number_2(5, '*')
print(temp)
print()

#print 3
temp = digitalclock.number_3(5, '*')
print(temp)
print()

#print 4
temp = digitalclock.number_4(5, '*')
print(temp)
print()

#print 5
temp = digitalclock.number_5(5, '*')
print(temp)
print()

#print 6
temp = digitalclock.number_6(5, '*')
print(temp)
print()

#print 7
temp = digitalclock.number_7(5, '*')
print(temp)
print()

#print 8
temp = digitalclock.number_8(5, '*')
print(temp)
print()

#print 9
temp = digitalclock.number_9(5, '*')
print(temp)
print()





#PART C

digitalclock.print_number(0, 5, '*')
digitalclock.print_number(1, 6, '*')
digitalclock.print_number(2, 7, '*')
digitalclock.print_number(3, 8, '*')
digitalclock.print_number(4, 9, '*')
digitalclock.print_number(5, 10, '*')
digitalclock.print_number(6, 11, '*')
digitalclock.print_number(7, 12, '*')
digitalclock.print_number(8, 13, '*')
digitalclock.print_number(9, 14, '*')







#PART D

temp = digitalclock.plus(5, '*')
print(temp)
print()

temp = digitalclock.minus(5, '*')
print(temp)




#PART E
answer1 = digitalclock.check_answer(1, 2, 3, "+")
print (answer1)
answer2 = digitalclock.check_answer(1, 2, -1, "-")
print (answer2)
answer3 = digitalclock.check_answer(9, 5, 3, "+")
print (answer3)
answer4 = digitalclock.check_answer(8, 2, 4, "-")
print (answer4)
'''



#PART F

def attempt():
    while True:
        trials1=int(input("How many problems would you like to attempt?  "))
        if trials1<1:
            print("Invalid Number,Try again")
        elif trials1 > 1:
            break
    return trials1
attempt1 = attempt()
def width():
    while True:
        wideness1=int(input("How wide do you want your digits to be? 5-10: "))
        if wideness1<5 or wideness1>10:
            print("Invalid width, try again")
        elif (wideness1>=5)and(wideness1<=10):
            break
    return wideness1
width1 = width()     
def character():
    while True:
        char1 = input("What character would you like to use? ")
        if len(char1)!= 1:
             print("String too long, try again")
        else:
            print("Here we go!")
            break
    return char1
character = character()    
    
def program():
        number1=random.randint(1, 9)
        number2=random.randint(1, 9)
        operator=random.randint(0,1)
        if operator==0:
             0 == "+"
        else:
            1 == "-"
        return number1, number2, operator

def problem():
    num1_printed = digitalclock.print_number(number1, width1, character)
    print("")
    plus_printed = digitalclock.plus(width1, character)
    minus_printed = digitalclock.minus(width1, character)
    if operator==0:
        print(plus_printed)
    else:
        print(minus_printed)
    print("")
    num2_printed = digitalclock.print_number(number2, width1, character)    
    return(num1_printed, plus_printed, minus_printed, num2_printed)
def check_answer():
    if operator==0:
        if answer==(number1+number2):
            print("Correct!")
            #correctAnswer+=1
            return correctAnswer
        else:
            print("Sorry that's not correct.")
    else:
        if answer==(number1-number2):
            print("Correct!")
            #correctAnswer+=1
            return correctAnswer
        else:
            print("Sorry that's not correct.")
correctAnswer=0            
for i in range(attempt1):
    i
    number1, number2, operator = program()
    print("What is....")
    problem()
    answer=int(input("= "))
    check_answer()
    if answer==(number1+number2):
        correctAnswer+=1
    if answer==(number1-number2):
        correctAnswer+=1
print("You got", correctAnswer, "out of", attempt, "correct!")
