#input the sound file only the \ and the file name without the extension
FileName=input("Please input the sound file that you wish to deal with:\n")

SoundFile="C:\Users\lzz0032\Documents\RumbleStrip\Data\sound"+FileName+".txt"

#deal with the sound data
Stxt=open(SoundFile)

Sdata=[]

for line in Stxt:
    Sdata.append(line.split(','))
    
S=Sdata[1:]

S1=[]

for data in S:
    S1.append(float(data[2]))

        
#Do the plot with pyplot    
import pylab as pl

import numpy as np

x=np.arange(len(S1))

pl.title('The Curve of the Sound'+FileName)

#Draw the sound curve
pl.plot(x,S1)
pl.title('The curve of sound')
pl.ylabel('dbA')


pl.show()
