import torch
import torch.nn as nn
import torch.optim as optim
from framework.utils import load_dataset, split_dataset
from models.lstm import LSTMDetector

def train_lstm():
    X, y = load_dataset()
    (X_train, y_train), (X_test, y_test) = split_dataset(X, y)

    X_train = torch.tensor(X_train, dtype=torch.float32).unsqueeze(1)
    y_train = torch.tensor(y_train, dtype=torch.float32).unsqueeze(1)

    model = LSTMDetector(input_dim=X_train.shape[2])
    criterion = nn.BCELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    for epoch in range(10):
        optimizer.zero_grad()
        outputs = model(X_train)
        loss = criterion(outputs, y_train)
        loss.backward()
        optimizer.step()
        print(f"Epoch {epoch+1}, Loss={loss.item():.4f}")

    return model

