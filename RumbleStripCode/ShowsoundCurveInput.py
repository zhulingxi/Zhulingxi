FileName=input("Please input the file that you wish to deal with:\n")

FileName="C:\Users\lzz0032\Documents\RumbleStrip"+ FileName+".csv"

Scsv=open(FileName)

Sdata=[]

for line in Scsv:
    Sdata.append(line.split(','))
    
S3=Sdata[7:]

s4=[]

for data in S3:
     s4.append(float(data[2]))
     

import matplotlib.pyplot as plt

import numpy as np

x=np.arange(len(s4))

plt.title('The Curve of the Sound')
plt.plot(x,s4,'b')
plt.show()
