import string


def string_length(string):
    stringlength=len(string)
    return stringlength

def string_isalpha(string):
    if (string.isalpha() == True):
        return True
    else:
        return False
    
def string_adjustcase(string,b):
    if b=="lower":
        string=string.lower()
        return string
    elif b=="upper":
        string=string.upper()
        return string
    else:
        return string
    
def string_capitalize(string):
    result = ""
    firstletter = string.split()
    # Iterate over all elements in list
    for first in firstletter:
        # capitalize first letter of each word and add to a string
        if len(result) > 0:
            result = result + " " + first.strip().capitalize()
        else:
            result = first.capitalize()
    if not result:
        return original_str
    else:
        return result


print( string_capitalize("happy birthday sad kitten") )
# Happy Birthday Sad Kitten

print( string_capitalize("every word in this phrase should start with a capital letter") )
# Every Word In This Phrase Should Start With A Capital Letter

print( string_capitalize("EVERYTHING IS UPPERCASE ALREADY!") )
# Everything Is Uppercase Already!

print( string_capitalize("cRaZy MIxeD cAse") )
# Crazy Mixed Case
