from models.lstm import LSTMDetector
from models.petri_net import detect_deadlock

class HybridDetector:
    def __init__(self, lstm_model):
        self.lstm = lstm_model

    def predict(self, seq, hold_matrix, wait_matrix):
        # LSTM output (probability)
        prob = self.lstm(seq).item()
        
        # Structural check
        deadlock, _ = detect_deadlock(hold_matrix, wait_matrix)

        if prob > 0.5 and deadlock:
            return 1  # Deadlock
        return 0  # Non-deadlock

