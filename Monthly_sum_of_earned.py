#!/usr/bin/python
# -*- coding: ISO-8859-1 -*-
#import necessary modules
import pandas as pd
import numpy as np
import os

# stored data for later use
"""
path = os.getcwd()
path = path + "/Incomeearned/"

files = os.listdir(path)
df = pd.DataFrame()
list1 = []
for f in files:
    data = pd.read_csv(os.path.join(path, f), sep=";", dtype={"Unnamed: 5":str})
    data=data.drop(data.index[:4])
    data= data.drop(data.index[-1:])
    df = df.append(data)
    
for x in df:
    print(x)
    if x == "Unnamed: 0":
        feeName = df["Unnamed: 0"]
        generalLedger = df["Unnamed: 3"]
        amount = df["Unnamed: 5"]
        #amount = pd.to_numeric(df["Unnamed: 5"], errors='coerce')
        print(feeName, generalLedger, amount)
"""

# loading data from a file (note that all_incomeearned data must be in one file, do
#  don't add total sums to a file)
df = pd.read_excel("all_incomeearned.xlsx", "Sheet1", dtype={"Fee Name": str, "General Ledger": int, "Amount":float})

feeName = df["Fee Name"]
generalLedger = df["General Ledger"]
amount = df["Amount"].astype(np.float64)
index = 0

sumManagementFee = 0
sumManagementFeePrincipal = 0
sumManagementFeeInterest = 0
sumServiceCharge1 = 0
sumAdhoc1 = 0
sumPenalty1 = 0
sumOrigination = 0
sumInvestment = 0

# processing and printing incomeearned data
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

print("Management fee sum "+ str(sumManagementFee))
print("Management fee principal sum "+ str(sumManagementFeePrincipal))
print("Management fee interest sum "+ str(sumManagementFeeInterest))
print("Service charge sum "+ str(sumServiceCharge1))
print("Adhoc charge sum "+ str(sumAdhoc1))
print("Penalty fee sum "+ str(sumPenalty1))
print("Origination fee sum "+ str(sumOrigination))
print("Investment fee sum "+ str(sumInvestment))
print("\n")

# reading and processing GL_transactions files from GL_Transactions folder
path = os.getcwd()
path = path + "/GL_Transactions/"

files = os.listdir(path)
df1 = pd.DataFrame()

# looping through files and processing and then printing total sums
# dtype formats data as string
for f in files:
    data = pd.read_csv(os.path.join(path, f), sep=";", dtype={'CONTRACTREFNO':str, 'TRANSACTIONREFNO':str, 
    'GL_DESCRIPTION':str, 'ACCOUNTBRANCH':str, 'TRANSACTIONBRANCH':str, 'TRANSACTIONCODE':str, 'TRANSACTION_DESCRIPTION':str,
    'DEPARTMENT':str, 'DR_CR':str, 'CURRENCY':str, 'TRANSACTION_AMOUNT':str, 'RATE':float, 'LCY_EQUIVALENT':str, 'BOOK_DATE':str, 
    'VALUE_DATE':str, 'EVENT':str, 'MODULE':str, 'CHANNEL':str, 'JOURNALDESCRIPTION':str, 'POSTEDBY':str, 
    'POSTEDON':str, 'APPROVEDBY':str, 'APPROVEDON':str, })
    df1 = df1.append(data)

lendersWalletAccount = 0
totalAssetsLoans = 0
incomePenaltyFee = 0
accruedInterestReceivable = 0
incomeManagementLoans = 0
incomeServiceCharge = 0
loanMirrorGl = 0
incomePrincipalRepayment = 0
transitLedger = 0
nostroAccountRegular = 0
interestEarnedLiability = 0
incomeInterestRepayment = 0
placementTaxWitheld = 0
incomeAdhocPenaltyCharge = 0
agentsCommissionAccount = 0
commissionExpenseLoan = 0
incomeRealized = 0
incomeAdhocCharge = 0
transitGl = 0
thirdPartySettlement = 0
paytrailSettlement = 0
paytrailCharge = 0
commissionExpenseLending = 0
commissionExpenseTele = 0
incomeInvestment = 0
incomeOrigination = 0
incomeAutoInvestment = 0

idx = 0

# if data from account branch is correct then sum values

