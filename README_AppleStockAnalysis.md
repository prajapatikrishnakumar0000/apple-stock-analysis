# Apple Stock Market Analysis (AAPL)

An end-to-end data science project on Apple Inc. (AAPL) stock data — covering real-time data collection via API, data cleaning, exploratory data analysis, visualization, and time-series forecasting. Completed during Data Science Internship at Widesoftech Pvt. Ltd. (Jan–Feb 2026).

## Project Overview

This project demonstrates a complete data science workflow using real Apple stock market data fetched through a financial API. The goal was to analyze historical price trends, engineer meaningful features, build visualizations for stakeholders, and apply time-series forecasting techniques.

## What Was Done

### 1. Data Collection
- Fetched 5+ years of daily AAPL stock data (Open, High, Low, Close, Volume) via financial API
- Automated data retrieval and stored as structured DataFrame

### 2. Data Cleaning & Preprocessing
- Standardized date formats, set date as index
- Handled missing values and outliers
- Validated data integrity across the full time range

### 3. Feature Engineering (10+ features)
- 20-day and 50-day Simple Moving Averages (SMA)
- Exponential Moving Average (EMA)
- Daily Returns (% change)
- Cumulative Returns
- Rolling Volatility (20-day standard deviation)
- Bollinger Bands (Upper, Lower, Middle)
- Volume Moving Average

### 4. Exploratory Data Analysis & Visualization (15+ charts)
- Closing price trend with moving averages
- Candlestick chart
- Bollinger Bands visualization
- Daily returns distribution
- Rolling volatility chart
- Correlation heatmap
- Volume trend analysis

### 5. Time-Series Forecasting
- Applied time-series analysis techniques to predict short-term price trends
- Achieved MAPE (Mean Absolute Percentage Error) below 5% on held-out test data

## Repository Structure

```
apple-stock-analysis/
├── AAPL_Stock_Analysis.ipynb    # Main Jupyter notebook (full workflow)
├── requirements.txt             # Python dependencies
└── README.md
```

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| Pandas | Data manipulation & time-series indexing |
| NumPy | Numerical computations |
| Matplotlib | Price charts, trend plots |
| Seaborn | Heatmaps, distribution plots |
| Financial API | Real-time/historical stock data |
| Jupyter Notebook | Development (inside VS Code) |

## How to Run

```bash
# Install dependencies
pip install pandas numpy matplotlib seaborn yfinance jupyter

# Open notebook
jupyter notebook AAPL_Stock_Analysis.ipynb
```

## Key Takeaways

- Understood end-to-end data science workflow on real financial data
- Gained hands-on experience with time-series feature engineering
- Learned how to communicate technical findings through clear visualizations
- Built reproducible, well-documented notebooks

## Internship Context

Completed at **Widesoftech Pvt. Ltd.** (07 Jan 2026 – 10 Feb 2026) as part of a Data Science Internship. All analysis steps were independently executed using Jupyter Notebook inside VS Code.

## Author

**Krishnakumar Prajapati**  
B.E. Information Technology | Parvatibai Genba Moze College of Engineering, Pune  
[LinkedIn](https://www.linkedin.com/in/krishnakumar-prajapati-b075193a6) | [GitHub](https://github.com/prajapatikrishnakumar0000)
