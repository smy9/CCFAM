from encoder.generator_model import Generator
import dnnlib.tflib as tflib
import numpy as np
import PIL.Image
import pickle


def generate_image(latent_vector, generator):
    # latent_vector = latent_vector.reshape((1, 18, 512))
    latent_vector = np.expand_dims(latent_vector, axis=0)
    generator.set_dlatents(latent_vector)
    img_array = generator.generate_images()[0]
    img = PIL.Image.fromarray(img_array, 'RGB')
    return img


def latent2image(latent, target_dir):
    tflib.init_tf()
    with open('models/karras2019stylegan-ffhq-1024x1024.pkl', "rb") as f:
        generator_network, discriminator_network, Gs_network = pickle.load(f)
    generator = Generator(Gs_network, batch_size=1, randomize_noise=False)
    result = generate_image(latent, generator)
    np.save(target_dir.replace('.png', '.npy'), latent)
    result.save(target_dir)
