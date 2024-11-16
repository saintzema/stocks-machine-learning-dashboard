import pandas as pd 
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Function to generate target column (buy = 1, sell = 0)
def create_target(ohlc: pd.DataFrame):
    ohlc["future_price"] = ohlc["close"].shift(-1)
    ohlc["target"] = (ohlc["future_price"] > ohlc["close"]).astype(int)
    ohlc = ohlc.dropna()  # Drop rows with no future price
    return ohlc

# Train the machine learning model
def train_model(ohlc: pd.DataFrame):
    ohlc = create_target(ohlc)
    features = ohlc[["open", "high", "low", "close", "volume"]]
    target = ohlc["target"]
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)
    
    # Scale features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    
    # Train Random Forest Classifier
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    return model

# Predict buy/sell using the trained model
def predict_buy_sell(ohlc: pd.DataFrame, model):
    try:
        # Select features for prediction
        features = ohlc[["open", "high", "low", "close", "volume"]].copy()

        # Convert features to numeric
        for column in features.columns:
            features[column] = pd.to_numeric(features[column], errors="coerce")
            if features[column].isnull().any():
                print(f"Non-numeric data found in column: {column}")
                print(features[features[column].isnull()])

        # Drop rows with NaN values
        features_cleaned = features.dropna()
        ohlc_cleaned = ohlc.loc[features_cleaned.index].copy()

        # Scale features using StandardScaler
        scaler = StandardScaler()
        features_scaled = scaler.fit_transform(features_cleaned)

        # Predict buy/sell using the trained model
        predictions = model.predict(features_scaled)

        # Convert predictions to labels ("buy" or "sell")
        prediction_label = ["buy" if p == 1 else "sell" for p in predictions]

        # Add predictions to a new column in the cleaned DataFrame
        ohlc_cleaned["prediction"] = prediction_label

        # Debug: Print the resulting DataFrame with predictions
        print("OHLC with Predictions:")
        print(ohlc_cleaned.head())

        return ohlc_cleaned

    except Exception as e:
        print(f"Error in predict_buy_sell: {e}")
        raise
