import numpy as np
import os

white_bg_aligned_dir = './ccfam/latent_representations/white/'
red_bg_aligned_dir = './ccfam/latent_representations/red/'

white_latent_list = os.listdir(white_bg_aligned_dir)
red_latent_list = os.listdir(red_bg_aligned_dir)

cnt = 0
sum = np.zeros((18, 512), dtype='float32')
for w_latent_name in white_latent_list:
    r_latent_name = w_latent_name.replace('w', 'r', 1)
    if r_latent_name in red_latent_list:
        w_latent = np.load(os.path.join(white_bg_aligned_dir, w_latent_name))
        r_latent = np.load(os.path.join(red_bg_aligned_dir, r_latent_name))
        sum += (r_latent - w_latent)
        cnt += 1
    else:
        print(r_latent_name)

direction = sum / cnt

np.save('./ccfam/directions/w2r_direction.npy', direction)
