MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def coins():
    quarters=int(input("How many quarters?"))*0.25
    dimes=int(input("How many dimes?"))*0.10
    nickels=int(input("How many nickels?"))*0.05
    pennies=int(input("How many pennies?"))*0.01
    money_given=float(quarters+dimes+nickels+pennies)
    return money_given


def when_report():
    global coffee_now
    coffee_now=resources['coffee']
    global water_now
    water_now=resources['water']
    global milk_now
    milk_now=resources['milk']


def resource_sufficient(coffee_ingredient):
    for item in coffee_ingredient:
        if resources[item]<coffee_ingredient[item]:
            print(f'Sorry there is not enough {item}')
            return False
    else:
        return True

def accounts(cost_coffee,coffee_chosen):
    if coffee_chosen== 'espresso' or coffee_chosen=='latte' or coffee_chosen=='cappuccino':
        print("Please insert coins")
        money_please = coins()
        if money_please < cost_coffee:
            print("Sorry that's not enough money. Money refunded")
            return
        elif money_please >= cost_coffee:
            change = money_please - MENU[coffee_chosen]["cost"]
            global profit
            profit+=MENU[coffee_chosen]["cost"]
            print(f"Here is ${round(change, 2)} in change")   #by myself!
            print(f"Here is your {coffee_chosen}. Enjoy!")

            ingredient_list = MENU[coffee_chosen]["ingredients"]
            for item in ingredient_list:
                resources[item]-=ingredient_list[item] #deduct the ingredients from resource
            return

profit=0       #declared here & inside accounts(). This is initial value, accounts() will contain profit value while coffee machine is running
coffee_over=False
while not coffee_over:
    coffee_type=input("What would you like?(espresso/latte/cappuccino)\n").lower()
    if coffee_type=='espresso' or coffee_type=='latte' or coffee_type=='cappuccino':
        ingredient_list = MENU[coffee_type]["ingredients"]
        cost_of= MENU[coffee_type]["cost"]

        is_sufficient=resource_sufficient(coffee_ingredient=ingredient_list)

        if is_sufficient:                  #DID THIS MYSELF!!!!
            accounts(cost_coffee=cost_of,coffee_chosen=coffee_type)

    elif coffee_type == 'report':
        when_report()        #reaaaalllly proud of myself for using this
        print(f"WATER:{water_now}ml")
        print(f"MILK:{milk_now}ml")
        print(f"COFFEE:{coffee_now}g")
        print(f"MONEY:${profit}")

    elif coffee_type == 'off':
        exit()



