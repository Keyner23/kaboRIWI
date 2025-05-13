inventory={}                 # We create the dictionary where the products are stored

def enter_product(name,price,amount):     # We declare the function to add products
        inventory[name]=(float(price),int(amount))     # We create the key which is the name with the price and quantity values
        


def consult_product(inventory):   # We declare the function to query the inventory product
    if not inventory:      # We validate if the inventory is empty
        print("")
        print("THE INVENTORY IS EMPTY.")
        print("")
        return
    product_name=input("Enter the product name: ").strip()     # we request the name to search for
    name=product_name 
    if name.isalpha()==False:    # We validate if the written value is valid
        print("")
        print("ONLY TEXT VALUES ARE ACCEPTED.")
        print("")
    else:
        if product_name in inventory:      # We check if the written name exists in the inventory
            product_name=inventory[name] 
            print("")
            price, amount = inventory[name]   # we unpack the key values
            print(f"NAME: {name.upper()}")
            print(f"PRICE $ {price}")
            print(f"AMOUNT: {amount}")
            print("")
        else:
            print("")
            print(f"THE PRODUCT {name.upper()} NOT IN INVENTORY.")    # since it does not exist in the inventory
            print("")



def update(inventory):      # We declare the function to update the values ​​to a product
    if not inventory:      # We validate if the inventory is empty
        print("THE INVENTORY IS EMPTY.")
        print("")
        return
    name_update=input("Product you want to update: ").strip()
    if name_update.isalpha()==False:    # We validate if the inventory is empty
        print("")
        print("ONLY TEXT VALUES ARE ACCEPTED.")
        print("")
    else:
        if name_update in inventory:    # We check if the written name exists in the inventory
            price_update=input("Enter the new price: ").strip()
            if price_update.isdigit() == False or int(price_update)<=0:     # We verify that the new price is positive and different from 0
                print("")
                print("ONLY POSITIVE NUMBERS ARE ACCEPTED.")
                print("")
            else: 
                update_quantity=input("Enter the new amount: ") 
                if update_quantity.isdigit() == False or int(price_update)<0:    # We check that the amount is not negative
                    print("")
                    print("ONLY NON-NEGATIVE NUMERICAL VALUES ARE ACCEPTED.")
                    print("")
                else:
                    nueva_tupla=(price_update,update_quantity)    # A new tuple is created with the previously requested values
                    nombre=name_update
                    inventory[nombre]=nueva_tupla    # we assign the new values ​​to the key      
                    print("")
                    print(f"THE PRODUCT {name_update.upper()} IT HAS BEEN UPDATED CORRECTLY, ITS PRICE TO $ {price_update} AND ITS AMOUNT TO {update_quantity}.")
                    print("")
        else:   
            print("")
            print("THE PRODUCT ENTERED IS NOT IN THE INVENTORY.")     # since the name is not written in the inventory
            print("")



def delete_product(inventory):       # We declare the function to delete a product that is no longer available.  
    if not inventory:    # We validate if the inventory is empty
        print("")
        print("THE INVENTORY IS EMPTY.")
        print("")
        return
    product_delete=input("Enter the name of the product you want to delete: ").strip()
    if product_delete.isalpha()==False:    # We validate if the inventory is empty
        print("")
        print("ONLY TEXT VALUES ARE ACCEPTED.")
        print("") 
    if product_delete in inventory:     # We check if the written name exists in the inventory
        name=product_delete
        del(inventory[name])     # We use the built-in function to delete everything related to that key. 
        print("")
        print(f"THE PRODUCT HAS BEEN CORRECTLY DISPOSED OF {product_delete.upper()} FROM THE INVENTORY.")
        print("")
    else:
        print("")
        print("THE WRITTEN PRODUCT IS NOT IN THE INVENTORY.")    #since the name is not written in the inventory
        print("")



total_value= lambda: sum(float(price) * int(amount) for price, amount in inventory.values())        # We use a lambda function to multiply the prices and the quantity of the products.
    
while True:   
            print("INVENTORY MANAGER...")  # options menu
            print("---------------------------------------------")
            print("1"".Enter product.")
            print("2"".Consult product.")
            print("3"".Update price and quantity.")
            print("4"".Remove product.")
            print("5"".Total inventory value..")
            print("6"".Exit inventory.")
            print("---------------------------------------------")
            option=input("Type the option you want to execute: ")
            print("")

            if option=="1":  #option 1
                    for i in range(1,6):  # We open a cycle to request the first 5 products
                        name=input(f"Enter the product name: ").strip()
                        if name.isalpha()==False: # We validate if the inventory is empty
                            print("")
                            print("ONLY TEXT VALUES ARE ACCEPTED.")
                            print("")
                            break
                        else:
                            if name  in inventory:   # We check if the written name exists in the inventory
                                print("")
                                print(f"THE PRODUCT IS NOW AVAILABLE {name.upper()} IN THE INVENTORY")  # We show if the product already exists
                                print("")
                                break
                            else:
                                price=input("Enter the price of the product: ").strip()
                                if price.isdigit() == False or int(price)<=0:   # We check if the price is valid
                                    print("")
                                    print("ONLY NUMERIC VALUES GREATER THAN 0 ARE ACCEPTED.")
                                    print("")
                                    break
                                else:
                                    amount=input("Enter the quantity of the product: ").strip()
                                    if amount.isdigit() == False or int(amount)<0:   # We verify if the amount is valid
                                        print("")
                                        print("NEGATIVE AMOUNTS ARE NOT ACCEPTED")
                                        print("")
                                        break
                                    else:
                                        enter_product(name,price,amount)   # we call the add product function
                                        i+=1
                                        print("")
                                        print("")
                        i+=1


            elif option=="2":  #option 2
                consult_product(inventory) # we call the product search function


            elif option=="3":  #option 3
                update(inventory)    # we call the update product function
            

            elif option=="4":   #option 4
                delete_product(inventory)  # we call the delete product function


            elif option=="5":   #option 5
                total_value()
                print(f"TOTAL INVENTORY VALUE IS $ {total_value():.2f}")     # we print the result with two decimal places
                print("")


            elif option=="6":   #option 6
                print("SECTION CLOSED")
                exit()


            elif option !="1" and option!="2" and option!="3" and option!="4" and option!="5" and option!="6":       # if the answer is outside the allowed range
                print("INVALID OPTION.")
                print("")