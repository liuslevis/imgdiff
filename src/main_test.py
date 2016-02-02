#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# ref http://stackoverflow.com/questions/189943/how-can-i-quantify-difference-between-two-images

import json
import os
import time
import sys
from util import *

import imagehash
from PIL import Image
from scipy.misc import imread, imsave
from scipy.linalg import norm
from scipy import sum, average

def main():
    if len(sys.argv) < 4:
        print '''
            usage:

                python ./src/main.py img1 img2 /path/to/diffimg

            output:
                
                YES / NO
                /path/to/diffimg
        '''
        return

    file1, file2 ,output = sys.argv[1:1+3]
    # read images as 2D arrays (convert to grayscale for simplicity)
    img1 = to_grayscale(imread(file1).astype(float))
    img2 = to_grayscale(imread(file2).astype(float))

    # compare
    n_m, n_0, diff_img = compare_images(img1, img2)
    diffhash, samehash = compare_images_hash(file1, file2)

    print "Manhattan norm:", n_m, "/ per pixel:", n_m/img1.size
    print "Zero norm:", n_0, "/ per pixel:", n_0*1.0/img1.size
    print "Diff hash:", diffhash, " Same hash:", samehash
    
    save_img(diff_img, output)
    pass

def compare_images(img1, img2):
    # normalize to compensate for exposure difference, this may be unnecessary
    # consider disabling it
    img1 = normalize(img1)
    img2 = normalize(img2)

    # calculate the difference and its norms
    diffimg = img1 - img2  # elementwise for scipy arrays
    m_norm = sum(abs(diffimg))  # Manhattan norm
    z_norm = norm(diffimg.ravel(), 0)  # Zero norm


    return (m_norm, z_norm, diffimg)

def compare_images_hash(file1, file2):
    hash1 = imagehash.average_hash(Image.open(file1))
    hash2 = imagehash.average_hash(Image.open(file2))

    # measure by feature
    diffhash = hash1 - hash2
    samehash = (hash1 == hash2)

    return diffhash, samehash

def save_img(imgarr, path):
    imsave(path, imgarr)


def to_grayscale(arr):
    "If arr is a color image (3D array), convert it to grayscale (2D array)."
    if len(arr.shape) == 3:
        return average(arr, -1)  # average over the last axis (color channels)
    else:
        return arr

def normalize(arr):
    rng = arr.max()-arr.min()
    amin = arr.min()
    return (arr-amin)*255/rng

if __name__ == '__main__':
    start_time = time.time()
    
    main()
    
    print("--- 运行时间：%.8f seconds ---" % float(time.time() - start_time))
