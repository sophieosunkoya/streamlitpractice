import urllib.request

url ="https://002-text-files.glitch.me/states.txt"

response=urllib.request.urlopen(url)

data=response.read().decode("utf-8")



data=data.split("\n")
states={}
for i in data:
    pair=i.split(",")
    states[pair[1]]=pair[0]
print(states)

import random
lives=3

stateslist=[]

for key in states:
    stateslist.append(key)

while lives>0:
    state=random.choice(stateslist)
    guess=input("What is the capital of"+state)
    if guess== states[state]:
        print("Correct")
    else:
        print("Incorrect")
        lives-=1
        if lives == 0:
            print("you lost")
        else:
            print("You have"+str(lives),"lives left")

#words=[]
#frequency=[]

#for i in data:
    #if i in words:
        #continue
    #else:
        #words.append(i)


#for i in words:
    #count=data.count(i)
    #frequency.append(count)

#mostword=frequency.index(max(frequency))

#winner=words[mostword]
#print(winner)
