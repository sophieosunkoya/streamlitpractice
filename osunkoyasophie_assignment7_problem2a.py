#ask for name
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
