#!/usr/bin/python
# -*- coding: ISO-8859-1 -*-
#import necessary modules
import pandas as pd
import numpy as np

# collecting data from a excel file
# dtype formats data as string 

df30 = pd.read_excel("all_incomeearned.xlsx", "Sheet1", dtype={"Fee Name": str, "General Ledger": int, "Amount":float})

# collecting fee name from a column 'Fee Name'
feeName = df30["Fee Name"]
amount = df30["Amount"].astype(np.float64)
index = 0

sumManagementFee = 0
sumManagementFeePrincipal = 0
sumManagementFeeInterest = 0
sumServiceCharge1 = 0
sumAdhoc1 = 0
sumPenalty1 = 0
sumOrigination = 0
sumInvestment = 0

# if fee name is correct sum values
for x in feeName:
    if x == "Management Fee":

        rows = float(amount.iloc[index])
        sumManagementFee += rows
    if x == "Management Fee - Principal":

        rows = float(amount.iloc[index])
        sumManagementFeePrincipal += rows 
    if x == "Management Fee - Interest":
        rows = float(amount.iloc[index])
        sumManagementFeeInterest += rows   
    if x == "Service Charge":
        rows = float(amount.iloc[index])
        sumServiceCharge1 += rows  
    if x == "Adhoc Charge":
        rows = float(amount.iloc[index])
        sumAdhoc1 += rows 
    if x == "Penalty Fee - Corporate":
        rows = float(amount.iloc[index])
        sumPenalty1 += rows  
    if x == "Origination fee":
        rows = float(amount.iloc[index])
        sumOrigination += rows    
    if x == "Investment fee":
        rows = float(amount.iloc[index])
        sumInvestment += rows            
    index += 1    

# printing fee sums

print("Management fee sum "+ str(sumManagementFee))
print("Management fee principal sum "+ str(sumManagementFeePrincipal))
print("Management fee interest sum "+ str(sumManagementFeeInterest))
print("Service charge sum "+ str(sumServiceCharge1))
print("Adhoc charge sum "+ str(sumAdhoc1))
print("Penalty fee sum "+ str(sumPenalty1))
print("Origination fee sum "+ str(sumOrigination))
print("Investment fee sum "+ str(sumInvestment))
print("\n")

# collecting data from xls files

