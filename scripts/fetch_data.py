import yfinance as yf

# Step 1: Define the stock and time period
stock = "AAPL"  # Apple
start_date = "2022-01-01"
end_date = "2022-12-31"

# Step 2: Download data
data = yf.download(stock, start=start_date, end=end_date)

# Step 3: Save as CSV in data/ folder
data.to_csv("../data/aapl_2022.csv")

print("Dataset saved as aapl_2022.csv in data/ folder")
