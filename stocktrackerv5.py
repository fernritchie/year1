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
        self.history = [price]  # list to store price change
        self.latest_loss = 0
        self.loss_history = []  # list to store all losses
        self.investment_splits = []  # stores year and investment
        self.invest = 0  # stores stock invested value
        self.invest_history = []  # stores all investment values
        self.owned = 0  # stores amount of stock owned

    def update_splits(self, year, invest):
        """
        Updates the investment splits for the stock.
        """
        self.investment_splits.append((self.name, year + 1, invest))  # Append the investment to the history
        return self.investment_splits  # Return the investment splits

    def update_price(self, index, year):
        """
        Updates the price of the stock based on a random index.
        """
        if self.price < 0.10:  # If the price is less than 10 pence
            print(f"{self.name} is too low to trade")

        else:
            """
            Randomly update the price of the stock based on the index.
            """
            surcharge_fee = self.price * 0.125
            if index <= 25:
                """
                Drop the price by a random percentage between 25% and 75%.
                Applies a 12.5% surcharge fee.
                Updates the latest loss and loss history.
                """
                drop_percent = random.randint(25, 75) / 100.0
                self.price -= surcharge_fee + (self.price * drop_percent)
                self.latest_loss = self.price * drop_percent
                self.loss_history.append((year + 1, self.latest_loss))
                print(f"***********Surcharge applied******************")

            elif index <= 50:
                """
                Increase the price by a random percentage between 1% and 25%.
                Applies a 12.5% surcharge fee.
                """
                increase_percent = random.randint(1, 25) / 100.0
                self.price -= surcharge_fee
                self.price += self.price * increase_percent
                print(f"***********Surcharge applied******************")
            else:
                """
                Increase the price by a random percentage between 15% and 35%.
                If there was a previous loss, add it to the price.
                """
                increase_percent = random.randint(15, 35) / 100.0
                self.price += self.price * increase_percent
                
                if self.latest_loss != 0:
                    self.price += self.latest_loss
                    print(f"***********Bonus applied: {self.latest_loss:.2f}******************")
                else:
                    print(f"***********NO BONUS OR SURCHARGE******************")
            """
            Append the updated price to the price history.
            """
            self.history.append(self.price)

    # Method to get the number of shares owned based on the investment amount
    def get_owned(self, invest):
        """
        Calculates the number of shares owned based on the investment amount.
        """
        self.owned = invest / self.price
        return self.owned

    # Method to get the current value of the investment in the stock
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

funds = 150  # Initialize funds outside the loop
year = 0  # Initialize year
quarter = 0  # Initialize quarter

# Dictionary to store stock prices over time for plotting
stock_prices = {stock.name: [] for stock in stocks}


def plot_investment_splits(stocks):
    """
    Plots the investment splits over time for each stock.
    """
    [plt.plot(range(len(stock.invest_history)), stock.invest_history, label=stock.name) for stock in stocks]
    plt.xlabel('Quarter')
    plt.ylabel('Investment (£)')
    plt.title('Investment Over Time')
    plt.legend()
    plt.show()


def plot_price_history(stocks):
    """
    Plots the price history of each stock over time.
    """
    [plt.plot(range(len(stock.history)), stock.history, label=stock.name) for stock in stocks]
    plt.xlabel('Quarter')
    plt.ylabel('Price')
    plt.title('Stock Price Over Time')
    plt.legend()
    plt.show()


