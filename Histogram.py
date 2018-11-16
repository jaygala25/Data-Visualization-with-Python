import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_excel(
	'Canada.xlsx',
	sheet_name='Canada by Citizenship',
	skiprows=range(20),
	skipfooter=2
)

hist,bin_edges = np.histogram(df[2013])
df[2013].plot(kind='hist',xticks=bin_edges)
plt.title("Immigration from 195 countries in 2013")
plt.xlabel("Number of Immigrants")
plt.ylabel("Number of Countries")
plt.show()