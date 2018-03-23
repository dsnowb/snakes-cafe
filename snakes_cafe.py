import uuid


class Order(object):
    '''
    Defines a blueprint for an Order, which is a cart filled with items selected from the available menu
    dictionary. Methods available include the ability to add or remove items from the cart, and print
    the cart, as well as display some values when global functions are used on the Order object
    '''
    tax = .101

    def __init__(self):
        self.cart = {}
        self.total = 0
        self.id = uuid.uuid4()

    def __str__(self):
        """Prints out all items in cart"""
        printstring = '{0}CART{0}\nOrder #{1}\n'.format('='*20, self.id)
        for item, amount in self.cart.items():
            printstring += '\n{}: {}'.format(item, amount)
        printstring += '\nTotal: {:>31}{:.2f}\n{}'.format('$', self.total, '='*43)
        return printstring

    def __len__(self):
        return sum([count for count in self.cart.values()])

    def __repr__(self):
        return '<Order #{} | Items: {} | Total: ${:.2f}>'.format(self.id, len(self), self.total)

    display_order = __str__

    def add_item(self, item, quantity=1):
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
                self.cart[item] = self.cart[item] + quantity if item in self.cart else quantity
                menu_stock[item] -= quantity
                self.total += (1+self.tax)*menu_prices[item]*quantity
                print('{} added to order.'.format(item))

    def remove_item(self, item, quantity=1):
        """
        Accepts a request/order from user_input and validates if the request is in the cart and if so removes 1 of the
        specified product. If the item is no longer in cart it gets truanted.
        """

        if item in self.cart:
            if quantity > self.cart[item]:
                print('Quantity is more than in cart for', item)
            else:
                self.total -= (1+self.tax)*menu_prices[item]*quantity
                self.cart[item] -= quantity
                menu_stock[item] += self.cart[item]
                print('Removed {0} {1}(s). {2} {1}(s) left.'.format(quantity, item, self.cart[item]))
                print('Total: {:>17}{:.2f}\n{}'.format('$', self.total, '*'*28))
                if self.cart[item] == 0:
                    del self.cart[item]
        else:
            print('{} not in cart.'.format(item))
            return False

    def print_receipt(self):
        """Creates receipt in seperate file"""
        with open('{}.csv'.format(self.id), 'w') as file:
            file.write(self.display_order())


menu_categories = {
    'Appetizers': ['Pop-Tarts', 'Breadsticks', 'Chimichangas', 'Nachos', 'Funyons', 'Snickers', 'Mini-Toast', 'Wheat-Thins', 'Fritos', 'Chicken Breasts', 'Rabbit', 'Waffles'],
    'Entrees': ['Cream of Frog', 'Clam Chowder', 'Crab Rangoon', 'Burger', 'Taco', 'Spaghetti', 'Steak', 'Shrimp stu', 'Hoagie', 'Duck', 'Goose', 'Pig'],
    'Desserts': ['Smarties', 'Mochi', 'Chocolate Circuits', 'Cheesecake', 'Fruit', 'Apple Pie', 'Dippin-Dots', 'M&Ms', 'Brownies', 'Creamsickle', 'Peanuts', 'Caramel'],
    'Drinks': ['Sprite', 'Most Bitterest IPA Ever', 'Root Beer Float', 'Coke', 'Milk', 'Coconut Juice', 'RedBull', 'Budweiser', 'Water', 'Wine', 'Coffee', 'Tea'],
    'Sides': ['Lemons', 'Popcorn', 'French Fries', 'French Toast', 'Mashed Potatoes', 'Corn', 'Wings', 'Stuffing', 'Cabbage', 'Bacon', 'Hash Browns', 'Pancakes'],
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
    'chicken breasts': 10.00,
    'rabbit': 5.00,
    'waffles': 7.00,
    'duck': 12.00,
    'goose': 18.00,
    'pig': 9.76,
    'creamsickle': 13.00,
    'peanuts': 12.00,
    'caramel': 2.50,
    'wine': 7.00,
    'coffee': 3.00,
    'tea': 1.25,
    'bacon': 3.00,
    'hash browns': 2.00,
    'pancakes': 17.00,
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
    'chicken breasts': 10,
    'rabbit': 5,
    'waffles': 7,
    'duck': 12,
    'goose': 18,
    'pig': 9,
    'creamsickle': 13,
    'peanuts': 12,
    'caramel': 2,
    'wine': 7,
    'coffee': 3,
    'tea': 1,
    'bacon': 3,
    'hash browns': 2,
    'pancakes': 17,
}


def user_input(order):
    """Accepts user input and invokes appropriate order methods"""
    try:
        while 1:
            cur = input('>> ')
            if cur == 'q':
                print('Goodbye.')
                break
            elif cur.split()[0] == 'remove':
                try:
                    order.remove_item(' '.join(cur[7:].split()[:-1]), int(cur.split()[-1]))
                except:
                    order.remove_item(cur[7:])
            elif cur.split()[0] == 'load':
                parse_menu(cur[5:])
            elif cur == 'menu':
                print_menu(menu_categories)
            elif cur == 'order':
                print(order)
            elif cur == 'check':
                order.print_receipt()
            else:
                try:
                    order.add_item(' '.join(cur.lower().split()[:-1]), int(cur.split()[-1]))
                except ValueError:
                    order.add_item(cur.lower())
    except KeyboardInterrupt:
        print('\b\bGoodbye.\n')
        exit()


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


def print_menu(menu):
    """Prints out all items on the Menu"""
    printstring = 'Our Menu:'
    for cat, cat_list in menu.items():
        printstring += '\n\n{}\n{}'.format(cat, '*'*25)
        for item in cat_list:
            printstring += '\n' + item

    print(printstring)
    return printstring


if __name__ == '__main__':
    print("Welcome to Snakes Cafe!\n\
            Press 'q' any time to exit\n\
            Type 'remove <item>' to remove an item\n\
            Type 'load <menu.csv>' to load custom menu\n\
            Type 'menu' to see our menu\n\
            Type 'order' to see your order\n")
    print_menu(menu_categories)
    print('\n{0}\n** What would you like to order? **\n{0}'.format('*' * 35))
    tom = Order()
    user_input(tom)
