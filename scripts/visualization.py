import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_real_time_data(file_path):
    data = pd.read_csv(file_path)
    plt.figure(figsize=(10, 6))
    sns.barplot(x="city", y="aqi", data=data, palette="coolwarm")
    plt.title("Air Quality Index (AQI) by City")
    plt.xlabel("City")
    plt.ylabel("AQI")
    plt.tight_layout()
    plt.savefig("data/aqi_by_city.png")
    plt.show()

def plot_model_performance(metrics, model_name):
    epochs = range(1, len(metrics['loss']) + 1)
    
    plt.figure(figsize=(10, 6))
    plt.plot(epochs, metrics['loss'], label='Loss', marker='o')
    plt.plot(epochs, metrics['mae'], label='MAE', marker='s')
    plt.title(f"{model_name} Training Performance")
    plt.xlabel("Epochs")
    plt.ylabel("Metrics")
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.savefig(f"models/{model_name.lower()}_performance.png")
    plt.show()
