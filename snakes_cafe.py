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
        print('***********************************\
                 ** What would you like to order? **\
                 ***********************************')

    def take_order():
        while 1:
            order = input('>> ')
            if order == 'q':
                print('Goodbye.')
                break
            elif order not in [item.lower() for item in appetizers + entrees + desserts + drinks]:
                print('{} not in menu.'.format(order))
            else:
                if order in cart:
                    cart[order] += 1
                else:
                    cart[order] = 1
                print_cart()


    def print_cart():
        print('CART')
        print('*'*25)
        for item, amount in cart.items():
            print('{}: {}'.format(item, amount))
        print('*'*25)


    print_welcome()
    take_order()
