# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 09:54:59 2020

@author: Bruger
"""

import pandas as pd
import matplotlib.pyplot as plt

dfLog = pd.read_csv("C:\\Users\\Bruger\\Desktop\\books\\THESIS start aug 3\\datasets\\LOGS.csv",delimiter=';')
dfLog.drop_duplicates(subset=['FILE_NAME','VERSION'],keep='last',inplace=True)

filenames = list(dfLog['FILE_NAME'])
version = list(dfLog['VERSION'])

for index,f in enumerate(filenames) :
    v=version[index]
    dfFile = dfLog[(dfLog['FILE_NAME'] == f)][['VARIABLES','TIME']]
    x=dfFile['VARIABLES']
    y=dfFile['TIME']
    plt.plot(x,y)
    plt.xlabel('TIME')
    plt.ylabel('SPACE')
    plt.title(f+' '+str(v))
    plt.show()