def withdraw_funds():
    """
    Gives the user the option to withdraw funds and shows portfolio summary/graphs
    """
    initial_investment = 150  # Initial funds
    final_funds = funds  # Final funds
    total_investment = initial_investment - final_funds  # Total investment made
    withdraw_funds = input(f"Would you like to withdraw funds (£{funds:.2f})? (yes/no): ")
    if withdraw_funds.lower() == "yes":
        print(f"Thank you for playing. You have withdrawn £{funds:.2f}")
        print("Your stock portfolio summary:")
        print("-" * 50)

        for stock in stocks:
            gain_loss_percentage = (stock.price - stock.history[0]) / stock.history[0] * 100
            print(f"Stock: {stock.name}")
            print(f"New Price: £{stock.price:.2f}")
            print(f"Old Price: £{stock.history[0]:.2f}")
            print(f"Gain/Loss: {gain_loss_percentage:.2f}%")
            print("-" * 50)

        print("End of portfolio summary.")

        print(f"You have made a gain/loss of £{total_investment:.2f}")  # Calculate gain/loss using total investment
        print(f"In total you invested £{total_investment:.2f}")

        # Plot the price history of each stock
        plot_price_history(stocks)
        # Plot the investment splits
        plot_investment_splits(stocks)
        raise SystemExit
    else:
        pass



# Main loop for the program
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

    total_invested = 0  # Track total investment made by the user

    for i, stock in enumerate(stocks):  # Enumerate through the stocks
        while True:  # Loop to handle user input
            try:
                print(f"You have £{funds:.2f} available to invest.")
                print(f"You can buy a total of {funds / stock.price:.2f} shares in {stock.name}")

                """
                If it's the first two stocks, ask the user for the investment amount.
                """
                if i < 2:
                    while True:
                        try:
                            invest = float(input(f"Enter the investment amount for {stock.name}: £"))
                            if invest < 0:
                                raise ValueError("Invalid amount. Please enter a positive number.")
                            if invest > funds:
                                raise ValueError(f"Insufficient funds. You have only £{funds:.2f} left.")
                            
                            break  # Break out of the inner loop if input is valid
                        except ValueError:
                            print("Invalid input. Please enter a number.")
                    stock.invest_history.append(invest)  # Append the investment to the history
                else:
                    invest = funds
                    stock.invest_history.append(invest)  # Append the investment to the history
                    print(f"All remaining funds will be invested in {stock.name}: £{invest:.2f}")

                print(f"You have invested £{invest:.2f} in {stock.name}")
                stock.update_splits(year, invest)
                stock.get_owned(invest)
                print(f"You now own {stock.owned:.2f} shares in {stock.name}")
                if invest < 0:
                    raise ValueError("Invalid amount. Please enter a positive number.")
                if invest > funds:
                    raise ValueError(f"Insufficient funds. You have only £{funds:.2f} left.")

                funds -= invest  # Deduct the investment from the funds
                stock.invest = invest  # Update the investment value of the stock in the class

                total_invested += invest
                break
            except ValueError as e:  # Handle exceptions
                print(e)

    while True:
        print(f'''
              -----------------------
              /Year {year + 1} and quarter {quarter + 1} /
              -----------------------
              ''')

        for stock in stocks:
            index = random.randint(1, 100)  # Generate a random index
            stock.update_price(index, year)  # Update the price of the stock
            stock.invest = stock.get_value()  # Get the current value of the investment
            stock.invest_history.append(stock.invest)  # Append the investment to the history
            print(f'''
------------------------------
The index was {index}
{stock.name} is now priced at £{stock.price:.2f}
{stock.name} latest loss: {stock.latest_loss}
{stock.name} loss history: {stock.loss_history}
Previous splits: {stock.investment_splits}
Investment history: {stock.invest_history}
Price history: {stock.history}
Your investment in {stock.name} is now worth £{stock.invest:.2f}
------------------------------
                  ''')

            stock_prices[stock.name].append(stock.price)

            funds = sum(stock.invest for stock in stocks) # Funds are the sum of all stock investment values

        # Increment the quarter
        quarter += 1
        if quarter == 4:
            quarter = 0
            year += 1

            # Reset the latest loss for each stock
            for stock in stocks:
                stock.latest_loss = 0

            break
    # Check if the year is greater than or equal to 3 then ask the user if they want to withdraw funds
    if year >= 3:
        withdraw_funds()


# ... rest of your code ...


# Call the function to plot the investment splits
plot_investment_splits(stocks)
