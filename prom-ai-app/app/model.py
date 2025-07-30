import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.preprocessing import MinMaxScaler

def build_autoencoder(input_dim):
    model = Sequential([
        Dense(64, activation='relu', input_shape=(input_dim,)),
        Dense(32, activation='relu'),
        Dense(64, activation='relu'),
        Dense(input_dim, activation='linear')
    ])
    model.compile(optimizer='adam', loss='mse')
    return model

def train_and_detect(df: pd.DataFrame):
    df = df.copy()
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(df[["value"]].values)

    model = build_autoencoder(1)
    model.fit(X_scaled, X_scaled, epochs=10, batch_size=32, verbose=0)

    reconstructions = model.predict(X_scaled)
    loss = np.mean(np.square(reconstructions - X_scaled), axis=1)
    threshold = np.percentile(loss, 99)
    df["anomaly"] = loss > threshold
    return df, float(threshold)
