#show two sound file in one figue,it has two file input
#one file is the smooth sound file
#the other file is the ramble strip file

import pylab as pl
import numpy as np

#give the directory that the sound file should be
FileDirectory="C:\Users\lzz0032\Documents\RumbleStrip\SortedData0319\All Data Display"

#let user input the file name that need to proceed
#while input the filename,it should be started with "\" and with out the extingction

#get the first file

FileName1=input('please input the smooth sound file name:   \n')

#get the second file

FileName2=input('Please input the ramble strip sound file:   \n')

#read the smooth sound file

File1=open(FileDirectory+FileName1+'.txt')

#read the ranble strip sound file

File2=open(FileDirectory +FileName2+'.txt')


#get the data from the smooth sound file

sdata=[]

for line in File1:
    sdata.append(line.split(','))
    
#delete the first line,because it has no data    
sdata=sdata[1:]

#get the sound data from the sdata

showData1=[]

#get the 3rd column data from sdata
for data in sdata:
    showData1.append(float(data[2]))
    
#get the rows of the first data
s1=len(showData1)

#get the data form the ramble strip sound file
#set sdata to empty

#Then do the same thing as deal with the fisrt file
sdata=[]

for line in File2:
    sdata.append(line.split(','))
    
sdata=sdata[1:]

showData2=[]

for data in sdata:
    showData2.append(float(data[2]))
    
#get the rows of the second file

s2=len(showData2)

#set the plot number of x to rumble strip files's number

#set the x to plot

x=0

if s2>s1:

#if number of ramble strip is large then the smooth
#set the x to s2
#and let the rest data of smooth file to the last data 
    lst=range(s2-s1)
    
    while lst:
        showData1.append(showData1[-1])
        lst=lst[1:]
              
else: 
    
#if the smooth data is more than ramble strip
#then set the number of showdata1 to the same as showdata2 

    showData1=showData1[:s2]


#set the x=the length of rumble strip
x=np.arange(s2)

    
#plot the two curve in one figue
pl.title("The compare between " +FileName1[1:] +'and '+ FileName2[1:])

#draw the smooth sound curve with the blue line
#draw the ramble strip curve with the red line
pl.plot(x,showData1,'b',x,showData2,'r')

pl.show()

#give the directory of the output file
FileSave="C:\Users\lzz0032\Documents\RumbleStrip\output" + FileName1+"Vs"+FileName2[1:]+".png"

pl.savefig(FileSave)

