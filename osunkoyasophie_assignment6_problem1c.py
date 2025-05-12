# function:   Valid date
# input:      two integers
# processing: computes if the date and month are valid
# output:     returns a boolean 


def valid_date(month,day):
    if isinstance(month,int)==False or isinstance(day,int)==False:
        return False

    if month<1 or month>12:
        return False
        
        
    if month==4 or month==6 or month==9 or month==11:
        if day<1 or day>30:
            return False
            

    if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
        if day<1 or day>31:
            return False
            

    if month==2:
        if day<1 or day>28:
            return False
            

    return True


        
        
