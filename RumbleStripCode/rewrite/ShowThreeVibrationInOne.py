#Show the 3 time of Vibration in one figue
#Get the Vibration Directory

import matplotlib.pyplot as plt

import numpy as np

#give the directory that the vibration file should be
FileDirectory="C:\Users\lzz0032\Documents\RumbleStrip\SortedData0319\All Data Display"

#let the user iniput the 3 file for vibration
FileName1=input('please input the firt Vibration file name:   \n')

File1=FileDirectory + FileName1+ ".csv"

FileName2=input('please input the sencond Vibration file name:   \n')

File2=FileDirectory + FileName2+ ".csv"

FileName3=input('please input the third Vibration file name:   \n')

File3=FileDirectory + FileName3+ ".csv"

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

plt.title('The Curve of the Vibration in '+FileName1[1:]+ "and "+FileName2[1:]+"and "+FileName3[1:])

ax1=plt.subplot(331)
ax2=plt.subplot(332)
ax3=plt.subplot(333)

#draw the A1 vurve
plt.sca(ax1)
plt.plot(x,A1)
plt.title('The curve of A1 in '+FileName1[1:])


#draw the A2 vurve
plt.sca(ax2)
plt.plot(x,A2)
plt.title('The curve of A2 in '+FileName1[1:])

#draw the A3 vurve
plt.sca(ax3)
plt.plot(x,A3)
plt.title('The curve of A3 in '+FileName1[1:])


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
plt.title('The curve of A1 in '+FileName2[1:])


#draw the A2 vurve
plt.sca(ax2)
plt.plot(x,A2)
plt.title('The curve of A2 in '+FileName2[1:])

#draw the A3 vurve
plt.sca(ax3)
plt.plot(x,A3)
plt.title('The curve of A3 in '+FileName2[1:])


####Deal with the 3 file
Scsv=open(File3)

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
plt.title('The curve of A1 in '+FileName3[1:])


#draw the A2 vurve
plt.sca(ax2)
plt.plot(x,A2)
plt.title('The curve of A2 in '+FileName3[1:])

#draw the A3 vurve
plt.sca(ax3)
plt.plot(x,A3)
plt.title('The curve of A3 in '+FileName3[1:])


plt.show()

#save the figur
SaveFile="C:\Users\lzz0032\Documents\RumbleStrip\output" +FileName1+"Vs" +FileName2[1:]+"Vs"+FileName3[1:]+"_Vib.png"

plt.savefig(SaveFile)
