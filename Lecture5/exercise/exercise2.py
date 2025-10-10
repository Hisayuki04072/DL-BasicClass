from PIL import Image
from pathlib import Path
from torchvision import transforms
import torch
from torch.utils.data import Dataset
from torch.utils.data import random_split

class ImageTransform():
    def __init__(self, resize, mean, std):
        self.data_transform = {
            'train': transforms.Compose([
                transforms.RandomResizedCrop(
                    resize, scale=(0.5, 1.0)), 
                transforms.RandomHorizontalFlip(),
                transforms.ToTensor(), 
                transforms.Normalize(mean, std)
            ]),
            'val': transforms.Compose([
                transforms.Resize(resize), 
                transforms.ToTensor(),  
                transforms.Normalize(mean, std)
            ])
        }

    def __call__(self, img, phase='train'):
        return self.data_transform[phase](img)
    
class MyDataset(Dataset):
    def __init__(self, img_list, transform=None, phase='train'):
        self.transform = transform
        self.phase = phase
        self.img_list = img_list
        
    def __len__(self):
        return len(self.img_list)
    
    def __getitem__(self, idx):
        img_path = self.img_list[idx]
        img = Image.open(img_path)
        img_tensor = self.transform(img, self.phase)
        # ファイル名からラベルの取得
        img_path = Path(img_path)
        parts = img_path.parts
        label = int(parts[-2])

        return img_tensor, label
    

if __name__ == "__main__":

    data_directory = "../../05/exercise/data"
    data_directory_path = Path(data_directory).resolve()
    dir_list = sorted(list(data_directory_path.glob("*")))
    file_list = []
    for dir in dir_list:
        file_path_list = list(dir.glob("*"))
        file_list += file_path_list

    dataset_size = len(file_list)

    # データセットを訓練データとテストデータに分割する割合を設定
    train_ratio = 0.8
    train_size = int(train_ratio * dataset_size)
    val_size = dataset_size - train_size

    # ランダムに分割
    train_dataset, val_dataset = random_split(file_list, [train_size, val_size])

    size = 24
    mean = (0.5,0.5,0.5)
    std = (0.5,0.5,0.5)

    train_dataset = MyDataset(train_dataset, transform=ImageTransform(size,mean,std), phase='train')
    val_dataset = MyDataset(val_dataset, transform=ImageTransform(size,mean,std), phase='val')
    
    batch_size = 8
    print("===== problem2 =====")
    print(f"Train dataset size: {len(train_dataset)}")
    print(f"val dataset size: {len(val_dataset)}")
    
     # DataLoaderを作成
    train_dataloader = torch.utils.data.DataLoader(
        train_dataset, batch_size=batch_size, shuffle=True)

    val_dataloader = torch.utils.data.DataLoader(
        val_dataset, batch_size=batch_size, shuffle=False)
    
    print("===== problem3 =====")
    for batch in train_dataloader:
        # batchはデータとラベルのタプル (data, labels)
        data, labels = batch
        print("Data shape:", data.shape)
        
        print("Labels:", labels)
