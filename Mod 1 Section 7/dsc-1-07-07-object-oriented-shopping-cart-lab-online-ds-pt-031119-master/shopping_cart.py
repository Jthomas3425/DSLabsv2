class ShoppingCart:
    # write your code here
    def __init__(self, emp_discount=None, total = 0, items = []):
        self.emp_discount = emp_discount
        self.total = total
        self.items = items
    
    def add_item(self, name, price, quantity=1):
        self.items.append({'name': name, 'price': price, 'quantity': quantity})
        self.total += price * quantity
        return self.total
        
    def mean_item_price(self):
        _quantity = 0
        for item in self.items:
            _quantity += item['quantity']
        return self.total/_quantity
        
    def median_item_price(self):
        prices = [i['price'] for i in self.items]
        prices.sort()
        return prices
        pass

    def apply_discount(self):
        return self.total * ((100 - self.emp_discount)/100) 

    def void_last_item(self):
        removed_item = self.items.pop()
        self.total -= removed_item['price']
        return self.items
        