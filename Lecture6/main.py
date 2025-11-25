import torch
from torch import nn, optim
from torch.utils.data import DataLoader
from dataset  import cifar_datasets
from model import CNN

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
if torch.cuda.is_available():
    print('gpu is available')

def run_epoch(model, dataloader, criterion, optimizer=None, is_train=True):
    model.train() if is_train else model.eval()

    total_loss = 0.
    correct = 0
    total = 0

    with torch.set_grad_enabled(is_train):
        for data, labels in dataloader:
            data, labels = data.to(device), labels.to(device)

            outputs = model(data)
            loss = criterion(outputs, labels)

            if is_train:
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()

            total_loss += loss.item()
            _, predict = outputs.max(1)
            total += labels.size(0)
            correct += predict.eq(labels).sum().item()

    avg_loss = total_loss / len(dataloader)
    accuracy = correct / total
    return avg_loss, accuracy

train_data, test_data = cifar_datasets()
train_loader = DataLoader(train_data, batch_size=64, shuffle=True)
test_loader = DataLoader(test_data, batch_size=64, shuffle=False)

num_epochs = 20
learning_rate = 0.01

model = CNN()
model = model.to(device)

criterion = nn.CrossEntropyLoss()

optimizer = optim.SGD(model.parameters(), lr=learning_rate)

for epoch in range(num_epochs):
    train_loss, train_acc = run_epoch(model, train_loader, criterion, optimizer, is_train=True)
    test_loss, test_acc = run_epoch(model, test_loader, criterion, optimizer, is_train=False)
    print(f'epoch {epoch+1:>2} - train loss: {train_loss:.4f} - train_acc: {train_acc:.4f} - test loss: {test_loss:.4f} - test acc: {test_acc:.4f}')

