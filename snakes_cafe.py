if __name__ == '__main__':

    appetizers = ['Pop-Tarts','Breadsticks','Chimichangas']
    entrees = ['Cream of Frog','Clam Chowder','Crab Rangoon']
    desserts = ['Smarties','Mochi','Chocolate Circuits']
    drinks = ['Sprite','Most Bitterest IPA Ever','Root Beer Float']
    categories = {
        'Appetizers': appetizers,
        'Entrees': entrees,
        'Desserts': desserts,
        'Drinks': drinks,
    }
    cart = {}

    
    def print_welcome():
        print("Welcome to Snake's Cafe!\nPress q any time to exit\n\nOur menu:\n")
        for cat,cat_list in categories.items():
            print('\n{}'.format(cat.upper()))
            for item in cat_list:
                print(item.title())
        print('\n{0}\n** What would you like to order? **\n{0}'.format('*'*35))


    def take_order():
        while 1:
            order = input('>> ')
            if order == 'q':
                print('Goodbye.')
                break
            elif order not in [item.lower() for item in appetizers + entrees + desserts + drinks]:
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
