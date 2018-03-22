import snakes_cafe as cafe
import pytest as pt


def test_valid_add_to_cart():
    """
    Tests that items not in the menu can't be added
    """
    cafe.cart = {}
    assert cafe.add_to_cart('thing',1) == False

def test_add_to_cart():
    """
    Tests that items that are in the menu but not in the cart are added to the cart
    """
    cafe.cart = {}
    cafe.add_to_cart('pop-tarts',1)
    assert 'pop-tarts' in cafe.cart

def test_multi_add_to_cart():
    """
    Tests that items that are in the menu and in the cart are incremented in the cart
    """
    cafe.cart = {}
    cafe.add_to_cart('pop-tarts',2)
    assert cafe.cart['pop-tarts'] == 2

def test_valid_remove_cart():
    """
    Tests that if item is not in cart, it is not removed
    """
    cafe.cart = {}
    assert cafe.remove_cart('pop-tarts') == False

def test_remove_cart():
    """
    Tests that if one of an item is in the cart, it is completely removed
    """
    cafe.cart = {'pop-tarts':5}
    cafe.remove_cart('pop-tarts')
    assert 'pop-tarts' not in cafe.cart

def test_print_menu():
    """
    validates that menu is a dictionary
    validates that expected menu is printed
    """
    assert (isinstance(cafe.menu_categories, dict) == True) and\
           (isinstance(cafe.print_menu(cafe.menu_categories), str))


def test_print_cart():
    """
    validates that cart is a dictionary
    validates that expected cart is printed
    """
    assert (isinstance(cafe.cart, dict) == True) and\
           (isinstance(cafe.print_cart(cafe.cart), str))

def test_parse_menu_valid_extension():
    """
    Validates that .csv files are allowed to be parsed and others are rejected
    """
    assert cafe.parse_menu('menu.csv')[0] == 'menu.csv'
    assert cafe.parse_menu('menu') is False

def test_parse_menu_valid_file():
    """
    Validates that a known good csv file will parse into the menu, but a non-
    existent file will raise an error
    """
    assert cafe.parse_menu('menu.csv')[0] == 'menu.csv'
    with pt.raises(Exception):
        assert cafe.parse_menu('notmenu.csv')

def test_parse_menu_bad_file():
    """
    Validates that a corrupt or improperly formatted file will raise an error
    """
    with pt.raises(Exception):
        assert cafe.parse_menu('bad_menu.csv')

def test_parse_menu_updated_menu():
    assert 'Drinks' not in cafe.parse_menu('menu.csv')[1].keys()
