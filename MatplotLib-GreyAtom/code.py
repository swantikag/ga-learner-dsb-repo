# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




#Code starts here
data = pd.read_csv(path)
loan_status = data["Loan_Status"].value_counts()
loan_status.plot(kind='bar')


# --------------
#Code starts here
property_and_loan = data.groupby(['Property_Area', 'Loan_Status'])
property_and_loan = property_and_loan.size().unstack()
property_and_loan.plot(kind='bar', stacked=False)
plt.xlabel("Property Area")
plt.ylabel("Loan Status")
plt.xticks(rotation=45)


# --------------
#Code starts here
education_and_loan = data.groupby(["Education","Loan_Status"])
education_and_loan = education_and_loan.size().unstack()
education_and_loan.plot(kind='bar', stacked=True)
plt.xlabel("Education Status")
plt.ylabel("Loan Status")
plt.xticks(rotation=45)


# --------------
#Code starts here
graduate = data[data["Education"]=="Graduate"]
not_graduate = data[data["Education"]=="Not Graduate"]
graduate["LoanAmount"].plot(kind='density', label='Graduate')
not_graduate["LoanAmount"].plot(kind='density', label='Not Graduate')












#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here
fig, (ax_1,ax_2,ax_3)=plt.subplots(3,1)
data.plot.scatter("ApplicantIncome","LoanAmount",ax=ax_1)
plt.title("Applicant Income")

data.plot.scatter("CoapplicantIncome","LoanAmount",ax=ax_2)
plt.title("Coapplicant Income")

data["TotalIncome"]=data["ApplicantIncome"] + data["CoapplicantIncome"]
data.plot.scatter("TotalIncome","LoanAmount",ax=ax_3)
plt.title("Total Income")


