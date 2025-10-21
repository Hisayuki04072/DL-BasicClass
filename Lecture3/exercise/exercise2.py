import torch
from torch import nn

if __name__ == "__main__":
    # problem1
    print("===problem1===")
    _in = torch.ones(32, 1024)
    print(f"_in : {_in.shape}")

    # problem2
    print("===problem2===")
    fc = nn.Linear(in_features=1024, out_features=256, bias=True)
    out1 = fc(_in)
    print(f"out1 : {out1.shape}")

    # problem3
    print("===problem3===")
    fc = nn.Linear(in_features=1024, out_features=2048, bias=True)
    out2 = fc(_in)
    print(f"out2 : {out2.shape}")

    # appendix
    print("===appendix===")
    out3 = out1.reshape(32, 16, 16)
    print(f"out3 : {out3.shape}")