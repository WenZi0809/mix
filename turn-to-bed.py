# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 10:04:03 2016

@author: Zi
"""

import os
datafolder = 'C:\\Users\\Zi\\Desktop\\Gm12878'
sigs=['Ctcf','Cux1','Yy1','Znf143','Spl1']
fileout={}
for s in sigs:    
    outfile=s+'.bed'    
    fileout[s]=open(outfile,'w')
for s in sigs:
    desfile='Gm12878'+s+'.narrowPeak'                     
    file2=open(os.path.join(datafolder, desfile))
    for line in file2:
        lists=line.split('\t')
        if int(lists[6])>=250.9:
           fileout[s].write(lists[0]+'\t'+lists[1]+'\t'+lists[2]+'\n')
    file2.close()
        
for s in sigs:
    fileout[s].close()