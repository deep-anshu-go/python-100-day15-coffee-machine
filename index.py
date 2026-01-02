import art 
import menu

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
        askMenu(menu.MENU, msg = "**Inavlid Secret**")

def coffeeMachine():
    on = True
    while(on):
        user_input = askMenu(menu.MENU)
        if(user_input == "off"):
           on = checkSecretCode()
        elif(user_input == "report"):
            # here, I pass the machine function which is coffeeMachine() to the report function to restart the machine after looking at the report
            report(machine = coffeeMachine)
            on = False
        
coffeeMachine()