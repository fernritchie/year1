import random

import matplotlib.pyplot as plt

class Stock:
    def __init__(self, name, price):  # constructor
        self.name = name
        self.price = price
        self.owned = 0
        self.price_history = [price]
        self.latest_loss = 0
        self.loss_history = []  # list to store the latest loss
        self.investment_splits = []  # list to store investment splits
        
        
    def buy(self, amount):
        self.owned += amount
        return self.owned
    
    def sell(self, amount):
        self.owned -= amount
        return self.owned
    
    def update_price(self):
        if self.price < 0.10:  # if the price is less than 10 pence
            print(f"{self.name} is too low to trade")
        else:
            index = random.randint(1, 100)
            if index <= 25:  # 25% chance of a price drop
                drop_percent = random.randint(25, 75) / 100.0
                self.price -= self.price * drop_percent
                self.price -= self.price * 0.125
                self.latest_loss = self.price * drop_percent
                #self.loss_history.append((year + 1, self.latest_loss))
            elif index <= 50:  # 25% chance of a price increase
                increase_percent = random.randint(1, 25) / 100.0
                self.price += self.price * increase_percent
                self.price -= self.price * 0.125
            else:
                increase_percent = random.randint(15, 35) / 100.0
                self.price += self.price * increase_percent + self.latest_loss
            return self.price
    
    def get_price(self):
        return self.price
    
    def get_investment(self):
        invest = float(input(f"How much would you like to invest in {self.name} £"))
        return invest
    
    def get_owned(self, invest):
        self.owned = invest / self.price
        return self.owned
    
    def get_value(self):
        return self.price * self.owned
    
    def split_pot(self, funds):
        sh = stocks[0].get_value()
        fn = stocks[1].get_value()
        tp = stocks[2].get_value()
        new_total = sh + fn + tp + funds
        
        return new_total
    
stocks = [Stock("sky hook", 1), Stock("fish", 2), Stock("tartan", 3)]

funds = 150
year = 0

print(f'''Welcome to the program!
      You have £{funds:.2f} left to split.
      
        Sky hook is currently worth £{stocks[0].price:.2f} per share
        Fish is currently worth £{stocks[1].price:.2f} per share
        Tartan is currently worth £{stocks[2].price:.2f} per share
      ''')

for stock in stocks:
    invest = stock.get_investment()
    stock.get_owned(invest)
    get_value = stock.get_value()
    funds -= invest
    print(f"You have £{funds} left")
    print(f"You have invested: {get_value}")
    print(f"You have {stock.owned} shares in {stock.name}")

year = 1  # Initialize year to 1
while year <= 4:  # Loop for 4 quarters
    print('''
        New Quarter''')
    for stock in stocks:
        stock.update_price()
        print(f"{stock.name} was worth {stock.price_history[0]} and is now worth {stock.get_price()}")
        print(f"The value of your investment is now {stock.get_value()}")
        print(f"Your investment has changed by {(stock.get_value() - invest) / invest * 100:.2f}%")
    
    funds = stock.split_pot(funds)
    print(funds - 150)
    year += 1
    

