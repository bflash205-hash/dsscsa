#Project on Coffee Shop
print("            ","COFFEE SHOP")
print("Hello!,welcome to our coffee shop")

menu={"espresso": 120,
      "black coffee":80,
      "cappuccino":100,
     "iced latte": 150,
    "latte americano": 100}

money=0
order_list=[]
def order_espresso(money):
    print("You ordered Espresso")
    money= money + menu["espresso"]
    order_list.append("Espresso")
    return money

def order_black_coffee(money):
    print("You ordered Black Coffee")
    money=money+ menu["black coffee"]
    order_list.append("Black Coffee")
    return money

def order_cappuccino(money):
    print("You ordered Cappuccino")
    money = money + menu["cappuccino"]
    order_list.append("Cappuccino")
    return money

def order_iced_latte(money):
    print("You ordered iced latte")
    money = money +menu["iced latte"]
    order_list.append("Iced Latte")
    return money

def order_latte_americano(money):
    print("You ordered Americano")
    money= money + menu["latte americano"]
    order_list.append("latte americano")
    return money

while True:
    print("\n Menu Card")
    print("1. espresso", menu["espresso"])
    print("2. black coffee", menu["black coffee"])
    print("3. cappuccino", menu["cappuccino"])
    print("4. iced latte", menu["iced latte"])
    print("5. latte americano", menu["latte americano"])
    print("6. View my order")
    print("7. Pay Bill and Exit")

    choice=int(input("enter your choice from (1-6):"))

    if choice == 1:
        money = order_espresso(money)
        print("espresso has been added")
    elif choice == 2:
        money = order_black_coffee(money)
        print("black coffee has been added")
    elif choice == 3:
        money = order_cappuccino(money)
        print("cappuccino has been added")
    elif choice == 4:
        money = order_iced_latte(money)
        print("iced latte has been added")
    elif choice == 5:
        money = order_latte_americano(money)
        print("latte americano has been added")
    elif choice==6:
        if len(order_list)==0:
            print("no items ordered yet")
        else:
            print("You have ordered")
            for items in order_list:
                print(items)

    
    elif choice == 7:
        print("Your total bill is:",money)
        pay=int(input("Enter the amount to be paid, thank you:Rs"))
        if pay==money:
            print("Paymenet successful, thanks for visiting")
            break
        elif pay<money:
            print("The entered amount is insufficient, please try again")
        else:
            change=pay-money
            print("Thanks for paying, here s your change-Rs",change)
            break
    else:
        print("Please choose a valid option")


