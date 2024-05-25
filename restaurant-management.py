# creating a restaurant management system using python

# MENU OF RESTAURANT
menu = {
    'Pizza' : 40,
    'Pasta' : 50,
    'Burger' : 60,
    'Sandwich' : 70,
    'Coffee' : 80,
}

print("WELCOME TO .PY RESTAURANT ")
# PRINT MENU 

print("MENU :>")
print("Pizza : Rs40\nPasta : Rs50\nBurger : Rs60\nSandwich : Rs70\nCoffee : Rs80")

order_total = 0

item_1 = input("Enter the name of item you want to order : ")
if item_1 in menu:
    order_total += menu[item_1]
    print("Your order is : ", item_1)
else:
    print(f"Item {item_1} is not available !!")

another_order = input("Do you want to anything else ? (Yes/No) ")
if another_order == "Yes":
    item_2 = input("Enter the name of second item : ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"Item {item_2} is not available !!")
print(f"The total amount of items to pay is {order_total}Rs")