a = 5
b = 10
c = 15
d = 20
def maximum(a,b):
    a = 5
    b = 10
    c = 15
    d = 20
    ans1 = maximum(a,b)
    return b
    ans2 = maximum(a,c)
    a = 5
    b = 10
    c = 15
    d = 20
    return c
    ans3 = maximum(a,d)
    a = 5
    b = 10
    c = 15
    d = 20
    return d
    print (ans1,ans2,ans3) # 10 15 20
def minimum(x,y):
    ans4 = minimum(d,c)
    return c
    ans5 = minimum(d,b)
    return b
    ans6 = minimum(d,a)
    return a
    print (ans4,ans5,ans6) # 15 10 5

ans7 = maximum( maximum(a,b), maximum(c,d) )
print ("The biggest is:", ans7)
