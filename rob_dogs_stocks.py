
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 13:07:06 2024

@author: Fern

Rob-Dogs Stocks and Shares

This is a stock investment game that does the following:
    
    1.) Starts the user with £150 in their funds pot.
    2.) Shows the user 3 stocks at different prices.
    3.) Allows the user to invest in the first two stocks, putting leftover funds in the third stock.
    4.) Generates price changes for each stock for 4 quarters.
    5.) Adds all the investment values together to recalculate the funds.
    6.) Asks the user to reinvest and repeats the quarterly changes/invest twice more.
    7.) On the third year, it will ask the user whether they would like to withdraw their funds/carry on.
    8.) If they withdraw, it will present the user with a short portfolio summary and some graphs.
    
    
"""

import random # Used for random number generation
import matplotlib.pyplot as plt # Used for plotting final graphs

"""Class to create stock and it's related attributes"""
class Stock:
    def __init__(self, name, price):
        self.name = name
        self.price = price # Stores current price
        self.history = [price] # Stores price history
        self.latest_loss = 0
        self.loss_history = []
        self.investment_splits = [] # Stores splits, name year and investment
        self.invest = 0 # Current invesment amount
        self.invest_history = []
        self.owned = 0


    """Updates the investment splits for the stock."""
    def update_splits(self, year, invest):
        self.investment_splits.append((self.name, year + 1, invest))
        return self.investment_splits
    
    
    """Updates the price of the stock based on a random index."""
    def update_price(self, index, year):       
        if self.price < 0.10:
            print(f"xxxxx {self.name} is too low to trade xxxxxx")
        else:
            surcharge_fee = self.price * 0.125 # Calculates surcharge fee, 12.5% of current price
            print("\n")
            print_section_header(self.name)
            if index <= 25:
                drop_percent = random.randint(25, 75) / 100.0 # Generates random drop percentage
                self.price -= surcharge_fee # Subtract surcharge fee from the price
                self.latest_loss = self.price * drop_percent # Calculates latest loss
                self.price -= self.price * drop_percent # Calculates loss and subtracts from price
                self.loss_history.append((year + 1, self.latest_loss)) # Updates loss history
                print(f"**Surcharge applied: -£{surcharge_fee:.2f}**")
                print(f"Loss: {drop_percent * 100:.2f}%")
            elif index <= 50:
                increase_percent = random.randint(1, 25) / 100.0 # Generates random increase percentage
                self.price -= surcharge_fee # Deducts surcharge fee
                self.price += self.price * increase_percent # Adds increate percentage
                print(f"**Surcharge applied: -£{surcharge_fee:.2f}**")
                print(f"Gain: {increase_percent * 100:.2f}%")
            else:
                increase_percent = random.randint(15, 35) / 100.0 # Generates random increase percentage
                self.price += self.price * increase_percent # Adds to current price
                
                
                """ If the latest loss is not 0, add the latest loss to the price as a bonus """
                if self.latest_loss != 0:
                    self.price += self.latest_loss
                    print(f"**Bonus applied: +£{self.latest_loss:.2f}**")
                    print(f"Gain: {increase_percent * 100:.2f}%")
                else:
                    print("**No bonus or surcharge**")
                    print(f"Gain: {increase_percent * 100:.2f}%")
            
            self.history.append(self.price) # Add price to price history
            


    """Gets number of shares owned"""
    def get_owned(self, invest):
        self.owned = invest / self.price
        return self.owned
    
    
    """Gets current value of investment based on shares owned"""
    def get_value(self):
        return self.price * self.owned
    
    
    """Plots graph for investment"""
    def plot_investment_splits(self):
        plt.plot(range(len(self.invest_history)), self.invest_history, label=self.name)
        plt.xlabel('Quarter')
        plt.ylabel('Investment (£)')
        plt.title('Investment Over Time')
        plt.legend()
        plt.show()
    
        
    """Plots graph to show price over time"""
    def plot_price_history(self):
        plt.plot(range(len(self.history)), self.history, label=self.name)
        plt.xlabel('Quarter')
        plt.ylabel('Price')
        plt.title('Stock Price Over Time')
        plt.legend()
        plt.show()

