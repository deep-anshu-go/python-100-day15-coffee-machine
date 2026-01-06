import art 
from menu import MENU

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coins = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01
}

money = 0

def formatResources(resources):
    print("\nResources")
    for key in resources:
        print(f"{key} - {resources[key]}{"ml" if key in ("water", "milk") else "g" if key == 'coffee' else ''}")
        
def restartMachine(machine):
    input("press enter ---->")
    machine()

def report(money = 0, machine = None):
    formatResources(resources)
    print(f"Money: ${money}")
    restartMachine(machine)
        
def showMenu(menu):
    print(art.coffee_art)
    print("Welcome!")
    for coffee in menu:
        print(f"{coffee.capitalize()} - ${menu[coffee]["cost"]}")

def askMenu(menu, msg = ""):
    if(msg != ""):
        print("\n" * 50)
        print(msg)
    showMenu(menu)
    user_input = input("What would you like? ")
    return user_input     

def checkSecretCode():
    secret_code = input("Secret Code: ")
    if(secret_code == "offcoff"):
        return False
    else:
        askMenu(MENU, msg = "**Inavlid Secret**")

def fill_missing_ingredients():
    for coffee in MENU:
        for ingredients in resources:
            if(not ingredients in MENU[coffee]["ingredients"]):
                MENU[coffee]["ingredients"].update({ingredients: 0})
              
def is_resources_available(coffee_resources, user_input_coffee_name):
    available = "yes"
    ingredient = ""
    for ingredients in coffee_resources:
        if(not ingredients in resources):
            available = "no"
            ingredient = ingredients
    return available, ingredient

def get_coffee_price(coffee):
    return MENU[coffee]["cost"]

def calculate_user_coin(user_coins):
    calculated_coin = {}
    for coin in user_coins:
        calculated_coin[coin] = round(coins[coin] * user_coins[coin],2)
        
    total_amount = 0
    for coin in calculated_coin:
        total_amount += calculated_coin[coin]
        
    return total_amount
        
def insert_coins(coffee_name):
    is_enough_money = "yes"
    user_input_coin = {}
    msg = ""
    
    for coin in coins:
        try:
            user_input_coin.update({coin: int(input(f"{coin}: $"))}) 
        except:
            
            total_amount = calculate_user_coin(user_input_coin)
            
            print(f"\nCoins Refunded: ${total_amount}")
            msg = "Invalid Coin entry"

            is_enough_money = "no"
    
    coffee_price = get_coffee_price(coffee_name)
    total_amount = calculate_user_coin(user_input_coin)
    
    if(total_amount != coffee_price):
        is_enough_money = "no"
        msg = "Sorry that's not enough money."
        print(f"\nMoney Refunded: ${total_amount}")

    return is_enough_money, msg

def is_enough_resource_available(coffee_resources, coffee_name, machine = None):
    is_enough_resource = "yes"
    ingredient = ""
    for resource in resources:
            if(resources[resource] - coffee_resources[resource] < 0):
                is_enough_resource = "no"
                ingredient = resource

    return is_enough_resource, ingredient  
    
def use_resource(coffee_name):
    for resource in MENU[coffee_name]["ingredients"]:
        resources.update({resource: resources[resource] - MENU[coffee_name]["ingredients"][resource]})

def calculate_coffee_resources(coffee_name, machine = None):
    coffee_resources = MENU[coffee_name]["ingredients"]
    available, unavailable_ingredient = is_resources_available(coffee_resources, coffee_name)
    if(available == "yes"):
        is_enough_resource, ingredient = is_enough_resource_available(coffee_resources, coffee_name, machine)
        if(is_enough_resource != "yes"):
            print(f"Sorry there is not enough {ingredient}")
        else:
             # here are you pending calulating resouces 
            is_enough_money, msg = insert_coins(coffee_name)
            if(is_enough_money == "yes"):
                use_resource(coffee_name)
                print(f"Enjoy sir, Here is your {coffee_name}")    
                restart_machine = machine()
            else:
                print(msg)
                restart_machine = machine()
                    
    else:
        print(f"{coffee_name.capitalize()} requires {unavailable_ingredient}, which we don’t have right now.")
        
def check_coffee(user_input, machine = None):
    if user_input in MENU:
        calculate_coffee_resources(user_input, machine)
    else:
        return "Invalid coffee name"

def coffeeMachine():
    fill_missing_ingredients()
    # what fill missing ingredients do ? it fill the missing ingredients that is in the resoures but not in the coffee ingredients with the value 0
    on = True
    while(on):
        user_input = askMenu(MENU)
        if(user_input == "off"):
           on = checkSecretCode()
        elif(user_input == "report"):
            # here, I pass the machine function which is coffeeMachine() to the report function to restart the machine after looking at the report
            report(machine = coffeeMachine)
            on = False
        else:
            check_coffee(user_input, machine = coffeeMachine)

coffeeMachine()