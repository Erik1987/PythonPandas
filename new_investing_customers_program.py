#import necessary modules
import pandas as pd
import csv
import re
from pandas import DataFrame

# collecting data from a .csv file
dataAlkuperainen = pd.read_csv("./FORTUM espoo, helsinki, vantaa, turku 6.5.2021.csv", 
sep=";", dtype={"d": str}, encoding='ISO-8859-1', engine = 'python')

# collecting gsm numbers
puh_raw = dataAlkuperainen['d']

# storing numbers to object list by id and gsm

tmp = {"ID": "0",
        "GSM": "0"}
tmplist = []
for x, y in puh_raw.items():
    y = y.replace('+358', '0')
    print(y)
    y = str(y)
    tmp = {"ID": x, "GSM": y}
    tmplist.append(tmp)
#print(tmplist)

# Collecting data from a Member_last_activited.csv file

dataMember_last_activated = pd.read_csv("Member_last_activited.csv", sep=";", dtype={"Phone Number": str})

# replacing prefixes from a phone number

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

    tmp2 = {"ID": z, "GSM": W}
    tmplist2.append(tmp2)
i = 0
n = 0
count = 0
finalList = []
finalListMatchingID = []

# looping through lists of numbers and comparing them
# and matches are stored by id to a list (id = row number for dataframe)
for x in tmplist:
    for z in tmplist2:
        if x.get("GSM") == z.get("GSM"):
            count += 1
            n += 1
            finalListMatchingID.append(x.get("ID"))  
        else:  
            i += 1
   
# deleting rows from a dataframe by id
i = 0
index = 0
rowss = dataAlkuperainen.index[[finalListMatchingID]]
dataAlkuperainen.drop(rowss, inplace=True)

# saving data to a .csv file
df = DataFrame(dataAlkuperainen, columns=['a', 'b', 'c', 'd', 'e', 'f', 'g', 
'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r'])
df.astype(str)
export_csv = df.to_csv (r'./test.csv', index = None, header=True, sep=";", encoding="ISO-8859-1")
print(df)

