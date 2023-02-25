from tqdm import tqdm_notebook
import config
import dnnlib
import json
import matplotlib.pylab as plt
import numpy as np
import os
import pickle
import warnings

warnings.filterwarnings('ignore')

LATENT_TRAINING_DATA = './FFHQ/latent_training_data.pkl'

qlatent_data, dlatent_data, labels_data = pickle.load(open(LATENT_TRAINING_DATA, "rb"))

print(qlatent_data.shape, dlatent_data.shape, len(labels_data))
