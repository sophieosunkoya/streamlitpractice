def validate(prompt,datatype='float',low='unlimited',high='unlimited'):
    s=input(prompt)
    if datatype=='float':#checking whether datatype is float
        try:#to catch datatype conversion error
            s=float(s)#converting to float
            if low!='unlimited':
                if s<low:#checking whether number is less than the lower limit
                    return 'invalid range, try again'
            if high!='unlimited':
                if s>high:#checking whether the number is greater than the higher limit
                    return 'invalid range, try again'
            return s
        except:#catching exception
            return ('Not a number')
        
    if datatype=='integer':#checking whether datatype is integer
        try:#to catch datatype conversion error
            s=int(s)#converting to integer
            if low!='unlimited':
                if s<low:#checking whether number is less than the lower limit
                    return 'invalid range, try again'
            if high!='unlimited':
                if s>high:#checking whether the number is greater than the higher limit
                    return 'invalid range, try again'
            return s
        except:#catching exception
            return ('Not a number')



#creating initial dictionary
inventory= {
                'soft drink': [0.99, 10],
                'onion rings': [1.29, 5],
                'small fries': [1.49, 20]
            }
#creating menu
choice=''
while choice!='q':
    print('(s)earch for a product ',end="")
    print('(l)ist all products ',end="")
    print('(a)dd a prodcut ',end="")
    print('(r)emove a product ',end="")
    print('(u)pdate a product ',end="")
    print('R(e)port on all products ',end="")
    print('(q)uit: ')
    
    choice=input()#getting user's choice
    if choice=='s':
        print()
        name=input('Enter a product name: ')
        if name in inventory:
            print('We sell \'',name,'\' at ',inventory[name][0],' per unit')
        else:
            print('Sorry, we don\'t sell \'',name,'\'')
        print()
    elif choice=='l':
        print()
        print('Product\t\tPrice\tQuantity')
        print('------------------------------')
        for x in inventory.keys():
            #x,'<10s',inventory[x][0],"<10s",inventory[x][1])
            table="{:<15s}{:<10.2f}{:<10d}".format(x,inventory[x][0],inventory[x][1])
            print(table)
        print()
    elif choice=='a':
        print()
        name=input('Enter a product name: ')
        if name in inventory:
            print('Duplicate product name')
        else:
            #performing validation
            price=''
            while True:
                price=validate("Enter a price(greater than 0)","float",0)
                if price=='Not a number' or price=='invalid range, try again':
                    print(price)
                    continue
                else:
                    break
            amount=''
            while True:
                amount=validate("Enter an inventory amount between 1 and 100","integer",1,100)
                if amount=='Not a number' or amount=='invalid range, try again':
                    print(amount)
                    continue
                else:
                    break
            inventory[name]=[price,amount]
            print('Product added')
            print()
    elif choice=='r':
        print()
        name=input('Enter a product name: ')
        if name not in inventory:
            print('Unknown product name')
        else:
            del inventory[name]#deleting product
            print('Product removed')
        print()
    elif choice=='u':
        print()
        name=input('Enter a product name: ')
        if name not in inventory:
            print('Unknown product name')
        else:
            y=input('(n)ame,  (p)rice,  (a)mount?')
            if y=='n':
                 #performing validation
                name2=''
                while True:
                    name2=input('Enter a new name: ')
                    if name2 in inventory:
                        print('Product name already exists')
                        break
                        
                    else:
                       
                        inventory[name2]=inventory.pop(name)
                        print('Product renamed')
                        print()
                        break
            elif y=='p':
                price=''
                while True:
                    price=validate("Enter a price: ","float",0)
                    if price=='Not a number' or price=='invalid range, try again':
                        print(price)
                        continue
                    else:
                        break
                inventory[name][0]=price
                print('Price updated')
                print()
            elif y=='a':
                amount=''
                while True:
                    amount=validate("Enter an inventory amount between 1 and 100","integer",1,100)
                    if amount=='Not a number' or amount=='invalid range, try again':
                        print(amount)
                        continue
                    else:
                        break
                inventory[name][1]=amount
                print('Product updated')
            else:
                print('invalid entry')
            print()
            
                
                
    elif choice=='e':
        print()
        minitem=maxitem=list(inventory.keys())[0]#getting the first key in dictionary
        min=max=inventory[minitem][0]#getting price of first product
        sum=0
        for x in inventory.keys():
            sum=sum+inventory[x][0]*inventory[x][1]#finding total price
            if min>inventory[x][0]:#checking for minimum value
                min=inventory[x][0]
                minitem=x
            if max<inventory[x][0]:#checking for highest value
                max=inventory[x][0]
                maxitem=x
        print('Total cost of all items in the inventory: ',sum)
        print('Highest priced item: ',max,' is ',maxitem)
        print('Lowest priced item: ',min,' is ',minitem)
        print()
    elif choice=='q':
        print()
        print('See you soon!')
        print()
    else:
        print()
        print('Unknown command, try again')
        print()
