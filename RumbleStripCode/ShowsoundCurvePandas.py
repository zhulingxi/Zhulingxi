FileName=input("Please input the file that you wish to deal with:\n")

import pandas

ShowData=pandas.read_csv(FileName,index_col=0,parse_dates=True)

ShowData.plot(y='Value')
