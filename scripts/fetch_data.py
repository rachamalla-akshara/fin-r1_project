import yfinance as yf

<<<<<<< HEAD
# Download Apple stock data for 2022
data = yf.download("AAPL", start="2022-01-01", end="2023-01-01")
print(data.head())

# Save data to the data/ folder (one level up from scripts/)
data.to_csv("../data/aapl_2022.csv")
=======
# Step 1: Define the stock and time period
stock = "AAPL"  # Apple
start_date = "2022-01-01"
end_date = "2022-12-31"

# Step 2: Download data
data = yf.download(stock, start=start_date, end=end_date)

# Step 3: Save as CSV in data/ folder
data.to_csv("../data/aapl_2022.csv")

print("Dataset saved as aapl_2022.csv in data/ folder")
>>>>>>> 3b788fef9587d5a97a4f2b6d7c9967ba8b455632
