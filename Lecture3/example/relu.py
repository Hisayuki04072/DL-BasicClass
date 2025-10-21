import torch
from torch import nn

if __name__ == "__main__":
    # 入力Tensorの定義
    _in = torch.tensor([
        [-1., -2., 3.],
        [43., 21., -21.],
        [-0.5, 0, 0.1]
    ]).unsqueeze(dim=0).unsqueeze(dim=0)

    # ReLU定義&適用
    relu = nn.ReLU()
    out = relu(_in)
    print(repr(out))