VibDataFile=open("E:\AuburnProject\RanmbleStrips\ViabData.csv")

import pandas 

VibDataShow=pandas.read_csv("E:\AuburnProject\RanmbleStrips\VibData.csv")

VibDataShow.plot(y='A1(g)')
VibDataShow.plot(y='A2(g)')
VibDataShow.plot(y='A3(g)')
