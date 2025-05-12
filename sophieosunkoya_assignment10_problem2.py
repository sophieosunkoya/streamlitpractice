import os



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




files = os.listdir("assignment10/data")
print (files)
  

all_files=os.listdir('assignment10/data')


    

search = {}

for file in files:
    f=open("assignment10/data/"+file,"r")
    text = f.read()
    text = cleanup_string(text)
    words = text.split(' ')
    for word in words:
        if word not in search:
            search[word] = [file]
        else:
            if file not in search[word]:
                search[word].append("assignment10/data")

print(len(search))






print ('happy:', search['happy'])
print ('cat:', search['cat'])
print ('rainbow:', search['rainbow'])
print ('apple:', search['apple'])

        
