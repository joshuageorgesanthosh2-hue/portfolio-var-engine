"""
Multi-Asset Portfolio Value at Risk (VaR) Engine by Joshua George Santhosh
Non-parametric Empirical Distribution Mapping (Historical Simulation)

Description:
    This engine fetches 2 years of live market data from the Yahoo Finance API,
    harmonizes asymmetric trading timelines across user-specified assets, 
    applies dynamic asset allocation weights, and evaluates the maximum 
    expected capital loss at variable confidence thresholds.
"""



import requests
import time

end_time = int(time.time())
start_time = end_time - (2*365*24*60*60)

ticker_input = input("Enter the tickers, seperated by spaces (e.g., AAPL MSFT GOOGL): ")
tickers = ticker_input.upper().split()

portfolio_prices = {}
headers = {"User-Agent": "Mozilla/5.0"}

for ticker in tickers:
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?period1={start_time}&period2={end_time}&interval=1d"
    response = requests.get(url, headers=headers)
    data = response.json()
    raw_prices = data["chart"]["result"][0]["indicators"]["quote"][0]["close"]
    portfolio_prices[ticker] = [p for p in raw_prices if p is not None]

min_length = min(len(portfolio_prices[ticker]) for ticker in tickers)
for ticker in tickers:
    portfolio_prices[ticker] = portfolio_prices[ticker][-min_length:]

portfolio_weights = {}
total_weight = 0.0
for ticker in tickers:
    weight = float(input(f"Enter the decimal weight for {ticker} (e.g., 0.5 for 50%):"))
    portfolio_weights[ticker] = weight
    total_weight += weight

portfolio_returns = []
for i in range (1, min_length):
    day_combined_return = 0.0
    
    for ticker in tickers:
        prices = portfolio_prices[ticker]
        individual_return = ((prices[i] - prices[i-1]) / prices[i-1]) * 100
        weighted_return = individual_return * portfolio_weights[ticker]
        day_combined_return += weighted_return
    portfolio_returns.append(day_combined_return)

portfolio_returns.sort()
total_days = len(portfolio_returns)

confidence_level = float(input("Enter confidence level percentage for VaR (e.g. 90, 95, 99): "))
portfolio_value = float(input("Enter portfolio value in USD: "))

risk_percentage = (100 - confidence_level)/100
var = int(risk_percentage * total_days)
var_percentage = portfolio_returns[var]
cash_loss = (var_percentage/100) * portfolio_value
print("=" * 55)
print(f"PORTFOLIO RISK REPORT ({' / '.join(tickers)})")
print("=" * 55)
print(f"Total trading days synchronized: {total_days}")
print(f"Worst combined historical day:   {portfolio_returns[0]:.2f}%")
print(f"Best combined historical day:    {portfolio_returns[-1]:.2f}%")
print("-" * 55)
print(f"{confidence_level}% 1-Day Portfolio VaR:  {var_percentage:.2f}%")
print(f"Maximum Expected Loss: ${abs(cash_loss):,.2f}")
print("=" * 55)
