#import necessary modules
import pandas as pd
import csv
import re
from pandas import DataFrame

def main():
    
    # Collecting data from .csv
    df1 = pd.read_csv("./2019/Member last activited2019.csv", 
    sep=";", dtype={"Account Number": str}, encoding='ISO-8859-1', engine = 'python')

    accountnum = df1["Account Number"]

    # Collecting data from .csv
    df2 = pd.read_csv("./2020/Member last activited2020.csv", 
    sep=";", dtype={"Account Number": str, "Phone Number": str}, encoding='ISO-8859-1', engine = 'python')

    accountnum2 = df2["Account Number"]

    # comparing account numbers and removing them if matched
 
    df3 = df2[~df2["Account Number"].isin(df1["Account Number"])]

    
    # removing all Auto-investment 'No' values
    df3 = df3[df3['Auto-Investment'] != 'No']
     
    # saving data to .csv file
    df = DataFrame(df3, columns=['Agent	', 'Account Manager', 'Member', 'Account Number', 
    'Phone Number', 'Email Id', 'Last Disbursment', 'Last New Investment', 'Last Auto-Investment',
    'Client Account Last Deposit', 'Client Account Last Withdrawal', 'Auto-Investment',
    'Direct Marketing', 'Tele-sales Agent'])
    df.astype(str)
    export_csv = df.to_csv (r'./test.csv', index = None, header=True, sep=";", encoding="ISO-8859-1")
    print(df)

if __name__== "__main__" :
    main()