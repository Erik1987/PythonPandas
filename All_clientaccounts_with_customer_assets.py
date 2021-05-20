#import necessary modules
import pandas as pd
import numpy as np
import csv
import re
import math
from pandas import DataFrame

# kerätään data tiedostosta .csv
dataAlkuperainen = pd.read_csv("DailyRunup-ClientAccount_000105022021_1.csv", 
sep=";", dtype={"CLIENTNUMBER":str, "CLIENTNAME": str, "ACCOUNTMANAGER":str, 
"ACCOUNTCURRENTBALANCE":str, "BLOCKEDAMOUNT":str, "AVAILABLEBALANCE":str, "EXPOSUREAMOUNT":str},  encoding='ISO-8859-1', engine = 'python')

clientnum = dataAlkuperainen["CLIENTNUMBER"]

tmplist = []
tmp = {"Rownum": "0","CLIENTNUM": "0"}
for x, y in clientnum.items():
    tmp = {"Rownum": x, "CLIENTNUM": y}
    tmplist.append(tmp)

# Kerätään dataa Member_last_activited.csv
clientAssets = pd.read_csv("customers_assets_2.csv", sep=";", dtype={"id":str, "person_name":str, 
"organisation_name":str, "total_assets":str, "balance_sheet_value":str}, encoding='ISO-8859-1')

customerID = clientAssets['id']

tmplist2 = []

tmp2 = {"customerID": "0"}
     
for key, value in customerID.items():
    tmp2 = {"Rownum": key, "customerID": value}
    tmplist2.append(tmp2)  
i = 0
n = 0
g = 0
count = 0
tmplist3 = []
finalListMatchingID = []

tmp3 = {"RownumX": "0", "CLIENTNUM": "0", "RownumY": "NaN", "customerID": "0"}
idx = 0
for x in tmplist:
    for y in tmplist2:
            
        if x.get("CLIENTNUM") == y.get("customerID"):
            tmp3 = { "RownumX": x.get("Rownum"), "CLIENTNUM": x.get("CLIENTNUM"), 
            "RownumY": y.get("Rownum"), 
            "customerID": y.get('customerID'), "person_name": clientAssets['person_name'][y.get("Rownum")],
            "organisation_name": clientAssets['organisation_name'][y.get("Rownum")], "total_assets":
            clientAssets["total_assets"][y.get("Rownum")], "balance_sheet_value": clientAssets['balance_sheet_value'][y.get("Rownum")]}
            tmplist3.append(tmp3)
            finalListMatchingID.append(x.get("Rownum"))
            count += 1
        else:
            n += 1
        idx += 1     
#print(finalListMatchingID)  

# Käydään läpi alkuperäinen .csv tiedosto ja verrataan ID osumia, jotka poistaa rivit
i = 0
#index = 0
rowss = dataAlkuperainen.index[[finalListMatchingID]]
#dataAlkuperainen.drop(rowss, inplace=True)
#dataAlkuperainen.append(rowss)

# Tallennetaan uusi data .csv tiedostoon
df = DataFrame(dataAlkuperainen, columns=[ "CLIENTNUMBER", "CLIENTNAME", "ACCOUNTMANAGER", 
"ACCOUNTCURRENTBALANCE", "BLOCKEDAMOUNT", "AVAILABLEBALANCE", "EXPOSUREAMOUNT", 
"TOTAL_ASSETS", "BALANCE_SHEET_VALUE" ], dtype=object)



# Iterate on each row and add value to 'TOTAL_ASSETS' column
for item in tmplist3:
    if item["RownumX"] in df.index:
        df.loc[item["RownumX"], "TOTAL_ASSETS"] = item["total_assets"]

# Iterate on each row and add value to 'BALANCE_SHEET_VALUE' column
for item in tmplist3:
    if item["RownumX"] in df.index:
        df.loc[item["RownumX"], "BALANCE_SHEET_VALUE"] = item["balance_sheet_value"]

df.astype(str)

export_csv = df.to_csv (r'./test.cvs', index = None, sep=";", header=True, encoding="ISO-8859-1")
#export_xls = df.to_excel(r'./test.xlsx', index=None, header=True, engine='openpyxl', encoding='ISO-8859-1')
print(df)

