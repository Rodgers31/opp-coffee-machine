from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


# items
items_menu = Menu()
drink_names = items_menu.get_items()


# report
# items_report = CoffeeMaker().report()

is_on = True
while is_on:
    choice = input(f"What would you like? ({drink_names}): ")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(CoffeeMaker().report())
    else:
        drink_exist = items_menu.find_drink(choice)
        if drink_exist:
            print('menu sh', )

            money_received = MoneyMachine().process_coins()
            # MoneyMachine().make_payment()


