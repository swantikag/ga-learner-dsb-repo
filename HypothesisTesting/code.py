# --------------
import pandas as pd
import scipy.stats as stats
import math
import numpy as np
import warnings

warnings.filterwarnings('ignore')
#Sample_Size
sample_size=2000

#Z_Critical Score
z_critical = stats.norm.ppf(q = 0.95)  


# path        [File location variable]
data = pd.read_csv(path)
#Code starts here
data_sample = data.sample(n=sample_size, random_state=0)
sample_mean = data_sample["installment"].mean()
sample_std = data_sample["installment"].std()
margin_of_error = z_critical * (sample_std/math.sqrt(sample_size))
confidence_interval = (sample_mean - margin_of_error, sample_mean + margin_of_error)
true_mean = data["installment"].mean()
print(true_mean)
if true_mean > confidence_interval[0] and true_mean < confidence_interval[1]:
    print(True)
else:
    print(False)



# --------------
import matplotlib.pyplot as plt
import numpy as np

#Different sample sizes to take
sample_size=np.array([20,50,100])

#Code starts here
fig, axes = plt.subplots(3, 1)
for i in range(len(sample_size)):
    m = list()
    for j in range(1000):
        data_sample = data["installment"].sample(n=sample_size[i])
        m.append(data["installment"].mean())
    mean_series = pd.Series(m)
    mean_series.plot(kind="hist", ax=axes[i])



# --------------
#Importing header files

from statsmodels.stats.weightstats import ztest

#Code starts here
data["int.rate"] = data["int.rate"].apply(lambda x : float(x.replace("%",""))/100)
df = data[data["purpose"]=="small_business"]["int.rate"]
m = data["int.rate"].mean()
print(m)
z_statistic, p_value = ztest(x1=df, value=m, alternative="larger")
print(z_statistic)
if p_value < 0.05:
    print("Reject")
else:
    print("Accept")


# --------------
#Importing header files
from statsmodels.stats.weightstats import ztest

#Code starts here
df1 = data[data["paid.back.loan"]=="No"]["installment"]
df2 = data[data["paid.back.loan"]=="Yes"]["installment"]
z_statistic, p_value = ztest(x1=df1, x2=df2)
z_statistic = round(z_statistic, 2)
p_value = round(p_value, 7)
print(z_statistic)
print(p_value)
if p_value < 0.05:
    print("Reject") 
else:
    print("Accept")


# --------------
#Importing header files
from scipy.stats import chi2_contingency

#Critical value 
critical_value = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                      df = 6)   # Df = number of variable categories(in purpose) - 1

#Code starts here
yes = data[data["paid.back.loan"]=="Yes"]["purpose"].value_counts()
no = data[data["paid.back.loan"]=="No"]["purpose"].value_counts()
print(yes)
print(no)
observed = pd.concat([yes.transpose(),no.transpose()], axis=1, keys=["Yes", "No"])
print(observed)
chi2, p, dof, ex = chi2_contingency(observed)
if chi2 > critical_value:
    print("Reject")
else:
    print("Accept")



