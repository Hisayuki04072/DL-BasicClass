from pathlib import Path
from torch.utils.data import random_split

if __name__ == "__main__":    
    data_directory = "../../05/exercise/data"
    data_directory_path = Path(data_directory).resolve()
    dir_list = sorted(list(data_directory_path.glob("*")))
    file_list = []
    for dir in dir_list:
        file_path_list = list(dir.glob("*"))
        file_list += file_path_list

    # データセット全体のサイズ
    dataset_size = len(file_list)

    # データセットを訓練データとテストデータに分割する割合を設定
    train_ratio = 0.8
    train_size = int(train_ratio * dataset_size)
    val_size = dataset_size - train_size

    # ランダムに分割
    train_dataset, val_dataset = random_split(file_list, [train_size, val_size])

    # 分割されたデータセットのサイズを確認
    print(f"dataset size:  {len(file_list)}")
    print(f"train dataset size: {len(train_dataset)}")
    print(f"val dataset size: {len(val_dataset)}")
