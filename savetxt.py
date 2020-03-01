# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 13:50:34 2020

@author: user
"""
import os
a=os.listdir('D:/yolov3/data/cell_phone/images/')
b=[]
for i in a:
    b.append(os.path.join('D:/yolov3/data/cell_phone/images/', i))
    
with open('data_cell_phone.txt', 'w') as filehandle:
    
    for listitem in b:
        filehandle.write('%s\n' % listitem)
        