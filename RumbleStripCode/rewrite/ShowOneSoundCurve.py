#deal with one sound file as *.txt and show the curve of the data
#The input of this process is a Filename
#the process use as directory as default

#import the pakage

import pylab as pl

#give the directory that the sound file should be
FileDirectory="C:\Users\lzz0032\Documents\RumbleStrip\SortedData0319\All Data Display"

#let user input the file name that need to proceed
#while input the filename,it should be started with "\" and with out the extingction

FileName=input("Please input the sound file that you want to see the curve:\n")

#open the file
File=open(FileDirectory + FileName +".txt")


sdata=[]
#get every data form the file

for line in File:
    sdata.append(line.split(","))

#delete the first line,because it is not the data
sdata=sdata[1:]

ShowData=[]

#get the sound data value from the 3rd column
for data in sdata:
    ShowData.append(float(data[2]))
    
#give the figue a title
pl.title("The curve of the sound:  "+ FileName[1:])

#plot the data
pl.plot(ShowData)

#show the figue
pl.show()

#give the saved figue file name
FileSave="C:\Users\lzz0032\Documents\RumbleStrip\output" + FileName +".png"

#save the figue
pl.savefig(FileSave)
