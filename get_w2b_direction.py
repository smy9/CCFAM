import numpy as np
import os

white_bg_aligned_dir = './ccfam/latent_representations/white/'
blue_bg_aligned_dir = './ccfam/latent_representations/blue/'

white_latent_list = os.listdir(white_bg_aligned_dir)
blue_latent_list = os.listdir(blue_bg_aligned_dir)

cnt = 0
sum = np.zeros((18, 512), dtype='float32')
for w_latent_name in white_latent_list:
    b_latent_name = w_latent_name.replace('w', 'b', 1)
    if b_latent_name in blue_latent_list:
        w_latent = np.load(os.path.join(white_bg_aligned_dir, w_latent_name))
        b_latent = np.load(os.path.join(blue_bg_aligned_dir, b_latent_name))
        sum += (b_latent - w_latent)
        cnt += 1
    else:
        print(b_latent_name)

direction = sum / cnt

np.save('./ccfam/directions/w2b_direction.npy', direction)
