import torch
from models import ExcerciseModel

if __name__ == "__main__":
    # 入力Tensorの定義
    in_tensor = torch.ones(32, 3 ,128, 128)

    # モデルインスタンスの作成
    model = ExcerciseModel()

    # 実行＆結果確認
    out = model(in_tensor)
    print(f"in : {repr(in_tensor.shape)}")
    print(f"out : {repr(out.shape)}")