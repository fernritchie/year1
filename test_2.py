import random

class Stock:
    def __init__(self, name, price):  # constructor
        self.name = name
        self.price = price
        self.invest = 0  # Initialize investment to 0
        self.history = [price]
        self.latest_loss = 0
        self.loss_history = []  # list to store the latest loss
        self.investment_splits = []  # list to store investment splits
        self.invested_history = []  # list to store the investment history
        self.invested_value = self.invest / price  # Calculate initial invested value

    def make_investment(self, amount):
        self.invest += amount  # Update investment when making investments
        num_shares = amount / self.price
        self.investment_splits.append((self.name, num_shares, self.price))  # Record investment splits
        self.invested_value = self.invest / self.price  # Update invested value based on new investment

    def update_price(self, index, year):  # method
        self.invested_history.append(self.invested_value)
        if self.price < 0.10:  # if the price is less than 10 pence
            print(f"{self.name} is too low to trade")
            return
        else:
            if index <= 25:  # 25% chance of a price drop
                drop_percent = random.randint(25, 75) / 100.0
                self.latest_loss = self.price * drop_percent  # Update latest loss
                self.price -= self.latest_loss
                self.loss_history.append((year + 1, self.latest_loss))
            elif index <= 50:  # 25% chance of a price increase
                increase_percent = random.randint(1, 25) / 100.0
                self.price += self.price * increase_percent
            else:
                increase_percent = random.randint(15, 35) / 100.0
                self.price += self.price * increase_percent
            
            # Update the invested value based on the new stock price
            if self.invest != 0:  # Ensure there's an investment to avoid division by zero
                self.invested_value = self.invest / self.price

        self.history.append(self.price)



stocks = [
    Stock('sky hooks', 1.57),
    Stock('tartan paint', 3.13),
    Stock('fishnet umbrellas', 2.59)
]

funds = 150
year = 0
quarter = 0

while True:
    if year == 0 and quarter == 0:
        print(f'''
              Welcome to the program!
              You have £{funds:.2f} left to split.
              
              The current stock prices are:
              {stocks[0].name} is currently worth £{stocks[0].price:.2f} per share
              {stocks[1].name} is currently worth £{stocks[1].price:.2f} per share
              {stocks[2].name} is currently worth £{stocks[2].price:.2f} per share
              '''
              )
    else:
        # Calculate total investment value
        total_investment_value = sum(stock.invested_value for stock in stocks)
        
        print(f'''
              Total investment value: £{total_investment_value:.2f}
              ''')
        
        # Ask the user if they want to reinvest
        reinvest = input("Would you like to reinvest? (y/n): ")
        if reinvest.lower() == 'y':
            funds += total_investment_value
            print(f"Total funds available for reinvestment: £{funds:.2f}")
            # Reset investments
            for stock in stocks:
                stock.invest = 0
                stock.invested_value = 0
            year = 0
            quarter = 0
            continue
        else:
            print("Thank you for playing.")
            break

    for stock in stocks:
        while True:
            try:
                print(f"You have £{funds:.2f} to invest.")
                print(f"You can buy a total of {funds / stock.price:.2f} shares in {stock.name}")
                invest = float(input(f"Enter investment amount for {stock.name}: £"))
                print(f"You have invested £{invest:.2f} in {stock.name}")
                
                # Make the investment and update the invested value
                stock.make_investment(invest)
                
                if invest < 0:
                    raise ValueError("Invalid amount. Please enter a positive number.")
                if invest > funds:
                    raise ValueError(f"Insufficient funds. You have only £{funds:.2f} left.")
                funds -= invest
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
            print(f"\nStock Update: {stock.name}")
            print(f"Current Stock Price: £{stock.price:.2f}")
            print(f"Your initial investment value was £{stock.invested_value:.2f}")
            print(f"Your investment value is now worth £{stock.invested_value:.2f}")
            print(f"Latest Loss for {stock.name}: £{stock.latest_loss:.2f}")
            print(f"Loss History for {stock.name}: {stock.loss_history}")
            print(f"Previous Investment Splits for {stock.name}: {stock.investment_splits}\n")
            print(f"Your initial investment in {stock.name} was £{stock.investment_splits[0][1]}, the stock has increased/decreased by £{stock.price - stock.history[0]:.2f} since then.\n")
            #print(f"Your initial investment in {stock.name} was £{stock.investment_splits[0, 1]}, the stock has increased/decreased by £{stock.price - stock.history[0]:.2f} since then.\n")
            print(f"Stock percentage change: {((stock.price - stock.history[0]) / stock.history[0]) * 100:.2f}%\n")

        quarter += 1
        if quarter == 4:
            quarter = 0
            year += 1

            for stock in stocks:
                stock.latest_loss = 0

            break

    if year >= 3:
        withdraw_funds = input("Would you like to withdraw funds? (y/n): ")
        if withdraw_funds == "y":
            print(f"Thank you for playing. You have withdrawn £{funds:.2f}")
            print(
                f'''Your stocks are now worth:
                ----------- 
                /sky hooks: {stocks[0].price:.2f}/
                -----------
                /tartan paint: {stocks[1].price:.2f}/
                ----------------
                /fishnet umbrella: {stocks[2].price:.2f}/
                ----------------'''
                )

            print(f"Your stock prices started at {stocks[0].history[0]:.2f}, {stocks[1].history[0]:.2f} and {stocks[2].history[0]:.2f}")
            raise SystemExit
        else:
            pass
