#import necessary modules
import pandas as pd
import numpy as np
import csv
import re
import math
from pandas import DataFrame


# collecting data from a csv file
dataAlkuperainen = pd.read_csv("persons_customers_AT.csv", 
sep=";", dtype={"counterparty_id":str, "counterparty_firstname": str, "counterparty_lastname":str, 
"counterparty_type":str, "date_of_birth":str},  encoding='ISO-8859-1', engine = 'python')

dataAlkuperainen2 = pd.read_csv("Organisations_customers_AT.csv", 
sep=";", dtype={"counterparty_id":str, "organisation_name": str},  encoding='ISO-8859-1', engine = 'python')

dateOfBirth = dataAlkuperainen["date_of_birth"]

# creating dataframe with new columns
df = DataFrame(dataAlkuperainen, columns=[ "counterparty_id", "organisation_name" ,"counterparty_firstname", "counterparty_lastname", 
"counterparty_type", "vuosi", "kuukausi", "paiva"], dtype=object)

df2 = DataFrame(dataAlkuperainen2, columns=[ "counterparty_id", "organisation_name"], dtype=object)
df.astype(str)

# slicing date of birth to sepparate selctions
vuosi = []
kk = []
paiva = []
for x in dateOfBirth:
    vuosi.append(x[:4])
    kk.append(x[5:7])
    paiva.append(x[8:10])

idObject = {"ID", "Organisation_name"}
listOfCompanies = []
idx = 0

# listing id and organisation names

for x, y in dataAlkuperainen2['counterparty_id'].items():
    idObject = {"ID": y, "Organisation_name": dataAlkuperainen2['organisation_name'][x]}
    listOfCompanies.append(idObject)

# setting values to dataframe

df['vuosi'] = vuosi
df['kuukausi'] = kk
df['paiva'] = paiva

df['counterparty_id'].loc[len(df)] = df2['counterparty_id'].values[:df.shape[1]]

# setting values to dataframe
for item in listOfCompanies:
    df.loc[item["ID"], "counterparty_id"] = item["ID"]
    df.loc[item["ID"], "organisation_name"] = item["Organisation_name"]

# exporting csv file
export_csv = df.to_csv (r'./test.csv', index = None, sep=";", header=True, encoding="ISO-8859-1")
print(df)



