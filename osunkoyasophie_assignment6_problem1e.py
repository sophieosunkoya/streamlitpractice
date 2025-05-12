def simple_sort_version2(a,b,c):
    if a<b and a<c:
        if b<c:
            return a,b,c
        else:
            return a,c,b
        
    if b<a and b<c:
        if a<c:
            return b,a,c
        else:
            return b,c,a

    if c<b and c<a:
        if b<a:
            return c,b,a
        else:
            return c,a,b
   
       

a,b,c = simple_sort_version2(20,10,6)

print(a,b,c)