df = pd.read_excel("AccountTransactions_000106012021_1.xls", "Sheet1", dtype={"Transaction Description": str})
df1 = pd.read_excel("AccountTransactions_000106022021_1.xls", "Sheet1", dtype={"Transaction Description": str})
df2 = pd.read_excel("AccountTransactions_000106032021_1.xls", "Sheet1", dtype={"Transaction Description": str})
df3 = pd.read_excel("AccountTransactions_000106042021_1.xls", "Sheet1", dtype={"Transaction Description": str})
df4 = pd.read_excel("AccountTransactions_000106052021_1.xls", "Sheet1", dtype={"Transaction Description": str})
df5 = pd.read_excel("AccountTransactions_000106062021_1.xls", "Sheet1", dtype={"Transaction Description": str})
df6 = pd.read_excel("AccountTransactions_000106072021_1.xls", "Sheet1", dtype={"Transaction Description": str})
df7 = pd.read_excel("AccountTransactions_000106082021_1.xls", "Sheet1", dtype={"Transaction Description": str})
df8 = pd.read_excel("AccountTransactions_000106092021_1.xls", "Sheet1", dtype={"Transaction Description": str})
df9 = pd.read_excel("AccountTransactions_000106102021_1.xls", "Sheet1", dtype={"Transaction Description": str})
df10 = pd.read_excel("AccountTransactions_000106112021_1.xls", "Sheet1", dtype={"Transaction Description": str})
df11 = pd.read_excel("AccountTransactions_000106122021_1.xls", "Sheet1", dtype={"Transaction Description": str})
df12 = pd.read_excel("AccountTransactions_000106132021_1.xls", "Sheet1", dtype={"Transaction Description": str})
df13 = pd.read_excel("AccountTransactions_000106142021_1.xls", "Sheet1", dtype={"Transaction Description": str})
df14 = pd.read_excel("AccountTransactions_000106152021_1.xls", "Sheet1", dtype={"Transaction Description": str})
df15 = pd.read_excel("AccountTransactions_000106162021_1.xls", "Sheet1", dtype={"Transaction Description": str})
df16 = pd.read_excel("AccountTransactions_000106172021_1.xls", "Sheet1", dtype={"Transaction Description": str})
df17 = pd.read_excel("AccountTransactions_000106182021_1.xls", "Sheet1", dtype={"Transaction Description": str})
df18 = pd.read_excel("AccountTransactions_000106192021_1.xls", "Sheet1", dtype={"Transaction Description": str})
df19 = pd.read_excel("AccountTransactions_000106202021_1.xls", "Sheet1", dtype={"Transaction Description": str})
df20 = pd.read_excel("AccountTransactions_000106212021_1.xls", "Sheet1", dtype={"Transaction Description": str})
df21 = pd.read_excel("AccountTransactions_000106222021_1.xls", "Sheet1", dtype={"Transaction Description": str})
df22 = pd.read_excel("AccountTransactions_000106232021_1.xls", "Sheet1", dtype={"Transaction Description": str})
df23 = pd.read_excel("AccountTransactions_000106242021_1.xls", "Sheet1", dtype={"Transaction Description": str})
df24 = pd.read_excel("AccountTransactions_000106252021_1.xls", "Sheet1", dtype={"Transaction Description": str})
df25 = pd.read_excel("AccountTransactions_000106262021_1.xls", "Sheet1", dtype={"Transaction Description": str})
df26 = pd.read_excel("AccountTransactions_000106272021_1.xls", "Sheet1", dtype={"Transaction Description": str})
df27 = pd.read_excel("AccountTransactions_000106282021_1.xls", "Sheet1", dtype={"Transaction Description": str})
#df28 = pd.read_excel("AccountTransactions_000106292021_1.xls", "Sheet1", dtype={"Transaction Description": str})
df29 = pd.read_excel("AccountTransactions_000106302021_1.xlsx", "Sheet1", dtype={"Transaction Description": str})


transactionDescription = df["Transaction Description"]
transactionAmount = df["Transaction Amount"]

# function that checks and return charge amount

