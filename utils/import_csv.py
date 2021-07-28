import numpy as np

import pandas as pd

#Get CSV data from CSV.
data = pd.read_csv('datasets/emotion_data_dataset.csv')

data.to_json('datasets/dataset.json')
