import string
import random

random_letter_choice = string.ascii_letters

#validate the string
def validate(string):
    return string.upper()=='A' or string.upper()=='X' or string.upper()=='F' or string.upper()=='U' or string.upper()=='D' or string.upper()=='L' or string.upper()=='R'

#Method to add random charcter after each letter
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
def ascii_shift_up(string):
    newstring=''
    for i in range(len(string)):
        newstring+=chr(ord(string[i])+1)
    return newstring

def ascii_shift_down(string,num):
    newstring=''
    for i in range(len(string)):
        newstring+=chr(ord(string[i])-1)
    return newstring

#Shift left
def shift_left(string):
    result = string[1:] + string[0]
    return result

#Shift right
def shift_right(string):
    result= string[-1]+string[0:-1]
    return result

def main():
    #Pattern
    pattern1=input("Enter an encoder pattern, 'end' to end: ")
#Loop until pattern end
    while pattern1.upper()!="END":
        word1=input("Enter a word to encode/decode: ")
        for i in range(len(pattern1)):
            if(validate(pattern1[i])):
                if pattern1[i].upper()=='A':
                    word1=add_letters(word1,1)
                    print('Added 1 character: ',word1)
                elif pattern1[i].upper()=='F':
                    word1=flip(word1)
                    print("Flipped: ",word1)
                elif pattern1[i].upper()=='U':
                    word1=ascii_shift_up(word1)
                    print('ASCII shifted up: ',word1)
                elif pattern1[i].upper()=='D':
                    word1=ascii_shift_down(word1)
                    print('ASCII shifted down: ',word1)
                elif pattern1[i].upper()=='L':
                    word1=shift_left(word1)
                    print('Shifted left: ',word1)
                elif pattern1[i].upper()=='R':
                    word1=shift_right(word1)
                    print('Shifted right: ',word1)
                elif pattern1[i].upper()=='X':
                    word1=delete_characters(word1)
                    print('Deleted 1 character: ',word1)
            else:
                print("Unrecognized command: ? -- ignoring")
        pattern1=input("Enter an encoder pattern, 'end' to end: ")


main()
