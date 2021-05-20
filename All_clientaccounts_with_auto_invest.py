#import necessary modules
import pandas as pd
import numpy as np
import csv
import re
import math
from pandas import DataFrame

# kerätään data tiedostosta .csv
dataAlkuperainen = pd.read_csv("DailyRunup-ClientAccount_000105022021_1.csv", 
sep=";", dtype={"ACCOUNTNUMBER":str, "ACCOUNTBRANCH":str, "CLIENTNUMBER":str,
"ACCOUNTCURRENTBALANCE":str, "BLOCKEDAMOUNT":str, "ACCOUNTMANAGER":str},  encoding='ISO-8859-1', engine = 'python')

accountnum = dataAlkuperainen["ACCOUNTNUMBER"]

tmplist = []
tmp = {"ID": "0", "ACCOUNTNUM": "0", "Auto-Invest": "NaN", "AccountProduct": "NaN"}
for x, y in accountnum.items():
    tmp = {"ID": x, "ACCOUNTNUM": y, "Auto-Invest": "NaN"}
    tmplist.append(tmp)

# Kerätään dataa Member_last_activited.csv
dataMember_last_activated = pd.read_csv("Member last activited.csv", sep=";", encoding='ISO-8859-1', dtype={"Account Number":str})

accountnum2 = dataMember_last_activated['Account Number']
auto_invest = dataMember_last_activated['Auto-Investment']
tmplist2 = []
nans = []
tmp2 = {"ID": "0",
        "ACCOUNTNUM": "0"}
d = 0        
for z, w in accountnum2.items():
    tmp2 = {"ID": z, "ACCOUNTNUM": w}
    
    if math.isnan(float(w)):
        nans.append(tmp2)
      #  d += 1
       # print(d)
    tmplist2.append(tmp2)   
i = 0
n = 0
g = 0
count = 0
tmplist3 = []
tmplist4 = []
tmplist5 = []
finalListMatchingID = []
tmp3 = {"ID": "0", "ACCOUNTNUM": "0", "Auto-Invest": "NaN", "AccountProduct": "NaN"}

def isNan(val):
    return math.isnan(float(val))

for x in tmplist:
    for z in tmplist2:
            
        if x.get("ACCOUNTNUM") == z.get("ACCOUNTNUM"):
            tmp3 = { "ID": x.get("ID"), "ACCOUNTNUM": x.get("ACCOUNTNUM"), 
            "Auto-Invest": auto_invest[z.get("ID")], 
            "AccountProduct": dataAlkuperainen['ACCOUNTPRODUCT'][x.get('ID')] }
            tmplist3.append(tmp3)
            count += 1
            tmplist5.append(auto_invest[z.get('ID')])
            #print(tmplist5)
            if tmplist3[i]['AccountProduct'] == "WA001":
                tmplist4.append(tmp3)
            else:    
                finalListMatchingID.append(tmp3['ID'])
            i += 1        
        else:
            n += 1

# Käydään läpi alkuperäinen .csv tiedosto ja verrataan ID osumia, jotka poistaa rivit
i = 0
#index = 0
rowss = dataAlkuperainen.index[[finalListMatchingID]]
dataAlkuperainen.drop(rowss, inplace=True)
#dataAlkuperainen.append(rowss)

# Tallennetaan uusi data .csv tiedostoon
df = DataFrame(dataAlkuperainen, columns=[ 'ACCOUNTNUMBER' ,
'CLIENTNUMBER', 'CLIENTNAME', 'ACCOUNTMANAGER','ACCOUNTCURRENTBALANCE',  
'BLOCKEDAMOUNT', 'SECUREDBLOCKEDAMOUNT',
'UNSECUREDBLOCKEDAMOUNT', 'SUBORDINATEBLOCKEDAMOUNT', 'HIGHRISKBLOCKEDAMOUNT', 
'NOASSETTYPEBLOCKEDAMOUNT', 'AVAILABLEBALANCE', 'MAXIMUMEXPOSUREPERCENTAGE',
'AUTOINVESTMENTTHRESHOLD', 'EXPOSUREAMOUNT', 'AUTO-INVESTMENT'], dtype=object)

# Iterate on each row and add value to 'AUTO-INVESTMENT' column
for item in tmplist3:
    if item["ID"] in df.index:
        df.loc[item["ID"], "AUTO-INVESTMENT"] = item["Auto-Invest"]

df.astype(str)
df = df.sort_values(by='ACCOUNTMANAGER', ascending=True)
export_csv = df.to_csv (r'./test.csv', index = None, header=True, sep=";", encoding="ISO-8859-1")
print(df)

uniques = df['ACCOUNTMANAGER'].unique()
#print(uniques)
d = df.groupby('ACCOUNTMANAGER')['ACCOUNTMANAGER'].agg(list).to_dict()

#print(d[uniques[2]])
idx = 0
for n, vals in df.groupby('ACCOUNTMANAGER')['ACCOUNTMANAGER'].agg(list).items():
    if n == uniques[idx]:
        globals()[n] = df[df.ACCOUNTMANAGER == n]
        export_csv = df[df.ACCOUNTMANAGER == n].to_csv (f'./{idx}test.csv', index = None, header=True, sep=";", encoding="ISO-8859-1")
        #export_excel = df[df.ACCOUNTMANAGER == n].to_excel(f'./{idx}test.xlsx', index=None, header=True, encoding="ISO-8859-1")
        idx += 1



#print (uudetlistat)
