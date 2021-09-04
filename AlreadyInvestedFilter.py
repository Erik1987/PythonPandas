#import necessary modules
import pandas as pd
import csv
import re
from pandas import DataFrame

# collecting data from a .csv file

dataAlkuperainen = pd.read_csv("LEI - CEO suora GSM.csv", 
sep=";", dtype={"CEO_puhelin": str}, encoding='ISO-8859-1', engine = 'python')

# collecting gsm numbers
puh_raw = dataAlkuperainen['CEO_puhelin']
company_num = dataAlkuperainen['yritys_puhelin']

# processing data to object list and preparing numbers without prefixes

tmp = {"ID": "0",
        "GSM": "0"}
tmplist = []
for x, y in puh_raw.items():
    y = str(y)
    y = y.replace(" ", "")
    dataAlkuperainen['CEO_puhelin'][x] = y
    tmp = {"ID": x, "GSM": y}
    tmplist.append(tmp)

# collecting data from Member_last_activited.csv file
# dtype formats data as string

dataMember_last_activated = pd.read_csv("Member last activited.csv", sep=";", dtype={"Phone Number": str})

# collecting data from column 'Phone Number'

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
for x in tmplist:
    for z in tmplist2:
        if x.get("GSM") == z.get("GSM"):
            count += 1
            n += 1
            print(z.get("GSM"))
            finalListMatchingID.append(x.get("ID")) 
            #print(finalListMatchingID)   
        else:  
            i += 1  
# adding list of ids to rows to be deleted from a data frame
i = 0
index = 0
rowss = dataAlkuperainen.index[[finalListMatchingID]]
dataAlkuperainen.drop(rowss, inplace=True)

# saving data to .csv file
df = DataFrame(dataAlkuperainen, columns=['Field1', 'Field2', 'Field3', 
'Field4', 'Field5', 'Field6', 'Field7', 
'Field1', 'yritysnimi', 'status', 
'yritys_puhelin', 'CEO_nimi', 'CEO_puhelin', 'talous_nimi', 'talous_puhelin'])
df.astype(str)
export_csv = df.to_csv (r'./test.csv', index = None, header=True, sep=";", encoding="ISO-8859-1")
print(df)

