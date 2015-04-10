#Fcvs=open("E:\AuburnProject\RanmbleStrips\ICUData\V5.csv")

FileName=input("Please input the file that you wish to deal with:\n")

FileName="E:\AuburnProject\RanmbleStrips\ICUData\Smoth147\Vibration"+ FileName+".csv"

Fcvs=open(FileName)

sdata=[]

for line in Fcvs:
    sdata.append(line.split(','))

sdata=sdata[1:]

S1=[]
S2=[]
S3=[]

for data in sdata:
    S1.append(float(data[1]))
    S2.append(float(data[2]))
    S3.append(float(data[3]))


import numpy as np

x=np.arange(len(S1))

import pylab as pl

from mpl_toolkits.mplot3d import Axes3D

fig = pl.figure()

ax = Axes3D(fig)

ax.plot(x, S1, 0)

#pl.plot(x,S1,'r',x,S2,'b',x,S3,'y')

pl.show()


