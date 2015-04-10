#Show the Vibration curve in one figue
#input is one Vibration file

import numpy as np
import pylab as pl

#give the directory that the vibration file should be
FileDirectory="C:\Users\lzz0032\Documents\RumbleStrip\SortedData0319\All Data Display"

#let user input the file name that need to proceed
#while input the filename,it should be started with "\" and with out the extingction

#get the first file

FileName=input('please input the Vibration file name:   \n')

#open the Vibration file

File=open(FileDirectory+FileName+'.csv')

#read the data from the file that opened

sdata=[]

for line in File:
    sdata.append(line.split(','))
    
#delete the first row of the data
sdata=sdata[1:]

#give the definition of A1,A2,A3 for the three Vibration
A1=[]
A2=[]
A3=[]

#get the data from sdata,ffrom the column 2,3,4

for data in sdata:
    A1.append(float(data[1]))
    A2.append(float(data[2]))
    A3.append(float(data[3]))
    
x=np.arange(len(A1))

pl.title("The Vibration curve of "+FileName)

pl.plot(x,A1,'b',x,A2,'g',x,A3,'r')

pl.show()

#give the directory of the output file
FileSave="C:\Users\lzz0032\Documents\RumbleStrip\output" + FileName+".png"

pl.savefig(FileSave)  