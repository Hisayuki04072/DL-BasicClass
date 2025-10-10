import matplotlib.pyplot as plt
from PIL import Image
from torchvision import transforms

if __name__ == "__main__":
    image_path = "./example_data/dog_img.png"
    image = Image.open(image_path)

    transform = transforms.Compose([
        transforms.RandomHorizontalFlip()
    ])
    # 変換を適用
    transformed_image = transform(image)
    # 画像出力
    plt.imshow(image)
    plt.show()
    plt.imshow(transformed_image)
    plt.show()