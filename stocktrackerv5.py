import random
import numpy as np
import matplotlib.pyplot as plt

class Stock:
    def __init__(self, name, price):
        """
        Constructor for the Stock class.
        Initializes the stock with a name, price, and other attributes.
        """
        self.name = name
        self.price = price
        self.history = [price]
        self.latest_loss = 0
        self.loss_history = []
        self.investment_splits = []
        self.invest = 0
        self.invest_history = []
        self.owned = 0

    def update_splits(self, year, invest):
        """
        Updates the investment splits for the stock.
        """
        self.investment_splits.append((self.name, year + 1, invest))
        return self.investment_splits

    def update_price(self, index, year):
        """
        Updates the price of the stock based on a random index.
        """
        if self.price < 0.10:
            print(f"{self.name} is too low to trade")
        else:
            if index <= 25:
                drop_percent = random.randint(25, 75) / 100.0
                self.price -= self.price * 0.125
                self.price -= self.price * drop_percent
                self.latest_loss = self.price * drop_percent
                self.loss_history.append((year + 1, self.latest_loss))
            elif index <= 50:
                increase_percent = random.randint(1, 25) / 100.0
                self.price -= self.price * 0.125
                self.price += self.price * increase_percent
            else:
                increase_percent = random.randint(15, 35) / 100.0
                self.price += self.price * increase_percent
                if self.latest_loss != 0:
                    self.price += self.latest_loss

            self.history.append(self.price)
    
    def get_owned(self, invest):
        """
        Calculates the number of shares owned based on the investment amount.
        """
        self.owned = invest / self.price
        return self.owned
            
    def get_value(self):
        """
        Calculates the current value of the investment in the stock.
        """
        return self.price * self.owned       

# Create instances of the Stock class
stocks = [
    Stock('sky hooks', 1.57),
    Stock('tartan paint', 3.13),
    Stock('fishnet umbrellas', 2.59)
]

funds = 150
year = 0
quarter = 0

# Lists to store stock prices over time
sky_hooks_prices = []
tartan_paint_prices = []
fishnet_umbrellas_prices = []

# Function to plot the investment splits
def plot_investment_splits(stocks):
    """
    Plots the investment splits over time for each stock.
    """
    for stock in stocks:
        plt.plot(range(len(stock.invest_history)), stock.invest_history, label=stock.name)
    plt.xlabel('Quarter')
    plt.ylabel('Investment (£)')
    plt.title('Investment Over Time')
    plt.legend()
    plt.show()
    
def plot_price_history(stocks):
    """
    Plots the price history of each stock over time.
    """
    for stock in stocks:
        plt.plot(range(len(stock.history)), stock.history, label=stock.name)
    plt.xlabel('Quarter')
    plt.ylabel('Price')
    plt.title('Stock Price Over Time')
    plt.legend()
    plt.show()
    
while True:
    if year == 0 and quarter == 0:
        print(f'''
        Welcome to the program!
        You have £{funds:.2f} left to split.
        --------------------------------            
        The current stock prices are:
        --------------------------------
        | Stock Name          | Price  |
        --------------------------------
        | {stocks[0].name:<20} | £{stocks[0].price:.2f} |
        | {stocks[1].name:<20} | £{stocks[1].price:.2f} |
        | {stocks[2].name:<20} | £{stocks[2].price:.2f} |
        --------------------------------
        '''
        )

    total_invested = 0
    for i, stock in enumerate(stocks):
        while True:
            try:
                print(f"You have £{funds:.2f} available to invest.")
                print(f"You can buy a total of {funds / stock.price:.2f} shares in {stock.name}")
                if i < 2:
                    invest = float(input(f"Enter the investment amount for {stock.name}: £"))
                    stock.invest_history.append(invest) # Append the investment to the history
                else:
                    invest = funds
                    stock.invest_history.append(invest) # Append the investment to the history
                    print(f"All remaining funds will be invested in {stock.name}: £{invest:.2f}")
                print(f"You have invested £{invest:.2f} in {stock.name}")
                stock.update_splits(year, invest)
                stock.get_owned(invest)
                print(f"You now own {stock.owned:.2f} shares in {stock.name}")
                if invest < 0:
                    raise ValueError("Invalid amount. Please enter a positive number.")
                if invest > funds:
                    raise ValueError(f"Insufficient funds. You have only £{funds:.2f} left.")
                funds -= invest
                stock.invest = invest
                
                total_invested += invest
                break
            except ValueError as e:
                print(e)
                
    while True:
        print(f'''
              -----------------------
              /Year {year + 1} and quarter {quarter + 1} /
              -----------------------
              ''')

        for stock in stocks:
            index = random.randint(1, 100)
            stock.update_price(index, year)
            stock.invest = stock.get_value()
            stock.invest_history.append(stock.invest) # Append the investment to the history
            print(f'''
------------------------------
{stock.name} is now priced at £{stock.price:.2f}
{stock.name} latest loss: {stock.latest_loss}
{stock.name} loss history: {stock.loss_history}
Previous splits: {stock.investment_splits}
Investment history: {stock.invest_history}
Price history: {stock.history}
Your investment in {stock.name} is now worth £{stock.invest:.2f}
------------------------------
                  ''')
            
            funds = 0
            if stock.name == 'sky hooks':
                sky_hooks_prices.append(stock.price)
            elif stock.name == 'tartan paint':
                tartan_paint_prices.append(stock.price)
            elif stock.name == 'fishnet umbrellas':
                fishnet_umbrellas_prices.append(stock.price)
            for stock in stocks:
                funds += stock.invest

        quarter += 1
        if quarter == 4:
            quarter = 0
            year += 1

            for stock in stocks:
                stock.latest_loss = 0

            break

    if year >= 3:
        withdraw_funds = input(f"Would you like to withdraw funds ({funds:.2f})? (yes/no): ")
        if withdraw_funds.lower() == "yes":
            print(f"Thank you for playing. You have withdrawn £{funds:.2f}")
            print(
                f'''
        Your stocks are now worth:
        --------------------------------
        | Stock Name          | Price  |
        --------------------------------
        | {stocks[0].name:<20} | £{stocks[0].price:.2f} |
        | {stocks[1].name:<20} | £{stocks[1].price:.2f} |
        | {stocks[2].name:<20} | £{stocks[2].price:.2f} |
        --------------------------------
        '''
                )

            print(f"Your stock prices started at {stocks[0].history[0]:.2f}, {stocks[1].history[0]:.2f} and {stocks[2].history[0]:.2f}")
            print(f"You have made a gain/loss of £{funds - total_invested:.2f}")

            # Plot the price history of each stock
            plot_price_history(stocks)
            # Plot the investment splits
            plot_investment_splits(stocks)
            raise SystemExit
        else:
            pass


# ... rest of your code ...


# Call the function to plot the investment splits
plot_investment_splits(stocks)
