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

sLen1=len(S1)

#deal with the 2 file

Sdata=[]

for line in File2:
    Sdata.append(line.split(','))
    
S=Sdata[1:]

S2=[]

for data in S:
    S2.append(float(data[2]))
    
sLen2=len(S2)

#deal with the 3 file

Sdata=[]

for line in File3:
    Sdata.append(line.split(','))
    
S=Sdata[1:]

S3=[]

for data in S:
    S3.append(float(data[2]))

sLen3=len(S3)
#deal with the 4 file

Sdata=[]

for line in File4:
    Sdata.append(line.split(','))
    
S=Sdata[1:]

S4=[]

for data in S:
    S4.append(float(data[2]))
    
sLen4=len(S4)
    
#deal with the 5 file

Sdata=[]

for line in File5:
    Sdata.append(line.split(','))
    
S=Sdata[1:]

S5=[]

for data in S:
    S5.append(float(data[2]))

sLen5=len(S5)

#deal with the 6 file
Sdata=[]

for line in File6:
    Sdata.append(line.split(','))
    
S=Sdata[1:]

S6=[]

for data in S:
    S6.append(float(data[2]))

sLen6=len(S6)

if sLen1>sLen2:
    smax=sLen1
else:
    smax=sLen2

if smax>sLen3:
    smax=smax
else:
    smax=sLen3

if smax>sLen4:
    smax=smax
else:
    smax=sLen4
    
if smax>sLen5:
    smax=smax
else:
    smax=sLen5
    
if smax>sLen6:
    smax=smax
else:
    smax=sLen6
    
#Do the plot with pylab in one figue   

pl.title('The Curve of the sound in the directory ' +FileDirectory)

#do the sync process,get the max row as the defautlt x
#pading the data of File1

if sLen1<smax:

#if number of ramble strip is large then the smooth
#set the x to s2
#and let the rest data of smooth file to the last data 
    lst=range(smax-sLen1)
    
    while lst:
        S1.append(S1[-1])
        lst=lst[1:]
              
else: 
    
#if the smooth data is more than ramble strip
#then set the number of showdata1 to the same as showdata2 

    S1=S1

    
#do the sync process,get the max row as the defautlt x
#pading the data of File2

if sLen2<smax:

#if number of ramble strip is large then the smooth
#set the x to s2
#and let the rest data of smooth file to the last data 
    lst=range(smax-sLen2)
    
    while lst:
        S2.append(S2[-1])
        lst=lst[1:]
              
else: 
    
#if the smooth data is more than ramble strip
#then set the number of showdata1 to the same as showdata2 

    S2=S2        
  
#do the sync process,get the max row as the defautlt x
#pading the data of File3

if sLen3<smax:

#if number of ramble strip is large then the smooth
#set the x to s2
#and let the rest data of smooth file to the last data 
    lst=range(smax-sLen3)
    
    while lst:
        S3.append(S3[-1])
        lst=lst[1:]
              
else: 
    
#if the smooth data is more than ramble strip
#then set the number of showdata1 to the same as showdata2 

    S3=S3
    
                  

#do the sync process,get the max row as the defautlt x
#pading the data of File4

if sLen4<smax:

#if number of ramble strip is large then the smooth
#set the x to s2
#and let the rest data of smooth file to the last data 
    lst=range(smax-sLen4)
    
    while lst:
        S4.append(S4[-1])
        lst=lst[1:]
              
else: 
    
#if the smooth data is more than ramble strip
#then set the number of showdata1 to the same as showdata2 

    S4=S4
    
                                               
#do the sync process,get the max row as the defautlt x
#pading the data of File5

if sLen5<smax:

#if number of ramble strip is large then the smooth
#set the x to s2
#and let the rest data of smooth file to the last data 
    lst=range(smax-sLen5)
    
    while lst:
        S5.append(S5[-1])
        lst=lst[1:]
              
else: 
    
#if the smooth data is more than ramble strip
#then set the number of showdata1 to the same as showdata2 

    S5=S5
    
#do the sync process,get the max row as the defautlt x
#pading the data of File1

if sLen6<smax:

#if number of ramble strip is large then the smooth
#set the x to s2
#and let the rest data of smooth file to the last data 
    lst=range(smax-sLen6)
    
    while lst:
        S6.append(S6[-1])
        lst=lst[1:]
              
else: 
    
#if the smooth data is more than ramble strip
#then set the number of showdata1 to the same as showdata2 

    S6=S6

x=np.arange(smax)
 
pl.plot(x,S1,'r',x,S2,'g',x,S3,'b',x,S4,'c',x,S5,'y',x,S6,'m')
                                                                                                                                                                                                                                                                    
pl.ylabel('dbA')

pl.show()

#save the figur
SaveFile="E:\AuburnProject\RanmbleStrips\output" +"\SoundInOne"

pl.savefig(SaveFile)
