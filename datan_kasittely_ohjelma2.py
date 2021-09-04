#!/usr/bin/env python
# -*- coding: utf-8 -*-
#import necessary modules
import pandas as pd
import csv
import re
from pandas import DataFrame

# collecting data from .csv file
dataAlkuperainen = pd.read_csv("Alkuperainen_OY_kaikki.csv", sep=";", encoding="utf8")
#dataAlkuperainen.apply(lambda x: pd.lib.infer_dtype(x.values))
taAlkuperainen = dataRaw.decode('utf8')
# printataan kaikki sarakkeet
#for row in dataAlkuperainen:
    #print(row)

# collecting gsm numebers
puh_raw = dataAlkuperainen['Kontaktin GSM']

# processing data. Setting id and gsm
tmp = {"ID": "0",
        "GSM": "0"}
tmplist = []
for x, y in puh_raw.items():
    Y = str(y)
    Y = Y[3:]
    number = '0'
    Y = number + Y
    #y = '0' + str(y)[3:]
    #tmp[x] = x
    tmp[x] = Y
    tmplist.append(Y)
#print(tmplist)

# collecting data from .csv file
dataMember_last_activated = pd.read_csv("Member_last_activited.csv", sep=";")
#for row2 in dataMember_last_activated:
    #print(row2)

# collecting phone numbers from column 'Phone Number'

puh2_raw = dataMember_last_activated['Phone Number']
tmplist2 = []
tmp2 = {"ID": "0",
        "GSM": "0"}
for z, w in puh2_raw.items():
    W = str(w)
    if(re.match(r'358', W) or re.match(r'\+358', W)):
        num = '0'
        W = W.replace('358', '0')
        W = W.replace('+358', '0')
        tmp2["ID"] = z
        tmp2["GSM"] = W
        tmplist2.append(W)
    else:
        tmplist2.append(W)
        #print(tmplist2)
count = 0
i = 0
for x in tmplist:

  for y in tmplist2:

        if y == x:
            count = count + 1
            print(x + " " + y)
print(count)

# creating data frame and adding dataAlkuperainen to its values. Then saving a csv file.
df = DataFrame(dataAlkuperainen, columns= dataAlkuperainen)
export_csv = df.to_csv (r'/Users/erik.ilonen/Desktop/Projekti_csv_data/test.csv', index = None, header=True) # here you have to write path, where result file will be stored
print (df)
  