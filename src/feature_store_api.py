import pandas as pd

class FeatureStore:
    def __init__(self):
        self.store = {}

    def save_features(self, key: str, features: pd.DataFrame):
        self.store[key] = features

    def get_features(self, key: str) -> pd.DataFrame:
        return self.store.get(key, pd.DataFrame())
