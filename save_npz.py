# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 20:38:31 2015

@author: ZI
"""
import numpy as np
chrom=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','X']
contact=np.load('GM12878-MboI-allReps-filtered-5K_c-sparse.npz')
D={}
for i in chrom:
    x=contact[i]['bin1']
    y=contact[i]['bin2']
    IF=contact[i]['IF']
    delta=y-x
    mask1=delta<200
    x_f=x[mask1]
    y_f=y[mask1]
    weit=IF[mask1]
    b=np.bincount(x_f,weights=weit)
    a=np.bincount(y_f,weights=weit)
    di = np.zeros(a.size)
    plus = a + b
    minus = b - a
    mask = (plus != 0) & (minus != 0)
    di[mask] = minus[mask]**3 / (abs(minus[mask]) * plus[mask])
    D[i]=di
np.savez('test_di.npz',**D)

    

    
    
    
        
        
    