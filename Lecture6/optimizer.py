import torch
from torch import nn
from torch import optim

class MyModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(1, 1)

    def forward(self, x):
        return self.linear(x)

def check_parameters(model):
    print('----- check parameter details -----')
    for name, param in model.named_parameters():
        print(f'name: {name}')
        print(f'shape: {param.shape}')
        print(f'value: {param.item()}')
        print('-----------------------------------')

if __name__ == "__main__":
    torch.manual_seed(0)
    x = torch.randn(100, 1)
    y = 3 * x + 0.5 * torch.randn(100, 1)

    model = MyModel()
    check_parameters(model=model)

    # loss function (Mean Square Error)
    criterion = nn.MSELoss()

    # optimizer (SGD)
    optimizer = optim.SGD(params=model.parameters(), lr=0.01)

    # learning section
    epochs =  100
    losses = []
    for epoch in range(epochs):
        model.train()

        # reset the gradients of parameters
        optimizer.zero_grad()

        # Forward, BackPropagation and parameters update
        outputs = model(x)
        loss = criterion(outputs, y)
        loss.backward()
        optimizer.step()

        losses.append(loss.item())

        if (epoch+1) % 10 == 0:
            print(f'Epoch: {epoch+1:>3}, Loss: {loss.item():.4f}')

    check_parameters(model=model)