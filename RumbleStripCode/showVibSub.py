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

plt.title('The Curve of the Vibration'+FileName)

ax1=plt.subplot(311)
ax2=plt.subplot(312)
ax3=plt.subplot(313)

#draw the A1 vurve
plt.sca(ax1)
plt.plot(x,A1)
plt.title('The A1')


#draw the A2 vurve
plt.sca(ax2)
plt.plot(x,A2)
plt.title('The A2')

#draw the A3 vurve
plt.sca(ax3)
plt.plot(x,A3)
plt.title('The A3')

plt.show()
