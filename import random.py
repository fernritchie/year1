import random

class Stock:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.new_price = 0
        self.funds = 150
        self.invested_funds = []
        self.price_history = [price]
    
    def update_invested_funds(self):
        for i in range(len(self.invested_funds)):
            self.invested_funds[i] = self.invested_funds[i] * (self.price / self.price_history[-1])
                
    def update_price(self):
        index = random.randint(0, 100)
        if index >= 50:
            drop_percentage = 20
            self.price -= self.price * drop_percentage
        else:
            self.price += self.price * 20
        self.price = self.new_price
        self.price_history.append(self.new_price)
        self.update_invested_funds()
        return self.price
    
stocks = [
    Stock('sky hooks', 1.57),
    Stock('tartan paint', 3.13),
    Stock('fishnet umbrellas', 2.59)
]    
    
for stock in stocks:
    print(stock.name, stock.price)
    stock.update_price()
    print(f"New price: {stock.price}")
                