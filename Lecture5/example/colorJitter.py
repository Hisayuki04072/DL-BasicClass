import matplotlib.pyplot as plt
from PIL import Image
from torchvision import transforms

if __name__ == "__main__":
    image_path = "./example_data/dog_img.png"
    image = Image.open(image_path)

    transform = transforms.Compose([
        transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.2),
    ])
    # 変換を適用
    transformed_image = transform(image)
    plt.imshow(image)
    plt.show()
    plt.imshow(transformed_image)
    plt.show()