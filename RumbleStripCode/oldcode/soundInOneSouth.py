#get all the sound file as 1,2,3,4
FileName=input("Please input the sound Direct that you wish to deal with:\n")

File1=FileName+ "\NorthCollege50mphSouth001.txt"
File2=FileName+ "\NorthCollege50mphSouth002.txt"
File3=FileName+ "\NorthCollege50mphSouth003.txt"
File4=FileName+ "\NorthCollege50mphSouth004.txt"
File5=FileName+ "\NorthCollege50mphSouth005.txt"
File6=FileName+ "\NorthCollege50mphSouth006.txt"

#deal with the first file

Stxt=open(File1)

Sdata=[]

for line in Stxt:
    Sdata.append(line.split(','))
    
S=Sdata[1:]

S1=[]

for data in S:
    S1.append(float(data[2]))

sLen=len(S1)

#deal with the 2 file

Stxt=open(File2)

Sdata=[]

for line in Stxt:
    Sdata.append(line.split(','))
    
S=Sdata[1:]

S2=[]

for data in S:
    S2.append(float(data[2]))
    

#deal with the 3 file

Stxt=open(File3)

Sdata=[]

for line in Stxt:
    Sdata.append(line.split(','))
    
S=Sdata[1:]

S3=[]

for data in S:
    S3.append(float(data[2]))

#deal with the 4 file

Stxt=open(File2)

Sdata=[]

for line in Stxt:
    Sdata.append(line.split(','))
    
S=Sdata[1:]

S4=[]

for data in S:
    S4.append(float(data[2]))
    
    
#deal with the 5 file

Stxt=open(File2)

Sdata=[]

for line in Stxt:
    Sdata.append(line.split(','))
    
S=Sdata[1:]

S5=[]

for data in S:
    S5.append(float(data[2]))


#deal with the 6 file

Stxt=open(File6)

Sdata=[]

for line in Stxt:
    Sdata.append(line.split(','))
    
S=Sdata[1:]

S6=[]

for data in S:
    S6.append(float(data[2]))

#Do the plot with pyplot    
import matplotlib.pyplot as plt

import numpy as np

plt.title('The Curve of the sound ')

ax1=plt.subplot(611)
ax2=plt.subplot(612)
ax3=plt.subplot(613)
ax4=plt.subplot(614)
ax5=plt.subplot(615)
ax6=plt.subplot(616)

#draw the S1 vurve
x1=np.arange(len(S1))
plt.sca(ax1)
plt.plot(x1,S1)
plt.title('The curve of sound south 001')
plt.ylabel('dbA')

#draw the S2 vurve
x2=np.arange(len(S2))
plt.sca(ax2)
plt.plot(x2,S2)
plt.title('The curve of sound south 002')
plt.ylabel('dbA')

#draw the S3 vurve
x3=np.arange(len(S3))
plt.sca(ax3)
plt.plot(x3,S3)
plt.title('The curve of sound south 003')
plt.ylabel('dbA')

#draw the S4 vurve
x4=np.arange(len(S4))
plt.sca(ax4)
plt.plot(x4,S4)
plt.title('The curve of sound south 004')
plt.ylabel('dbA')

#draw the S5 vurve
x5=np.arange(len(S5))
plt.sca(ax5)
plt.plot(x5,S5)
plt.title('The curve of sound south 005')
plt.ylabel('dbA')

#draw the S6 vurve
x6=np.arange(len(S6))
plt.sca(ax6)
plt.plot(x6,S6)
plt.title('The curve of sound south 006')
plt.ylabel('dbA')

plt.show()

#save the figur
SaveFile="C:\Users\lzz0032\Documents\RumbleStrip\stuff" +"\SoundInOnesouth50mph1-3"

plt.savefig(SaveFile)
