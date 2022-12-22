from coffee_menu import resources
print(resources)
machine_off = False
water = 300
milk = 200
coffee = 100


def check_resources(water, milk, coffee, order_no):

    if order_no == '1':
        water -= 50
        coffee -= 18
    elif order_no == '2':
        water -= 200
        milk -= 150
        coffee -= 24
    elif order_no == '3':
        water -= 250
        milk -= 100
        coffee -= 24
    else:
        print("Error : Enter correctly !")
    if water > 0 and milk > 0 and coffee > 0:
        return 1
    else:
        return 0


def coin_calculate():
    quarters = int(input("Enter no of Quarters : "))
    dimes = int(input("Enter no of dimes : "))
    nickles = int(input("Enter no of nickles : "))
    pennies = int(input("Enter no of pennies : "))
    cost = (quarters*0.25)+(dimes*0.10)+(nickles*0.05)+(pennies*0.01)
    return cost


def transaction_successful(order_no, payment):
    if order_no == '1':
        if payment >= 1.5:
            return 1
        else:
            return 0
    elif order_no == '2':
        if payment >= 2.5:
            return 1
        else:
            return 0
    elif order_no == '3':
        if payment >= 3.0:
            return 1
        else:
            return 0
    else:
        return "Error"


def change(order_no, payment):
    change_money = 0.0
    if order_no == '1':
        if transaction_successful(order_no,payment) == 1:
            change_money = payment - 1.5
    elif order_no == '2':
        if transaction_successful(order_no, payment) == 1:
            change_money = payment - 2.5
    elif order_no == '3':
        if transaction_successful(order_no, payment) == 1:
            change_money = payment - 3.0
    return change_money


while not machine_off:
    order = input("What would you like : \n"
                      "---MENU---\n"
                      "1 for Espresso   - $1.5\n"
                      "2 for latte      - $2.5\n"
                      "3 for cappuccino - $3.0\n")
    sufficient_resource = check_resources(300, 200, 100, order)
    if order == 'report':
        print(f"Available resources are :\nWater = {water}ml\nMilk = {milk}ml\nCoffee = {coffee}mg")
    elif order == 'off':
        machine_off = True
    if sufficient_resource == 1:
        total_bill = coin_calculate()
        sufficient_coin = transaction_successful(order, total_bill)
        if sufficient_coin == 1:
            total_change = change(order, total_bill)
            print(f"Here's your Coffee ☕\nAnd Here's your change {total_change}")
        else:
            print(f"Sorry , You've to enter more money for your drink .")
    else:
        print("Sorry but the machine's out of resources . Enter report during menu to know the current resources.")

    cont=int(input("Would you like to continue (1 for YES /0 for NO) ?"))
    if cont == 1:
        machine_off = False
    elif cont == 0:
        machine_off = True