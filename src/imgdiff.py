#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import imagehash
from PIL import Image
from scipy.misc import imread, imsave
from scipy.linalg import norm
from scipy import sum, average

DIFF_THRESHOLD = 1 

'''
输入： 图片路径 imagefile1 imagefile2，输出差异图片路径 diffimg_path
条件： 输入图片必须是 PNG 无损格式，尺寸一致。
输出： isDiff(Bool) 是否有差异；
      m_norm(int) 两个输入图片灰度化后的L1距离（曼哈顿距离，差值的绝对值的和）；
      如果isDiff==True，保存差异图片到 diffimg_path
'''
def imgdiff(imagefile1, imagefile2, diffimg_path):
    img1 = to_grayscale(imread(imagefile1).astype(float))
    img2 = to_grayscale(imread(imagefile2).astype(float))

    diffimg = img1 - img2  # elementwise for scipy arrays
    
    #两张图片灰度化后的像素差的和，既L1距离
    m_norm = sum(abs(diffimg))  # Manhattan norm

    # 如果两幅图片差异大于阈值，保存diff图片
    isDiff = False
    if m_norm > DIFF_THRESHOLD:
        isDiff = True
        imsave(diffimg_path, diffimg)


    return isDiff, int(m_norm)

def to_grayscale(arr):
    if len(arr.shape) == 3:
        return average(arr, -1)  # average over the last axis (color channels)
    else:
        return arr

def normalize(arr):
    rng = arr.max()-arr.min()
    amin = arr.min()
    return (arr-amin)*255/rng