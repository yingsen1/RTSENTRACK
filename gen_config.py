import os
from os.path import join, isdir
from tracker import *
import numpy as np

import argparse

import pickle

import math
import StringIO
import scipy

def genConfig(seq_path, set_type):

    path, seqname = os.path.split(seq_path)


    if set_type == 'OTB':
      

        img_list = sorted([seq_path + '/img/' + p for p in os.listdir(seq_path + '/img') if os.path.splitext(p)[1] == '.jpg'])
        gt_path = os.path.join(seq_path,"groundtruth_rect.txt")


        if seqname == 'David':
            img_list = img_list[299:]
          
        if seqname == 'Football1':
            img_list = img_list[0:74]
        if seqname == 'Freeman3':
            img_list = img_list[0:460]
        if seqname == 'Freeman4':
            img_list = img_list[0:283]
        if seqname == 'Diving':
            img_list = img_list[0:215]
        if seqname == 'Tiger1':
            img_list = img_list[5:]

        print(seq_path.split('/')[-1])

        # convert to the same format
        s = open(gt_path).read().replace('\t', ',')
        s = s.replace(' ', ',')
        gt = np.loadtxt(StringIO.StringIO(s), delimiter=',')



        ##polygon to rect
    if gt.shape[1] == 8:
        x_min = np.min(gt[:, [0, 2, 4, 6]], axis=1)[:, None]
        y_min = np.min(gt[:, [1, 3, 5, 7]], axis=1)[:, None]
        x_max = np.max(gt[:, [0, 2, 4, 6]], axis=1)[:, None]
        y_max = np.max(gt[:, [1, 3, 5, 7]], axis=1)[:, None]
        gt = np.concatenate((x_min, y_min, x_max - x_min, y_max - y_min), axis=1)

    return img_list, gt