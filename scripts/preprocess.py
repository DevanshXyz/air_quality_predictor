import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def preprocess_data(file_path):
    data = pd.read_csv(file_path)
    features = data[["pm25", "pm10", "no2", "so2", "co", "ozone"]].fillna(0)
    labels = data["aqi"]
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)
    X_train, X_test, y_train, y_test = train_test_split(
        scaled_features, labels, test_size=0.2, random_state=42
    )
    return X_train, X_test, y_train, y_test
