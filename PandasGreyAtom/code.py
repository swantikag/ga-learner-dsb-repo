# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 



# code starts here
bank = pd.read_csv(path)
categorical_var = bank.select_dtypes(include='object')
print(categorical_var)
numerical_var = bank.select_dtypes(include='number')
print(numerical_var)


# code ends here


# --------------
# code starts here
banks=bank.drop(["Loan_ID"], axis=1)
print(banks.isnull().sum())
bank_mode = banks.mode().iloc[0]
banks.fillna(bank_mode, inplace=True)
banks.isnull().sum()
#code ends here


# --------------
# Code starts here
import pandas as pd
avg_loan_amount=pd.pivot_table(banks, index=['Gender','Married','Self_Employed'], values='LoanAmount', aggfunc='mean')



# code ends here



# --------------
# # code starts here
x=banks[banks["Self_Employed"]=="Yes"]
y=x[x["Loan_Status"]=="Y"]
loan_approved_se = len(y)
x=banks[banks["Self_Employed"]=="No"]
y=x[x["Loan_Status"]=="Y"]
loan_approved_nse = len(y)
Loan_Status = 614
percentage_se = (loan_approved_se/Loan_Status) * 100
percentage_nse = (loan_approved_nse/Loan_Status)*100
# code ends here


# --------------
# code starts here
def convertToYear(num):
    return num/12

loan_term=banks["Loan_Amount_Term"].apply(lambda x:convertToYear(x))
big_loan_term = len(loan_term[loan_term>=25])

# code ends here


# --------------
# code starts here
loan_groupby=banks.groupby("Loan_Status")
loan_groupby = loan_groupby["ApplicantIncome","Credit_History"]
mean_values=loan_groupby.agg({"ApplicantIncome":"mean","Credit_History":"mean"})


# code ends here


