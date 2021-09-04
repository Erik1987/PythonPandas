#import necessary modules
import pandas as pd
import csv
import re
from pandas import DataFrame

# Collecting data from .csv
dataAlkuperainen = pd.read_csv("./DailyRunup-ClientAccount_000107272021_1.csv", 
sep=";", dtype={"ACCOUNTNUMBER": str}, encoding='ISO-8859-1', engine = 'python')

# collecting
accountNum = dataAlkuperainen['ACCOUNTNUMBER']

# Collecting data from .csv
dataAlkuperainen2 = pd.read_csv("./Member last activited.csv", 
sep=";", dtype={"Account Number": str, "Phone Number": str}, encoding='ISO-8859-1', engine = 'python')

accountNum2 = dataAlkuperainen2['Account Number']
"""
idx = 0
count = 0

for x in accountNum.items():
    for y in accountNum2.items():
        if(x[1] == y[1]):
            count += 1
    idx += 1
print(count)
"""  
puh_raw = dataAlkuperainen2['Phone Number']
# collecting and processing phone numbers

tmplist2 = []
tmp2 = {"ID": "0",
        "GSM": "0"}
for z, w in puh_raw.items():
    W = str(w)
    if(re.match(r'358', W) or re.match(r'\+358', W)):
        num = '0'
        W = W.replace('358', '0')
        W = W.replace('+358', '0')
        W = W.replace(' ', '')

    tmp2 = {"ID": z, "GSM": W}
    tmplist2.append(tmp2)


dataAlkuperainen3 = pd.read_csv("./29.7.2021.VAURAUS.LEI.CEO.suora.GSM.csv", 
sep=";", dtype={"CEO_puhelin": str}, encoding='ISO-8859-1', engine = 'python')

puh_raw2 = dataAlkuperainen3['CEO_puhelin']

tmplist3 = []
tmp3 = {"ID": "0",
        "GSM": "0"}
for z, w in puh_raw2.items():
    W = str(w)
    if(re.match(r'358', W) or re.match(r'\+358', W)):
        num = '0'
        W = W.replace('358', '0')
        W = W.replace('+358', '0')
        W = W.replace(' ', '')

    tmp3 = {"ID": z, "GSM": W}
    tmplist3.append(tmp3)    
i = 0
n = 0
count = 0
finalList = []
finalListMatchingID = []
for x in tmplist2:
    for z in tmplist3:
        if x.get("GSM") == z.get("GSM"):
            count += 1
            n += 1
            finalListMatchingID.append(z.get("ID"))  
        else:  
            i += 1

dataAlkuperainen4 = pd.read_csv("./29.7.2021.VAURAUS.+50k.kaikki.csv", 
sep=";", dtype={"ï»¿Puhelinnumero": str}, encoding='ISO-8859-1', engine = 'python')
print(dataAlkuperainen4)
puh_raw3 = dataAlkuperainen4['ï»¿Puhelinnumero']

tmplist4 = []
tmp4 = {"ID": "0",
        "GSM": "0"}
for z, w in puh_raw3.items():
    W = str(w)
    if(re.match(r'358', W) or re.match(r'\+358', W)):
        num = '0'
        W = W.replace('358', '0')
        W = W.replace('+358', '0')
        W = W.replace(' ', '')

    tmp4 = {"ID": z, "GSM": W}
    tmplist4.append(tmp3)

finalListMatchingID2 = []
for x in tmplist2:
    for z in tmplist4:
        if x.get("GSM") == z.get("GSM"):
            count += 1
            n += 1
            finalListMatchingID2.append(z.get("ID"))  
        else:  
            i += 1

"""   
# removing rows that are matched
i = 0
index = 0
rowss = dataAlkuperainen.index[[finalListMatchingID]]
dataAlkuperainen.drop(rowss, inplace=True)

# saving data to .csv file
df = DataFrame(dataAlkuperainen, columns=['a', 'b', 'c', 'd', 'e', 'f', 'g', 
'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r'])
df.astype(str)
export_csv = df.to_csv (r'./test.csv', index = None, header=True, sep=";", encoding="ISO-8859-1")
print(df)

"""