def CheckChargesAmount(transactionDescription, transactionAmount):
    line = 0
    sumServiceChargePrincipal = 0
    sumServiceChargeInterest = 0
    sumServiceCharge = 0
    sumAdhoc = 0
    sumServiceChargeManagement = 0
    sumServiceChargeManagementNew = 0
    sumServiceChargePenaltyFee = 0
    sumComissionExpenses = 0
    sumOutgoingTransfer = 0
    sumTeleCommission = 0
    sumCreditProcessing = 0
    sumInteresDueComponent = 0
    sumInterestOverdueComponent = 0
    sumInterestReceived = 0
    sumLoanPayment = 0
    sumPrincipalOverdueComponent = 0
    sumPaytrailSettlement = 0
    sumRedistPrincipal = 0
    sumRedistInterest = 0
    sumTaxWitheld = 0
    sumRedistCharge = 0
    sumPaytrailTransaction = 0
    sumLoanPayment2 = 0
    sumDebitProcessing = 0

    for x in transactionDescription:
        if x == "Service Charge":
            rows = transactionAmount.iloc[line]
            sumServiceCharge += rows
        if x == "Service Charge-Management Fee-Principal" and line <= len(transactionAmount):
            rows1 = transactionAmount.iloc[line]
            sumServiceChargePrincipal += rows1
        if x == ("Service Charge-Management Fee-Interest"):
            rows2 = transactionAmount.iloc[line]
            sumServiceChargeInterest += rows2
        if x == "Service Charge - Adhoc fee":
            rows3 = transactionAmount.iloc[line]
            sumAdhoc += rows3
        if x == "Service charge - Management (loans)":
            rows4 = transactionAmount.iloc[line]
            sumServiceChargeManagement += rows4   
        if x == "Service charge - Management (new loans)":
            rows5 = transactionAmount.iloc[line]
            sumServiceChargeManagementNew += rows5 
        if x == "Service charge - Penalty Fee - Corporate":
            rows6 = transactionAmount.iloc[line]
            sumServiceChargePenaltyFee += rows6  

        if x == "Commission expenses - Client / Credit":
            rows7 = transactionAmount.iloc[line]
            sumComissionExpenses += rows7
        if x == "Outgoing transfer":
            rows8 = transactionAmount.iloc[line]
            sumOutgoingTransfer += rows8 
        if x == "Tele sales agent commission transfer":
            rows9 = transactionAmount.iloc[line]
            sumTeleCommission += rows9
        if x == "Credit processing transaction code (Client / CR)":
            rows10 = transactionAmount.iloc[line]
            sumCreditProcessing += rows10 
        if x == "Interest due component":
            rows11 = transactionAmount.iloc[line]
            sumInteresDueComponent += rows11
        if x == "Interest overdue component":
            rows12 = transactionAmount.iloc[line]
            sumInterestOverdueComponent += rows12 
        if x == "Interest received - Client / Debit":
            rows13 = transactionAmount.iloc[line]
            sumInterestReceived += rows13
        if x == "Loan payment / repayment - Client / Debit":
            rows14 = transactionAmount.iloc[line]
            sumLoanPayment += rows14  
        if x == "Principal overdue component":
            rows15 = transactionAmount.iloc[line]
            sumPrincipalOverdueComponent += rows15 

        if x == "Paytrail settlement(Db/client)":
            rows16 = transactionAmount.iloc[line]
            sumPaytrailSettlement += rows16  
        if x == "Redistribution of Principal due component":
            rows17 = transactionAmount.iloc[line]
            sumRedistPrincipal += rows17 
        if x == "Redistribution of Interset due component":
            rows18 = transactionAmount.iloc[line]
            sumRedistInterest += rows18 
        if x == "Tax withheld - Placement":
            rows19 = transactionAmount.iloc[line]
            sumTaxWitheld += rows19 
        if x == "Redistribution of charge component PIRDLT":
            rows20 = transactionAmount.iloc[line]
            sumRedistCharge += rows20 
        if x == "Paytrail transactions crdt":
            rows21 = transactionAmount.iloc[line]
            sumPaytrailTransaction += rows21 
        if x == "Loan payment / repayment - Client / Credit":
            rows22 = transactionAmount.iloc[line]
            sumLoanPayment2 += rows22 
        if x == "Debit processing transaction code (Client / DB)":
            rows23 = transactionAmount.iloc[line]
            sumDebitProcessing += rows23             
 
        line += 1
    return (sumServiceCharge, 
    sumServiceChargePrincipal, 
    sumServiceChargeInterest, 
    sumAdhoc, 
    sumServiceChargeManagement, sumServiceChargeManagementNew, sumServiceChargePenaltyFee,
    sumComissionExpenses,
    sumOutgoingTransfer,
    sumTeleCommission,
    sumCreditProcessing,
    sumInteresDueComponent,
    sumInterestOverdueComponent,
    sumInterestReceived,
    sumLoanPayment,
    sumPrincipalOverdueComponent,
    sumPaytrailSettlement,
    sumRedistPrincipal,
    sumRedistInterest,
    sumTaxWitheld,
    sumRedistCharge,
    sumPaytrailTransaction,
    sumLoanPayment2,
    sumDebitProcessing)

# function that sums amounts for charges

def SumAmounts(a, b, c, d, e, f, g, h, i, j, k, l , m, n, o, p, q, r, s, t, u, v, w, x, y, z, aa, ab, 
ac, ad, ae, af, ag, ah, ai, aj, ak, al, am, an, ao, ap, aq, ar, at, au, av, aw):
    a += y
    b += z
    c += aa
    d += ab
    e += ac
    f += ad
    g += ae
    h += af
    i += ag
    j += ah
    k += ai
    l += aj
    m += ak
    n += al
    o += am
    p += an
    q += ao
    r += ap
    s += aq
    t += ar
    u += at
    v += au
    w += av
    x += aw


    return a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x

# summing all transactions

(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, 
r, s, t, u, v, w, x ) = CheckChargesAmount(transactionDescription, transactionAmount)

