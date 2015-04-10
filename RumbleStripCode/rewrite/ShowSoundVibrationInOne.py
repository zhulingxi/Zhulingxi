#input the vib file only the \ and the file name without the extension
VibFileName=input("Please input the vibration file that you wish to deal with:\n")

VibFile="C:\Users\lzz0032\Documents\RumbleStrip\SortedData0319\All Data Display"+VibFileName+".csv"

#input the sound file only the \ and the file name without the extension
soundFileName=input("Please input the sound file that you wish to deal with:\n")

SoundFile="C:\Users\lzz0032\Documents\RumbleStrip\SortedData0319\All Data Display"+soundFileName+".csv"

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
Scsv=open(SoundFile)

Sdata=[]

for line in Scsv:
    Sdata.append(line.split(','))
    
S=Sdata[7:]

S1=[]

for data in S:
    S1.append(float(data[2]))

        
#Do the plot with pyplot    
import matplotlib.pyplot as plt

import numpy as np

x=np.arange(len(A1))
y=np.arange(len(S1))

plt.title('The Curve of the Vibration in'+VibFileName[1:]+ " and the curve of the sound in "+soundFileName[1:])

ax1=plt.subplot(411)
ax2=plt.subplot(412)
ax3=plt.subplot(413)
ax4=plt.subplot(414)

#draw the A1 vurve
plt.sca(ax1)
plt.plot(x,A1)
plt.title('The curve of A1 in the file '+VibFileName[1:])
plt.ylabel('g')

#draw the A2 vurve
plt.sca(ax2)
plt.plot(x,A2)
plt.title('The curve of A2 in the file '+VibFileName[1:])
plt.ylabel('g')

#draw the A3 vurve
plt.sca(ax3)
plt.plot(x,A3)
plt.title('The curve of A3 int the file '+VibFileName[1:])
plt.ylabel('g')

#Draw the sound curve
plt.sca(ax4)
plt.plot(y,S1)
plt.title('The curve of sound')
plt.ylabel('dbA')

plt.show()

#give the direvtory for the file to output
FilePath="C:\Users\lzz0032\Documents\RumbleStrip\output"

#Give the File name of the figue
SaveFile=FilePath + VibFileName +'_Curve of Vibration and sound'

plt.savefig(SaveFile)
