from scripts.waqi_fetch import fetch_multiple_cities
from scripts.preprocess import preprocess_data
from scripts.ann_model import train_ann_model
from scripts.svm_model import train_svm_model
from scripts.lstm_model import train_lstm_model
from scripts.visualization import visualize_real_time_data, plot_model_performance

if __name__ == "__main__":
    # Fetch real-time data
    cities = ["Delhi", "Los Angeles", "Beijing", "London"]
    data_file = "data/real_time_air_quality.csv"
    data = fetch_multiple_cities(cities)
    data.to_csv(data_file, index=False)

    # Visualize real-time data
    visualize_real_time_data(data_file)

    # Preprocess data
    X_train, X_test, y_train, y_test = preprocess_data(data_file)

    # Train and visualize ANN model
    ann_history = train_ann_model(X_train, y_train)
    plot_model_performance(ann_history, "ANN")

    # Train SVM model
    train_svm_model(X_train, y_train)

    # Train and visualize LSTM model
    lstm_history = train_lstm_model(X_train, y_train)
    plot_model_performance(lstm_history, "LSTM")

    print("All models trained and visualized successfully.")
