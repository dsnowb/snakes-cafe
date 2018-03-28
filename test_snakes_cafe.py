import snakes_cafe as cafe
import pytest as pt


@pt.fixture()
def cur():
    """Initializes dependencies"""
    order = cafe.Order()
    return order


def test_valid_add_to_cart(cur):
    """Tests that items not in the menu can't be added."""
    assert cur.add_item('thing', 1) is False


def test_add_to_cart(cur):
    """Tests that items that are in the menu but not in the cart are added to\
    the cart"""
    cur.add_item('pop-tarts', 1)
    assert 'pop-tarts' in cur.cart


def test_multi_add_to_cart(cur):
    """Tests that items that are in the menu and in the cart are incremented in\
    the cart."""
    cur.add_item('pop-tarts', 2)
    assert cur.cart['pop-tarts'] == 2


def test_valid_remove_cart(cur):
    """Tests that if item is not in cart, it is not removed."""
    cur.cart = {}
    assert cur.remove_item('pop-tarts') is False


def test_remove_cart(cur):
    """Tests that if an item is in the cart, if so completely remove it."""
    cur.cart = {'pop-tarts': 1}
    cur.remove_item('pop-tarts')
    assert 'pop-tarts' not in cur.cart


def test_remove_cart_multi(cur):
    """Tests that if more than one of an item is in the cart, multi will remove\
    specified count"""
    cur.cart = {'pop-tarts': 2}
    cur.remove_item('pop-tarts', 2)
    assert 'pop-tarts' not in cur.cart


def test_remove_cart_multi_valid(cur):
    """Tests that if more than the number of items in the cart are attempted to\
    be removed, the remove fails"""
    cur.cart = {'pop-tarts': 3}
    cur.remove_item('pop-tarts', 4)
    assert cur.cart['pop-tarts'] == 3


def test_remove_cart_multi_fewer(cur):
    """Tests that if some items are in cart and some are removed but not all the total is updated correctly"""
    cur.cart = {'pop-tarts': 3}
    cur.remove_item('pop-tarts', 2)
    assert cur.cart['pop-tarts'] == 1


def test_print_menu(cur):
    """
    validates that print menu printed
    validates that menu printed an item add to the cart
    """
    cafe.menu_categories = {'drinks': ['sprite']}
    assert cafe.print_menu(cafe.menu_categories) == 'Our Menu:\n\ndrinks\n{}\nsprite'.format('*'*25)


def test_display_order(cur):
    """
    validates that cart is a dictionary
    validates that expected cart is printed
    """
    cur.cart = {'pop-tarts': 2}
    assert isinstance(cur.cart, dict) is True
    assert isinstance(cur.display_order(), str)
    assert cur.display_order() == '====================CART====================\nOrder #{}\n\n\
pop-tarts: 2\nTotal:                               $0.00\n==========================================='.format(cur.id)


def test_parse_menu_valid_extension(cur):
    """Validates that .csv files are allowed to be parsed and others are rejected"""
    assert cafe.parse_menu('menu.csv')[0] == 'menu.csv'
    assert cafe.parse_menu('menu') is False


def test_parse_menu_valid_file(cur):
    """
    Validates that a known good csv file will parse into the menu, but a non-
    existent file will raise an error
    """
    assert cafe.parse_menu('menu.csv')[0] == 'menu.csv'
    with pt.raises(Exception):
        assert cafe.parse_menu('notmenu.csv')


def test_parse_menu_bad_file(cur):
    """Validates that a corrupt or improperly formatted file will raise an error"""
    with pt.raises(Exception):
        assert cafe.parse_menu('bad_menu.csv')


def test_parse_menu_updated_menu(cur):
    """Validates that the menu updates when a custom menu is loaded"""
    assert 'Drinks' not in cafe.parse_menu('menu.csv')[1].keys()


def test_receipt_writes(cur):
    """Validates that the receipt writes as it should"""
    cur.cart = {'pop-tarts': 1}
    cur.print_receipt()
    with open('{}.csv'.format(cur.id)) as f:
        assert cur.display_order() == f.read()


def test_print_menu_categories():
    cafe.menu_categories = {'Category': ['Item'], 'Another Category':['Cat2 Item', 'Another Cat2 Item']}
    assert cafe.print_menu_category('Category') == 'Category\n\nItem'
    assert cafe.print_menu_category('booyas') == 0
