# importing necessary things
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# creating objects using classes
moneyMachine = MoneyMachine()
coffeeMaker = CoffeeMaker()
menu = Menu()
is_on = True

# using classes and all the building blocks, assemble them and make the coffee machine
while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        coffeeMaker.report()
        moneyMachine.report()
    else:
        drink = menu.find_drink(choice)

        drink_being_none = drink is not None
        are_resources_sufficient = coffeeMaker.is_resource_sufficient(drink)
        transactions_successful = moneyMachine.make_payment(drink.cost)

        if drink_being_none and are_resources_sufficient and transactions_successful:
            coffeeMaker.make_coffee(drink)

# --------------------------------------end----------------------------------
