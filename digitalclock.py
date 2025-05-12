
# function:   horizontal_line
# input:      a width value (integer) and a single character (string)
# processing: generates a single horizontal line of the desired size
# output:     returns the generated pattern (string)
def horizontal_line(width,char):
    return width*char + "\n"

# function:   vertical_line
# input:      a shift value and a height value (both integers)  and a single character (string)
# processing: generates a single vertical line of the desired height.  the line is
#             offset from the left side of the screen using the shift value
# output:     returns the generated pattern (string)
def vertical_line(shift,height,char):
    pattern = ""
    for i in range(height):
        pattern += shift*" " + char + "\n"
    return pattern

# function:   two_vertical_lines
# input:      a width value and a height value (both integers)  and a single character (string)
# processing: generates two vertical lines.  the first line is along the left side of
#             the screen. the second line is offset using the "width" value supplied
# output:     returns the generated pattern (string)
def two_vertical_lines(width,height,char):
    pattern = ""
    for i in range(height):
        pattern += char + " "*(width-2) + char + "\n"
    return pattern

#Calling numbers from 0 to 9 PART B
#number 0
def number_0(width, character):
    pattern = ""
    pattern += horizontal_line(width, character)
    pattern += two_vertical_lines(width, 5, character)
    pattern += horizontal_line(width, character)
    return pattern

# function:   number_1
# input:      a width value (integer) and a single character (string)
# processing: generates the number 1 as it would appear on a digital display
#             using the supplied width value
# output:     returns the generated pattern (string)
def number_1(width, character):
	pattern = vertical_line(width-1, 5, character)
	return pattern
#number 2
def number_2(width, character):
    pattern = ""
    pattern += horizontal_line(width, character)
    pattern += vertical_line(width-1, 5, character)
    pattern += horizontal_line(width, character)
    pattern += vertical_line(0, 5, character)
    pattern += horizontal_line(width, character)
    return pattern
#number 3
def number_3(width, character):
    pattern = ""
    pattern += horizontal_line(width, character)
    pattern += vertical_line(width-1, 5, character)
    pattern += horizontal_line(width, character)
    pattern += vertical_line(width-1, 5, character)
    pattern += horizontal_line(width, character)
    return pattern
#number 4
def number_4 (width, character):
    pattern = ""
    pattern += two_vertical_lines(width, 5, character)
    pattern += horizontal_line(width, character)
    pattern += vertical_line(width-1, 5, character)
    return pattern
#number 5
def number_5 (width, character):
    pattern = ""
    pattern += horizontal_line(width, character)
    pattern += vertical_line(0, 5, character)
    pattern += horizontal_line(width, character)
    pattern += vertical_line(width-1, 5, character)
    pattern += horizontal_line(width, character)
    return pattern
#number 6
def number_6 (width, character):
    pattern = ""
    pattern += horizontal_line(width, character)
    pattern += vertical_line(0, 5, character)
    pattern += horizontal_line(width, character)
    pattern += two_vertical_lines(width, 5, character)
    pattern += horizontal_line(width, character)
    return pattern

#number 7
def number_7 (width, character):
    pattern = ""
    pattern += horizontal_line(width, character)
    pattern += vertical_line(width-1, 5, character)
    return pattern
#number 8
def number_8 (width, character):
    pattern = ""
    pattern += horizontal_line(width, character)
    pattern += two_vertical_lines(width, 5, character)
    pattern += horizontal_line(width, character)
    pattern += two_vertical_lines(width, 5, character)
    pattern += horizontal_line(width, character)
    return pattern
#number 9
def number_9 (width, character):
    pattern = ""
    pattern += horizontal_line(width, character)
    pattern += two_vertical_lines(width, 5, character)
    pattern += horizontal_line(width, character)
    pattern += vertical_line(width-1, 5, character)
    pattern += horizontal_line(width, character)
    return pattern
#PRINT DESIRED NUMBER PART C
# function:   print_number
# input:      a number to print (integer), a width value (integer) and a single character (string)
# processing: prints the desired number to the screen using the supplied width value
# output:     does not return anything
# function:   print_number
# input:      a number to print (integer), a width value (integer) and a single character (string)
# processing: prints the desired number to the screen using the supplied width value
# output:     does not return anything

def print_number (number, width, character):
    if number == 0:
        print (number_0(width, character))
    elif number == 1:
        print (number_1(width, character))
    elif number == 2:
         print (number_2(width, character))
    elif number == 3:
         print (number_3(width, character))
    elif number == 4:
         print (number_4(width, character))
    elif number == 5:
         print (number_5(width, character))
    elif number == 6:
        print (number_6(width, character))
    elif number == 7:
         print (number_7(width, character))
    elif number == 8:
         print (number_8(width, character))
    elif number == 9:
          print (number_9(width, character))
    print()

#PART D
def plus(width,character):
    pattern = ""
    space = width//2
    #loops 5 times because height is 5
    for i in range(0,5):
        # is width even
        if width%2==0:
            pattern+=((spacing-1)*" "+character+character+(space-1)*" ")+"\n"
            
        elif (i==2):
            pattern+=width*character+"\n"
        else:
            pattern+=(space*" "+character+space*" ")+"\n"
    return pattern

def minus(width, character):
    pattern=""
    #loops 5 times because height is 5
    for i in range(0,5):
        if(i==2):
            pattern+=(width*character)+"\n"

        else:
            pattern+=width*" "+"\n"

    return pattern

#PART E
# function:   check_answer
# input:      two numbers (number1 & number2, both integers); an answer (an integer)
#             and an operator (+ or -, expressed as a String)
# processing: determines if the supplied expression is correct.  for example, if the operator
#             is "+", number1 = 1, number2 = 2 and answer = 3 then the expression is correct
#             (1 + 2 = 3).
# output:     returns True if the expression is correct, False if it is not correct
# function:   check_answer
# input:      two numbers (number1 & number2, both integers); an answer (an integer)
#             and an operator (+ or -, expressed as a String)
# processing: determines if the supplied expression is correct.  for example, if the operator
#             is "+", number1 = 1, number2 = 2 and answer = 3 then the expression is correct
#             (1 + 2 = 3).
# output:     returns True if the expression is correct, False if it is not correct
def check_answer(num1,num2,answers,operator):
    if operator=="+":
        if (num1+num2)==answers:
            return True
        else:
            return False
    elif operator=="-":
        if (num1-num2) == answers:
            return True
        else:
            return False
    else:
        return False


