import pandas as pd
import matplotlib.pyplot as plt
df_can=pd.read_excel(
	'Canada.xlsx',
	sheet_name='Canada by Citizenship',
	skiprows=range(20),
	skipfooter=2
)
years=list(map(int,range(1980,2014)))
df_can.set_index('OdName',inplace=True)
df_can.sort_values(['Total'],ascending=False,axis=0,inplace=True)
#df_can.drop('Total',axis=1,inplace=True)
df_top5=df_can.head()
print(df_top5)
df_top5=df_top5[years].transpose()
print(df_top5)
df_top5.plot(kind="area")
plt.title("Immigration trend of top 5 countries")
plt.xlabel("Years")
plt.ylabel("Number of Immigrants")
plt.show()
print()
#print(df_top5.loc[1980,'India'])