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
                """
                記述
                """
            ]),
            'val': transforms.Compose([
                """
                記述
                """
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

    """
    記述
    """
    train_dataset = "記述"
    val_dataset = "記述"
    size = 24
    mean = (0.5,0.5,0.5)
    std = (0.5,0.5,0.5)
    train_dataset = MyDataset(train_dataset, transform=ImageTransform(size,mean,std), phase='train')
    val_dataset = MyDataset(val_dataset, transform=ImageTransform(size,mean,std), phase='val')