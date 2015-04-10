FileName=input("Please input the file that you wish to deal with:\n")

File="C:\Users\lzz0032\Documents\RumbleStrip\Data\Vibration"+FileName+".csv"

Scsv=open(File)

Sdata=[]

for line in Scsv:
    Sdata.append(line.split(','))
    
S3=Sdata[1:]

A1=[]
A2=[]
A3=[]

for data in S3:
     A1.append(float(data[1]))
     A2.append(float(data[2]))
     A3.append(float(data[3]))
    
import matplotlib.pyplot as plt

import numpy as np

x=np.arange(len(A1))

plt.title('The Curve of the Sound'+FileName)
plt.plot(x,A1,'r',x,A2,'b',x,A3,'g')
plt.show()
