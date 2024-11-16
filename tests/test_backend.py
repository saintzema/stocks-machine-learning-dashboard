import pandas as pd
from src.backend import trade_to_ohlc

def test_trade_to_ohlc():
    data = {
        "price": [1, 2, 3, 4],
        "volume": [10, 20, 30, 40],
        "time": pd.to_datetime(["2023-01-01 00:00:00", "2023-01-01 00:01:00", "2023-01-01 00:02:00", "2023-01-01 00:03:00"])
    }
    df = pd.DataFrame(data)
    ohlc = trade_to_ohlc(df, "1min")
    assert not ohlc.empty