"""Performs quarterly updates"""
def quarterly_calculations(stocks,year):
    for stock in stocks:
        index = random.randint(1, 100)
        stock.update_price(index, year) #Updates price of stock based on random index
        stock.invest = stock.get_value() # Gets the invested value of the stock
        stock.invest_history.append(stock.invest) # Adds the investment history
        print_quarterly_update(stock) # Prints quarterly update
       #print(f"{stock.latest_loss}") Testing purposes
       #funds = sum(stock.invest for stock in stocks) # Recalculates funds
    

"""Prints header for stock quarterly updates"""
def print_section_header(header):
    print("-" * 50)
    print(header)
    print("-" * 50)


"""Prints end portfolio summary"""
def print_stock_summary(stock):
    gain_loss_percentage = (stock.price - stock.history[0]) / stock.history[0] * 100
    print(f"Stock: {stock.name}")
    print(f"Starting Price: £{stock.history[0]:.2f}")
    print(f"New Price: £{stock.price:.2f}")
    print(f"Initial Investment: £{stock.invest_history[0]:.2f}")
    print(f"Gain/Loss: {gain_loss_percentage:.2f}%")

"""Format portfolio summary"""
def print_portfolio_summary(stocks, initial_funds, final_funds):
    print("Your stock portfolio summary:")
    print_section_header("Stock Summary")
    for stock in stocks:
        print_stock_summary(stock)
        print("-" * 50)
    """If total_investment is a negative number, it turns it to a positive for user output"""
    total_investment = initial_funds - final_funds
    if total_investment < 0:
        print(f"Congratulations! You made a profit of: £{total_investment * -1:.2f}")
    else:
        print(f"You have made a loss of £{total_investment:.2f}")


"""Prints quarterly update"""
def print_quarterly_update(stock):
    print("-" * 50)
    
    print(f"Initial price: £{stock.history[0]}")
    print(f"Previous price: £{stock.history[-2]:.2f}")
    print(f"New price: £{stock.price:.2f}")
    print(f"Shares owned: {stock.owned:.2f}")
    print(f"Investment value: £{stock.invest:.2f}")
    print("-" * 50)
    input("Press enter to continue") 

def print_year_and_quarter(year,quarter):
    print("\n")
    print("-" * 50)
    print(f"/Year {year + 1} and quarter {quarter + 1} /")
    print("-" * 50)
    print("\n")

"""Gives the user the option to withdraw funds. If they do, prints summary and graph"""
def withdraw_funds():
    initial_investment = 150
    final_funds = funds
    total_investment = initial_investment - final_funds
    
    
    """Asks the user to either choose yes or no, else it will print invalid input"""
    while True:
        try:
            withdraw_funds = input(f"Would you like to withdraw funds (£{funds:.2f})? (yes/no): ").lower()
            if withdraw_funds == "yes":
                print(f"Thank you for playing. You have withdrawn £{funds:.2f}")
                print_portfolio_summary(stocks, initial_investment, final_funds)
                for stock in stocks:
                    stock.plot_price_history()
                    stock.plot_investment_splits()
                raise SystemExit
            elif withdraw_funds == "no":
                break  # Exit the loop if the user chooses not to withdraw funds
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
        except ValueError:
            print("Invalid input. Please enter 'yes' or 'no'.")



"""Checks that the total value of the stocks is not more than funds"""
def check_total_value(stocks, funds):
    total_share_price = sum(stock.price for stock in stocks)
    return funds < total_share_price


"""Checks that the price of the stock has not fallen below zero"""
def check_stock_values(stocks):
    for stock in stocks:
        if stock.price < 0:
            raise ValueError(f"The price of {stock.name} has fallen below zero. Exiting program.")


