import torch
from torch import nn

if __name__ == "__main__":
    #Tenorを定義
    #実際に学習に使われるデータは，
    #　(Batchsize, channel, width, height)
    #という形状
    my_tensor = torch.ones((16, 3, 256, 256))
    print(f"original : {my_tensor.shape}")

    #畳み込み定義＆適用
    conv = nn.Conv2d(in_channels=3, out_channels=64, kernel_size=3)
    out = conv(my_tensor)
    print(f"out1 : {out.shape}")

    #Optional引数も指定
    conv2 = nn.Conv2d(in_channels=3, out_channels=64, kernel_size=3, stride=1, padding=1)
    out2 = conv2(my_tensor)
    print(f"out2 : {out2.shape}")
