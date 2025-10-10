from torchvision import transforms
from PIL import Image
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # 画像のリサイズと正規化の前処理を定義
    preprocess_1 = transforms.Compose([
        transforms.Resize((256, 256)),      # 画像を256x256にリサイズ
        transforms.ToTensor(),               # テンソルに変換
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))  # RGBの各チャンネルを正規化
    ])

    # ランダムな水平反転と色調の変更の前処理を定義
    preprocess_2 = transforms.Compose([
        transforms.RandomHorizontalFlip(),  # 50%の確率で水平反転
        transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.2),  # 色調のランダムな変更
        transforms.ToTensor()               # テンソルに変換
    ])

    # ランダムな回転とクロップの前処理を定義
    preprocess_3 = transforms.Compose([
        transforms.RandomHorizontalFlip(),      # 50%の確率で水平反転
        transforms.RandomResizedCrop(224),       # ランダムなサイズとアスペクト比でクロップ
        transforms.ToTensor()                # テンソルに変換
    ])
    # サンプル画像を読み込んで前処理を適用
    image_path = "./exercise_data/dog_img.png"
    image = Image.open(image_path)
    
    processed_image = preprocess_1(image)
    # テンソルに変換した画像を表示
    plt.imshow(processed_image.permute(1, 2, 0))  # チャンネル次元を最後に移動
    plt.show()

    processed_image = preprocess_2(image)
    plt.imshow(processed_image.permute(1, 2, 0))  # チャンネル次元を最後に移動
    plt.show()

    processed_image = preprocess_3(image)
    plt.imshow(processed_image.permute(1, 2, 0))  # チャンネル次元を最後に移動
    plt.show()



