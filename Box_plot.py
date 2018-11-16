import matplotlib.pyplot as plt
import pandas as pd

df_can=pd.read_excel(
	'Canada.xlsx',
	sheet_name='Canada by Citizenship',
	skiprows=range(20),
	skipfooter=2
)
df_can.set_index('OdName',inplace=True)
years=list(map(int,range(1980,2014)))
df_jap=df_can.loc['Japan',years]
df_jap.plot(kind='box')
plt.title("Japanese immigrants from 1980-2013")
plt.ylabel('Number of Immigrants')
plt.show()