if __name__ == '__main__':
    
    appetizers = ['Pop-Tarts','Breadsticks','Chimichangas']
    entrees = ['Cream of Frog','Clam Chowder','Crab Rangoon']
    deserts = ['Smarties','Mochi','Chocolate Circuits']
    drinks = ['Sprite','Most Bitterest IPA Ever','Root Beer Float']
    categories = {'Appetizers':appetizers, 'Entrees':entrees, 'Deserts':deserts, 'Drinks':drinks}
    
    def print_welcome():
        print("Welcome to Snake\'s Cafe!\nPress \'q\' any time to exit\n\nOur menu:\n")
        for cat,cat_list in categories.items():
            print('\n{}'.format(cat.upper()))
            for item in cat_list:
                print(item)

    print_welcome()
