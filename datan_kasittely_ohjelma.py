#import necessary modules
import pandas as pd
import csv
import re
from pandas import DataFrame

# kerätään data tiedostosta .csv
dataAlkuperainen = pd.read_csv("Alkuperainen_OY_kaikki.csv", dtype={"Postinro":str}, sep=";", encoding='ISO-8859-1', engine = 'python')
# kerätään gsm numerot
puh_raw = dataAlkuperainen['Kontaktin GSM']

#print(dataAlkuperainen.head())
# käsitellään dataa
tmp = {"ID": "0",
        "GSM": "0"}
tmplist = []
for x, y in puh_raw.items():
    y = '0' + str(y)[3:]
    tmp = {"ID": x, "GSM": y}
    tmplist.append(tmp)

# Kerätään dataa Member_last_activited.csv
dataMember_last_activated = pd.read_csv("Member_last_activited.csv", sep=";")

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
            finalListMatchingID.append(x.get("ID"))
                
        else:  
            i += 1
   
# Käydään läpi alkuperäinen .csv tiedosto ja verrataan ID osumia, jotka poistaa rivit
i = 0
index = 0
rowss = dataAlkuperainen.index[[finalListMatchingID]]
dataAlkuperainen.drop(rowss, inplace=True)

# Tallennetaan uusi data .csv tiedostoon
df = DataFrame(dataAlkuperainen, columns=['Y-Tunnus', 'Toimipaikan nimi', 'Kayntiosoite', str('Postinro'), 'Postitoimipaikka', 'Yhtiomuoto', 'Toimiala',
'Etunimi', 'Sukunimi', 'Vastuualue', 'Titteli', 'Kontaktin GSM', 'Maakoodi', 'Liikevaihtoluokka', 'Riskiluokituksen selite', 
'Tilikauden tulos', 'Liikevaihto', 'Omavaraisuusaste %', 'Taseen loppusumma', 'Oma paaoma', 'Bruttotulos' ])
export_csv = df.to_csv (r'./test.csv', index = None, header=True, sep=";", encoding="ISO-8859-1")
print(df)
    