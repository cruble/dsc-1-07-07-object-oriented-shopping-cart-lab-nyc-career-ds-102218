class ShoppingCart:
    # write your code here
    def __init__(self, employee_discount=None):
    	self._total = 0
    	self._items = {}
    	self._employee_discount = employee_discount

    def get_total(self):
    	return self._total

    def set_total(self, total):
    	self._total = total  

    total = property(get_total, set_total)

    @property
    def items(self):
    	return self._items 

    @items.setter
    def items(self, items):
    	self._items = items

    @property
    def employee_discount(self):
    	return self._employee_discount

    @employee_discount.setter
    def employee_discount(self, employee_discount):
    	self._employee_discount = employee_discount

    def add_item(self, name, price, quantity=1):
    	self._total += (price * quantity)
    	self._items[name] = price 
    	return self._total 

    def mean_item_price(self):
    	print(list(self._items.values()))
    	return sum(self._items.values())/len(self._items)


    def median_item_price(self):
    	sorted_prices = sorted(self._items.values())
    	if len(sorted_prices) % 2 == 0:
    		index = len(sorted_prices)/2
    		median = (sorted_prices[index] + sorted_prices[index+1])/2
    	else: 
    		index = len(sorted_prices)/2 + 1  
    		median = sorted_prices[index]
    	return median 

    def apply_discount(self):
    	if self._employee_discount: 
    		print("total pre", self._total)
    		self._total = self._total - (self._total*self._employee_discount)/100
    		print("total post", self._total)

    		return self._total 
    	else: 
    		return "Sorry, there is no discount to apply to your cart :("

    def item_names(self):
    	return self._items.keys()

    def void_last_item(self):
    	if self._items: 
    		names_list = self._items.keys()
    		print(names_list[-1])
    		self._items.pop(names_list[-1])

    		self._total = sum(self._items.values())
    		return 
    	else: 
    		return "There are no items in your cart!"




 # Let's define a method called void_last_item that removes the last item from our shopping cart and updates its total. If there are no items in the shopping cart, void_last_item should return "There are no items in your cart!".

# Now, let's define an instance method called apply_discount that applies a discount if one is provided and returns the discounted total. For example, if we initialize a new shopping cart with a discount of 20% then our total should be discounted in the amount of 20%. So, if our total were $100, after the discount we only would owe $80.

# If our shopping cart does not have an employee discount, then it should return a string saying: "Sorry, there is no discount to apply to your cart :("
    	
