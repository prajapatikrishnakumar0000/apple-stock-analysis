import yfinance as yf
import pandas as pd

# Fetch real-world data from internet using API
data = yf.download(
    "AAPL", start="2020-01-01", end="2025-01-01", group_by="coumn", auto_adjust=False
)

print(data.head())
print("Rows, Columns:", data.shape)

# Save dataset
data.to_csv("sales_data.csv")

print("Dataset created successfully!")
