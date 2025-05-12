

userName=input("Name: ")
editedName=""
sum1=0

#change to lowercase

userName=userName.lower()
#change to letters
for i in userName:
    if (i>="a" and i<="z"):
        editedName+=i
#print output
print("Your 'cleaned up' name is:",editedName)

print("Your 'cleaned up' name reduces to:")

for x in range(len(editedName)-1):
    i=ord(editedName[x])-96
    sum1+=i
    print(i,end='+')

sum1+= ord(editedName[-1])-96
print(ord(editedName[-1])-96,"=",sum1)




length=len(userName)
x=0

while(x!=length):
    sum1=sum1+(ord(userName[x])-97)
    x=x+1

while(sum1>9):
    n=sum1
    sum1=0
    while(x > 0):
        y=x%10
        sum1=sum1+y
        x = x//10

if(sum1==0): print ("emptiness, nothingness, blank");
if(sum1==1): print ("independence, loneliness, creativity, originality, dominance, leadership, impatience");
if(sum1==2): print ("quiet, passive, diplomatic, co-operation, comforting, soothing, intuitive, compromising, patient");
if(sum1==3): print ("charming, outgoing, self expressive, extroverted, abundance, active, energetic, proud");
if(sum1==4): print ("harmony, truth, justice, order discipline, practicality");
if(sum1==5): print ("new directions, excitement, change, adventure");
if(sum1==6): print ("love, harmony, perfection, marriage, tolerance, public service");
if(sum1==7): print ("spirituality, completeness, isolation, introspection");
if(sum1==8): print ("organization, business, commerce, new beginnings");
if(sum1==9): print ("romatic, rebellious, determined, passionate, compassionate");

