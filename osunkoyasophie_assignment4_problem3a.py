import string
import random
random_letter_choice = string.ascii_letters
def add_letters(string,num):
    newstring =""
    for i in string:
        letters=''
        for x in range(num):
            letters+=random.choice(random_letter_choice)
        newstring+= i +letters
    return newstring
#Method to delete a character
def delete_characters(string,num):
    i=0
    newstring=''
    while i<len(string):
        newstring+=string[i]
        i=i+num+1
    return newstring

#Function to flip word
def flip(string):
    mid=len(string)//2
    if len(string)%2 != 0:
         x=string[:mid]
         middle=string[mid]
         y=string[mid+1:]
         string=(y[::]+middle+x[::])
         return string
    else:
         x=string[:mid]
         y=string[mid:]
         string=(y[::]+x[::])
         return string

#Function ascii shift
def ascii_shift(string,num):
    newstring=''
    for i in range(len(string)):
        newstring+=chr(ord(string[i])+num)
    return newstring

#Shift left
def shift_left(string):
    result = string[1:] + string[0]
    return result

#Shift right
def shift_right(string):
    result= string[-1]+string[0:-1]
    return result

# define original word
original = "Hello!"

# loop to demonstrate the function
for num in range(1, 5):

    # scramble the word using 'num' extra characters
    scrambled = add_letters(original, num)

    # output
    print ("Adding", num, "random characters to", original, "->", scrambled)
