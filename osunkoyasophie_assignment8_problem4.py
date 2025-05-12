# function:    listlen
# INPUT:       a list
# PROCESSING:  determines the size of the list
# OUTPUT:      an integer representing the size of the list

def listlen(list1):
    x=0
    for i in list1:
        x=x+1
    return x


mylist=[10,20,30]
y=listlen(mylist)
print (y)

# function:    listmax
# INPUT:       a list
# PROCESSING:  obtains the largest element in the list
# OUTPUT:      returns the largest element in the list

def listmax(list1):
    x=list1[0]
    for i in list1:
        if i>x:
            x=i
    return x


mylist = [10, 20, 30, 5, 3]
y = listmax(mylist)
print (y)
print (mylist)

# function:    listcopy
# INPUT:       a list
# PROCESSING:  creates a new list which serves as a copy of the supplied list
# OUTPUT:      returns a new copy of the list

def listcopy(list1):
    x=[]
    for i in list1:
        x=x+[i]
    return x

mylist = [10, 20, 30]
y = listcopy(mylist)
print (y)

# function:    listappend
# INPUT:       a list and an element to add to the list (any data type)
# PROCESSING:  creates a new list which includes the new element appended
#              to the end of the list
# OUTPUT:      returns a new copy of the list

def listappend(list1,element):
    list1=list1+[element]
    return list1

mylist = [10, 20, 30]
y = listappend(mylist, 999)
print (y)

# function:    listinsert
# INPUT:       a list, a location (integer) and a data 
#              element (can be a string, float, Boolean or 
#              int)
# PROCESSING:  inserts the supplied data element into the 
#              list at the desired location
# OUTPUT:      return a new copy of the list that contains
#              the inserted element
def listinsert(list1,location,element):
   
    list1=list1+[0]
    
    for i in range(len(list1)-1,location-1,-1):
        if i == location:
            list1[location]=element
        else:
            list1[i]=list1[i-1]
           
    return list1

mylist = [10, 20, 30]
x = listinsert(mylist, 1, 999)
print (x)
print (mylist)

# function:    listremove
# INPUT:       a list and a data element (can be a string, 
#              float, Boolean or int)
# PROCESSING:  removes all occurrences of the supplied 
#              data element from the list.  You can assume 
#              that the data element is present in the list 
#              somewhere.
# OUTPUT:      return a new copy of the list with the
#              desired element removed

def listremove(list1, element):
    if list1:
        result = listremove(list1[1:], element)
        if list1[0] != element:
            result = [list1[0]] + result
        return result
    return []

mylist = [10, 20, 30]
y = listremove(mylist, 20)
print (y)
print (mylist)


# function:    listreverse
# INPUT:       a list
# PROCESSING:  creates a copy of the supplied list that
#              contains the same elements as the original
#              list, but in reverse order
# OUTPUT:      return a new copy of the list in reverse order

def listreverse(list1):
    if list1:
        return listreverse(list1[1:]) + [list1[0]]
    return []

mylist = [10, 20, 30]
x = listreverse(mylist)
print (x)
print (mylist)
