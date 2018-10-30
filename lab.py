from shopping_cart import ShoppingCart 

shopping_cart = ShoppingCart()

print(shopping_cart.total)
print(shopping_cart.employee_discount)

print(shopping_cart.add_item("rainbow sandals", 45.99)) # 45.99
print(shopping_cart.add_item("agyle socks", 10.50)) # 56.49)
print(shopping_cart.add_item("jeans", 50.00, 3))

# print(shopping_cart.mean_item_price())

print(shopping_cart.median_item_price())

discount_shopping_cart = ShoppingCart(20)
print(discount_shopping_cart.add_item("rainbow sandals", 45.00)) # 45.00
print(discount_shopping_cart.add_item("agyle socks", 15.00)) # 60.00
print(discount_shopping_cart.apply_discount()) # 48.00
print(discount_shopping_cart.add_item("macbook air", 1000.00)) # 1060.00
print(discount_shopping_cart.apply_discount()) # 848.00
print(shopping_cart.apply_discount()) # Sorry, there is no discount to apply to your cart :(

print("item names" , shopping_cart.item_names())

print("before: ", shopping_cart.total)

shopping_cart.void_last_item()
print("after: ", shopping_cart.total)
