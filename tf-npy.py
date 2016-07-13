# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 19:36:24 2016

@author: Zi
"""
import numpy as np
import os
datafolder = 'C:\\Users\\Zi\\Desktop\\k562'
Cell='K562'
chro='21'
chrom='chr21'
dtype=[('chr', 'S3'), ('start', '<i4'), ('end', '<i4'), ('value', '<f8')]
Sigs = ['C-Jun']
database = {}
for s in Sigs:
    desFil = Cell + '_' + s + '.narrowPeak'
    database[s] = open(os.path.join(datafolder, desFil))

for name in Sigs:
    cfile=database[name]
    arrd=np.zeros(9624,dtype=dtype)
#    arrd=np.zeros(10249,dtype=dtype)
    for line in cfile:
        list1=line.split('\t')
        if (list1[0]==chrom):
            arrd['start'][int(list1[1])/5000]=int(list1[1])/5000
            arrd['end'][int(list1[1])/5000]=int(list1[1])/5000
            arrd['value'][int(list1[1])/5000]=float(list1[6])+arrd['value'][int(list1[1])/5000]
#            print arrd['value'][int(list1[1])/5000]
    arrd['chr']=chro 
    np.save(Cell+'_'+name,arrd)  
#
for s in Sigs:
    desFil = Cell + '_' + s + '.narrowPeak'
    database[s].close()