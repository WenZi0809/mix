# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 10:22:29 2016

@author: Zi
"""

import os
datafolder = 'C:\\Users\\Zi\\Desktop\\recent\\Gm12878'
chrs=['chr1','chr2','chr3','chr4','chr5','chr6','chr7','chr8','chr9','chr10','chr11','chr12','chr13','chr14','chr15','chr16','chr17','chr18','chr19','chr20','chr21','chr22','chrX']
sigs=['Yy1','Spl1','Znf143','Cux1']
fileout={}
for s in sigs:    
    outfile='co_'+s+'_narrowpeakstrong.txt'    
    fileout[s]=open(outfile,'w')
for chorm in chrs:    
    file1=open(os.path.join(datafolder, 'Gm12878Ctcf.narrowPeak'))
    ctcf_bind=[] 
    for line in file1:             
            lists1=line.split('\t')             
            if lists1[0]==chorm and int(lists1[4])>=399:                               
                ctcf_bind.append([lists1[1],lists1[2]])
    for s in sigs:        
        desfile='Gm12878'+s+'.narrowPeak'                     
        file2=open(os.path.join(datafolder, desfile))                                             
        for line in file2:             
            lists2=line.split('\t')             
            if lists2[0]==chorm  and int(lists2[4])>=399:                                  
                for x in ctcf_bind:                    
                    if (int(x[0])>=int(lists2[1]) and int(x[0])<int(lists2[2])) or (int(x[1])>=int(lists2[1]) and int(x[1])<int(lists2[2])):   
                        Maxs=max(int(x[0]),int(x[1]),int(lists2[1]),int(lists2[2]))
                        Mins=min(int(x[0]),int(x[1]),int(lists2[1]),int(lists2[2]))
                        fileout[s].write(chorm+'\t'+str(Mins)+'\t'+str(Maxs)+'\n')
                        break
        file1.close()       
        file2.close()
for s in sigs:    
    fileout[s].close() 