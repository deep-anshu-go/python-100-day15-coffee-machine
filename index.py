import art 
from menu import MENU

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
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

def get_total_ingredients_arr():
    max_ingredient_length = 0
    total_ingredients = {} 
    for key in MENU:
        ingredient_length = len(MENU[key]["ingredients"])
        if(ingredient_length > max_ingredient_length):
            max_ingredient_length = ingredient_length
            total_ingredients = MENU[key]["ingredients"]
    
    ingredients = []
    for key in total_ingredients:
        ingredients.append(key)
    
    return ingredients
    

def check_ingredients(coffee_name):
    
    ingredients = get_total_ingredients_arr()
    coffee_ingredients = MENU[coffee_name]["ingredients"]
    for ingredient in ingredients:
        try:
            MENU[coffee_name]["ingredients"][ingredient]
        except KeyError:
            coffee_ingredients.update({ingredient: 0})
            
    
    return coffee_ingredients

def check_coffee_resources(coffee_name):
    check_ingredients(coffee_name)
    # you are here you got the coffee ingredients 

        

def check_coffee(user_input):
    if user_input in MENU:
        check_coffee_resources(coffee_name = user_input)
    else:
        return "Invalid coffee name"

def coffeeMachine():
   
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
            check_coffee(user_input)
coffeeMachine()