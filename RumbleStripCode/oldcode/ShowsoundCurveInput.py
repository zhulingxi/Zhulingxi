#get all the sound file as 1,2,3,4
FileName=input("Please input the sound Direct that you wish to deal with:\n")

File1=FileName+ "NorthCollegeSmooth20mph.txt"
File2=FileName+ "NorthCollegeSmooth30mph.txt"
File3=FileName+ "NorthCollegeSmooth40mph.txt"
File4=FileName+ "NorthCollegeSmooth50mph.txt"
File5=FileName+ "NorthCollegeSmooth60mph.txt"

Scsv=open(FileName)

Sdata=[]

for line in Scsv:
    Sdata.append(line.split(','))
    
S3=Sdata[7:]

s4=[]

for data in S3:
     s4.append(float(data[2]))
     

import matplotlib.pyplot as plt

import numpy as np

x=np.arange(len(s4))

plt.title('The Curve of the Sound')
plt.plot(x,s4,'b')
plt.show()
