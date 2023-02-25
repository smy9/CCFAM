from encoder.generator_model import Generator
import dnnlib.tflib as tflib
import numpy as np
import os
import PIL.Image
import pickle


latent_dir = 'ccfam/latent_representations/white'
target_dir = 'ccfam/re_direction_results/white_red'
direction = np.load('ccfam/directions/w2r_direction.npy')
coeffs = -1.2

list = os.listdir(latent_dir)

tflib.init_tf()
with open('models/karras2019stylegan-ffhq-1024x1024.pkl', "rb") as f:
    generator_network, discriminator_network, Gs_network = pickle.load(f)
generator = Generator(Gs_network, batch_size=1, randomize_noise=False)

cnt = 0
for i in list:
    cnt += 1
    print(cnt)
    latent = np.load(os.path.join(latent_dir, i))
    latent[:8] = (latent + coeffs * direction)[:8]
    latent = np.expand_dims(latent, axis=0)
    generator.set_dlatents(latent)
    img_array = generator.generate_images()[0]
    img = PIL.Image.fromarray(img_array, 'RGB')
    j = i.replace('.npy', '.png')
    img.save(os.path.join(target_dir, j))