transactionDescription = df1["Transaction Description"]
transactionAmount = df1["Transaction Amount"]

(y, z, aa, ab, ac, ad, ae, af, ag, ah, ai, aj, ak, al, am,
an, ao, ap, aq, ar, at, au, av, aw )= CheckChargesAmount(transactionDescription, transactionAmount)

(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, 
r, s, t, u, v, w, x ) = SumAmounts(a, b, c, d, e, f, g, h, i, j, k, l , m, n, o, p, q, r, s, t, u, v, w, x, y, z, aa, ab, 
ac, ad, ae, af, ag, ah, ai, aj, ak, al, am, an, ao, ap, aq, ar, at, au, av, aw)

transactionDescription = df2["Transaction Description"]
transactionAmount = df2["Transaction Amount"]

(y, z, aa, ab, ac, ad, ae, af, ag, ah, ai, aj, ak, al, am,
an, ao, ap, aq, ar, at, au, av, aw )= CheckChargesAmount(transactionDescription, transactionAmount)

(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, 
r, s, t, u, v, w, x ) = SumAmounts(a, b, c, d, e, f, g, h, i, j, k, l , m, n, o, p, q, r, s, t, u, v, w, x, y, z, aa, ab, 
ac, ad, ae, af, ag, ah, ai, aj, ak, al, am, an, ao, ap, aq, ar, at, au, av, aw)

transactionDescription = df3["Transaction Description"]
transactionAmount = df3["Transaction Amount"]

(y, z, aa, ab, ac, ad, ae, af, ag, ah, ai, aj, ak, al, am,
an, ao, ap, aq, ar, at, au, av, aw )= CheckChargesAmount(transactionDescription, transactionAmount)

(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, 
r, s, t, u, v, w, x ) = SumAmounts(a, b, c, d, e, f, g, h, i, j, k, l , m, n, o, p, q, r, s, t, u, v, w, x, y, z, aa, ab, 
ac, ad, ae, af, ag, ah, ai, aj, ak, al, am, an, ao, ap, aq, ar, at, au, av, aw)

transactionDescription = df4["Transaction Description"]
transactionAmount = df4["Transaction Amount"]

(y, z, aa, ab, ac, ad, ae, af, ag, ah, ai, aj, ak, al, am,
an, ao, ap, aq, ar, at, au, av, aw )= CheckChargesAmount(transactionDescription, transactionAmount)

(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, 
r, s, t, u, v, w, x ) = SumAmounts(a, b, c, d, e, f, g, h, i, j, k, l , m, n, o, p, q, r, s, t, u, v, w, x, y, z, aa, ab, 
ac, ad, ae, af, ag, ah, ai, aj, ak, al, am, an, ao, ap, aq, ar, at, au, av, aw)

transactionDescription = df5["Transaction Description"]
transactionAmount = df5["Transaction Amount"]

(y, z, aa, ab, ac, ad, ae, af, ag, ah, ai, aj, ak, al, am,
an, ao, ap, aq, ar, at, au, av, aw )= CheckChargesAmount(transactionDescription, transactionAmount)

(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, 
r, s, t, u, v, w, x ) = SumAmounts(a, b, c, d, e, f, g, h, i, j, k, l , m, n, o, p, q, r, s, t, u, v, w, x, y, z, aa, ab, 
ac, ad, ae, af, ag, ah, ai, aj, ak, al, am, an, ao, ap, aq, ar, at, au, av, aw)

transactionDescription = df6["Transaction Description"]
transactionAmount = df6["Transaction Amount"]

(y, z, aa, ab, ac, ad, ae, af, ag, ah, ai, aj, ak, al, am,
an, ao, ap, aq, ar, at, au, av, aw )= CheckChargesAmount(transactionDescription, transactionAmount)

(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, 
r, s, t, u, v, w, x ) = SumAmounts(a, b, c, d, e, f, g, h, i, j, k, l , m, n, o, p, q, r, s, t, u, v, w, x, y, z, aa, ab, 
ac, ad, ae, af, ag, ah, ai, aj, ak, al, am, an, ao, ap, aq, ar, at, au, av, aw)

