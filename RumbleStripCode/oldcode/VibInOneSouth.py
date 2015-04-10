#Show the 6 time of Vibration in one figue
#Get the Vibration Directory

import matplotlib.pyplot as plt

import numpy as np

FileName=input("Please input the Vibration Direct that you wish to deal with:\n")

File1=FileName+ "\NorthCollege50mphNorth001.csv"
File2=FileName+ "\NorthCollege50mphNorth002.csv"
File3=FileName+ "\NorthCollege50mphNorth003.csv"
File4=FileName+ "\NorthCollege50mphNorth004.csv"
File5=FileName+ "\NorthCollege50mphNorth005.csv"
File6=FileName+ "\NorthCollege50mphNorth006.csv"

#Deal with the first file
Scsv=open(File1)

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
    
x=np.arange(len(A1))

plt.title('The Curve of the Vibration'+FileName)

ax1=plt.subplot(331)
ax2=plt.subplot(332)
ax3=plt.subplot(333)

#draw the A1 vurve
plt.sca(ax1)
plt.plot(x,A1)
plt.title('The 1 time of A1')


#draw the A2 vurve
plt.sca(ax2)
plt.plot(x,A2)
plt.title('The 1 time of A2')

#draw the A3 vurve
plt.sca(ax3)
plt.plot(x,A3)
plt.title('The 1 time of A3')


####Deal with the second file
Scsv=open(File2)

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
    
x=np.arange(len(A1))

ax1=plt.subplot(334)
ax2=plt.subplot(335)
ax3=plt.subplot(336)

#draw the A1 vurve
plt.sca(ax1)
plt.plot(x,A1)
plt.title('The 2 time of A1')


#draw the A2 vurve
plt.sca(ax2)
plt.plot(x,A2)
plt.title('The 2 time of A2')

#draw the A3 vurve
plt.sca(ax3)
plt.plot(x,A3)
plt.title('The 2 time of A3')


####Deal with the 3 file
Scsv=open(File2)

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
    
x=np.arange(len(A1))

ax1=plt.subplot(337)
ax2=plt.subplot(338)
ax3=plt.subplot(339)

#draw the A1 vurve
plt.sca(ax1)
plt.plot(x,A1)
plt.title('The 3 time of A1')


#draw the A2 vurve
plt.sca(ax2)
plt.plot(x,A2)
plt.title('The 3 time of A2')

#draw the A3 vurve
plt.sca(ax3)
plt.plot(x,A3)
plt.title('The 3 time of A3')


plt.show()

#save the figur
SaveFile="E:\AuburnProject\RanmbleStrips\stuff" +FileName+"Vib"

#plt.savefig(SaveFile)
