import urllib.request


url ="http://002-text-files.glitch.me/world-series.txt"



    # initiate request to URL
response = urllib.request.urlopen(url)

    # read data from URL as a String, making sure
    # that the String is formatted as a series of ASCII characters
data = response.read().decode('utf-8')
    
    # let's split our data into a list
split_data = data.split("\n")


test_list = ["Sophie", "Emily", "Emily"]
def most_frequent(split_data):
    counter = 0
    num = split_data[0]
     
    for i in split_data:
        frequency = split_data.count(i)
       
        if(frequency> counter):
            counter = frequency
            num = i
 
    return num

print(most_frequent(split_data))


