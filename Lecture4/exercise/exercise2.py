from PIL import Image
from pathlib import Path
from torch.utils.data import Dataset

class MyDataset(Dataset):
    def __init__(self, dataset_dir):
        dir_path = Path(dataset_dir)
        self.img_list = list(dir_path.glob("**/*.png"))

        
    def __len__(self):
        return len(self.img_list)
    
    def __getitem__(self, idx):
        img_path = self.img_list[idx]
        img = Image.open(img_path)
        
        return img
    
if __name__ == "__main__":
    my_dataset = MyDataset("Lecture4/exercise/data")
    print("===== problem1.1 =====")
    print(len(my_dataset))
    print("===== problem1.2 =====") 
    print(my_dataset[0].size)