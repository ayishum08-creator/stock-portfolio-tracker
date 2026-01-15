# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320
}

portfolio = {}
total_investment = 0

n = int(input("Enter number of different stocks you bought: "))

for i in range(n):
    stock_name = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock_name in stock_prices:
        price = stock_prices[stock_name]
        investment = price * quantity
        portfolio[stock_name] = investment
        total_investment += investment
    else:
        print("Stock not found in price list.")

print("\n--- Stock Portfolio Summary ---")
for stock, value in portfolio.items():
    print(stock, ":", value)

print("Total Investment Value:", total_investment)

# Optional: Save result to file
file = open("portfolio.txt", "w")
file.write("Stock Portfolio Summary\n")
for stock, value in portfolio.items():
    file.write(f"{stock} : {value}\n")
file.write(f"Total Investment Value: {total_investment}")
file.close()

print("\nPortfolio saved to portfolio.txt")
