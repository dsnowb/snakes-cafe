import snakes_cafe as cafe

def test_valid_add_to_cart():
    """
    Tests that items not in the menu can't be added
    """
    cafe.cart = {}
    assert cafe.add_to_cart('thing') == False

def test_add_to_cart():
    """
    Tests that items that are in the menu but not in the cart are added to the cart
    """
    cafe.cart = {}
    cafe.add_to_cart('pop-tarts')
    assert 'pop-tarts' in cafe.cart

def test_multi_add_to_cart():
    """
    Tests that items that are in the menu and in the cart are incremented in the cart
    """
    cafe.cart = {}
    cafe.add_to_cart('pop-tarts')
    cafe.add_to_cart('pop-tarts')
    assert cafe.cart['pop-tarts'] == 2

def test_valid_remove_cart():
    """
    Tests that if item is not in cart, it is not removed
    """
    cafe.cart = {}
    assert cafe.remove_cart('pop-tarts') == False

def test_multi_remove_cart():
    """
    Tests that if more than one of an item is in the cart, it is decremented by one in the cart
    """
    cafe.cart = {'pop-tarts':2}
    cafe.remove_cart('pop-tarts')
    assert cafe.cart['pop-tarts'] == 1

def test_remove_cart():
    """
    Tests that if one of an item is in the cart, it is completely removed
    """
    cafe.cart = {'pop-tarts':1}
    cafe.remove_cart('pop-tarts')
    assert 'pop-tarts' not in cafe.cart

