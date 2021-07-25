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

emotions_frame = pd.read_csv(
    'datasets/emotion_data_with_painting_location.csv')
n = 0
datasetArray = []
print('Loading and organizing Dataset')
while n < emotions_frame.shape[0]:
    img_name = emotions_frame.iloc[n, 0]
    emotions = emotions_frame.iloc[n, 1:9]
    emotions = np.asarray(emotions)

    #print('Image name: {}'.format(img_name))
    #print('Emotions from CSV: {}'.format(emotions))
    emotionMax = emotions.argmax()
    #print('Max emotion vote: {}'.format(emotionMax))
    #print('Max emotion name: {}'.format(emotions_frame.columns[emotionMax]))
    datasetArray.append([img_name, emotions.argmax(), emotions_frame.columns[emotionMax]])
    n += 1
print('Adding to CSV')
emotions_dataset = pd.DataFrame(datasetArray, columns=['image_name', 'labels', 'emotion_name'])
emotions_dataset.to_csv('datasets/emotion_data_dataset.csv', index=False)
print('Done')
