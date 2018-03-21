import uuid


menu_categories = {
    'Appetizers': ['Pop-Tarts', 'Breadsticks', 'Chimichangas', 'Nachos', 'Funyons', 'Snickers'],
    'Entrees': ['Cream of Frog', 'Clam Chowder', 'Crab Rangoon', 'Burger', 'Taco', 'Spaghetti'],
    'Desserts': ['Smarties', 'Mochi', 'Chocolate Circuits', 'Cheesecake', 'Fruit', 'Apple Pie'],
    'Drinks': ['Sprite', 'Most Bitterest IPA Ever', 'Root Beer Float', 'Coke', 'Milk', 'Coconut Juice'],
    'Sides': ['Lemons', 'Popcorn', 'French Fries', 'French Toast', 'Mashed Potatoes', 'Corn'],
}

menu_prices = {
    'pop-tarts': 2.50,
    'breadsticks': 1.10,
    'chimichangas': 7.50,
    'nachos': 5.00,
    'funyons': 4.50,
    'snickers': 2.00,
    'cream of frog': 11.95,
    'clam chowder': 11.00,
    'crab rangoon': 22.00,
    'burger': 5.00,
    'taco': 2.00,
    'spaghetti': 9.50,
    'smarties': 1.00, 
    'mochi': 2.50,
    'chocolate circuits': 4.00,
    'cheesecake': 7.00,
    'fruit': 25.00,
    'apple pie': 11.00,
    'sprite': 2.50,
    'most bitterest ipa ever': 8.00,
    'root beer float': 8.00,
    'coke': 45.00, 'Milk': 5.00,
    'coconut juice': 2.50,
    'lemons': 2.00,
    'popcorn': 2.50,
    'french fries': 1.45,
    'french toast': 3.50,
    'mashed potatoes': 4.50,
    'corn': 2.50,
}

tax = 10.01
cart = {}


def user_input():
    while 1:
        order = input('>> ')
        if order == 'q':
            print('Goodbye.')
            break
        elif order.split()[0] == 'remove':
            remove_cart(order[7:].lower())
        elif order == 'menu':
            print_menu()
        elif order == 'order':
            print_cart(cart)
        else:
            add_to_cart(order.lower())

def print_cart(cart):
    """prints out all items in cart
    """
    printstring = '{0}CART{0}\nOrder #{1}\n'.format('='*20, uuid.uuid4())
    for item, amount in cart.items():
        printstring += '\n{}: {}'.format(item, amount)
    printstring += '\nTotal: {:>31}{:.2f}\n{}'.format('$', sum([menu_prices[item]*count for item,count in cart.items()]), '='*43)
    print(printstring)
    return printstring

def print_menu(menu):
    """
    Prints out all items on the Menu
    """
    printstring = 'Our Menu:'
    for cat,cat_list in menu.items():
        printstring += '\n\n{}\n{}'.format(cat,'*'*25)
        for item in cat_list:
            printstring += '\n' + item

    print(printstring)
    return printstring


def remove_cart(item):
    """
    Accepts a request/order from user_input and validates if the request is in the cart and if so removes 1 of the
    specified product. If the item is no longer in cart it gets truanted.
    """

    if item in cart:
        cart[item] -= 1
        if cart[item] == 0:
            del cart[item]
        print('{} has been removed.'.format(item))
        print('Total: {:>17}{:.2f}\n{}'.format('$', sum([menu_prices[item]*count for item,count in cart.items()]), '*'*28))
    else:
        print('{} not in cart.'.format(item))


def add_to_cart(item):
    """
    Accepts a request/order from user_input and validates if the request is inside the menu dictionary
    And if then appends to the users cart for checkout
    """
    if item not in [item.lower() for item in menu_prices]:
        print('{} not in menu.'.format(item))
    else:
        cart[item] = cart[item] + 1 if item in cart else 1
        print('{} added to order.'.format(item))


if __name__ == '__main__':
    print("Welcome to Snakes Cafe!\n\
            Press 'q' any time to exit\n\
            Type 'remove <item>' to remove an item\n\
            Type 'menu' to see our menu\n\
            Type 'order' to see your order\n")
    print_menu(menu_categories)
    print('\n{0}\n** What would you like to order? **\n{0}'.format('*' * 35))
    user_input()

