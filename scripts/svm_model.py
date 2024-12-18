from sklearn.svm import SVR
from joblib import dump

def train_svm_model(X_train, y_train):
    model = SVR(kernel='rbf')
    model.fit(X_train, y_train)
    dump(model, "models/svm_model.joblib")
    print("SVM model trained and saved.")
