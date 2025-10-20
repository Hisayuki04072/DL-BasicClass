import torch
from torch import nn

class MyModel(nn.Module):
    def __init__(self, num_class=10):
        super().__init__()

        self.conv = nn.Conv2d(in_channels=3, out_channels=64,
                              kernel_size=3, stride=1, padding=1)
        self.bn = nn.BatchNorm2d(num_features=64)
        self.relu = nn.ReLU()

        input_features = 64 * 256 * 256
        self.fc = nn.Linear(in_features=input_features, out_features=num_class)

    def forward(self, x):
        x = self.conv(x)
        x = self.bn(x)
        x = self.relu(x)
        x = torch.flatten(x, 1)
        x = self.fc(x)
        return x 

if __name__ == "__main__":
    model = MyModel()
    x = torch.ones(32, 3, 256, 256)
    logits = model(x)
    print(logits.shape)