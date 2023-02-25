import numpy as np
import os

blue_bg_aligned_dir = './ccfam/latent_representations/blue/'
white_bg_aligned_dir = './ccfam/latent_representations/white/'

blue_latent_list = os.listdir(blue_bg_aligned_dir)
white_latent_list = os.listdir(white_bg_aligned_dir)

cnt = 0
sum = np.zeros((18, 512), dtype='float32')
for b_latent_name in blue_latent_list:
    w_latent_name = b_latent_name.replace('b', 'w', 1)
    if w_latent_name in white_latent_list:
        b_latent = np.load(os.path.join(blue_bg_aligned_dir, b_latent_name))
        w_latent = np.load(os.path.join(white_bg_aligned_dir, w_latent_name))
        sum += (w_latent - b_latent)
        cnt += 1
    else:
        print(w_latent_name)

direction = sum / cnt

np.save('./ccfam/directions/b2w_direction.npy', direction)
