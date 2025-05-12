import os
from collections import defaultdict

# function:   cleanup_string
# input:      a string to clean up
# processing: (1) makes the entire string lowercase.
#             (2) retains only alphabetic and space characters
#                 [all numbers, punctuation and special characters removed]
# output:     returns the cleaned up string
def cleanup_string(s):
    result = ''
    for ch in s:
        if ch.isalpha() or ch.isspace():
            result += ch.lower()
    return result


# TEST CODE
test1 = cleanup_string("Hello World! This is a simple test of this function!")
print(test1)
# hello world this is a simple test of this function

test2 = cleanup_string("ABC123abc this is Another TEST!!!#@@")
print(test2)
# abcabc this is another test

test3 = cleanup_string("I'm so happy today! La la la la it doesn't get any better than this.")
print(test3)
# im so happy today la la la la it doesnt get any better than this

files = os.listdir("data")
print (files)
