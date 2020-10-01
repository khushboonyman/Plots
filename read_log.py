# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 09:54:59 2020

@author: Bruger
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

location_v2 = "C:\\Users\\Bruger\\source\\repos\\CompressionV2\\CompressionV2\\a.exe"
location_v3 = "C:\\Users\\Bruger\\source\\repos\\CompressionV3\\a.exe"

os.system(location_v2)
os.system(location_v3)

dfLog = pd.read_csv("C:\\Users\\Bruger\\Desktop\\books\\THESIS start aug 3\\datasets\\LOGS.csv",delimiter=';')
dfLog.drop_duplicates(subset=['FILE_NAME','VERSION'],keep='last',inplace=True)

filenames = list(set(dfLog['FILE_NAME']))
version = list(set(dfLog['VERSION']))

for index,f in enumerate(filenames) :
    v=version[index]
    dfFile = dfLog[(dfLog['FILE_NAME'] == f)][['MEMORY','TIME']]
    x=dfFile['MEMORY']
    y=dfFile['TIME']
    plt.plot(x, y, 'go--', linewidth=2, markersize=12)
    plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    labelbottom=False) # labels along the bottom edge are off
    plt.xlabel('TIME')
    plt.ylabel('MEMORY')
    plt.title(f+' '+str(v))
    plt.show()
    
    
