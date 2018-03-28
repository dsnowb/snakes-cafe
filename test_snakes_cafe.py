import snakes_cafe as cafe
import pytest as pt


@pt.fixture()
def cur():
    order = cafe.Order()
    return order


def test_valid_add_to_cart(cur):
    """Tests that items not in the menu can't be added."""
    assert cur.add_item('thing', 1) is False


def test_add_to_cart(cur):
    """Tests that items that are in the menu but not in the cart are added to\
    the cart."""
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


def test_parse_menu_valid_extension(cur):
    """
    Validates that .csv files are allowed to be parsed and others are rejected
    """
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
    """
    Validates that a corrupt or improperly formatted file will raise an error
    """
    with pt.raises(Exception):
        assert cafe.parse_menu('bad_menu.csv')


def test_parse_menu_updated_menu(cur):
    """
    Validates that the menu updates when a custom menu is loaded
    """
    assert 'Drinks' not in cafe.parse_menu('menu.csv')[1].keys()
