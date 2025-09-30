import pandas as pd
import numpy as np

def load_dataset(path="dataset/dataset.csv"):
    """
    Load TestAdapt dataset from CSV.
    Returns X (features), y (labels).
    """
    df = pd.read_csv(path)
    
    # Suppose "label" is the column (0=non-deadlock, 1=deadlock)
    X = df.drop(columns=["label"]).values
    y = df["label"].values
    
    return X, y

def split_dataset(X, y, train_ratio=0.8):
    n = len(X)
    idx = int(n * train_ratio)
    return (X[:idx], y[:idx]), (X[idx:], y[idx:])
