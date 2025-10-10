import matplotlib.pyplot as plt
from PIL import Image
from torchvision import transforms

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
                transforms.CenterCrop(resize),
                transforms.ToTensor(),  
                transforms.Normalize(mean, std)
            ])
        }

    def __call__(self, img, phase='train'):
        """
        phase : 'train' or 'val'
        """
        return self.data_transform[phase](img)

if __name__ == "__main__":
    image_file_path = "./example_data/dog_img.png"
    img = Image.open(image_file_path)

    # 元の画像の出力
    plt.imshow(img)
    plt.show()

    # 画像の前処理と処理済み画像の表示
    size = 224
    mean = (0.485, 0.456, 0.406)
    std = (0.229, 0.224, 0.225)

    transform = ImageTransform(size, mean, std)
    img_transformed = transform(img, phase="train") 

    # (色、高さ、幅)を (高さ、幅、色)に変換
    plt.imshow(img_transformed.permute(1, 2, 0))  # チャンネル次元を最後に移動
    plt.show()
    
