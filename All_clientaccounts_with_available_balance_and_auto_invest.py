#import necessary modules
import pandas as pd
import numpy as np
import csv
import re
import math
from pandas import DataFrame

# collecting data from a csv file
# dtype formats data as string

dataAlkuperainen = pd.read_csv("DailyRunup-ClientAccount_000106282021_1.csv", 
sep=";", dtype={"ACCOUNTNUMBER":str, "ACCOUNTBRANCH":str, "CLIENTNUMBER":str,
"ACCOUNTCURRENTBALANCE":str, "BLOCKEDAMOUNT":str, "ACCOUNTMANAGER":str},  encoding='ISO-8859-1', engine = 'python')

# collecting data from a column 'account number'

accountnum = dataAlkuperainen["ACCOUNTNUMBER"]

# creating temporary object list with auto-invest etc

tmplist = []
tmp = {"ID": "0", "ACCOUNTNUM": "0", "Auto-Invest": "NaN", "AccountProduct": "NaN"}
for x, y in accountnum.items():
    tmp = {"ID": x, "ACCOUNTNUM": y, "Auto-Invest": "NaN"}
    tmplist.append(tmp)

# collecting data from a Member_last_activited.csv file
dataMember_last_activated = pd.read_csv("Member last activited.csv", sep=";", encoding='ISO-8859-1', dtype={"Account Number":str})

accountnum2 = dataMember_last_activated['Account Number']
auto_invest = dataMember_last_activated['Auto-Investment']
tmplist2 = []
nans = []
tmp2 = {"ID": "0",
        "ACCOUNTNUM": "0"}

# adding nan values to a list and account numbers to another list
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

# function to determine nan values
def isNan(val):
    return math.isnan(float(val))

# looping through lists and comparing account numbers, then adding ids to list
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
# deleting rows from a dataframe by collected ids
i = 0
#index = 0
rowss = dataAlkuperainen.index[[finalListMatchingID]]
dataAlkuperainen.drop(rowss, inplace=True)
#dataAlkuperainen.append(rowss)

# creating new dataframe by column names
df = DataFrame(dataAlkuperainen, columns=[ 'ACCOUNTNUMBER' ,
'CLIENTNUMBER', 'CLIENTNAME', 'ACCOUNTMANAGER', 
'BLOCKEDAMOUNT', 'AVAILABLEBALANCE', 'EXPOSUREAMOUNT', 'AUTO-INVESTMENT'], dtype=object)

# Iterate on each row and add value to 'AUTO-INVESTMENT' column
for item in tmplist3:
    if item["ID"] in df.index:
        df.loc[item["ID"], "AUTO-INVESTMENT"] = item["Auto-Invest"]

# sorting data by available balance and auto-investment 
df.astype(str)
df = df.sort_values(['AVAILABLEBALANCE', 'AUTO-INVESTMENT'], ascending=[False, True])
#df = df.sort_values(by='AUTO-INVESTMENT', ascending=False)

# exporting data to csv file
export_csv = df.to_csv (r'./test.csv', index = None, header=True, sep=";", encoding="ISO-8859-1")
print(df)


# uniques are the unique values from a list

uniques = df['ACCOUNTMANAGER'].unique()
#print(uniques)

# grouping by accountmanager name then saving to a file by account managers name

d = df.groupby('ACCOUNTMANAGER')['ACCOUNTMANAGER'].agg(list).to_dict()
#print(d[uniques[2]])
idx = 0
index = 0
for n, vals in df.groupby('ACCOUNTMANAGER')['ACCOUNTMANAGER'].agg(list).items():
    if n == uniques[idx]:
        globals()[n] = df[df.ACCOUNTMANAGER == n]
        export_csv = df[df.ACCOUNTMANAGER == n].to_csv (f'./{index}test.csv', index = None, header=True, sep=";", encoding="ISO-8859-1")
        
        
    if (n == 'anniina.lukkarinen' or n == 'henri.pitkanen'
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
        export_to_csv = df[df.ACCOUNTMANAGER == n].to_csv(f'./myyja{idx}test.csv', index=False, header=True, encoding="ISO-8859-1")
        idx += 1 

#print (uudetlistat)
