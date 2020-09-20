
import os
import shutil
import random
import glob
import numpy as np
import re

os.chdir('/Volumes/Data/ML_Datasets/dogs-vs-cats/xtest')
c =0
d =0
for i in os.listdir():
    if re.match('cat',i):
        c +=1
for i in os.listdir():
    if re.match('dog',i):
        d +=1    
print(d,c)

if os.path.isdir('dog') is False:
    os.makedirs('train/dog')
    os.makedirs('train/cat')
    os.makedirs('test/dog')
    os.makedirs('test/cat')
    os.makedirs('val/dog')
    os.makedirs('val/cat')
    
    for i in random.sample(glob.glob('cat*'),round(c*0.6)):
        shutil.move(i, 'train/cat')      
    for i in  random.sample(glob.glob('dog*'),round(d*0.6)):
        shutil.move(i, 'train/dog')
    for i in random.sample(glob.glob('cat*'),round(c*0.2)):
        shutil.move(i, 'val/cat')      
    for i in  random.sample(glob.glob('dog*'),round(d*0.2)):
        shutil.move(i, 'val/dog')
    for i in glob.glob('cat*'):
        shutil.move(i,'test/cat')
    for i in glob.glob('dog*'):
        shutil.move(i,'test/dog')
        
   
