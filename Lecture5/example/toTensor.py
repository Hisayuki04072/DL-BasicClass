from PIL import Image
from torchvision import transforms
import numpy as np

if __name__ == "__main__":
    image_path = "./example_data/dog_img.png"
    image = Image.open(image_path)

    transform = transforms.Compose([
        transforms.ToTensor()
    ])
    # 変換を適用
    transformed_image = transform(image)
    print("変換前の型表示:\n",type(image))
    # NumPy配列に変換
    image_array = np.array(image)
    print("変換前のサイズ表示:\n",image_array.shape)

    print("変換後の型表:\n",type(transformed_image))
    print("変換後のサイズ表示:\n",transformed_image.size())