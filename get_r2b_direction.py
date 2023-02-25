import numpy as np
import os

red_bg_aligned_dir = './ccfam/latent_representations/red/'
blue_bg_aligned_dir = './ccfam/latent_representations/blue/'

red_latent_list = os.listdir(red_bg_aligned_dir)
blue_latent_list = os.listdir(blue_bg_aligned_dir)

cnt = 0
sum = np.zeros((18, 512), dtype='float32')
for r_latent_name in red_latent_list:
    b_latent_name = r_latent_name.replace('r', 'b', 1)
    if b_latent_name in blue_latent_list:
        r_latent = np.load(os.path.join(red_bg_aligned_dir, r_latent_name))
        b_latent = np.load(os.path.join(blue_bg_aligned_dir, b_latent_name))
        sum += (b_latent - r_latent)
        cnt += 1
    else:
        print(b_latent_name)

direction = sum / cnt

np.save('./ccfam/directions/r2b_direction.npy', direction)
