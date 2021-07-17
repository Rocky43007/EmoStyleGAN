from __future__ import print_function, division
import os
import torch
import pandas as pd
from skimage import io, transform
import numpy as np
import matplotlib.pyplot as plt
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, utils

# Ignore warnings
import warnings
warnings.filterwarnings("ignore")

plt.ion()   # interactive mode

emotions_frame = pd.read_csv('datasets/emotion_data_with_painting_location.csv')

n = 0
img_name = emotions_frame.iloc[n, 0]
emotions = emotions_frame.iloc[n, 1:]
emotions = np.asarray(emotions)
#emotions = emotions.astype('float').reshape(-1, 2)

print('Image name: {}'.format(img_name))
print('Emotions shape: {}'.format(emotions.shape))
print('First 4 Emotions from CSV: {}'.format(emotions[:4]))