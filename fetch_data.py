import yfinance as yf
import pandas as pd

# List of top 50 Indian stock tickers (example: NIFTY 50 stocks with '.NS' for NSE)
tickers = [
    "RELIANCE.NS", "TCS.NS", "INFY.NS", "HDFCBANK.NS", "ICICIBANK.NS", "LT.NS", "SBIN.NS", "HINDUNILVR.NS", 
    "ITC.NS", "KOTAKBANK.NS", "AXISBANK.NS", "ASIANPAINT.NS", "BAJFINANCE.NS", "MARUTI.NS", "HCLTECH.NS", 
    "WIPRO.NS", "BHARTIARTL.NS", "SUNPHARMA.NS", "NTPC.NS", "ONGC.NS", "ULTRACEMCO.NS", "TITAN.NS", 
    "NESTLEIND.NS", "POWERGRID.NS", "TECHM.NS", "TATAMOTORS.NS", "COALINDIA.NS", "JSWSTEEL.NS", 
    "HINDALCO.NS", "BAJAJ-AUTO.NS", "GRASIM.NS", "ADANIENT.NS", "ADANIPORTS.NS", "BPCL.NS", "EICHERMOT.NS", 
    "BRITANNIA.NS", "CIPLA.NS", "SHREECEM.NS", "DIVISLAB.NS", "HEROMOTOCO.NS", "DRREDDY.NS", "INDUSINDBK.NS", 
    "TATACONSUM.NS", "SBILIFE.NS", "BAJAJFINSV.NS", "HDFCLIFE.NS", "ICICIPRULI.NS", "M&M.NS", "APOLLOHOSP.NS", "LTIM.NS"
]

# Fetch adjusted closing prices (automatically adjusted)
data = yf.download(tickers, start="2020-01-01", end="2024-12-31", auto_adjust=True)['Close']

# Save to CSV
data.to_csv("data.csv")
print("✅ Data saved to data.csv")