transactionDescription = df7["Transaction Description"]
transactionAmount = df7["Transaction Amount"]

(y, z, aa, ab, ac, ad, ae, af, ag, ah, ai, aj, ak, al, am,
an, ao, ap, aq, ar, at, au, av, aw )= CheckChargesAmount(transactionDescription, transactionAmount)

(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, 
r, s, t, u, v, w, x ) = SumAmounts(a, b, c, d, e, f, g, h, i, j, k, l , m, n, o, p, q, r, s, t, u, v, w, x, y, z, aa, ab, 
ac, ad, ae, af, ag, ah, ai, aj, ak, al, am, an, ao, ap, aq, ar, at, au, av, aw)

transactionDescription = df8["Transaction Description"]
transactionAmount = df8["Transaction Amount"]

(y, z, aa, ab, ac, ad, ae, af, ag, ah, ai, aj, ak, al, am,
an, ao, ap, aq, ar, at, au, av, aw )= CheckChargesAmount(transactionDescription, transactionAmount)

(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, 
r, s, t, u, v, w, x ) = SumAmounts(a, b, c, d, e, f, g, h, i, j, k, l , m, n, o, p, q, r, s, t, u, v, w, x, y, z, aa, ab, 
ac, ad, ae, af, ag, ah, ai, aj, ak, al, am, an, ao, ap, aq, ar, at, au, av, aw)

transactionDescription = df9["Transaction Description"]
transactionAmount = df9["Transaction Amount"]

(y, z, aa, ab, ac, ad, ae, af, ag, ah, ai, aj, ak, al, am,
an, ao, ap, aq, ar, at, au, av, aw )= CheckChargesAmount(transactionDescription, transactionAmount)

(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, 
r, s, t, u, v, w, x ) = SumAmounts(a, b, c, d, e, f, g, h, i, j, k, l , m, n, o, p, q, r, s, t, u, v, w, x, y, z, aa, ab, 
ac, ad, ae, af, ag, ah, ai, aj, ak, al, am, an, ao, ap, aq, ar, at, au, av, aw)

transactionDescription = df10["Transaction Description"]
transactionAmount = df10["Transaction Amount"]

(y, z, aa, ab, ac, ad, ae, af, ag, ah, ai, aj, ak, al, am,
an, ao, ap, aq, ar, at, au, av, aw )= CheckChargesAmount(transactionDescription, transactionAmount)

(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, 
r, s, t, u, v, w, x ) = SumAmounts(a, b, c, d, e, f, g, h, i, j, k, l , m, n, o, p, q, r, s, t, u, v, w, x, y, z, aa, ab, 
ac, ad, ae, af, ag, ah, ai, aj, ak, al, am, an, ao, ap, aq, ar, at, au, av, aw)

transactionDescription = df11["Transaction Description"]
transactionAmount = df11["Transaction Amount"]

(y, z, aa, ab, ac, ad, ae, af, ag, ah, ai, aj, ak, al, am,
an, ao, ap, aq, ar, at, au, av, aw )= CheckChargesAmount(transactionDescription, transactionAmount)

(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, 
r, s, t, u, v, w, x ) = SumAmounts(a, b, c, d, e, f, g, h, i, j, k, l , m, n, o, p, q, r, s, t, u, v, w, x, y, z, aa, ab, 
ac, ad, ae, af, ag, ah, ai, aj, ak, al, am, an, ao, ap, aq, ar, at, au, av, aw)

transactionDescription = df12["Transaction Description"]
transactionAmount = df12["Transaction Amount"]

(y, z, aa, ab, ac, ad, ae, af, ag, ah, ai, aj, ak, al, am,
an, ao, ap, aq, ar, at, au, av, aw )= CheckChargesAmount(transactionDescription, transactionAmount)

(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, 
r, s, t, u, v, w, x ) = SumAmounts(a, b, c, d, e, f, g, h, i, j, k, l , m, n, o, p, q, r, s, t, u, v, w, x, y, z, aa, ab, 
ac, ad, ae, af, ag, ah, ai, aj, ak, al, am, an, ao, ap, aq, ar, at, au, av, aw)

transactionDescription = df13["Transaction Description"]
transactionAmount = df13["Transaction Amount"]

