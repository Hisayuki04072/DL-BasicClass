import torch
from torch import nn

if __name__=="__main__":
    # problem1
    print("===problem1===")
    my_tensor = torch.ones(32, 3, 128, 128)
    print(f"original : {my_tensor.shape}")

    # problem2
    print("===problem2===")
    conv1 = nn.Conv2d(in_channels=3, out_channels=64, kernel_size=3)
    out1 = conv1(my_tensor)
    print(f"out1 : {out1.shape}")

    # problem3
    print("===problem3===")
    conv2 = nn.Conv2d(in_channels=3, out_channels=256, kernel_size=3, stride=2, padding=1)
    out2 = conv2(my_tensor)
    print(f"out2 : {out2.shape}")

    # problem4
    print("===problem4===")
    conv3 = nn.Conv2d(in_channels=3, out_channels=64, kernel_size=5, stride=1, padding=1)
    out3 = conv3(my_tensor)
    print(f"out1(kernel=5) : {out3.shape}")

    conv4 = nn.Conv2d(in_channels=3, out_channels=256, kernel_size=5, stride=2, padding=2)
    out4 = conv4(my_tensor)
    print(f"out2(kernel=5) : {out4.shape}")