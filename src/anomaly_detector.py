def detect_anomalies(df, model):

    features = [
        "Close",
        "MA_5",
        "MA_10",
        "Volatility",
        "Price_Return"
    ]

    X = df[features]

    df["Anomaly"] = model.predict(X)

    return df