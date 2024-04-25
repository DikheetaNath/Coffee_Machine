Menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "milk": 150
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100

        },
        "cost": 3.0
    }
}

resources = {
    "water": 300,
    "coffee": 100,
    "milk": 200
}

# TODO : 1.Create coffee maker function by checking resources and  deducting respective amt from total
# TODO : 2.Create process money and give change back or not enough money

coffee_ready : bool = True
Machine : bool = True

from art import logo
print(f'{logo}')

def take_money():
    print('Please insert coins')
    quarter = float(input('How many quaters?'))
    dime = float(input('How many dimes?'))
    nickel = float(input('How many nickels?'))
    penny = float(input('How many pennies?'))
    total = quarter * 0.25 + dime * 0.1 + nickel * 0.05 + penny * 0.01

    return total


def process_coins(coffee):
    coffee_ready = True
    total = take_money()
    if round(total,2) >= Menu[coffee]["cost"]:
        change = total - Menu[coffee]["cost"]
        print(f'Here is your change ${round(change,2)}')

    else:
        print('Sorry, that\'s not enough money.Money refunded')
        coffee_ready = False

    return coffee_ready


def coffee_maker(coffee):
    coffee_ready = False
    for ing in Menu[coffee]['ingredients']:
        if resources[ing] > Menu[coffee]['ingredients'][ing]:
            resources[ing] = resources[ing] - Menu[coffee]['ingredients'][ing]
            coffee_ready = True
        else:
            coffee_ready = False
            print(f'Sorry, there\'s not enough {ing}')
            break

    return coffee_ready


def print_report():
    for item in resources:
        print(f'{item} = {resources[item]}')


def check_function(Machine, coffee):
    if coffee == 'off':
        Machine = False
        return Machine
    elif coffee == 'report':
        print_report()
        return Machine
    else:
        if coffee_maker(coffee):
            if process_coins(coffee):
                print(f'Here\'s your order ☕. Enjoy your {coffee}')
                return Machine


while Machine:
    coffee = input(
        'what would you like to have?\ncoffee options -> \'espresso\', \'cappuccino\', \'latte\' \n2.\'off\' to turn off the machine\n3.\'report\' to print report\n')
    Machine = check_function(Machine, coffee)