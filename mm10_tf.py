# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 09:21:42 2016

@author: Zi
"""

import numpy as np
import os
datafolder = 'C:\\Users\\Zi\\Desktop\\mm10_tf'
Cell='mES'
chrs='chr1'
dtype=[('chr', 'S3'), ('start', '<i4'), ('end', '<i4'), ('value', '<f8')]
Sigs = ['Med1','Med12','Smc1','Smc3']
fold = 20000
database = {}
for s in Sigs:
    desFil = Cell +'_'+s+ '_' +'min0.5.mm10.bedgraph'
    database[s] = open(os.path.join(datafolder, desFil))

for name in Sigs:
    cfile=database[name]
    arrd=np.zeros(195471971/fold,dtype=dtype)
#    arrd=np.zeros(10249,dtype=dtype)
    for line in cfile:
        list1=line.split('\t')
        if (list1[0]==chrs):
            arrd['start'][int(list1[1])/fold]=int(list1[1])/fold
            arrd['end'][int(list1[1])/fold]=int(list1[1])/fold
            arrd['value'][int(list1[1])/fold]=float(list1[3])+arrd['value'][int(list1[1])/fold]
#            print arrd['value'][int(list1[1])/5000]
    arrd['chr']='1' 
    np.save(Cell+'_'+name,arrd)  
#
for s in Sigs:
    desFil = Cell +s+ '_' +'min0.5.mm10.bedgraph'
    database[s].close()