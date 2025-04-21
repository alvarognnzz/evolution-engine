from pyfastnoiselite.pyfastnoiselite import FastNoiseLite, NoiseType
import numpy as np
import matplotlib.pyplot as plt

def generate_noise_map(width, height, seed=1233, noise_type=NoiseType.NoiseType_OpenSimplex2S, frequency=0.05):
    noise = FastNoiseLite(seed=seed)
    noise.noise_type = noise_type
    noise.frequency = frequency

    x_coords = np.arange(width, dtype=np.float32)
    y_coords = np.arange(height, dtype=np.float32)
    xx, yy = np.meshgrid(x_coords, y_coords)

    coords = np.array([xx.flatten(), yy.flatten()], dtype=np.float32)

    noise_values = noise.gen_from_coords(coords)

    noise_map = noise_values.reshape((height, width))

    noise_map = (noise_map + 1) / 2.0

    return noise_map

if __name__ == '__main__':
    width = 100
    height = 100

    noise_map = generate_noise_map(width, height)

    plt.imshow(noise_map, cmap='gray')
    plt.title("FastNoiseLite 2D Noise Map")
    plt.axis('off')
    plt.savefig("fastnoise_noise_map.png")
