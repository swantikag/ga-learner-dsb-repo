# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path

#Code starts here 
data = pd.read_csv(path)
data["Gender"].replace("-","Agender", inplace = True)
gender_count = data["Gender"].value_counts()
gender_count.plot.bar()


# --------------
#Code starts here
import matplotlib.pyplot as plt
alignment = data["Alignment"].value_counts()
plt.pie(alignment)
plt.title("Character Alignment")


# --------------
#Code starts here
import numpy as np
sc_df = data[["Strength", "Combat"]]
sc_covariance = sc_df.cov().iloc[0,1].round(2)
sc_strength = sc_df["Strength"].std().round(2)
sc_combat = sc_df["Combat"].std().round(2)
sc_pearson = sc_covariance / (sc_strength * sc_combat).round(2)
ic_df = data[["Intelligence", "Combat"]]
ic_covariance = ic_df.cov().iloc[0,1].round(2)
ic_intelligence = ic_df["Intelligence"].std().round(2)
ic_combat = ic_df["Combat"].std().round(2)
ic_pearson = ic_covariance/(ic_intelligence*ic_combat).round(2)


# --------------
#Code starts here
total_high = data["Total"].quantile(0.99)
super_best = data[data["Total"]>total_high]
super_best_names = super_best["Name"].values.tolist()
print(super_best_names)


# --------------
#Code starts here
import matplotlib.pyplot as plt
fig, (ax_1, ax_2, ax_3) = plt.subplots(1,3)
data.boxplot(column="Intelligence",ax=ax_1)
ax_1.title.set_text("Intelligence")
data.boxplot(column="Speed",ax=ax_2)
ax_1.title.set_text("Speed")
data.boxplot(column="Power",ax=ax_3)
ax_1.title.set_text("Power")


