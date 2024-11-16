import pandas as pd
from src.feature_store_api import FeatureStore

def test_feature_store():
    store = FeatureStore()
    data = pd.DataFrame({"a": [1, 2, 3]})
    store.save_features("test_key", data)
    assert not store.get_features("test_key").empty
