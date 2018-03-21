# Test Plan

## add_to_cart
if item is not in menu, indicates not in menu
if item is in menu and item is not in cart, item is added to cart
if item is in menu and item is in cart, item increments in cart

## remove_cart
if item is not in cart, indicates not in cart
if more than one of the item is in cart, substract one from item in cart
if one item is in cart, item is removed completely from cart

## print_menu
validate that menu is a dictionary
validate that expected menu is printed

## print_cart
validate that cart is a dictionary
validate that expected cart is printed
