def create_features(df):

    df["MA_5"] = df["Close"].rolling(5).mean()

    df["MA_10"] = df["Close"].rolling(10).mean()

    df["Volatility"] = (
        df["Close"]
        .rolling(10)
        .std()
    )

    df["Price_Return"] = (
        df["Close"]
        .pct_change()
    )

    df = df.dropna()

    return df