(y, z, aa, ab, ac, ad, ae, af, ag, ah, ai, aj, ak, al, am,
an, ao, ap, aq, ar, at, au, av, aw )= CheckChargesAmount(transactionDescription, transactionAmount)

(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, 
r, s, t, u, v, w, x ) = SumAmounts(a, b, c, d, e, f, g, h, i, j, k, l , m, n, o, p, q, r, s, t, u, v, w, x, y, z, aa, ab, 
ac, ad, ae, af, ag, ah, ai, aj, ak, al, am, an, ao, ap, aq, ar, at, au, av, aw)

transactionDescription = df14["Transaction Description"]
transactionAmount = df14["Transaction Amount"]

(y, z, aa, ab, ac, ad, ae, af, ag, ah, ai, aj, ak, al, am,
an, ao, ap, aq, ar, at, au, av, aw )= CheckChargesAmount(transactionDescription, transactionAmount)

(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, 
r, s, t, u, v, w, x ) = SumAmounts(a, b, c, d, e, f, g, h, i, j, k, l , m, n, o, p, q, r, s, t, u, v, w, x, y, z, aa, ab, 
ac, ad, ae, af, ag, ah, ai, aj, ak, al, am, an, ao, ap, aq, ar, at, au, av, aw)

transactionDescription = df15["Transaction Description"]
transactionAmount = df15["Transaction Amount"]

(y, z, aa, ab, ac, ad, ae, af, ag, ah, ai, aj, ak, al, am,
an, ao, ap, aq, ar, at, au, av, aw )= CheckChargesAmount(transactionDescription, transactionAmount)

(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, 
r, s, t, u, v, w, x ) = SumAmounts(a, b, c, d, e, f, g, h, i, j, k, l , m, n, o, p, q, r, s, t, u, v, w, x, y, z, aa, ab, 
ac, ad, ae, af, ag, ah, ai, aj, ak, al, am, an, ao, ap, aq, ar, at, au, av, aw)

transactionDescription = df16["Transaction Description"]
transactionAmount = df16["Transaction Amount"]

(y, z, aa, ab, ac, ad, ae, af, ag, ah, ai, aj, ak, al, am,
an, ao, ap, aq, ar, at, au, av, aw )= CheckChargesAmount(transactionDescription, transactionAmount)

(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, 
r, s, t, u, v, w, x ) = SumAmounts(a, b, c, d, e, f, g, h, i, j, k, l , m, n, o, p, q, r, s, t, u, v, w, x, y, z, aa, ab, 
ac, ad, ae, af, ag, ah, ai, aj, ak, al, am, an, ao, ap, aq, ar, at, au, av, aw)

transactionDescription = df17["Transaction Description"]
transactionAmount = df17["Transaction Amount"]

(y, z, aa, ab, ac, ad, ae, af, ag, ah, ai, aj, ak, al, am,
an, ao, ap, aq, ar, at, au, av, aw )= CheckChargesAmount(transactionDescription, transactionAmount)

(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, 
r, s, t, u, v, w, x ) = SumAmounts(a, b, c, d, e, f, g, h, i, j, k, l , m, n, o, p, q, r, s, t, u, v, w, x, y, z, aa, ab, 
ac, ad, ae, af, ag, ah, ai, aj, ak, al, am, an, ao, ap, aq, ar, at, au, av, aw)

transactionDescription = df18["Transaction Description"]
transactionAmount = df18["Transaction Amount"]

(y, z, aa, ab, ac, ad, ae, af, ag, ah, ai, aj, ak, al, am,
an, ao, ap, aq, ar, at, au, av, aw )= CheckChargesAmount(transactionDescription, transactionAmount)

(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, 
r, s, t, u, v, w, x ) = SumAmounts(a, b, c, d, e, f, g, h, i, j, k, l , m, n, o, p, q, r, s, t, u, v, w, x, y, z, aa, ab, 
ac, ad, ae, af, ag, ah, ai, aj, ak, al, am, an, ao, ap, aq, ar, at, au, av, aw)

transactionDescription = df19["Transaction Description"]
transactionAmount = df19["Transaction Amount"]

