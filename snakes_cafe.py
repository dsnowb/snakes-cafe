import uuid


menu_categories = {
    'Appetizers': ['Pop-Tarts', 'Breadsticks', 'Chimichangas', 'Nachos', 'Funyons', 'Snickers', 'Mini-Toast', 'Wheat-Thins', 'Fritos'],
    'Entrees': ['Cream of Frog', 'Clam Chowder', 'Crab Rangoon', 'Burger', 'Taco', 'Spaghetti', 'Steak', 'Shrimp stu', 'Hoagie'],
    'Desserts': ['Smarties', 'Mochi', 'Chocolate Circuits', 'Cheesecake', 'Fruit', 'Apple Pie', 'Dippin-Dots', 'M&Ms', 'Brownies'],
    'Drinks': ['Sprite', 'Most Bitterest IPA Ever', 'Root Beer Float', 'Coke', 'Milk', 'Coconut Juice', 'RedBull', 'Budweiser', 'Water'],
    'Sides': ['Lemons', 'Popcorn', 'French Fries', 'French Toast', 'Mashed Potatoes', 'Corn', 'Wings', 'Stuffing', 'Cabbage'],
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
    'mini-toast': 3.50,
    'wheat-thins': 5.50,
    'fritos': 7.25,
    'steak': 22.00,
    'shrimp stu': 10,
    'hoagie': 5.15,
    'dippin-dots': 7.35,
    'm&ms': 2.25,
    'brownies': 3.00,
    'redbull': 8.25,
    'budweiser': 15.00,
    'water': 3.25,
    'wings': 7.00,
    'stuffing': 2.25,
    'cabbage': 14.50,
}
menu_stock = {
    'pop-tarts': 10,
    'breadsticks': 10,
    'chimichangas': 50,
    'nachos': 51,
    'funyons': 40,
    'snickers': 20,
    'cream of frog': 15,
    'clam chowder': 10,
    'crab rangoon': 22,
    'burger': 50,
    'taco': 20,
    'spaghetti': 90,
    'smarties': 10,
    'mochi': 20,
    'chocolate circuits': 40,
    'cheesecake': 70,
    'fruit': 25,
    'apple pie': 11,
    'sprite': 25,
    'most bitterest ipa ever': 80,
    'root beer float': 80,
    'coke': 45, 'Milk': 50,
    'coconut juice': 25,
    'lemons': 20,
    'popcorn': 25,
    'french fries': 14,
    'french toast': 35,
    'mashed potatoes': 45,
    'corn': 25,
    'mini-toast': 3,
    'wheat-thins': 5,
    'fritos': 7,
    'steak': 22,
    'shrimp stu': 10,
    'hoagie': 5,
    'dippin-dots': 7,
    'm&ms': 21,
    'brownies': 3,
    'redbull': 8,
    'budweiser': 15,
    'water': 32,
    'wings': 7,
    'stuffing': 21,
    'cabbage': 14,
}
tax = .101
cart = {}


def user_input():
    try:
        while 1:
            order = input('>> ')
            if order == 'q':
                print('Goodbye.')
                break
            elif order.split()[0] == 'remove':
                remove_cart(order[7:].lower())
            elif order.split()[0] == 'load':
                print(order)
                parse_menu(order[5:])
            elif order == 'menu':
                print_menu(menu_categories)
            elif order == 'order':
                print_cart(cart)
            else:
                try:
                    int(order.split()[-1])
                except ValueError:
                    add_to_cart(order.lower(), 1)
                else:
                    add_to_cart(' '.join(order.lower().split()[:-1]), int(order.split()[-1]))
    except KeyboardInterrupt:
        print('\b\bGoodbye.\n')
        exit()


def print_cart(cart):
    """prints out all items in cart
    """
    printstring = '{0}CART{0}\nOrder #{1}\n'.format('='*20, uuid.uuid4())
    for item, amount in cart.items():
        printstring += '\n{}: {}'.format(item, amount)
    printstring += '\nTotal: {:>31}{:.2f}\n{}'.format('$', (1+tax)*sum([menu_prices[item]*count for item, count in cart.items()]), '='*43)
    print(printstring)
    return printstring


def print_menu(menu):
    """
    Prints out all items on the Menu
    """
    printstring = 'Our Menu:'
    for cat, cat_list in menu.items():
        printstring += '\n\n{}\n{}'.format(cat, '*'*25)
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
        menu_stock[item] += cart[item]
        del cart[item]
        print('{} has been removed.'.format(item))
        print('Total: {:>17}{:.2f}\n{}'.format('$', (1+tax)*sum([menu_prices[item]*count for item, count in cart.items()]), '*'*28))
    else:
        print('{} not in cart.'.format(item))
        return False


def add_to_cart(item, quantity):
    """
    Accepts a request/order from user_input and validates if the request is inside the menu dictionary
    And if then appends to the users cart for checkout
    """
    if quantity <= 0:
        print('Please enter a positive quantity')
    elif item not in [item.lower() for item in menu_prices]:
        print('{} not in menu.'.format(item))
        return False
    else:
        if quantity > menu_stock[item]:
            print('Not added to cart. Only {} in stock'.format(menu_stock[item]))
        else:
            cart[item] = cart[item] + quantity if item in cart else quantity
            menu_stock[item] -= quantity
            print('{} added to order.'.format(item))


def parse_menu(menu_file):
    """Parse Menu excepts a `.CSV` file that updates/overwrites previous dictionaries to update the Restaurant Menu."""
    if menu_file[-4:] != '.csv':
        print('Invalid file extension')
        return False
    try:
        with open(menu_file) as file:
            data = [line[:-1].split(',') for line in list(file)]
    except FileNotFoundError:
        print('File not found')

    new_menu_categories = {}
    new_menu_prices = {}
    new_menu_stock = {}
    try:
        for line in data:
            if line[1] in new_menu_categories:
                new_menu_categories[line[1]].append(line[0])
            else:
                new_menu_categories[line[1]] = [line[0]]
            new_menu_prices[line[0]] = float(line[2])
            new_menu_stock[line[0]] = int(line[3])
    except ValueError as e:
        print('Invalid:', e)
    except:
        print('Invalid Data Formatting')
    else:
        global menu_categories, menu_stock, menu_prices
        menu_categories = new_menu_categories
        menu_prices = new_menu_prices
        menu_stock = new_menu_stock
        return menu_file, menu_categories


if __name__ == '__main__':
    print("Welcome to Snakes Cafe!\n\
            Press 'q' any time to exit\n\
            Type 'remove <item>' to remove an item\n\
            Type 'load <menu.csv>' to load custom menu\n\
            Type 'menu' to see our menu\n\
            Type 'order' to see your order\n")
    print_menu(menu_categories)
    print('\n{0}\n** What would you like to order? **\n{0}'.format('*' * 35))
    user_input()
