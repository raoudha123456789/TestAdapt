import torch
from sklearn.metrics import accuracy_score, f1_score
from framework.utils import load_dataset, split_dataset
from models.lstm import LSTMDetector

def evaluate(model):
    X, y = load_dataset()
    (_, _), (X_test, y_test) = split_dataset(X, y)

    X_test = torch.tensor(X_test, dtype=torch.float32).unsqueeze(1)
    y_pred = (model(X_test).detach().numpy() > 0.5).astype(int)

    acc = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    print(f"Accuracy={acc:.3f}, F1={f1:.3f}")
