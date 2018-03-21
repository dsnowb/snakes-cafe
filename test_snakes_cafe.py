import snakes_cafe as cafe
import pytest


def check_if_men

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