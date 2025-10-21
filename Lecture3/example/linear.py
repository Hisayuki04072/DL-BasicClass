import torch
from torch import nn

if __name__ == "__main__":
    #入力Tensorの定義
    _in = torch.ones((32, 1280))
    print(f"_in : {_in.shape}")

    #全結合定義＆適用
    fc = nn.Linear(in_features=1280, out_features=256, bias=True)
    out = fc(_in)
    print(f"out : {out.shape}")