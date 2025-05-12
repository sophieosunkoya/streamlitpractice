#name constants
product_names = ["soft drink","onion rings","small fries"]
product_costs = [0.99,1.29,1.49]
product_qty =[10,5,20]

#define function for adding the name
def isnameThere(name,string1):
    
    for i in product_names:
        if(i==name):
            print("Sorry, we already sell that product. Try again.")
            return True
    return False
#define add feature
def add():
      while True:
        product_name = input("Enter a new product name:")
        if product_name in product_names:
            print("Sorry, we already sell that product. Try again.")
            continue
        else:
            while True:
                price = float(input("Enter a product cost:"))
                if price <= 0:
                    print("Invalid cost. Try again.")
                    continue
                else:
                    while True:
                        quantity = int(input("How many of these products do we have? :"))
                        if quantity <= 0:
                            print("Invalid quantity. Try again.")
                            continue
                        else:
                            product_names.append(product_name)
                            product_costs.append(price)
                            product_qty.append(quantity)
                            break
                    break
        print("Product added!")
        break

#define remove feature
def remove():
    productName =input("Enter a product name: ")
    if productName in product_names:
        index = product_names.index(productName)
        product_names.pop(index)
        product_costs.pop(index)
        product_qty.pop(index)   
        print("Product removed! ")
    else:
        print("Product doesn't exist. Can't remove.")

#define update feature
def update():
    productName = input("Enter a product name: ")
    if productName in product_names:
        print("What would you like to update?")
        
        foodOption= input("(n)ame, (c)ost or (q)uantity: ")

        if foodOption=="n":
            name=input("Enter a new name: ")
            while (isnameThere(name, "Duplicate name!")):
                name=input("Enter a new name: ")
            product_names[product_names.index(productName)] =name
            print("Product name has been updated")
        elif foodOption =="c":
            cost=0
            while True:
                cost = float(input("Enter a new cost: "))
                if(cost <=0):
                    print("Invalid cost!")
                else:
                    product_costs[product_names.index(productName)]=cost
                    print("Product cost has been updated")
                    break
        elif foodOption =="q":
            qty =0
            while True:
                qty= int(input("Enter a new Quantity"))
                if(qty<=0):
                     print("Invalid quantity!")
                else:
                    product_qty[product_names.index(productName)]=qty
                    print("Product quantity has been updated")
                    break
            else:
                print("Invalid option")
            
    else:
        print("Product doesn't exist. Can't update.")
        return

 #define product lists feature   
def product_lists():
    while True:
        foodOption = input("(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate ,r(e)port or (q)uit:")
        if foodOption =="s":
            userInput = input("Enter a product name: ")
            if userInput in product_names:
                product_index = product_names.index(userInput)
                print('We sell "',userInput,'" at ',product_costs[product_index]," per unit",sep='')
                print("we currently have",product_qty[product_index],"in stock")
            else:
                print('Sorry, we don\'t sell "',userInput,'"',sep='')
        elif foodOption =="l":
            print("Product".ljust(25), "Price".ljust(7),"Quantity")
            for i in range(len(product_names)):
                print( product_names[i].ljust(25),str(product_costs[i]).ljust(7),product_qty[i])
        elif foodOption =="a":
            add()
        elif foodOption =="r":
            remove()
        elif foodOption =="u":
            update()
        elif foodOption == "e":
            print("Most expensive product: \t", max(product_costs), " (",
                  product_names[product_costs.index(max(product_costs))], ")", sep="")
            print("Least expensive product:\t", min(product_costs), " (",
                  product_names[product_costs.index(min(product_costs))], ")", sep="")
            value = 0
            for i in range(len(product_costs)):
                value += float(product_costs[i])*int(product_qty[i])
            print("Total value of all products:", round(value,2))

        elif foodOption =="q":
            print("See you soon!")
            break
        else:
            print("Invalid option,try again.")    
        print()        

product_lists()
