#import necessary modules
import pandas as pd
import numpy as np
import csv
import re
import math
from pandas import DataFrame


# collecting data from .csv file and adding it to variable dataAlkuperainen
# dtype formats data as strings for processing
dataAlkuperainen = pd.read_csv("DailyRunup-ClientAccount_000105192021_1.csv", 
sep=";", dtype={"CLIENTNUMBER":str, "CLIENTNAME": str, "ACCOUNTMANAGER":str, 
"ACCOUNTCURRENTBALANCE":str, "BLOCKEDAMOUNT":str, "AVAILABLEBALANCE":str, "EXPOSUREAMOUNT":str},  encoding='ISO-8859-1', engine = 'python')

clientnum = dataAlkuperainen["CLIENTNUMBER"]

tmplist = []
tmp = {"Rownum": "0","CLIENTNUM": "0"}
for x, y in clientnum.items():
    tmp = {"Rownum": x, "CLIENTNUM": y}
    tmplist.append(tmp)

# collecting data from Member_last_activited.csv file
clientAssets = pd.read_csv("customers_assets_2.csv", sep=";", dtype={"id":str, "person_name":str, 
"organisation_name":str, "total_assets":str, "balance_sheet_value":str}, encoding='ISO-8859-1')

customerID = clientAssets['id']

# collecting IDs to object list
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

# comparing row numbers and ids
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

# processing original dataframe and comparing by id list to delete rows
i = 0
#index = 0
rowss = dataAlkuperainen.index[[finalListMatchingID]]
#dataAlkuperainen.drop(rowss, inplace=True)
#dataAlkuperainen.append(rowss)

# Saving data to .csv file
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

# exporting to csv file called test.csv
export_csv = df.to_csv (r'./test.csv', index = None, sep=";", header=True, encoding="ISO-8859-1")
#export_xls = df.to_excel(r'./test.xlsx', index=None, header=True, engine='openpyxl', encoding='ISO-8859-1')
print(df)

# sorting data frame by accountmanager
df = df.sort_values(by='ACCOUNTMANAGER', ascending=True)
export_csv = df.to_csv (r'./test.csv', index = None, header=True, sep=";", encoding="ISO-8859-1")
print(df)

# uniques are instances that are found uniquely in a list
uniques = df['ACCOUNTMANAGER'].unique()
#print(uniques)

# then groupby by accountmanager and saving by accountmanager to csv files

d = df.groupby('ACCOUNTMANAGER')['ACCOUNTMANAGER'].agg(list).to_dict()
#print(d[uniques[2]])
idx = 0
index = 0
for n, vals in df.groupby('ACCOUNTMANAGER')['ACCOUNTMANAGER'].agg(list).items():
    if n == uniques[idx]:
        globals()[n] = df[df.ACCOUNTMANAGER == n]
        export_csv2 = df[df.ACCOUNTMANAGER == n].to_csv (f'./{index}test.csv', index = None, header=True, sep=";", encoding="ISO-8859-1")
        index += 1
        idx += 1
    """if (n == 'anniina.lukkarinen' or n == 'henri.pitkanen'
        or n == 'henri.pitk\x8anen' or n == 'jouni.hannula' 
        or n == 'juha.ukkola.agent' or n == 'jussi.heikkil\x8a'
        or n == 'jyrki.ter\x8avuo' or n == 'kari.kaivo-oja'
        or n == 'kari.luomi' or n == 'lasse.kankaanp\x8a\x8a'
        or n == 'lauri.ketoja' or n == 'mika.immonen' 
        or n == 'mikko.kaihlam\x8aki' or n == 'mikko.kaihlam\x8aki.agent'
        or n == 'okko.karsikko' or n == 'otto.viher\x8a'
        or n == 'pasi.hellman' or n == 'teemu.kalliokuja' 
        or n == 'vaurauden.asiakaspalvelu' or n == 'vauraus.asiakaspalvelu'
        or n == 'vesa.karhapaa' or n == 'vesa.karhap\x8a\x8a'):    
        export_excel = df[df.ACCOUNTMANAGER == n].to_excel(f'./myyja{idx}test.xlsx', index=False, header=True, encoding="windows-1252")
        idx += 1 """
print('finished')
