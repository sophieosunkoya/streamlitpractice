scores = "95,100,67,33,88"

result=[]

splitdata=scores.split(",")

for i in splitdata:
    int_i=int(i)
    result.append(int_i)

print("Total",len(result)) 
print("Average",sum(result)/len(result))
print("Highest",max(result))
print("lowest",min(result))

print("drop lowest",( sum(result) - min(result) ) / (len(result)-1))
