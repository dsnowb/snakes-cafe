import snakes_cafe as cafe
import pytest


def test_valid_add_to_cart():
    assert cafe.add_to_cart('thing') == False

    def test_add_to_cart():
    cafe.add_to_cart('pop-tarts')
    assert 'pop-tarts' in cafe.cart

    def test_case_add_to_cart():
    assert cafe.add_to_cart('pop-tarts') == None
    assert cafe.add_to_cart('POP-TARTS') == None

def test_multi_add_to_cart():
    cafe.add_to_cart('pop-tarts')
    cafe.add_to_cart('pop-tarts')
    assert cafe.cart['pop-tarts'] == 2


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
