import matplotlib.pyplot as plt
import torch
import numpy as np
from model_utils import Generator
import os

# 设置生成图片数量
NUM_IMAGES = 1000
SAVE_PATH = './images/'

def create_directories(path):
    if not os.path.exists(path):
        os.mkdir(path)

def load_model():
    model = Generator()
    model.load_state_dict(torch.load('Generator.pth', map_location=torch.device('cpu')))
    return model

def generate(model, num_images):
    images = model(torch.randn(num_images, 100, 1, 1))
    return images.detach().numpy()

def save_anime(path, images):
    for i in range(len(images)):
        anime = images[i].reshape(3, 64, 64)
        anime = np.moveaxis(anime, 0, 2)
        anime = anime * np.array((0.5, 0.5, 0.5)) + np.array((0.5, 0.5, 0.5))
        anime = np.clip(anime, 0, 1)

        if i < 4:
            plt.imshow(anime)
            plt.show()

        plt.imsave(os.path.join(path, f'character{i+1}.png'), anime)

if __name__ == '__main__':
    create_directories(SAVE_PATH)
    model = load_model()
    print('Generating Characters...')
    images = generate(model, NUM_IMAGES)
    print('Saving Characters...')
    save_anime(SAVE_PATH, images)
    print('Done')
