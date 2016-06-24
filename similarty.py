 #-*- coding: UTF-8 -*- 
import tensorflow as tf
import numpy as np
import scipy.io
import scipy.misc
import os
import time
dic={}

def get_imlist(path):
  return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.npy')]
npylist=get_imlist('/home/lcw/下載/tensorflow/npy/')
c = np.load('/home/lcw/下載/tensorflow//npy/Gauguin123.npy')
def build_style_loss(A, G):
  loss = np.sum((A-G)**2)
  print loss
  print  '---------'
  return loss


for npypath in npylist:
  d = np.load(npypath)
  a=npypath.split('/')[6].split('.')[0]
  dic.update({
	a:build_style_loss(c,d)
   })
  

dict= sorted(dic.iteritems(), key=lambda d:d[1], reverse = True)
for a in dict:
  print a[0],a[1]

  

    
#build_style_loss(c,d)
