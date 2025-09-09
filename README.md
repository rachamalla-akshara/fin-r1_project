
# Fin-R1 Project: Stock Price Prediction

## Project Overview
This project predicts stock closing prices using a Linear Regression model trained on historical stock data.

## Folder Structure
fin-r1_project/
├── data/         # CSV files of stock data
├── models/       # Trained Linear Regression models
└── notebooks/    # Jupyter/Colab notebooks

## How to Run
1. Open the notebook in notebooks/.
2. Install required libraries:
   pip install yfinance pandas matplotlib scikit-learn joblib
3. Run all cells from start to finish.
4. Input the stock symbol when prompted (e.g., AAPL).
5. The notebook will:
   - Load stock data from data/
   - Train/load the Linear Regression model
   - Predict stock prices
   - Plot actual vs predicted prices

## Features
- Fetch stock data for a given symbol
- Train Linear Regression model
- Plot actual vs predicted closing prices
- End-to-end workflow organized in a professional structure

## Notes
- Currently, only stocks for which CSV data exists in data/ will work.
- Future enhancements can include multiple stocks, future predictions, and interactive dashboards.
