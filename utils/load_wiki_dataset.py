from __future__ import print_function, division
import os
import torch
import pandas as pd
from skimage import io, transform
import numpy as np
import matplotlib.pyplot as plt
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, utils
from PIL import Image
from glob import glob
result = [y for x in os.walk('~/EmoStyleGAN/datasets/wikiart_256') for y in glob(os.path.join(x[0], '*.jpg'))]

# Ignore warnings
import warnings
warnings.filterwarnings("ignore")

plt.ion()   # interactive mode

emotions_frame = pd.read_csv(
    'datasets/emotion_data_with_painting_location.csv')
n = 0
image_dict = {"labels":[]}
print('Loading and organizing Dataset')
while n < emotions_frame.shape[0]:
    img_name = emotions_frame.iloc[n, 0]
    image_loc = emotions_frame.iloc[n, 14]
    emotions = emotions_frame.iloc[n, 1:9]
    emotions = np.asarray(emotions)
    #print('File Location: {}'.format(emotions_frame.iloc[n, 14]))
    findFile = str([x for x in result if '{}'.format(img_name) in x])
    fileLoc = findFile.partition('/')[2]
    fileLoc1 = fileLoc.rpartition(']')[0]
    fileLoc2 = fileLoc1.rpartition("'")[0]
    fileLoc3 = fileLoc2.partition('/')[2]
    fileLoc4 = fileLoc3.partition('/')[2]
    fileLoc5 = fileLoc4.partition('/')[2]
    fileLoc6 = fileLoc5.partition('/')[2]
    fileLoc7 = fileLoc6.partition('/')[2]
    #img2.show()
    image_dict['labels'].append('{}'.format(fileLoc7)),
    image_dict['labels'].append(int(emotions.argmax()));
    n += 1
print('Adding to JSON File')
import json
with open('dataset.json', 'w') as f: 
    json.dump(image_dict, f)
print('Done')

# Notes
    #print('Image name: {}'.format(img_name))
    #print('Emotions from CSV: {}'.format(emotions))
    #emotionMax = emotions.argmax()
    #print('Max emotion vote: {}'.format(emotionMax))
    #print('Max emotion name: {}'.format(emotions_frame.columns[emotionMax]))
    #print('image loc: {}'.format(image_loc))
    #emotions_dataset = pd.DataFrame(datasetArray, columns=['image_name', 'labels', 'emotion_name'])
#emotions_dataset = pd.DataFrame(datasetArray, columns=['labels'])
#emotions_dataset.to_csv('datasets/emotion_data_dataset2.csv', index=False)
#datasetAray.append([image_loc, emotions.argmax()])
