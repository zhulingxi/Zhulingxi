#show all the sound file in the same directory

import numpy as np
import pylab as pl
import os

#let user input the directory that the sound file should be
FileDirectory=input("Input the directory you want to do:  \n")

#get the file list of the given directory
FileList=[]

#get the file names from the directory

FileNames=os.listdir(FileDirectory)

#Get the Fullname of the File use the os.path.join

for fn in FileNames:
    FullFileName=os.path.join(FileDirectory,fn)
    FileList.append(FullFileName)
    
    
#open all the File in the File list
#need to impove

#open the 1 file
File1=open(FileList[0])

##open the 2 file
File2=open(FileList[1])


##open the 3 file
File3=open(FileList[2])

##open the 4 file
File4=open(FileList[3])   

##open the 5 file
File5=open(FileList[4])

##open the 6 file
File6=open(FileList[5])

#process the sound data

#deal with the first file

Sdata=[]

for line in File1:
    Sdata.append(line.split(','))
    
S=Sdata[1:]

S1=[]

for data in S:
    S1.append(float(data[2]))

sLen=len(S1)

#deal with the 2 file

Sdata=[]

for line in File2:
    Sdata.append(line.split(','))
    
S=Sdata[1:]

S2=[]

for data in S:
    S2.append(float(data[2]))
    

#deal with the 3 file

Sdata=[]

for line in File3:
    Sdata.append(line.split(','))
    
S=Sdata[1:]

S3=[]

for data in S:
    S3.append(float(data[2]))

#deal with the 4 file

Sdata=[]

for line in File4:
    Sdata.append(line.split(','))
    
S=Sdata[1:]

S4=[]

for data in S:
    S4.append(float(data[2]))
    
    
#deal with the 5 file

Sdata=[]

for line in File5:
    Sdata.append(line.split(','))
    
S=Sdata[1:]

S5=[]

for data in S:
    S5.append(float(data[2]))


#deal with the 6 file
Sdata=[]

for line in File6:
    Sdata.append(line.split(','))
    
S=Sdata[1:]

S6=[]

for data in S:
    S6.append(float(data[2]))

#Do the plot with pyplot    
import matplotlib.pyplot as plt

import numpy as np

plt.title('The Curve of the sound in the directory of '+ FileDirectory)

ax1=plt.subplot(321)
ax2=plt.subplot(322)
ax3=plt.subplot(323)
ax4=plt.subplot(324)
ax5=plt.subplot(325)
ax6=plt.subplot(326)

#draw the S1 vurve
x1=np.arange(len(S1))
plt.sca(ax1)
plt.plot(x1,S1)
plt.title('Curve file:'+ FileList[0])
plt.ylabel('dbA')

#draw the S2 vurve
x2=np.arange(len(S2))
plt.sca(ax2)
plt.plot(x2,S2)
plt.title('Curve file:'+ FileList[1])
plt.ylabel('dbA')

#draw the S3 vurve
x3=np.arange(len(S3))
plt.sca(ax3)
plt.plot(x3,S3)
plt.title('Curve file:'+ FileList[2])
plt.ylabel('dbA')

#draw the S4 vurve
x4=np.arange(len(S4))
plt.sca(ax4)
plt.plot(x4,S4)
plt.title('Curve file:'+ FileList[3])
plt.ylabel('dbA')

#draw the S5 vurve
x5=np.arange(len(S5))
plt.sca(ax5)
plt.plot(x5,S5)
plt.title('Curve file:'+ FileList[4])
plt.ylabel('dbA')

#draw the S6 vurve
x6=np.arange(len(S6))
plt.sca(ax6)
plt.plot(x6,S6)
plt.title('Curve file:'+ FileList[5])
plt.ylabel('dbA')

plt.show()

#save the figur
SFile=FileList[0]
SFile=SFile[:-7]
SFile=SFile+'.png'

SaveFile=SFile

plt.savefig(SaveFile)
