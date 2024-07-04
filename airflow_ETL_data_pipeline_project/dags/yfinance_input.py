import yfinance as yf
import pandas as pd



def import_data(start , end):
    data = yf.download(tickers="AAPL",start=start,end=end)
    data = data[["Close","Volume"]]
    data.to_csv("Input_File/APPL.csv")


