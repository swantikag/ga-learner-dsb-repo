# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df = pd.read_csv(path)
total = len(df)
p_a = len(df[df["fico"]>700])/total
p_b = len(df[df["purpose"]=="debt_consolidation"])/total
df1 = df[df["purpose"]=="debt_consolidation"]
p_a_and_b = len(df[(df["fico"]>700) & (df["purpose"]=="debt_consolidation")])/total
p_a_b = p_a_and_b/p_a
p_b_a = p_a_and_b/p_b
result = p_b_a == p_a
print(result)
# code ends here


# --------------
# code starts here
total = len(df)
new_df = df[df["paid.back.loan"]=="Yes"]
prob_lp = len(new_df)/total
df2 = df[df["credit.policy"]=="Yes"]
prob_cs = len(df2)/total
df_lp_cs = df[(df["paid.back.loan"]=="Yes") & (df["credit.policy"]=="Yes")]
prob_lp_a_cs = len(df_lp_cs)/total
# prob_pd_cs = prob_lp_a_cs/prob_cs
prob_pd_cs = new_df[new_df['credit.policy'] == 'Yes'].shape[0] / new_df.shape[0]
bayes = (prob_pd_cs * prob_lp) / prob_cs
print(bayes)
# code ends here


# --------------
# code starts here
df_purpose = df["purpose"].value_counts()
df_purpose.plot(kind="bar")
df1 = df[df["paid.back.loan"]=="No"]
df1["purpose"].value_counts().plot(kind="bar")
# code ends here


# --------------
# code starts here
inst_median = df["installment"].median()
inst_mean = df.installment.mean()
df.installment.hist()
df["log.annual.inc"].hist()
# code ends here


