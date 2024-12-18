from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

def train_lstm_model(X_train, y_train):
    X_train = X_train.reshape((X_train.shape[0], 1, X_train.shape[1]))
    model = Sequential([
        LSTM(50, activation='relu', input_shape=(X_train.shape[1], X_train.shape[2])),
        Dense(1)
    ])
    model.compile(optimizer='adam', loss='mse', metrics=['mae'])
    history = model.fit(X_train, y_train, epochs=50, batch_size=8, verbose=1)
    model.save("models/lstm_model.h5")
    print("LSTM model trained and saved.")
    return history.history
