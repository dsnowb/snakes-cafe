if __name__ == '__main__':


    menu = {
        'Appetizers': {'Pop-Tarts': 2.50, 'Breadsticks': 1.10, 'Chimichangas': 7.50, 'Nachos': 5.00, 'Funyons': 4.50, 'Snickers': 2.00},
        'Entrees': {'Cream of Frog': 11.95, 'Clam Chowder': 11.00, 'Crab Rangoon': 22.00, 'burger': 5.00, 'taco': 2.00, 'spaghetti': 9.50},
        'Desserts': {'Smarties': 1.00, 'Mochi': 2.50, 'Chocolate Circuits': 4.00, 'Cheesecake': 7.00, 'Fruit': 25.00, 'Apple Pie': 11.00},
        'Drinks': {'Sprite': 2.50, 'Most Bitterest IPA Ever': 8.00, 'Root Beer Float': 8.00, 'Coke': 45.00, 'Milk': 5.00, 'Coconut juice': 2.50},
        'Sides': {'Lemons': 2.00, 'Popcorn': 2.50, 'French Fries': 1.45, ' French Toast': 3.50, 'Mashed Potatoes': 4.50, 'Corn': 2.50},
    }
    tax = 10.01
    cart = {}

    def user_input():
        order = input('>> ')
        while 1:
            if order == 'q':
                print('Goodbye.')
                break
            if order.split()[0] == 'remove':
                remove_cart(order)
            if order == 'menu':
                print_menu()

    def print_menu():
        pass

    def remove_cart(item):
        print '{} has been removed.'.format(item)
        if item in cart:
            cart[item] -= 1
            if cart[item] == 0:
                del cart[item]
        else:
            print '{} not in cart.'.format(item)



    def add_to_cart():
        pass

    def print_welcome():
        print("Welcome to Snake's Cafe!\nPress q any time to exit\n\nOur menu:\n")
        for cat, cat_list in menu.items():
            print('\n{}'.format(cat.upper()))
            for item in cat_list:
                print(item.title())
        print('\n{0}\n** What would you like to order? **\n{0}'.format('*'*35))

    def take_order():
        while 1:
            order = user_input()

            elif order not in [item.lower() for cat in menu.keys() for item in menu[cat]]:
                print('{} not in menu.'.format(order))
            else:
                cart[order] = cart[order] + 1 if order in cart else 1
                print_cart()

    def print_cart():
        print('{0}CART{0}\n'.format('*'*12))
        for item, amount in cart.items():
            print('{}: {}'.format(item, amount))
        print('\n' + '*'*28)

    print_welcome()
    take_order()
