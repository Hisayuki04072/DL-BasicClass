import torch
from torch import nn

if __name__ == "__main__":
    # 入力Tensorの定義
    _in1 = torch.ones(32, 256, 64, 64)

    # Batch Normalization定義＆適用
    print("===BNの定義&適用===")
    norm = nn.BatchNorm2d(num_features=256)
    out1 = norm(_in1)
    print(f"out1 : {out1.shape}")

    # 動作確認用
    print("===動作確認===")
    _in2 = torch.tensor([
        [3., 2., 5.],
        [16., 43., 1.],
        [18., 3.1, 56],
    ]).unsqueeze(dim=0).unsqueeze(dim=0)
    norm2 = nn.BatchNorm2d(num_features=1, affine=False)
    out2 = norm2(_in2)
    print("===before===")
    print(repr(_in2))
    print(f"mean : {torch.mean(_in2)}, var : {torch.var(_in2)}")
    print("===after===")
    print(repr(out2))
    print(f"mean : {torch.mean(out2)}, var : {torch.var(out2)}")
