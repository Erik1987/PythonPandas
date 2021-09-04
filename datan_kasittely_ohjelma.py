#import necessary modules
import pandas as pd
import csv
import re
from pandas import DataFrame

# Collecting data from .csv file. dtype means formatting data to string
dataAlkuperainen = pd.read_csv("Alkuperainen_OY_kaikki.csv", dtype={"Postinro":str}, sep=";", encoding='ISO-8859-1', engine = 'python')
# collecting gsm numbers
puh_raw = dataAlkuperainen['Kontaktin GSM']

#print(dataAlkuperainen.head())
# processing data
tmp = {"ID": "0",
        "GSM": "0"}
tmplist = []
for x, y in puh_raw.items():
    y = '0' + str(y)[3:]
    tmp = {"ID": x, "GSM": y}
    tmplist.append(tmp)

# collectingn data Member_last_activited.csv
dataMember_last_activated = pd.read_csv("Member_last_activited.csv", sep=";")

puh2_raw = dataMember_last_activated['Phone Number']
tmplist2 = []
tmp2 = {"ID": "0",
        "GSM": "0"}
# looping through gsm and replacing prefixes. Adding similarities to finalListMatchingID by id
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
            finalListMatchingID.append(x.get("ID"))
                
        else:  
            i += 1
   
# Processing through original dataAlkuperainen dataframe and comparing ID hits to delete rows
i = 0
index = 0
rowss = dataAlkuperainen.index[[finalListMatchingID]]
dataAlkuperainen.drop(rowss, inplace=True)

# Saving new data .csv file uusi
df = DataFrame(dataAlkuperainen, columns=['Y-Tunnus', 'Toimipaikan nimi', 'Kayntiosoite', str('Postinro'), 'Postitoimipaikka', 'Yhtiomuoto', 'Toimiala',
'Etunimi', 'Sukunimi', 'Vastuualue', 'Titteli', 'Kontaktin GSM', 'Maakoodi', 'Liikevaihtoluokka', 'Riskiluokituksen selite', 
'Tilikauden tulos', 'Liikevaihto', 'Omavaraisuusaste %', 'Taseen loppusumma', 'Oma paaoma', 'Bruttotulos' ])
export_csv = df.to_csv (r'./test.csv', index = None, header=True, sep=";", encoding="ISO-8859-1")
print(df)
    
