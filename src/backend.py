import requests
import pandas as pd

def get_kraken_data(pair: str):
    url = f"https://api.kraken.com/0/public/Trades?pair={pair}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()["result"]
    key = list(data.keys())[0]
    trades = pd.DataFrame(data[key], columns=["price", "volume", "time", "buy_sell", "market_limit", "misc", "order_id"])
    trades["time"] = pd.to_datetime(trades["time"], unit="s")
    return trades

def trade_to_ohlc(trades: pd.DataFrame, interval: str = "1min"):
    ohlc = trades.resample(interval, on="time").agg({
        "price": ["first", "max", "min", "last"],
        "volume": "sum"
    })


     # Flatten multi-level columns from aggregation (if any)
    ohlc.columns = ["open", "high", "low", "close", "volume"]
    
        # If there are more than 6 columns, drop the extra ones
    if ohlc.shape[1] > 6:
        ohlc = ohlc.iloc[:, :6]

    # Debug: Print columns and first few rows
    print(f"OHLC Data Columns: {ohlc.columns}")
    print(ohlc.head())

    ohlc.columns = ["open", "high", "low", "close", "volume"]
    ohlc = ohlc.dropna().reset_index()
    return ohlc