for x in df1['ACCOUNTBRANCH']:
    if x == "Lender's Wallet account":
        rows = float(df1['RATE'].iloc[idx])
        lendersWalletAccount += rows
    if x == "Total Assets - Loans":
        rows = float(df1['RATE'].iloc[idx])
        totalAssetsLoans += rows
    if x == "Income - Penalty Fee - Corporate":
        rows = float(df1['RATE'].iloc[idx])
        incomePenaltyFee += rows
    if x == "Accrued interest receivable":
        rows = float(df1['RATE'].iloc[idx])
        accruedInterestReceivable += rows
    if x == "Income - Management (loans)":
        rows = float(df1['RATE'].iloc[idx])
        incomeManagementLoans += rows
    if x == "Income -Service Charge":
        rows = float(df1['RATE'].iloc[idx])
        incomeServiceCharge += rows
    if x == "Loan mirror GL":
        rows = float(df1['RATE'].iloc[idx])
        loanMirrorGl += rows
    if x == "Income - Principal repayment":
        rows = float(df1['RATE'].iloc[idx])
        incomePrincipalRepayment += rows
    if x == "Transit ledger":
        rows = float(df1['RATE'].iloc[idx])
        transitLedger += rows
    if x == "Nostro account - regular":
        rows = float(df1['RATE'].iloc[idx])
        nostroAccountRegular += rows
    if x == "Interest earned liability":
        rows = float(df1['RATE'].iloc[idx])
        interestEarnedLiability += rows
    if x == "Income - Interest repayment":
        rows = float(df1['RATE'].iloc[idx])
        incomeInterestRepayment += rows
    if x == "Placement - Tax withheld":
        rows = float(df1['RATE'].iloc[idx])
        placementTaxWitheld += rows
    if x == "Income -Adhoc/Penalty Charge":
        rows = float(df1['RATE'].iloc[idx])
        incomeAdhocPenaltyCharge += rows
    if x == "Agent's commission account":
        rows = float(df1['RATE'].iloc[idx])
        agentsCommissionAccount += rows
    if x == "Commission Expense - Loan Agent":
        rows = float(df1['RATE'].iloc[idx])
        commissionExpenseLoan += rows
    if x == "Income realized":
        rows = float(df1['RATE'].iloc[idx])
        incomeRealized += rows
    if x == "Income -Adhoc Charge":
        rows = float(df1['RATE'].iloc[idx])
        incomeAdhocCharge += rows
    if x == "Transit GL":
        rows = float(df1['RATE'].iloc[idx])
        transitGl += rows
    if x == "Third party settlement account":
        rows = float(df1['RATE'].iloc[idx])
        thirdPartySettlement += rows
    if x == "Paytrail Settlement":
        rows = float(df1['RATE'].iloc[idx])
        paytrailSettlement += rows
    if x == "Paytrail Charge":
        rows = float(df1['RATE'].iloc[idx])
        paytrailCharge += rows
    if x == "Commission Expense - Lending Agent":
        rows = float(df1['RATE'].iloc[idx])
        commissionExpenseLending += rows
    if x == "Commission Expense - Tele-Sales Agent":
        rows = float(df1['RATE'].iloc[idx])
        commissionExpenseTele += rows
    if x == "Income - Investment (Placements)":
        rows = float(df1['RATE'].iloc[idx])
        incomeInvestment += rows
    if x == "Income - Origination (loans)":
        rows = float(df1['RATE'].iloc[idx])
        incomeOrigination += rows
    if x == "Income - Auto-investment (Placements)":
        rows = float(df1['RATE'].iloc[idx])
        incomeAutoInvestment += rows
    idx += 1

# printing the values

print("Lender's Wallet account " + str(lendersWalletAccount))
print("Total Assets - Loans " + str(totalAssetsLoans))
print("Income - Penalty Fee - Corporate " + str(incomePenaltyFee))
print("Accrued interest receivable " + str(accruedInterestReceivable))
print("Income - Management (loans) " + str(incomeManagementLoans))
print("Income -Service Charge " + str(incomeServiceCharge))
print("Loan mirror GL " + str(loanMirrorGl))
print("Income - Principal repayment " + str(incomePrincipalRepayment))
print("Transit ledger " + str(transitLedger))
print("Nostro account - regular " + str(nostroAccountRegular))
print("Interest earned liability " + str(interestEarnedLiability))
print("Income - Interest repayment " + str(incomeInterestRepayment))
print("Placement - Tax withheld " + str(placementTaxWitheld))
print("Income -Adhoc/Penalty Charge " + str(incomeAdhocPenaltyCharge))
print("Agent's commission account " + str(agentsCommissionAccount))
print("Commission Expense - Loan Agent " + str(commissionExpenseLoan))
print("Income realized " + str(incomeRealized))
print("Income -Adhoc Charge " + str(incomeAdhocCharge))
print("Transit GL " + str(transitGl))
print("Third party settlement account " + str(thirdPartySettlement))
print("Paytrail Settlement " + str(paytrailSettlement))
print("Paytrail Charge " + str(paytrailCharge))
print("Commission Expense - Lending Agent " + str(commissionExpenseLending))
print("Commission Expense - Tele-Sales Agent " + str(commissionExpenseTele))
print("Income - Investment (Placements) " + str(incomeInvestment))
print("Income - Origination (loans) " + str(incomeOrigination))
print("Income - Auto-investment (Placements) " + str(incomeAutoInvestment))
