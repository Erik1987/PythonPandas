#import necessary modules
import pandas as pd
import csv
import re
from pandas import DataFrame

# collecting data from a .csv file
dataAlkuperainen = pd.read_csv("Oskarin_potet_2021.csv", 
sep=";", dtype={"Kontaktin GSM numero": str}, encoding='ISO-8859-1', engine = 'python')

# collecting gsm numbers
puh_raw = dataAlkuperainen['Kontaktin GSM numero']

# adding numbers to list of objects by id and gsm

tmp = {"ID": "0",
        "GSM": "0"}
tmplist = []
for x, y in puh_raw.items():
    y = str(y)
    tmp = {"ID": x, "GSM": y}
    tmplist.append(tmp)

# collecting data from a Member_last_activited.csv file
# dtype formats data as strings

dataMember_last_activated = pd.read_csv("Member_last_activited.csv", sep=";", dtype={"Phone Number": str})

# collecting phone numbers from a column 'Phone Number'

puh2_raw = dataMember_last_activated['Phone Number']
tmplist2 = []

# removing phone number prefixes
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
# comparing phone numbers and adding matched numbers to list as id
for x in tmplist:
    for z in tmplist2:
        if x.get("GSM") == z.get("GSM"):
            count += 1
            n += 1
            finalListMatchingID.append(x.get("ID"))  
        else:  
            i += 1
   
# deleting rows from a dataframe by ids
i = 0
index = 0
rowss = dataAlkuperainen.index[[finalListMatchingID]]
dataAlkuperainen.drop(rowss, inplace=True)

# creating a new dataframe by column names, saving to a csv file

df = DataFrame(dataAlkuperainen, columns=['Y-Tunnus', 'Toimipaikan nimi', 'Kunta', 
'Etunimi', 'Sukunimi', 'Vastuualueen koodi', 'Titteli', 
'Sukupuoli', str('Kontaktin GSM numero'), 'Kontaktin sahkopostiosoite', 
'Kontaktin lankanumero'])
df.astype(str)
export_csv = df.to_csv (r'/Users/erik.ilonen/Desktop/Projekti_csv_data/Toinen_testiohjelma/test.csv', index = None, header=True, sep=";", encoding="ISO-8859-1")
print(df)