(y, z, aa, ab, ac, ad, ae, af, ag, ah, ai, aj, ak, al, am,
an, ao, ap, aq, ar, at, au, av, aw )= CheckChargesAmount(transactionDescription, transactionAmount)

(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, 
r, s, t, u, v, w, x ) = SumAmounts(a, b, c, d, e, f, g, h, i, j, k, l , m, n, o, p, q, r, s, t, u, v, w, x, y, z, aa, ab, 
ac, ad, ae, af, ag, ah, ai, aj, ak, al, am, an, ao, ap, aq, ar, at, au, av, aw)

transactionDescription = df20["Transaction Description"]
transactionAmount = df20["Transaction Amount"]

(y, z, aa, ab, ac, ad, ae, af, ag, ah, ai, aj, ak, al, am,
an, ao, ap, aq, ar, at, au, av, aw )= CheckChargesAmount(transactionDescription, transactionAmount)

(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, 
r, s, t, u, v, w, x ) = SumAmounts(a, b, c, d, e, f, g, h, i, j, k, l , m, n, o, p, q, r, s, t, u, v, w, x, y, z, aa, ab, 
ac, ad, ae, af, ag, ah, ai, aj, ak, al, am, an, ao, ap, aq, ar, at, au, av, aw)

transactionDescription = df21["Transaction Description"]
transactionAmount = df21["Transaction Amount"]

(y, z, aa, ab, ac, ad, ae, af, ag, ah, ai, aj, ak, al, am,
an, ao, ap, aq, ar, at, au, av, aw )= CheckChargesAmount(transactionDescription, transactionAmount)

(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, 
r, s, t, u, v, w, x ) = SumAmounts(a, b, c, d, e, f, g, h, i, j, k, l , m, n, o, p, q, r, s, t, u, v, w, x, y, z, aa, ab, 
ac, ad, ae, af, ag, ah, ai, aj, ak, al, am, an, ao, ap, aq, ar, at, au, av, aw)

transactionDescription = df22["Transaction Description"]
transactionAmount = df22["Transaction Amount"]

(y, z, aa, ab, ac, ad, ae, af, ag, ah, ai, aj, ak, al, am,
an, ao, ap, aq, ar, at, au, av, aw )= CheckChargesAmount(transactionDescription, transactionAmount)

(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, 
r, s, t, u, v, w, x ) = SumAmounts(a, b, c, d, e, f, g, h, i, j, k, l , m, n, o, p, q, r, s, t, u, v, w, x, y, z, aa, ab, 
ac, ad, ae, af, ag, ah, ai, aj, ak, al, am, an, ao, ap, aq, ar, at, au, av, aw)

transactionDescription = df23["Transaction Description"]
transactionAmount = df23["Transaction Amount"]

(y, z, aa, ab, ac, ad, ae, af, ag, ah, ai, aj, ak, al, am,
an, ao, ap, aq, ar, at, au, av, aw )= CheckChargesAmount(transactionDescription, transactionAmount)

(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, 
r, s, t, u, v, w, x ) = SumAmounts(a, b, c, d, e, f, g, h, i, j, k, l , m, n, o, p, q, r, s, t, u, v, w, x, y, z, aa, ab, 
ac, ad, ae, af, ag, ah, ai, aj, ak, al, am, an, ao, ap, aq, ar, at, au, av, aw)

transactionDescription = df24["Transaction Description"]
transactionAmount = df24["Transaction Amount"]

(y, z, aa, ab, ac, ad, ae, af, ag, ah, ai, aj, ak, al, am,
an, ao, ap, aq, ar, at, au, av, aw )= CheckChargesAmount(transactionDescription, transactionAmount)

(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, 
r, s, t, u, v, w, x ) = SumAmounts(a, b, c, d, e, f, g, h, i, j, k, l , m, n, o, p, q, r, s, t, u, v, w, x, y, z, aa, ab, 
ac, ad, ae, af, ag, ah, ai, aj, ak, al, am, an, ao, ap, aq, ar, at, au, av, aw)

transactionDescription = df25["Transaction Description"]
transactionAmount = df25["Transaction Amount"]

