import matplotlib.pyplot as plt
from PIL import Image
from torchvision import transforms

if __name__ == "__main__":
    image_path = "./example_data/dog_img.png"
    image = Image.open(image_path)

    transform = transforms.Compose([
        transforms.Resize((224,224))
    ])
    # 変換を適用
    transformed_image = transform(image)
    print("変換前の画像サイズ")
    print(image.size)
    print("変換後の画像サイズ")
    print(transformed_image.size)
    plt.imshow(image)
    plt.show()
    plt.imshow(transformed_image)
    plt.show()