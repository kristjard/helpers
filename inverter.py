import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from os import listdir
from os.path import isfile, join


def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])


path = "/home/kristjan/Documents/work/estonian_gt/raw"
path2 = "/home/kristjan/Documents/work/estonian_gt/inverted"
files = [f for f in listdir(path) if isfile(join(path, f))]
i = 0

for f in files:
    i += 1
    img = mpimg.imread(path + "/" + f)
    gray = rgb2gray(img)
    inverted = 1 - gray
    enhanced = inverted * 10
    enhanced = np.clip(enhanced, 0, 1)
    norm_image = cv2.normalize(enhanced, None, alpha = 0, beta = 255, norm_type = cv2.NORM_MINMAX, dtype = cv2.CV_32F)
    print("processed ", i, " /", str(len(files)))
    cv2.imwrite(path2 + f, norm_image)


