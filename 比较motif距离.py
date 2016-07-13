# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 15:05:15 2016

@author: Zi
"""

import os
from collections import Counter
datafolder = 'C:\\Users\\Zi\\Desktop\\co_motif'
finleout3=open('Resoult.txt','w')
chrs=['chr1','chr2','chr3','chr4','chr5','chr6','chr7','chr8','chr9','chr10','chr11','chr12','chr13','chr14','chr15','chr16','chr17','chr18','chr19','chr20','chr21','chr22','chrX']
sigs=['Cux1','Yy1','Spl1','Znf143']
resoult={}
for s in sigs:
   resoult[s]=[]
for chorm in chrs:
    for s in sigs:
        desfile1='co_'+s+'_motif.txt'
        desfile2='co_'+s+'_peak.txt'
        file1=open(os.path.join(datafolder, desfile1))
        file2=open(os.path.join(datafolder, desfile2))
        file1_mid=[]
        for line in file1:
            lists1=line.split('\t')
            if lists1[0]==chorm:
                mid=(int(lists1[1])+int(lists1[2]))/2
                dis=abs(int(lists1[1])-int(lists1[2]))
                file1_mid.append([mid,dis])
        for line in file2:
            lists2=line.split('\t')
            if lists2[0]==chorm:
               x=int(lists2[1])
               y=int(lists2[2])
               if x>y:
                 lists2[1]=str(y)
                 lists2[2]=str(x)
                 for motif in file1_mid:
                    if motif[0]<(int(lists2[2])+150) and motif[0]>(int(lists2[1])-150):
                       finleout3.write(chorm+'\t'+lists2[1]+'\t'+lists2[2]+'\n')
                       resoult[s].append(motif[1])
                       break
        file1.close()
        file2.close()
Counter(resoult[s])
finleout3.close()