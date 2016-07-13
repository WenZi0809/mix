# -*- coding: utf-8 -*-
"""
Created on Fri May 20 10:36:39 2016

@author: Zi
"""
import numpy as np
import os
Bindata=np.load('C:\\Users\\Zi\\Desktop\\gm12878\\npz\\ctcf-bind.npz')
Unbindata=np.load('C:\\Users\\Zi\\Desktop\\gm12878\\npz\\ctcf-unbind.npz')
Sigs=['Cmyc','Cux1','Hcfc1','Max','Mxi1','Sp1','Spl1','Srf','Tbp','Yy1','Znf143','Znf384']
chrs=['chr1','chr2','chr3','chr4','chr5','chr6','chr7','chr8','chr9','chr10','chr11','chr12','chr13','chr14','chr15','chr16','chr17','chr18','chr19','chr20','chr21','chr22','chrX']
datafold='C:\\Users\\Zi\\Desktop\\gm12878'
wind=1000
bindbase={}
for c in chrs:
    Bindchr=Bindata[c]
    sigdatabase=np.zeros([len(Bindchr),len(Sigs)+1],int)
    for x in range(len(Bindchr)):
        sigdatabase[x][0]=1
    for n in range(len(Sigs)):
        sigchr=[]
        desFil = 'Gm12878'+Sigs[n]+'.narrowpeak'   
        filein = open(os.path.join(datafold, desFil))
        for line in filein:
            lists=line.split('\t')
            if lists[0]==c:
                sigchr.append(lists[1:3])
        for j in range(len(Bindchr)):
            for i in sigchr:
                if Bindchr[j]>=((int(i[0])+int(i[1]))/2-wind) and Bindchr[j]<=((int(i[0])+int(i[1]))/2+wind):
                     sigdatabase[j][n+1]=1                    
    bindbase[c]=sigdatabase
    
ubindbase={}
for c in chrs:
    Bindchr=Unbindata[c]
    sigdatabase=np.zeros([len(Bindchr),len(Sigs)+1],int)
    for x in range(len(Bindchr)):
        sigdatabase[x][0]=0
    for n in range(len(Sigs)):
        sigchr=[]
        desFil = 'Gm12878'+Sigs[n]+'.narrowpeak'   
        filein = open(os.path.join(datafold, desFil))
        for line in filein:
            lists=line.split('\t')
            if lists[0]==c:
                sigchr.append(lists[1:3])
        for j in range(len(Bindchr)):
            for i in sigchr:
                if Bindchr[j]>=((int(i[0])+int(i[1]))/2-wind) and Bindchr[j]<=((int(i[0])+int(i[1]))/2+wind):
                     sigdatabase[j][n+1]=1                    
    ubindbase[c]=sigdatabase 