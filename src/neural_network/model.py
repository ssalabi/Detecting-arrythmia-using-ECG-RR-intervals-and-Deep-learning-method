import torch.nn as nn
from torch import Tensor


class Model(nn.Module):
    def __init__(self, lstm_drop, layers, batch_size=1024, device='cpu'):
        super().__init__()
        self.h_dim = 200
        self.device = device
        self.layers = layers
        self.batch_size = batch_size
        self.lstm = nn.GRU(input_size=100, hidden_size=self.h_dim, bidirectional=True, dropout=lstm_drop, num_layers=layers, bias=True)
        #self.tan = nn.Tanh()
        self.max_pool = nn.MaxPool1d(1)
        self.fc1 = nn.Linear(400, 50, bias=True)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(0.1)
        # self.fc2 = nn.Linear(256, 64)
        # self.relu2 = nn.ReLU()
        # self.dropout2 = nn.Dropout(0.1)
        self.fc3 = nn.Linear(50, 1, bias=True)
        self.sig = nn.Sigmoid()

    def forward(self, x: Tensor, hidden_state):
        y, hidden_state = self.lstm(x, hidden_state)
        #y = self.tan(y)
        y = self.max_pool(y)
        y = self.fc1(y)
        y = self.relu(y)
        y = self.dropout(y)
        # y = self.fc2(y)
        # y = self.relu2(y)
        # y = self.dropout2(y)
        y = self.fc3(y)
        y = self.sig(y)
        return y, hidden_state
