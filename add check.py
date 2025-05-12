product_names = ["soft drink","onion rings","small fries"]
product_costs = [0.99,1.29,1.49]
product_qty =[10,5,20]
def isnameThere(name,string1):
    
    for i in product_names:
        if(i==name):
            print("Sorry, we already sell that product. Try again.")
            return True
    return False
def add_product():
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
            break
    print("Product added!")
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
            add_product()




  cost=0
            while(cost<=0):
                try:
                    cost = float(input("Enter a new cost: "))
                    if(cost <=0):
                        raise Exception()
                except:
                    print("Invalid cost!")
            product_costs[product_names.index(productName)]=cost
            print("Product cost has been updated")
product_lists()
