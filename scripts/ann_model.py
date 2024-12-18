from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

def train_ann_model(X_train, y_train):
    model = Sequential([
        Dense(64, input_dim=X_train.shape[1], activation='relu'),
        Dense(32, activation='relu'),
        Dense(1, activation='linear')
    ])
    model.compile(optimizer='adam', loss='mse', metrics=['mae'])
    history = model.fit(X_train, y_train, epochs=50, batch_size=8, verbose=1)
    model.save("models/ann_model.h5")
    print("ANN model trained and saved.")
    return history.history
