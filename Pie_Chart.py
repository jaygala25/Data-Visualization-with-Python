import matplotlib.pyplot as plt
import pandas as pd

df_can = pd.read_excel(
	'Canada.xlsx',
	sheet_name='Canada by Citizenship',
	skiprows=range(20),
	skipfooter=2
)
df=df_can.groupby('AreaName',axis=0).sum()
print(df)
df['Total'].plot(
	kind='pie',
    autopct='%1.1f%%', 
    shadow=True,  
	#labels=None,	
	startangle=90,
	#pctdistance=1.2
)
#plt.legend(labels=df.index,loc='upper left')
plt.title("Immigrants to Canada by Continent [1980-2013]")
plt.show()