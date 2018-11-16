import matplotlib.pyplot as plt
import pandas as pd

df_canada=pd.read_excel(
	'Canada.xlsx',
	sheet_name='Canada by Citizenship',
	skiprows=range(20),
	skipfooter=2
)
df_canada.set_index('OdName',inplace=True)
years = list(map(int,range(1980,2014)))
df=df_canada.loc['Iceland',years]
df.plot(kind='bar')
plt.title("Icelandic immigrants to canada from 1980 to 2013")
plt.xlabel("Year")
plt.ylabel("Number of Immigrants")
plt.show()