#get all the sound file as 1,2,3,4
FileName=input("Please input the sound Direct that you wish to deal with:\n")

File1=FileName+ "\NorthCollegeSmooth20mph.txt"
File2=FileName+ "\NorthCollegeSmooth30mph.txt"
File3=FileName+ "\NorthCollegeSmooth40mph.txt"
File4=FileName+ "\NorthCollegeSmooth50mph.txt"
File5=FileName+ "\NorthCollegeSmooth60mph.txt"

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



#Do the plot with pyplot    
import matplotlib.pyplot as plt

import numpy as np

plt.title('The Curve of the sound ')

ax1=plt.subplot(511)
ax2=plt.subplot(512)
ax3=plt.subplot(513)
ax4=plt.subplot(514)
ax5=plt.subplot(515)

#draw the S1 vurve
x1=np.arange(len(S1))
plt.sca(ax1)
plt.plot(x1,S1)
plt.title('The curve of sound 20mph')
plt.ylabel('dbA')

#draw the S2 vurve
x2=np.arange(len(S2))
plt.sca(ax2)
plt.plot(x2,S2)
plt.title('The curve of sound 30mph')
plt.ylabel('dbA')

#draw the S3 vurve
x3=np.arange(len(S3))
plt.sca(ax3)
plt.plot(x3,S3)
plt.title('The curve of sound 40mph')
plt.ylabel('dbA')

#draw the S4 vurve
x4=np.arange(len(S4))
plt.sca(ax4)
plt.plot(x4,S4)
plt.title('The curve of sound 50mph')
plt.ylabel('dbA')

#draw the S5 vurve
x5=np.arange(len(S5))
plt.sca(ax5)
plt.plot(x5,S5)
plt.title('The curve of sound 60mph')
plt.ylabel('dbA')
plt.show()

#save the figur
SaveFile="E:\AuburnProject\RanmbleStrips\stuff" +"\SoundInOne"

plt.savefig(SaveFile)