(y, z, aa, ab, ac, ad, ae, af, ag, ah, ai, aj, ak, al, am,
an, ao, ap, aq, ar, at, au, av, aw )= CheckChargesAmount(transactionDescription, transactionAmount)

(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, 
r, s, t, u, v, w, x ) = SumAmounts(a, b, c, d, e, f, g, h, i, j, k, l , m, n, o, p, q, r, s, t, u, v, w, x, y, z, aa, ab, 
ac, ad, ae, af, ag, ah, ai, aj, ak, al, am, an, ao, ap, aq, ar, at, au, av, aw)

transactionDescription = df26["Transaction Description"]
transactionAmount = df26["Transaction Amount"]

(y, z, aa, ab, ac, ad, ae, af, ag, ah, ai, aj, ak, al, am,
an, ao, ap, aq, ar, at, au, av, aw )= CheckChargesAmount(transactionDescription, transactionAmount)

(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, 
r, s, t, u, v, w, x ) = SumAmounts(a, b, c, d, e, f, g, h, i, j, k, l , m, n, o, p, q, r, s, t, u, v, w, x, y, z, aa, ab, 
ac, ad, ae, af, ag, ah, ai, aj, ak, al, am, an, ao, ap, aq, ar, at, au, av, aw)

transactionDescription = df27["Transaction Description"]
transactionAmount = df27["Transaction Amount"]

(y, z, aa, ab, ac, ad, ae, af, ag, ah, ai, aj, ak, al, am,
an, ao, ap, aq, ar, at, au, av, aw )= CheckChargesAmount(transactionDescription, transactionAmount)

(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, 
r, s, t, u, v, w, x ) = SumAmounts(a, b, c, d, e, f, g, h, i, j, k, l , m, n, o, p, q, r, s, t, u, v, w, x, y, z, aa, ab, 
ac, ad, ae, af, ag, ah, ai, aj, ak, al, am, an, ao, ap, aq, ar, at, au, av, aw)

transactionDescription = df29["Transaction Description"]
transactionAmount = df29["Transaction Amount"]

(y, z, aa, ab, ac, ad, ae, af, ag, ah, ai, aj, ak, al, am,
an, ao, ap, aq, ar, at, au, av, aw )= CheckChargesAmount(transactionDescription, transactionAmount)

(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, 
r, s, t, u, v, w, x ) = SumAmounts(a, b, c, d, e, f, g, h, i, j, k, l , m, n, o, p, q, r, s, t, u, v, w, x, y, z, aa, ab, 
ac, ad, ae, af, ag, ah, ai, aj, ak, al, am, an, ao, ap, aq, ar, at, au, av, aw)


# printing charges 

print("Service Charge " + str(a))    
print("Service Charge-Management Fee-Principal " + str(b))   
print("Service Charge-Management Fee-Interest " + str(c))
print("Service Charge - Adhoc fee " + str(d))
print("Service charge - Management (loans) " + str(e))
print("Service charge - Management (new loans) " + str(f))
print("Service charge - Penalty Fee - Corporate " + str(g))
print("transaction total management fee is " + str(e + f))
print("Commission expenses - Client / Credit " + str(h))    
print("Outgoing transfer " + str(i))   
print("Tele sales agent commission transfer " + str(j))
print("Credit processing transaction code (Client / CR) " + str(k))
print("Interest due component " + str(l))
print("Interest overdue component " + str(m))
print("Interest received - Client / Debit " + str(n))
print("Loan payment / repayment - Client / Debit " + str(o))
print("Principal overdue component " + str(p))    
print("Paytrail settlement(Db/client) " + str(q))   
print("Redistribution of Principal due component " + str(r))
print("Redistribution of Interset due component " + str(s))
print("Tax withheld - Placement " + str(t))
print("Redistribution of charge component PIRDLT " + str(u))
print("Paytrail transactions crdt " + str(v))
print("Loan payment / repayment - Client / Credit " + str(w))
print("Debit processing transaction code (Client / DB) " + str(x))

# df_xlsx=pd.read_excel(‘/Users/viktornurmela/Downloads/Incomeearnedreport (17).xlsx’)
          