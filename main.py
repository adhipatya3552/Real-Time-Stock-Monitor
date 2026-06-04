from src.data_ingestion import fetch_stock_data
from src.preprocessing import preprocess
from src.feature_engineering import create_features
from src.train_model import train_model
from src.anomaly_detector import detect_anomalies

# In-memory cache for trained models
_model_cache = {}

def run_pipeline(stock_symbol):

    df = fetch_stock_data(
        stock_symbol
    )

    df = preprocess(df)

    df = create_features(df)

    # Get cached model or train a new one in-memory
    if stock_symbol not in _model_cache:
        _model_cache[stock_symbol] = train_model(df)

    model = _model_cache[stock_symbol]
    df = detect_anomalies(df, model)

    return df