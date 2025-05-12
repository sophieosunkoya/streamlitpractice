# function:   Maximum
# input:      two integers
# processing: compare the integers 
# output:     returns the biggest integer

def maximum(a,b):
    if a>b:
        return a
    else:
        return b

# function:   Minimum
# input:      two integers
# processing: compare the integers 
# output:     returns the smallest integer
def minimum(a,b):
    if a<b:
        return a
    else:
        return b
a = 5
b = 10
c = 15
d = 20

ans1 = maximum(a,b)
ans2 = maximum(a,c)
ans3 = maximum(a,d)
print (ans1,ans2,ans3) # 10 15 20

ans4 = minimum(d,c)
ans5 = minimum(d,b)
ans6 = minimum(d,a)
print (ans4,ans5,ans6) # 15 10 5

ans7 = maximum( maximum(a,b), maximum(c,d) )
print ("The biggest is:", ans7)
