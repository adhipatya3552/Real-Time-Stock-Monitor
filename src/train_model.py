from sklearn.ensemble import IsolationForest

def train_model(df):

    features = [
        "Close",
        "MA_5",
        "MA_10",
        "Volatility",
        "Price_Return"
    ]

    X = df[features]

    model = IsolationForest(
        contamination=0.02,
        random_state=42
    )

    model.fit(X)

    return model