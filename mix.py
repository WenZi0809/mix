# -*- coding: utf-8 -*-
"""
Created on Thu May 05 16:20:27 2016

@author: Zi
"""

import os
datafolder = 'C:\\Users\\Zi\\Desktop\\mouse\\peaks'
Cell='mES'
chrs='chr1'
Sigs = ['CapD3','Med1','Med12','CTCF']
database = {}
outbase = {}
for s in Sigs:    
    desFil = 'mES_'+s+'_mm10-macs-sort.bed'    
    database[s] = open(os.path.join(datafolder, desFil))
for s in Sigs:    
    desFil = 'mES_'+s+'_meme-input.bed'    
    outbase[s] = open(os.path.join(datafolder, desFil),'w')
for name in Sigs:    
    cfile=database[name]    
    ofile=outbase[name]    
    for line in cfile:        
        list1=line.split('\t')        
        mid=(int(list1[1])+int(list1[2]))/2        
        start=str(mid-100)        
        end=str(mid+100)        
        ofile.write(list1[0]+'\t'+start+'\t'+end+'\t')    
    cfile.close()    
    ofile.close()    
    
import numpy as np
import os
datafolder = 'C:\\Users\\Zi\\Desktop\\human\\gm12878\\peak'
Cell='Gm12878'
chrs='chr1'
dtype=[('chr', 'S3'), ('start', '<i4'), ('end', '<i4'), ('value', '<f8')]
#Sigs = ['Ctcf','Cmyc','Max','Mxi1','Rad21','Sp1','Yy1','Znf143']
Sigs = ['H3k4me1','H3k4me3']
fold = 1000
database = {}
for s in Sigs:    
    desFil = Cell +s+'.bed'    
    database[s] = open(os.path.join(datafolder, desFil))
for name in Sigs:    
    cfile=database[name]    
    arrd=np.zeros(249250621/fold,dtype=dtype)
    #    arrd=np.zeros(10249,dtype=dtype)    
    for line in cfile:        
        list1=line.split('\t')        
        if (list1[0]==chrs):            
            arrd['start'][int(list1[1])/fold]=int(list1[1])/fold            
            arrd['end'][int(list1[1])/fold]=int(list1[1])/fold            
            arrd['value'][int(list1[1])/fold]=float(list1[6])+arrd['value'][int(list1[1])/fold]
            #            print arrd['value'][int(list1[1])/5000]    
            arrd['chr']='1'     
            np.save(Cell+'_'+name,arrd)  
for s in Sigs:    
    desFil = Cell +s+'.bed'    
    database[s].close()
    
    
    
import numpy as np
import os
datafolder = 'C:\\Users\\Zi\\Desktop'
Cell='Gm12878'
chrs='chr1'
dtype=[('chr', 'S3'), ('start', '<i4'), ('end', '<i4'), ('value', '<f8')]
Sigs = ['CTCF']
fold = 1000
database = {}
for s in Sigs:    
    desFil = s+ '.txt'    
    database[s] = open(os.path.join(datafolder, 'gm12878__CTCFBindingsite.txt'))
    for name in Sigs:    
        cfile=database[name]    
        arrd=np.zeros(249250621/fold,dtype=dtype)    
        arrd1=np.zeros(249250621/fold,dtype=dtype)
        #    arrd=np.zeros(10249,dtype=dtype)    
        for line in cfile:        
            list1=line.split('\t')        
            if (list1[1]==chrs and list1[4]=='+' and float(list1[5])>16.2298):            
                arrd['start'][int(list1[2])/fold]=int(list1[2])/fold            
                arrd['end'][int(list1[2])/fold]=int(list1[2])/fold            
                arrd['value'][int(list1[2])/fold]=1+arrd['value'][int(list1[2])/fold]
            if (list1[1]==chrs and list1[4]=='-' and float(list1[5])>16.2298):
                arrd1['start'][int(list1[2])/fold]=int(list1[2])/fold            
                arrd1['end'][int(list1[2])/fold]=int(list1[2])/fold            
                arrd1['value'][int(list1[2])/fold]=1+arrd1['value'][int(list1[2])/fold]
#            print arrd['value'][int(list1[1])/5000]    
        arrd['chr']='1'     
        np.save(Cell+'_'+name+'_motif-',arrd)   
        arrd1['chr']='1'     
        np.save(Cell+'_'+name+'_motif+',arrd1)    #
for s in Sigs:   
    desFil = s+ '.txt'    
    database[s].close()     
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    