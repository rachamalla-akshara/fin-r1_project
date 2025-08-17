# Step 1: Import libraries
import pandas as pd
import numpy as np

# Step 2: Load the CSV file
data = pd.read_csv("../data/aapl_2022.csv", skiprows=1, index_col=0)

# Step 3: Check current column names
print("Columns in dataset:", data.columns)

# Step 4: Remove the first row (extra header)
data = data.iloc[1:, :]
data.reset_index(drop=True, inplace=True)

# Step 5: Rename columns
data.columns = ["Open", "High", "Low", "Close", "Volume"]

# Step 6: Convert columns to numeric
cols = ["Open", "High", "Low", "Close", "Volume"]
data[cols] = data[cols].apply(pd.to_numeric)

# Step 7: Check for missing values
print("\nMissing values in each column:")
print(data.isnull().sum())

# Step 8: Preview first 5 rows
print("\nCleaned dataset first 5 rows:")
print(data.head())

# Step 9: Column info and summary statistics
print("\nColumn info and data types:")
print(data.info())
print("\nSummary statistics:")
print(data.describe())
