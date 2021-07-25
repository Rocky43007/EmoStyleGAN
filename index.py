#!/usr/local/bin/python3

import cv2
import glob
from multiprocessing import Pool 

def thumbnail(params): 
    filename, N = params
    try:
        # Load just once, then successively scale down
        im = cv2.imread(filename)
        im = cv2.resize(im, (1600,1600))
        cv2.imwrite("t-%d-1600.jpg" % N, im) 
        im = cv2.resize(im, (720,720))
        cv2.imwrite("t-%d-720.jpg" % N, im) 
        im = cv2.resize(im, (256,256))
        cv2.imwrite("t-%d-120.jpg" % N, im) 
        return 'OK'
    except Exception as e: 
        return e 

files = glob.glob('image*.jpg')
pool = Pool(8)
results = pool.map(thumbnail, zip(files,range((len(files)))))
