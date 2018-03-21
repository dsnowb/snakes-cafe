import snakes_cafe as cafe

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