"""Prints message upon opening the program"""
def program_welcome():
    print(f'''
Welcome to the program!
        
You have been gifted £{funds:.2f}.

Here are the rules of the program:
    
1.) You can split these funds between 3 stocks.

2.) The total amount of the funds must be used. To ensure this is the case, after the first two investments have been allocated, the remaining value of your funds will automatically be invested in the last stock.

3.) You will be asked to split your funds at the end of each year for the first 3 years. After that, you can either withdraw your funds or continue investing.

4.) You must enter the investment in pounds or in pounds and pence eg. £5 or £5.00

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

    
"""Prints yearly price update after all quarters have been calculated"""
def yearly_price_update():
    print(f'''
          --------------------------------
          The current stock prices are:
          --------------------------------
          | Stock Name          | Price  |
          --------------------------------
          | {stocks[0].name:<20} | £{stocks[0].price:.2f} |
          | {stocks[1].name:<20} | £{stocks[1].price:.2f} |
          | {stocks[2].name:<20} | £{stocks[2].price:.2f} |
          --------------------------------
          ''')    

"""Resets stock loss"""
def reset_stock_loss():
    for stock in stocks:
        stock.latest_loss = 0
        #print(f"Resetting latest loss: {stock.latest_loss}") Testing purposes
       
       
"""Creates instances of the Stock class and initialises name and price, assigning to list 'stocks'."""
stocks = [
    Stock('Sky Hooks', 1.57),
    Stock('Tartan Paint', 3.13),
    Stock('Fishnet Umbrellas', 2.59)
]


"""Initialising funds, year and quarter"""
funds = 150 # Set initial funds
year = 0
quarter = 0


"""Main loop"""
while True:
    
    
    """Prints program welcome if first run"""
    if year == 0 and quarter == 0:
        program_welcome()
    else:
        yearly_price_update()  
         
         
    """Loop through all stocks and ask the user to invest"""
    for i, stock in enumerate(stocks):
        while True:
            try:
                funds = round(funds, 2) # Added to round the funds at the last possible moment
                print(f"\nYou have £{funds:.2f} available to invest.")
                #print(f"\nYou can buy a total of {funds / stock.price:.2f} shares in {stock.name}")
                
                
                """First 2 stocks choose the investment amount."""
                if i < 2:
                    """Prompt user for investment amount, validating input"""
                    while True:
                        try:
                            invest = float(input(f"\nEnter the investment amount for {stock.name}: £"))
                            if invest < 0:
                                raise ValueError("\nInvalid amount. Please enter a positive number.")
                            if invest > funds:
                                raise ValueError(f"\nInsufficient funds. You have only £{funds:.2f} left.")
                            break
                        except ValueError as ve:
                            if "positive" in str(ve):
                                print("\nInvalid amount. Please enter a positive number.")
                            elif "Insufficient" in str(ve):
                                print(f"\nInsufficient funds. You have only £{funds:.2f} left.")
                            else:
                                print("\nIncorrect input. Please enter an amount to invest (eg. £50)")
                    stock.invest_history.append(invest) # Update investment history
            
                
                else:
                    """Invests all remaining funds in final stock"""
                    invest = funds
                    stock.invest_history.append(invest)
                    print(f"\nAll remaining funds will be invested in {stock.name}: £{invest:.2f}")
                    
                
                stock.update_splits(year, invest) # Update splits
                stock.get_owned(invest) # Get the amount of shares purchased
                print(f"\n**You have invested £{invest:.2f} in {stock.name} and own {stock.owned:.2f} shares**")
                input("\nPress enter to continue")
                funds -= invest # Update funds by subtracting the amount invested in that stock
                stock.invest = invest # Update the amount invested in stock

                break
            except ValueError as e:
                print(e)
                
                
    """Prints year and quarter. Updates stock price, investment balue, investment history, and funds"""
    while True:
        print_year_and_quarter(year, quarter)
        quarterly_calculations(stocks, year) # Calculate quarterly price changes
        funds = sum(stock.invest for stock in stocks) # Recalculates funds
        check_stock_values(stocks) # Checks stock value is not less than 0
        
        """Imcrements quarter and if quarter == 4 sets to 0 then increments the year."""
        quarter += 1
        if quarter == 4:
            quarter = 0
            year += 1
            
            """Resets latest_loss for stock in new year."""
            reset_stock_loss()
                
            break
        
        # Check if the total value of stocks exceeds current funds
        if check_total_value(stocks, funds):
            print("Total value of current funds is lower than the total combined share price. Ending program.")
            raise SystemExit
        

            
    """Gives the user the option to withdraw funds after 3rd year."""
    if year >= 3:
        withdraw_funds()
