# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 16:01:31 2016

@author: Zi
"""

import os
from collections import Counter
datafolder = 'C:\\Users\\Zi\\Desktop\\motif_alone'
file1=open(os.path.join(datafolder, 'closest-ctcf_spi1.txt'))
dis=[]
for line in file1:
    lists=line.split('\t')
    distance=abs(int(lists[1])-int(lists[4]))
    if distance <= 1000:
       dis.append(str(distance))
c=Counter(dis)
t=0
for i in range(1001):
    t=c[str(i)]+t  
    if i%50==0:
        print i,t
        t=0