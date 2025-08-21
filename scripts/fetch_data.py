import yfinance as yf

# Download Apple stock data for 2022
data = yf.download("AAPL", start="2022-01-01", end="2023-01-01")
print(data.head())

# Save data to the data/ folder (one level up from scripts/)
data.to_csv("../data/aapl_2022.csv")
