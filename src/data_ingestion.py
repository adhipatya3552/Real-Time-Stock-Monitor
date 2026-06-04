import yfinance as yf
import pandas as pd

def fetch_stock_data(symbol):

    df = yf.download(
        symbol,
        period="30d",
        interval="15m",
        auto_adjust=True,
        progress=False
    )

    if isinstance(df.columns, pd.MultiIndex):
        df.columns = [
            col[0]
            for col in df.columns
        ]

    return df