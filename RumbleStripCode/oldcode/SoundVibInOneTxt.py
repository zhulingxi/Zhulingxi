#input the vib file only the \ and the file name without the extension
FileName=input("Please input the vibration file that you wish to deal with:\n")

VibFile="E:\AuburnProject\RanmbleStrips\ICUData\Smoth147\Vibration"+FileName+".csv"

#input the sound file only the \ and the file name without the extension
FileName=input("Please input the sound file that you wish to deal with:\n")

SoundFile="E:\AuburnProject\RanmbleStrips\ICUData\Smoth147\sound"+FileName+".txt"

#deal with the Vibration data
Vcsv=open(VibFile)

Vdata=[]

for line in Vcsv:
    Vdata.append(line.split(','))
    
V=Vdata[1:]

A1=[]
A2=[]
A3=[]

for data in V:
     A1.append(float(data[1]))
     A2.append(float(data[2]))
     A3.append(float(data[3]))

#deal with the sound data
Stxt=open(SoundFile)

Sdata=[]

for line in Stxt:
    Sdata.append(line.split(','))
    
S=Sdata[1:]

S1=[]

for data in S:
    S1.append(float(data[2]))

        
#Do the plot with pyplot    
import matplotlib.pyplot as plt

import numpy as np

x=np.arange(len(A1))
y=np.arange(len(S1))

plt.title('The Curve of the Vibration'+FileName)

ax1=plt.subplot(411)
ax2=plt.subplot(412)
ax3=plt.subplot(413)
ax4=plt.subplot(414)

#draw the A1 vurve
plt.sca(ax1)
plt.plot(x,A1)
plt.title('The curve of A1')
plt.ylabel('g')

#draw the A2 vurve
plt.sca(ax2)
plt.plot(x,A2)
plt.title('The curve of A2')
plt.ylabel('g')

#draw the A3 vurve
plt.sca(ax3)
plt.plot(x,A3)
plt.title('The curve of A3')
plt.ylabel('g')

#Draw the sound curve
plt.sca(ax4)
plt.plot(y,S1)
plt.title('The curve of sound')
plt.ylabel('dbA')

plt.show()

#save the figur
SaveFile="E:\AuburnProject\RanmbleStrips\stuff" +FileName+"VibSound"

plt.savefig(SaveFile)
