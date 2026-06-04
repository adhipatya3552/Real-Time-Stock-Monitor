import pandas as pd

def preprocess(df):

    df = df.dropna()

    df = df.reset_index()

    df["Datetime"] = pd.to_datetime(
        df["Datetime"]
    )

    return df