import numpy as np
import os

red_bg_aligned_dir = './ccfam/latent_representations/red/'
white_bg_aligned_dir = './ccfam/latent_representations/white/'

red_latent_list = os.listdir(red_bg_aligned_dir)
white_latent_list = os.listdir(white_bg_aligned_dir)

cnt = 0
sum = np.zeros((18, 512), dtype='float32')
for r_latent_name in red_latent_list:
    w_latent_name = r_latent_name.replace('r', 'w', 1)
    if w_latent_name in white_latent_list:
        r_latent = np.load(os.path.join(red_bg_aligned_dir, r_latent_name))
        w_latent = np.load(os.path.join(white_bg_aligned_dir, w_latent_name))
        sum += (w_latent - r_latent)
        cnt += 1
    else:
        print(w_latent_name)

direction = sum / cnt

np.save('./ccfam/directions/r2w_direction.npy', direction)
